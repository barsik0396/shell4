import os
import sys
import traceback

from src import shell4


def exception(_, value, exc_traceback):
    print("shell4 crashed. this isn't your problem; you have nothing to do with it.")
    print("debugging information:")
    tb = traceback.extract_tb(exc_traceback)
    print(" === <RUNNER> ===")
    for e in tb:
        print(f" === {os.path.basename(e.filename).upper()} ===")
        print(f"Line: {e.lineno}")
        print(f"Function: {e.name}")
        print(f"Code: {e.line}")
    print(f"Error: {type(value).__name__}: {value}")
    sys.exit(1)
sys.excepthook = exception
shell4.main()
