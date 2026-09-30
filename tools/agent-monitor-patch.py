from pathlib import Path
import json, shutil, hashlib, sys
root=Path(sys.argv[1])
manifest=json.loads((root/'package.json').read_text(encoding='utf-8'))
if manifest.get('version')!='0.7.0':
    raise SystemExit('Expected Agent Monitor 0.7.0; inspect new version before patching.')
config=root.parent/'AgentMonitorConfig'
config.mkdir(exist_ok=True)
helper="""'use strict';
// Local fixed-session list. Conversation history and Codex settings are never modified.
const fs = require('fs');
const path = require('path');
const file = path.resolve(fs.realpathSync(__dirname), '../../AgentMonitorConfig/watched-sessions.json');
let signature = '', cached = null;
function load() {
  let st;
  try { st = fs.statSync(file); } catch (e) { if (e.code === 'ENOENT') return null; throw e; }
  const sig = `${st.mtimeMs}:${st.size}`;
  if (sig === signature) return cached;
  const data = JSON.parse(fs.readFileSync(file, 'utf8').replace(/^\\uFEFF/, ''));
  if (!Array.isArray(data.sessions)) throw new Error('watched-sessions.json requires a sessions list');
  const entries = new Map();
  for (const s of data.sessions) {
    if (!s || !/^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i.test(s.id)) throw new Error('Invalid watched session id');
    const id = s.id.toLowerCase();
    if (entries.has(id)) throw new Error('Duplicate watched session id');
    entries.set(id, String(s.label || id));
  }
  cached = entries; signature = sig;
  return cached;
}
module.exports = { load };
"""
monitor=root/'lib/monitor.js'
source=monitor.read_text(encoding='utf-8')
marker="const watchedSessions = require('./watched-sessions');"
if marker in source:
    raise SystemExit('Patch already present; do not overwrite or replace backups.')
replacements=[
("const fs = require('fs');", "const fs = require('fs');\n"+marker),
("      const keep = [...this.focus].filter((k) => k.startsWith(name + ':'));", "      const keep = [...this.focus].filter((k) => k.startsWith(name + ':'));\n      const watched = watchedSessions.load();\n      if (name === 'codex' && watched) for (const id of watched.keys()) keep.push('codex:' + id);"),
("        if (!inWindow && !s.live && !this.focus.has(s.key)) continue;", "        if (!inWindow && !s.live && !keep.includes(s.key)) continue;"),
("    for (const slot of this.slots) this.scanSlot(slot, now, sessions, q);", "    for (const slot of this.slots) this.scanSlot(slot, now, sessions, q);\n\n    // Local fixed-session list: retains named conversations even while idle.\n    const watched = watchedSessions.load();\n    if (watched) {\n      for (let i = sessions.length - 1; i >= 0; i--) {\n        const s = sessions[i];\n        if (s.provider !== 'codex' || (!watched.has(s.id.toLowerCase()) && now - (s.updatedMs || 0) >= 24 * 60 * 60 * 1000)) sessions.splice(i, 1);\n        else if (watched.has(s.id.toLowerCase())) s.title = watched.get(s.id.toLowerCase());\n      }\n    }")]
for old,new in replacements:
    if source.count(old)!=1: raise SystemExit('Patch anchor changed; no files written: '+old)
    source=source.replace(old,new,1)
backup=config/'backups/0.7.0'
backup.mkdir(parents=True,exist_ok=True)
if (backup/'monitor.js').exists(): raise SystemExit('Backup already exists; inspect before replacing.')
shutil.copy2(monitor,backup/'monitor.js')
(backup/'monitor.js.sha256').write_text(hashlib.sha256(monitor.read_bytes()).hexdigest()+'\n',encoding='ascii')
(root/'lib/watched-sessions.js').write_text(helper,encoding='utf-8')
monitor.write_text(source,encoding='utf-8')
print('Patched monitor.js; backup: '+str(backup))