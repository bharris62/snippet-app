import logging
import argparse
import psycopg2

logging.basicConfig(filename='snippets.log', level=logging.DEBUG)
logging.debug('Connecting to PostgreSQL')
connection = psycopg2.connect(database="snippets")
logging.debug("Database Connection Established")


def put(name, snippet):
    """Store a snippet with an associated name."""
    try:
        with connection, connection.cursor() as cursor:
            command = "insert into snippets values (%s, %s)"
            cursor.execute(command, (name, snippet))
    except psycopg2.IntegrityError as e:

        with connection, connection.cursor() as cursor:
            command = "Update snippets set message=%s where keyword=%s"
            cursor.execute(command, (snippet, name))

    logging.debug("Snippet stored successfully")

    return name, snippet


def get(name):
    """Retrieve the snippet with a given the name."""

    with connection, connection.cursor() as cursor:
        cursor.execute("select message from snippets where keyword=%s", (name,))
        snippet = cursor.fetchone()

    logging.debug("Snippet retrieved successfully")

    if not snippet:
        return "404: Snippet Not Found"
    return snippet[0]


def catalog():
    """Get a list of the keywords"""
    with connection, connection.cursor() as cursor:
        cursor.execute("select keyword from snippets ")
        keyword = cursor.fetchall()


    temp = []
    for word in keyword:
        temp.append(word[0])

    return "keywords: " + " | ".join(temp)


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

    # subparser for the catalog command
    logging.debug("Constructing subparser")
    subparser.add_parser("catalog", help="fetch the keywords")

    arguments = parser.parse_args()
    # convert parsed arguments from Namespace to dictionary

    arguments = vars(arguments)
    command = arguments.pop("command")

    if command == 'put':
        name, snippet = put(**arguments)
    elif command == 'catalog':
        kword = catalog()
        print(kword)
    elif command == 'get':
        snippet = get(**arguments)
        print("Retrieved snippet: {!r}".format(snippet))


if __name__ == '__main__':
    main()