import os
import platform
import sys
import shutil

from . import send_telemetry
from .errors import CatsError

try:
    if not send_telemetry.is_sent():
        send_telemetry.prep()
        send_telemetry.send()
except Exception:                     # noqa: BLE001
    print("\r(  ✗  ) Failed to send telemetry")
    with open(os.path.expanduser("~/.shell4/runfile"), "w") as f:
        f.write("meow")

def main():
    print("welcome to \x1b[32mshell4\x1b[0m version v0.2.0!")
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
            print("shell4 version v0.2.0")
        elif inp == "help":
            print("Available commands:")
            print("  help        show this help")
            print("  exit        quit")
            print("  version     show version")
            print("  bin <cmd>   run non-shell4 command")
            print("  platform    show platform")
            print("  crash       crash shell4")
            print("  cd <path>   change directory")
            print("  touch <file>create empty file")
            print("  rm <file>   remove file")
            print("  read <file> read file")
            print("  where       where am i?")
            print("  write <file>write text to file")
            print("  write-append <file>append text to file")
            print("  files       show files in this dir")
            print("  dir <dir>   create new directory")
            print("  deldir <dir>remove directory")
        elif inp == "crash":
            raise CatsError.CatsError("shell4 is too good.")
        elif inp == "cd":
            print("arg required")
        elif inp.startswith("cd "):
            os.chdir(inp.removeprefix("cd "))
            print("cd")
        elif inp == "touch":
            print("arg required")
        elif inp.startswith("touch"):
            open(inp.removeprefix("touch "), "w")   # noqa: SIM115
            print("touch")
        elif inp == "rm":
            print("arg required")
        elif inp.startswith("rm"):
            os.remove(inp.removeprefix("rm "))
            print("rm")
        elif inp == "read":
            print("arg required")
        elif inp.startswith("read"):
            with open(inp.removeprefix("read "), "r") as f:
                print(f.read())
        elif inp == "where":
            print(os.getcwd())
        elif inp == "write":
            print("arg required")
        elif inp == "write-append":
            print("arg required")
        elif inp.startswith("write-append "):
            with open(inp.removeprefix("write-append "), "a") as f:
                print("Write text, finish using '(END)'")
                d = ""
                while True:
                    d += input(">> ")
                    if d.endswith("(END)"):
                        d = d.removesuffix("(END)")
                        break
                    d += "\n"
                f.write(d)
            print("write+append")
        elif inp.startswith("write "):
            with open(inp.removeprefix("write "), "w") as f:
                print("Write text, finish using '(END)'")
                d = ""
                while True:
                    d += input(">> ")
                    if d.endswith("(END)"):
                        d = d.removesuffix("(END)")
                        break
                    d += "\n"
                f.write(d)
            print("write")
        elif inp == "files":
            print(".")
            files = os.listdir(".")
            for file in files:
                print(f"|-- {file}")
        elif inp == "dir":
            print("arg required")
        elif inp.startswith("dir"):
            os.makedirs(inp.removeprefix("dir "))
            print("dir")
        elif inp == "deldir":
            print("arg required")
        elif inp.startswith("deldir"):
            shutil.rmtree(inp.removeprefix("deldir "))
            print("deldir")

        else:
            print("\x1b[31mUnknown command!\x1b[0m")