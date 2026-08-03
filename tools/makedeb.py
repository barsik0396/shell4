print("=== shell4 makedeb tool ===")
print("verb import subprocess")
import subprocess
print("verb import sys")
import sys
print("verb import shutil")
import shutil
print("verb import os")
import os

print("verb checkargs")
if len(sys.argv) == 1:
    sys.stderr.write("error no args\n")
    sys.stderr.write("  USAGE: makedeb.py [BINARY: LINUX AMD64]\n")
    sys.exit(1)

print("verb makedirs")
os.makedirs("etc/deb/usr/bin", exist_ok=True)
print("verb copybin")
shutil.copy(sys.argv[1], "etc/deb/usr/bin/shell4")
print("verb run build")
subprocess.run(["dpkg-deb", "-b", "-z9", "-Zxz", "-v", "etc/deb/", "package.deb"])
print("    DONE")