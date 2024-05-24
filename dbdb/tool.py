import sys
import dbdb


BAD_KEY = 'key was not found in the database'
OK = 'OK'
BAD_VERB = 'verb (operation) provided is not valid (not “get”, “set” or “delete”).'
BAD_ARGS = 'incorrect number of arguments passed on the command line.'


def usage():
    """
    Exibe informações sobre como usar o programa.
    """
    usage_info = """
        Usage:
        python dbdb.tool <db_name> <verb> <key> [value]

        Argumentos:
        <db_name>: Database name to use.
        <verb>: Operation to be performed (get, set ou delete).
        <key>: Key to access or modify the value in the database.
        [value]: Value to be set (only for 'set' operation).
        Exemple:
        $ python -m dbdb.tool example.db set first_name "Hericlys"
        $ python -m dbdb.tool example.db get first_name
        $ python -m dbdb.tool example.db delete first_name
    """
    print(usage_info)


def main(argv):
    if not (4 <= len(argv) <= 5):
        usage()
        return BAD_ARGS
    dbname, verb, key, value = (argv[1:] + [None])[:4]
    if verb not in {'get', 'set', 'delete'}:
        usage()
        return BAD_VERB
    db = dbdb.connect(dbname)          # CONNECT
    try:
        if verb == 'get':
            sys.stdout.write(db[key])  # GET VALUE
        elif verb == 'set':
            db[key] = value
            db.commit()
        else:
            del db[key]
            db.commit()
    except KeyError:
        print("Key not found", file=sys.stderr)
        return BAD_KEY
    return OK