# Source this file in the terminal used for the Jiaan workspace.
# This only sets the current shell environment; it does not edit Git or shell configuration.
case ":${GIT_CEILING_DIRECTORIES-}:" in
  *:/data/LFT-W02_data/jiaan:*) ;;
  *) export GIT_CEILING_DIRECTORIES="${GIT_CEILING_DIRECTORIES:+${GIT_CEILING_DIRECTORIES}:}/data/LFT-W02_data/jiaan" ;;
esac
