@echo off
setlocal
set /p TDKEY=Paste your Twelve Data API key: 
if "%TDKEY%"=="" (
  echo No API key entered. Nothing was changed.
  exit /b 1
)
(
  echo TWELVE_DATA_API_KEY=%TDKEY%
  echo DERIV_APP_ID=1089
  echo LUCY_DB_PATH=./lucy.db
  echo LUCY_CACHE_SECONDS=120
) > .env
echo.
echo API key saved securely in .env for this project.
echo Start the app with: uvicorn app.main:app --reload
endlocal
