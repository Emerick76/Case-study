# Case Study 1 – Robinhood Traders and the Case of GameStop

**Course:** MATH 60231A – Financial Econometrics, HEC Montréal (Fall 2026)
**Student:** Emerick Derome
**Instructor:** Rubén Fernández Fuertes

## Contents

| Folder / file | Description |
|---|---|
| `rapport/CS1_report_final.pdf` | Final report (PDF) |
| `rapport/CS1_report_final.docx` | Final report (Word) |
| `code/CS1_code.ipynb` | Notebook that produces every table, figure and number in the report |
| `code/CS1_code.html` | Read-only HTML version of the notebook, with outputs |
| `code/RH_data.csv` | Robinhood holdings (provided with the case) |
| `code/stock_data.csv` | CRSP daily returns of the Robinhood tickers and CRSP value-weighted market (WRDS) |
| `code/sp500_yahoo.csv` | S&P 500 (^GSPC) and SPY daily returns (Yahoo Finance) |
| `code/gme_yahoo.csv` | GameStop daily prices, 2002–2022 (Yahoo Finance) |
| `code/build_market_files.py` | Shows how the two Yahoo files were built (not needed to run the notebook) |
| `code/requirements.txt` | Python packages required |
| `code/tables/` | Tables 1–6 of the report (CSV) and `report_numbers.json` (numbers quoted in the text) |
| `code/figures/` | Figures 1–6 of the report (PNG) |

## How to run the code

1. **Get the files.** Download the repository (green **Code** button → **Download ZIP**), then **extract the zip** before opening anything. Files opened directly inside a zip cannot be saved or run properly.
2. **Install Python 3** (e.g., with Anaconda) and the required packages. In a terminal opened in the `code` folder:

   ```
   pip install -r requirements.txt
   ```

3. **Open the notebook** `code/CS1_code.ipynb` in Jupyter Notebook, JupyterLab or VS Code (with the Python and Jupyter extensions).
4. **Run everything:** *Kernel → Restart & Run All* (Jupyter) or **Run All** (VS Code). The four CSV files must stay in the same folder as the notebook.

The notebook runs in about 15 seconds. It recreates `tables/` and `figures/`, and the results match the report exactly. No internet connection is needed.

## Data sources

- Robinhood holdings: provided with the case (Sanford, 2026).
- CRSP daily stock file, accessed through Wharton Research Data Services (WRDS).
- Yahoo Finance daily prices: ^GSPC and SPY via the Microsoft Qlib US dataset; GME via the `us_stock_eod` repository.

## Use of AI

This project was made with the help of AI (Claude, Anthropic). This README was written by AI.
