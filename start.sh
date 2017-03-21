#!/bin/bash
PIDFILE=/tmp/nagbot.pid 
LOGFILE=/tmp/nagbot.log
if [[ -f $PIDFILE ]]; then
  echo "nagbot appears to be running." >&2
  exit 1
fi
PYVER="`python3 -V`"
if [[ ${PYVER#Python } < 3.4 ]]; then
  echo "requires python version 3.4+" >&2
  exit 1
fi
nagbot/nagbot.py </dev/null >$LOGFILE & disown
if [[ $? ]]; then
  echo $! >$PIDFILE
else
  echo "Something went wrong starting nagbot" >&2
  cat $LOGFILE >&2
fi
