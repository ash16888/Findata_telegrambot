#!/bin/bash
# $PATH$ to your bot
PIDFILE= $PATH$ /bot.pid

if pgrep --pidfile $PIDFILE &>/dev/null; then
    echo "Exit! Python bot is already running!"
    exit 1
else
  nohup /usr/bin/python3.9 $PATH$/main.py &>/dev/null &
  echo $!>$PIDFILE
fi
