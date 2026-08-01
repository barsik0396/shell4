#!/bin/bash

echo """      _          _ _ _  _   
  ___| |__   ___| | | || |  
 / __| '_ \ / _ \ | | || |_ 
 \__ \ | | |  __/ | |__   _|
 |___/_| |_|\___|_|_|  |_|  
                            """

# ⠋ ⠙ ⠹ ⠸ ⠼ ⠴ ⠦ ⠧ ⠇ ⠏
# ✓ ✗

PLATFORM=$(uname -s | tr '[:upper:]' '[:lower:]')
ARCH=$(uname -m)

install() {
printf '(  ⠋  ) sending telemetry with DOWNLOAD action...'

curl -s -X POST "https://shell4-telemetry.barsik0396.workers.dev/download" \
  -H "Content-Type: application/json" \
  -d "{\"platform\": \"$PLATFORM\", \"arch\": \"$ARCH\"}" \
  > /dev/null 2>&1 || true

printf '\r(  ✓  ) telemetry with DOWNLOAD action sent!     \n'

if [ $ARCH != "x86_64" ]; then
    printf '\r(  ✗  ) arch is not x86_64 (amd64)!\n'
    exit 0
else
    printf '\r(  ✓  ) ok - arch amd64\n'
fi
if [ $PLATFORM != "linux" ]; then
    printf '\r(  ✗  ) platform is not linux!\n'
    exit 0
else
    printf '\r(  ✓  ) ok - platform linux\n'
fi

printf '\r(  ⠙  ) downloading shell4 v0.2.0p1'
wget -O "/tmp/shell4-installation" "https://github.com/barsik0396/shell4/releases/download/v0.2.0p1/shell4-v0.2.0p1-linux-amd64" > /dev/null 2>&1
printf '\r(  ✓  ) downloaded shell4 v0.2.0 preview 1\n'
printf '\r(  ⠹  ) moving file'
mv /tmp/shell4-installation "$HOME/.local/bin/shell4"
printf '\r(  ✓  ) binary moved to local\n'
printf '\r(  ⠸  ) chmodding binary'
chmod +x "$HOME/.local/bin/shell4"
printf '\r(  ✓  ) chmodded binary \n'
printf '\r(  ⠼  ) sending telemetry with INSTALL action...'
curl -s -X POST "https://shell4-telemetry.barsik0396.workers.dev/install" \
  -H "Content-Type: application/json" \
  -d "{\"platform\": \"$PLATFORM\", \"arch\": \"$ARCH\"}" \
  > /dev/null 2>&1 || true

printf '\r(  ✓  ) telemetry with INSTALL action sent!     \n'

echo '  ✓ DONE INSTALLING SHELL4!'
echo '    You can run it using command: shell4'
}
uninstall() {
printf '(  ?  ) really uninstall shell4? data will been removed. [y/n] '
read -r ans
if [ "$ans" == "y" ]; then
    printf '\033[A\r(  ✓  ) really uninstall shell4? yes                              \n'
elif [ "$ans" == "n" ]; then
    printf '\033[A\r(  ✓  ) really uninstall shell4? no                               \n'
    exit 0
else
    printf '\033[A\r(  ✗  ) really uninstall shell4? invalid input                    \n'
    exit 1
fi
printf '(  ⠋  ) removing binary...'
rm "$HOME/.local/bin/shell4" >/dev/null 2>&1 ||true 
printf '\r(  ✓  ) binary removed    \n'
printf '(  ⠙  ) sending telemetry with UNINSTALL action...'
curl -s -X POST "https://shell4-telemetry.barsik0396.workers.dev/uninstall" \
  -H "Content-Type: application/json" \
  -d "{\"platform\": \"$PLATFORM\", \"arch\": \"$ARCH\"}" \
  > /dev/null 2>&1 || true
printf '\r(  ✓  ) telemetry with UNINSTALL action sent!     \n'
printf '(  ⠹  ) removing runfile...'
rm "$HOME/.shell4/runfile" > /dev/null 2>&1 || true
printf '\r(  ✓  ) runfile removed!   \n'
printf "\r(  ⠸  ) removing ~/.shell4/"
rm -rf "$HOME/.shell4" > /dev/null 2>&1 || true
printf "\r(  ✓  ) removed ~/.shell4/ folder\n"
echo '  ✓ DONE UNINSTALLING SHELL4!'
}
if [ "$1" == "" ]; then
    install
elif [ "$1" == "uninstall" ]; then
    uninstall
else
    echo "unk arg: $1"
    exit 1
fi