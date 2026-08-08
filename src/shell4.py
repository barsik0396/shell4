from . import loadlang

loadlang.load()
lang = loadlang.lang
# print("welcome to \x1b[32mshell4\x1b[0m version v0.3.0-nightly.1!")
print(lang["init.welcome"])
import os
import platform
import shutil
import sys

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
    while True:
        inp = input("shell4# \x1b[32m")
        print("\r\x1b[0m\r", end="", flush=True)
        if inp == "exit":
            print(lang["cmd.exit"])
            sys.exit()
        elif inp == "":
            pass
        elif inp.startswith("bin "):
            os.system(inp.removeprefix("bin "))
        elif inp == "platform":
            print(platform.platform())
        elif inp == "version":
            print(lang["cmd.version"])
        elif inp == "help":
            print(lang["cmd.help.title"])
            print(f"  help        {lang["cmd.help.help"]}")
            print(f"  exit        {lang["cmd.help.exit"]}")
            print(f"  version     {lang["cmd.help.version"]}")
            print(f"  bin <cmd>   {lang["cmd.help.bin"]}")
            print(f"  platform    {lang["cmd.help.platform"]}")
            print(f"  crash       {lang["cmd.help.crash"]}")
            print(f"  cd <path>   {lang["cmd.help.cd"]}")
            print(f"  touch <file>{lang["cmd.help.touch"]}")
            print(f"  rm <file>   {lang["cmd.help.rm"]}")
            print(f"  read <file> {lang["cmd.help.read"]}")
            print(f"  where       {lang["cmd.help.where"]}")
            print(f"  write <file>{lang["cmd.help.write"]}")
            print(f"  write-append <file>{lang["cmd.help.write-append"]}")
            print(f"  files       {lang["cmd.help.files"]}")
            print(f"  dir <dir>   {lang["cmd.help.dir"]}")
            print(f"  deldir <dir>{lang["cmd.help.deldir"]}")
        elif inp == "crash":
            raise CatsError.CatsError(lang["cmd.crash"])
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
        elif inp == "write" or inp == "write-append":
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
            print(f"\x1b[31m{lang["cmd.unknown"]}\x1b[0m")