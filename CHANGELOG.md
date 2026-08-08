# shell4 changelog

## v0.3.0-nightly.1
### added
1. languages support
### installation
1. download binary
2. copy it to `~/.local/bin/shell4`
3. install language:
```bash
mkdir -p ~/.shell4/config
mkdir -p ~/.shell4/languages

# for english
wget -O "$HOME/.shell4/languages/en-US.lang" "https://raw.githubusercontent.com/barsik0396/shell4/refs/heads/main/lang/en-US.lang"
printf "en-US" > "$HOME/.shell4/config/language"

# for russian
wget -O "$HOME/.shell4/languages/ru-RU.lang" "https://raw.githubusercontent.com/barsik0396/shell4/refs/heads/main/lang/ru-RU.lang"
printf "ru-RU" > "$HOME/.shell4/config/language"
```

## v0.2.0 [Aug 4, 2026, 7:30 PM GMT+3]
### added
1. `files` command
2. `write` command
3. `write-append` command
4. `dir` command
5. `deldir` command

## v0.2.0-preview.2 [Aug 3, 2026, 2:33 PM GMT+3]
### added
1. telemetry
2. basic file operations: `cd`, `where`, `touch`, `read`, `rm`

## v0.2.0-preview.1 [Jul 30, 2026, 5:28 PM GMT+3]
### added
1. `crash` command
2. excepthook

## v0.1.1 [Jul 28, 2026, 5:46 PM GMT+3]
### added
1. windows support
2. `help` command
3. `version` command
4. `platform` command

## v0.1.0 [Jul 22, 2026, 12:13 AM GMT+3]
(initial release)