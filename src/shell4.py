print('welcome to \x1b[32mshell4\x1b[0m version 0.1!')
import os
while True:
    inp = input("shell4# \x1b[32m")
    print('\x1b[0m', end='')
    if inp == "exit":
        import sys
        sys.exit()
    elif inp == "":
        pass
    elif inp.startswith('bin '):
        os.system(inp.removeprefix('bin '))
    else:
        print('\x1b[31mUnknown command!\x1b[0m')