#!/usr/bin/python3
from __future__ import print_function  # avoids linting complaints
from sys import (
  version_info,
  stderr,
  exit,
)
from aiohttp import web
from asyncio import coroutine

from actions import ACTIONS
from util import (
    MATTERMOST_TOKEN,
    KEYWORD,
    version,
)


@coroutine
def nagios_bot_get(request):
    """ Respond with simple hello. """
    return web.Response(text=version())


@coroutine
def nagios_bot_post(request):
    """ Accept nagios commands and pass on to handlers. """
    post = yield from request.post()

    if post.get('token') != MATTERMOST_TOKEN:
        return web.Response(status=403, text="Forbidden")

    user = post.get('user', 'anonymous')
    command = post.get('text', '').split(' ')
    if command[0] != KEYWORD:
        response = "Missing keyword from message. Expected %s." % KEYWORD
    else:
        command = command[1:]
        try:
            func = ACTIONS[command[0]]
        except:
            response = "Unknown action: %s." % command[0]
        else:
            response = func(user, command[1:])

    return web.json_response(data={'text': response})


def main():
    """ Start webserver. """
    app = web.Application()
    app.router.add_get("/nagios_bot", nagios_bot_get)
    app.router.add_post("/nagios_bot", nagios_bot_post)
    web.run_app(app)


if __name__ == "__main__":
  if not version_info >= (3, 4):
      print("Script requires python 3.4", file=stderr)
      exit(1)
  main()
