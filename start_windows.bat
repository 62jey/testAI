@echo off
setlocal
cd /d "%~dp0"
if not exist .venv (
  py -m venv .venv 2>nul || python -m venv .venv
)
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
start "LUCY PWA" http://127.0.0.1:8000
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
endlocal
