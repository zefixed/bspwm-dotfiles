
# Create aliases
alias cls="clear"
alias g="git"
alias n="nvim"
alias m="micro"
alias sudo="sudo -E"

function sudo
    if test "$argv[1]" = "n"
        command sudo -E nvim $argv[2..-1]
    else
        command sudo $argv
    end
end

# TODO: Replace journal aliases after switching to OpenRC

# Display critical errors
alias syslog_emerg="sudo dmesg --level=emerg,alert,crit"

# Output common errors
alias syslog="sudo dmesg --level=err,warn"

# Print logs from x server
alias xlog='grep "(EE)\|(WW)\|error\|failed" ~/.local/share/xorg/Xorg.0.log'

# Remove archived journal files until the disk space they use falls below 100M
alias vacuum="journalctl --vacuum-size=100M"

# Make all journal files contain no data older than 2 weeks
alias vacuum_time="journalctl --vacuum-time=2weeks"

set -U fish_greeting
set fish_color_command green
set -gx EDITOR micro
set -gx VISUAL micro
set -gx BROWSER /usr/bin/firefox

set -gx GOPATH $HOME/go
set -gx GOBIN $HOME/go/bin
set -gx PATH $GOBIN $PATH


if status is-interactive
    # Commands to run in interactive sessions can go here
end

xset -b
