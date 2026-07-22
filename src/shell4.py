print('welcome to \x1b[32mshell4\x1b[0m version 0.1.1!')
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
    elif inp == "platform":
        import platform
        print(platform.platform())
    elif inp == "help":
        print("  help       show this help")
        print("  exit       quit shell4")
        print("  version    show shell4 version")
        print("  bin <cmd>  run file from PATH")
        print("  platform   show platform")
    elif inp == 'version':
        print("shell4 version v0.1.1")
    else:
        print('\x1b[31mUnknown command!\x1b[0m')