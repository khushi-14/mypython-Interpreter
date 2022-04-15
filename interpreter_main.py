from glob import glob
import itertools

def get_user_input():

    text_file = open('mypython_input.txt', 'r+')
    input = text_file.read()
    text_file.close()

    for i in itertools.count():
        try:
            yield i, input
        except KeyboardInterrupt:
            pass
        except EOFError:
            break

def exec_function(user_input):

    try:
        compile(user_input, "<stdin>", "eval")
    except SyntaxError:
        return exec
    return eval
     

def exec_user_input(i, user_input, user_globals):
    
    user_globals = user_globals.copy()
    try:
        retval = exec_function(user_input)(user_input, user_globals)
    except Exception as e:
        print("%s: %s" % (e.__class__.__name__, e))
    else:
        if retval is not None:
            globals.output = retval
    return user_globals


def selected_user_globals(user_globals):

    return (
        (key, user_globals[key])
        for key in sorted(user_globals)
        if not key.startswith("__") or not key.endswith("__")
    )


def save_user_globals(user_globals, path="user_globals.txt"):

    with open(path, "w") as fd:
        for key, val in selected_user_globals(user_globals):
            fd.write("%s = %s (%s)\n" % (key, val, val.__class__.__name__))


def main():

    user_globals = {}
    global save_user_globals
    global selected_user_globals
    global get_user_input
    global exec_function
    global exec_user_input
    save_user_globals(user_globals)
    for i, user_input in get_user_input():
        user_globals = exec_user_input(i, user_input, user_globals)
        save_user_globals(user_globals)


if __name__ == "__main__":
    main()
