from util import version as _v


def version(user, args):
    """ Respond with version number. """
    return _v()


def hello(user, args):
    """ Basic hello version to test out. """
    return "@%s hello to you good sir." % user


ACTIONS = {
  'version': version,
  'hello': hello,
}
