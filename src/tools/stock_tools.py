import requests
import datetime
import json

# ── Tool 1: Cafef ──────────────────────────────────────────────

def fetch_Cafef_stock(stock_name: str) -> str:
    """
    Fetch historical daily stock data from Cafef for a Vietnamese stock ticker.
    Input: stock ticker symbol (e.g. "VNM", "FPT", "VIC").
    Returns: JSON string with the latest 5 trading days (date, open, high, low, close, volume).
    """
    ticker = stock_name.upper()
    mock_data = [
        {"ticker": ticker, "date": "2025-06-02", "open": 90000, "high": 92000, "low": 89500, "close": 91000, "volume": 1200000},
        {"ticker": ticker, "date": "2025-06-03", "open": 91000, "high": 93000, "low": 90500, "close": 92500, "volume": 1350000},
        {"ticker": ticker, "date": "2025-06-04", "open": 92500, "high": 94000, "low": 91800, "close": 93200, "volume": 1100000},
        {"ticker": ticker, "date": "2025-06-05", "open": 93200, "high": 95000, "low": 92000, "close": 94500, "volume": 1500000},
        {"ticker": ticker, "date": "2025-06-06", "open": 94500, "high": 96000, "low": 93800, "close": 95500, "volume": 1400000},
    ]
    return json.dumps(mock_data, ensure_ascii=False)


