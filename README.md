# LUCY Market Analysis PWA — Production-Ready Analysis Edition

An installable, analysis-only PWA for live market analysis. It does **not** connect to a broker and does **not** place trades.

## Four independent strategy modules

1. **AOL / TAOL** — liquidity area, sweep, BOS, displacement and retest-zone logic.
2. **XAU Bible** — XAUUSD-focused H4/H1/M15 alignment, momentum and entry-trigger logic.
3. **Candlestick Bible** — trend, support/resistance rejection, pin bars and engulfing patterns.
4. **ICT / SMC** — liquidity, BOS/MSS, displacement, FVG, order block and OTE logic.

**Compare All Strategies** evaluates all four independently, preserves their individual directions and scores, and selects the strongest qualifying module. It does not force agreement or manufacture a setup.

## Included

- Live Twelve Data routing for configured forex, metals, indices, stocks and crypto symbols
- Deriv WebSocket routing for configured synthetic indices
- M5, M15, H1, H4, D1, W1 and MN1 timeframe support where the provider supports it
- Single-symbol analysis and category/all-market scanner
- Strict `VALID_SETUP` or `NO_SETUP` output
- One direction, one pending-order type, one refined entry, SL, TP1–TP3, score, confidence, reason and invalidation
- Strategy selector and independent strategy statistics
- Watchlist, journal, CSV export and signal-outcome tracking
- PWA manifest, service worker, responsive UI and install prompt
- Windows and Linux/macOS launchers
- Render deployment file
- Offline smoke test

## Run on Windows

Double-click `start_windows.bat`, or run:

```bat
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Open `http://127.0.0.1:8000`.

## Run on Linux/macOS

```bash
chmod +x start_linux_mac.sh
./start_linux_mac.sh
```

## API configuration

The local `.env` file is already configured with the key supplied for this build. Keep it private. For Render, set these environment variables in the Render dashboard because `.env` is intentionally excluded from Git:

```env
TWELVE_DATA_API_KEY=your_private_key
DERIV_APP_ID=1089
LUCY_DB_PATH=/var/data/lucy.db
LUCY_CACHE_SECONDS=120
```

## Test the project

```bash
python smoke_test.py
```

The live-data request requires internet access and sufficient provider credits. The offline smoke test validates application startup, API routes, all four strategy modules and Compare All behavior without consuming API credits.

## Important limitations

- The strategy rules are deterministic software interpretations of the supplied strategy descriptions. They do not guarantee profitable trades.
- Twelve Data plan limits can restrict large all-market, multi-timeframe scans. Use category scanning and caching when the free plan is active.
- Suggested lot size is indicative only and is not broker-aware. The project is analysis-only.
- If both SL and TP occur inside the same historical candle, the tracker uses conservative stop-first ordering because tick order is unavailable.
