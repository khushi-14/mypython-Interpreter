from io import StringIO
import sys

old_stdout = sys.stdout
sys.stdout = mystdout = StringIO()

eval("print('Heyo')")

sys.stdout = old_stdout

message = mystdout.getvalue()

print(message)
