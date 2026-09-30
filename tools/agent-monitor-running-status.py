from pathlib import Path
import hashlib, json, shutil, sys

root = Path(sys.argv[1]).resolve()
if json.loads((root / 'package.json').read_text(encoding='utf-8'))['version'] != '0.7.0':
    raise SystemExit('Expected Agent Monitor 0.7.0; inspect new version before patching.')
target = root / 'extension.js'
original = target.read_text(encoding='utf-8')
marker = '// Local running-count-only status bar.'
if marker in original:
    print('Running-count patch already installed.')
    raise SystemExit(0)
start = original.index('  updateStatusBar(now) {')
end = original.index('\n  statusTooltip(now, showCost) {', start)
replacement = '''  updateStatusBar(now) {
    // Local running-count-only status bar.
    const item = this.statusItem;
    const count = this.lamps ? Number(this.lamps.counts.working) || 0 : 0;
    if (!this.cfg().get('showStatusBar', true) || count === 0) {
      item.hide();
      this.chrome.barSig = null;
      return;
    }
    const text = `$(sync~spin) 运行中 ${count}`;
    if (this.chrome.barSig !== text) {
      this.chrome.barSig = text;
      item.text = text;
      item.color = undefined;
      item.backgroundColor = undefined;
      item.tooltip = `正在运行：${count} 个对话`;
      item.accessibilityInformation = { label: `运行中 ${count} 个对话` };
    }
    item.show();
  }
'''
old_badge = "    const b = loaded && this.lamps ? fmt.formatBadge(this.lamps.counts, i18n) : { value: 0, tooltip: '' };"
if original.count(old_badge) != 1:
    raise SystemExit('Badge anchor changed; no files written.')
updated = original[:start] + replacement + original[end:]
updated = updated.replace(old_badge, "    const b = { value: 0, tooltip: '' }; // Count only in the bottom status bar; no unread badges.", 1)
backup = root.parent / 'AgentMonitorConfig' / 'backups' / '0.7.0-running-status'
backup.mkdir(parents=True, exist_ok=True)
if (backup / 'extension.js').exists():
    raise SystemExit('Backup exists but patch absent; inspect before proceeding.')
shutil.copy2(target, backup / 'extension.js')
(backup / 'extension.js.sha256').write_text(hashlib.sha256(target.read_bytes()).hexdigest() + '\n', encoding='ascii')
if target.read_text(encoding='utf-8') != original:
    raise SystemExit('Extension changed concurrently; not overwritten.')
target.write_text(updated, encoding='utf-8')
print('Installed running-count-only status bar; backup: ' + str(backup))