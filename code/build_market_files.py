"""How sp500_yahoo.csv and gme_yahoo.csv were built (not needed to run the notebook).

Both files are Yahoo Finance daily data, taken from two public GitHub copies:
  - S&P 500 (^GSPC) and SPY: Microsoft Qlib US daily dataset (Yahoo collector), release v2, data to 10 Nov 2020.
    Field `change` = daily return of the adjusted close.
  - GME: us_stock_eod repository (wumiq), Yahoo daily prices 13 Feb 2002 - 25 Mar 2022.
Written with the help of Claude (Anthropic, 2026). Run: python build_market_files.py  (downloads about 450 MB)
"""
import io
import urllib.request
import zipfile

import numpy as np
import pandas as pd

QLIB = "https://github.com/SunsetWolf/qlib_dataset/releases/download/v2/qlib_data_us_1d_latest.zip"
GME = "https://raw.githubusercontent.com/wumiq/us_stock_eod/main/G/GME.csv"

z = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(QLIB).read()))
cal = pd.to_datetime(z.read("calendars/day.txt").decode().split())


def load(sym, field):
    """Qlib .bin file: first float32 = position of the first date in the calendar, then one float32 per day."""
    a = np.frombuffer(z.read(f"features/{sym}/{field}.day.bin"), dtype="<f4")
    start, values = int(a[0]), a[1:].astype(float)
    return pd.Series(values, index=cal[start:start + values.size])


sp = pd.DataFrame({"sp500_ret": load("^gspc", "change"), "sp500_close_norm": load("^gspc", "close"),
                   "spy_ret": load("spy", "change")}).loc["2018-12-31":"2020-08-31"]
sp.index.name = "date"
sp.to_csv("sp500_yahoo.csv")
pd.read_csv(io.BytesIO(urllib.request.urlopen(GME).read())).to_csv("gme_yahoo.csv", index=False)
print("written: sp500_yahoo.csv, gme_yahoo.csv")
