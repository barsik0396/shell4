import os
import platform
import sys

from .errors import CatsError
from .       import send_telemetry

try:
    if not send_telemetry.is_sent():
        send_telemetry.prep()
        send_telemetry.send()
except:
    print("\r(  ✗  ) Failed to send telemetry")
    open(os.path.expanduser("~/.shell4/runfile"), "w")

def main():
    print("welcome to \x1b[32mshell4\x1b[0m version v0.2.0p1!")
    while True:
        inp = input("shell4# \x1b[32m")
        print("\r\x1b[0m\r", end="", flush=True)
        if inp == "exit":
            print("Bye!")
            sys.exit()
        elif inp == "":
            pass
        elif inp.startswith("bin "):
            os.system(inp.removeprefix("bin "))
        elif inp == "platform":
            print(platform.platform())
        elif inp == "version":
            print("shell4 version v0.2.0p1")
        elif inp == "help":
            print("Available commands:")
            print("  help        show this help")
            print("  exit        quit")
            print("  version     show version")
            print("  bin <cmd>   run non-shell4 command")
            print("  platform    show platform")
            print("  crash       crash shell4")
        elif inp == "crash":
            raise CatsError.CatsError("shell4 is too good.")
        else:
            print("\x1b[31mUnknown command!\x1b[0m")