#!/usr/bin/env sh
set -eu
printf 'Paste your Twelve Data API key: '
stty -echo
IFS= read -r TDKEY
stty echo
printf '\n'
if [ -z "$TDKEY" ]; then
  echo 'No API key entered. Nothing was changed.'
  exit 1
fi
cat > .env <<EOF
TWELVE_DATA_API_KEY=$TDKEY
DERIV_APP_ID=1089
LUCY_DB_PATH=./lucy.db
LUCY_CACHE_SECONDS=120
EOF
chmod 600 .env 2>/dev/null || true
echo 'API key saved in .env. Start with: uvicorn app.main:app --reload'
