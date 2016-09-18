import logging
import argparse

logging.basicConfig(filename='snippets.log', level=logging.DEBUG)


def put(name, snippet):
    """
    Store a snippet with an associated name.

    Return the name and the snippet
    """
    logging.error("FIXME: Unimplemented - put({!r}, {!r})".format(name, snippet))
    return name, snippet

def get(name):
    """Retrieve the snippet with a given name.

    If there is no such snippet, return '404: Snippet Not Found'
    Returns the snippet
    """
    logging.error("FIXME: Unimplemented - get({!r})".format(name))
    return ""


def main():
    '''Main Function'''
    logging.info("Constructing Parser")
    parser = argparse.ArgumentParser(description="Store and Retrieve snippets of text")

    subparser = parser.add_subparsers(dest="command", help="Available commands")

    # subparser for the put command
    logging.debug("Constructing put subparser")
    put_parser = subparser.add_parser("put", help="Store a snippet")
    put_parser.add_argument("name", help="Name of the snippet")
    put_parser.add_argument("snippet", help="Snippet text")

    # subparser for the get command
    logging.debug("Constructing put subparser")
    put_parser = subparser.add_parser("get", help="Store a snippet")
    put_parser.add_argument("name", help="Name of the snippet")

    arguments = parser.parse_args()

if __name__ == '__main__':
    main()