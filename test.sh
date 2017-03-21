#!/bin/bash
COMMAND="nagbot version"
if (( $# > 1 ));  then
  COMMAND=$@
fi
COMMAND=${COMMAND/ /+}
curl -v --data "text=$COMMAND&token=ehtest"  http://0.0.0.0:8080/nagios_bot
