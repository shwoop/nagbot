NAGBOT
===

Nagios bot designed to integrate with a mattermost outgoing webhook.

The idea being that the webhook will redirect any messages matching the
regex `^nagbot` expecting the format `nagbot ACTION {ARGS}`.

New actions can be added to `nagbot/actions.py` by simply createing a function
with the pattern `foo(user, args)` and registering it to the ACTIONS dictionary
in the form `'action': method`.

Currently just a proof of concept but `test.sh` will simulate message
posting.
```lang=bash
$ ./test.sh nagbot hello                                                                                                                                                                
*   Trying 0.0.0.0...
* Connected to 0.0.0.0 (127.0.0.1) port 8080 (#0)
> POST /nagios_bot HTTP/1.1
> Host: 0.0.0.0:8080
> User-Agent: curl/7.47.0
> Accept: */*
> Content-Length: 30
> Content-Type: application/x-www-form-urlencoded
> 
* upload completely sent off: 30 out of 30 bytes
< HTTP/1.1 200 OK
< Content-Type: application/json; charset=utf-8
< Content-Length: 45
< Date: Tue, 21 Mar 2017 18:15:35 GMT
< Server: Python/3.5 aiohttp/1.2.0
< 
* Connection #0 to host 0.0.0.0 left intact
{"text": "@anonymous hello to you good sir."}

$ ./test.sh nagbot version                                                                                                                                                              
*   Trying 0.0.0.0...
* Connected to 0.0.0.0 (127.0.0.1) port 8080 (#0)
> POST /nagios_bot HTTP/1.1
> Host: 0.0.0.0:8080
> User-Agent: curl/7.47.0
> Accept: */*
> Content-Length: 32
> Content-Type: application/x-www-form-urlencoded
> 
* upload completely sent off: 32 out of 32 bytes
< HTTP/1.1 200 OK
< Content-Type: application/json; charset=utf-8
< Content-Length: 51
< Date: Tue, 21 Mar 2017 18:15:48 GMT
< Server: Python/3.5 aiohttp/1.2.0
< 
* Connection #0 to host 0.0.0.0 left intact
{"text": "Elastichosts Nagios-Mattermost bot v0.1"}
```
