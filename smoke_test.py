"""Offline smoke tests for the LUCY PWA core and HTTP application."""
from __future__ import annotations
import math
from fastapi.testclient import TestClient
from app.main import app
from app.lucy_engine import analyse


def synthetic_bars(count: int = 500) -> list[dict[str, float]]:
    bars=[]; price=1.10
    for i in range(count):
        open_price=price
        close=open_price+0.00005+math.sin(i/9)*0.00003
        bars.append({"time":1700000000+i*3600,"open":open_price,"high":max(open_price,close)+0.00012,"low":min(open_price,close)-0.00012,"close":close,"volume":100})
        price=close
    bars[-1]["open"]=bars[-2]["close"]-0.0001
    bars[-1]["close"]=max(item["high"] for item in bars[-11:-1])+0.0003
    bars[-1]["high"]=bars[-1]["close"]+0.0001
    bars[-1]["low"]=bars[-1]["open"]-0.0002
    return bars


def run() -> None:
    bars=synthetic_bars()
    series={tf:{"bars":bars,"source":"TEST"} for tf in ("M15","H1","H4","D1")}
    for strategy in ("AOL_TAOL","XAU_BIBLE","CANDLESTICK_BIBLE","ICT_SMC","ALL_STRATEGIES"):
        result=analyse("XAUUSD","Metals",series,primary_tf="H1",digits=2,strategy=strategy)
        assert result["conclusion"] in {"VALID_SETUP","NO_SETUP"}
        assert result["primary_strategy"] in {"AOL_TAOL","XAU_BIBLE","CANDLESTICK_BIBLE","ICT_SMC"}
    with TestClient(app) as client:
        for path in ("/","/manifest.json","/api/health","/api/symbols","/api/statistics","/api/watchlist"):
            response=client.get(path)
            assert response.status_code==200, (path,response.text)
    print("All offline smoke tests passed.")

if __name__ == "__main__":
    run()
