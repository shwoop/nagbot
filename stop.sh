#!/bin/bash
PIDFILE=/tmp/nagbot.pid 
if [[ ! -f $PIDFILE ]]; then
  echo -e "nagbot does not appear to be running." \
    "\nPlease refer to 'psauxwwf | grep nagbot' to kill it manually." >&2
  exit 1
fi
read PID <$PIDFILE
kill -9 $PID
while kill -0 $PID >/dev/null; do
  sleep 1
done
rm $PIDFILE
