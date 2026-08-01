import requests
import os
import threading
import time
import sys
import platform

def is_sent():
    if os.path.exists(os.path.expanduser("~/.shell4/runfile")):
        return True
    else:
        return False

def prep():
    if not os.path.isdir(os.path.expanduser("~/.shell4/")):
        os.mkdir(os.path.expanduser("~/.shell4"))

def _spinner():
    symbols = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    while True:
        for symbol in symbols:
            print(f"\r(  {symbol}  ) sending telemetry...", end="", flush=True)
            time.sleep(0.1)
            if _stop_spinner: break
        if _stop_spinner: break

def send():
    global _stop_spinner
    _stop_spinner = False
    threading.Thread(target=_spinner).start()
    requests.post("https://shell4-telemetry.barsik0396.workers.dev/run", json={"platform": sys.platform, "arch": platform.machine()})
    _stop_spinner = True
    print("\r(  ✓  ) telemetry sent!     ")
    open(os.path.expanduser("~/.shell4/runfile"), "w")