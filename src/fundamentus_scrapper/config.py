BASE_URL = "https://www.fundamentus.com.br/resultado.php"
FILTERS = {
    # Add your filters here (e.g., 'pl_min': 5, 'roe_min': 10)
}

STOCKS_CONFIG = {
    "Papel": {
        "numeric": False,
        "order": None,
        "convert": False,
        "percent": False,
        "description": "Stock ticker or identifier"
    },
    "Cotação": {
        "numeric": True,
        "order": "desc",
        "convert": True,
        "percent": False,
        "description": "Current stock price"
    },
    "P/L": {
        "numeric": True,
        "order": "asc",
        "convert": True,
        "percent": False,
        "description": "Price-to-Earnings Ratio"
    },
    "P/VP": {
        "numeric": True,
        "order": "asc",
        "convert": True,
        "percent": False,
        "description": "Price-to-Book Ratio"
    },
    "PSR": {
        "numeric": True,
        "order": "asc",
        "convert": True,
        "percent": False,
        "description": "Price-to-Sales Ratio"
    },
    "Div.Yield": {
        "numeric": True,
        "order": "desc",
        "convert": True,
        "percent": True,
        "description": "Dividend Yield (%)"
    },
    "P/Ativo": {
        "numeric": True,
        "order": "asc",
        "convert": True,
        "percent": False,
        "description": "Price-to-Assets Ratio"
    },
    "P/Cap.Giro": {
        "numeric": True,
        "order": "asc",
        "convert": True,
        "percent": False,
        "description": "Price-to-Working Capital Ratio"
    },
    "P/EBIT": {
        "numeric": True,
        "order": "asc",
        "convert": True,
        "percent": False,
        "description": "Price-to-EBIT Ratio"
    },
    "P/Ativ Circ.Liq": {
        "numeric": True,
        "order": "asc",
        "convert": True,
        "percent": False,
        "description": "Price to Net Current Assets"
    },
    "EV/EBIT": {
        "numeric": True,
        "order": "asc",
        "convert": True,
        "percent": False,
        "description": "Enterprise Value / EBIT"
    },
    "EV/EBITDA": {
        "numeric": True,
        "order": "asc",
        "convert": True,
        "percent": False,
        "description": "Enterprise Value / EBITDA"
    },
    "Mrg Ebit": {
        "numeric": True,
        "order": "desc",
        "convert": True,
        "percent": True,
        "description": "EBIT Margin (%)"
    },
    "Mrg. Líq.": {
        "numeric": True,
        "order": "desc",
        "convert": True,
        "percent": True,
        "description": "Net Margin (%)"
    },
    "Liq. Corr.": {
        "numeric": True,
        "order": "desc",
        "convert": True,
        "percent": False,
        "description": "Current Ratio"
    },
    "ROIC": {
        "numeric": True,
        "order": "desc",
        "convert": True,
        "percent": True,
        "description": "Return on Invested Capital (%)"
    },
    "ROE": {
        "numeric": True,
        "order": "desc",
        "convert": True,
        "percent": True,
        "description": "Return on Equity (%)"
    },
    "Liq.2meses": {
        "numeric": True,
        "order": "desc",
        "convert": True,
        "percent": False,
        "description": "2-month average liquidity"
    },
    "Patrim. Líq": {
        "numeric": True,
        "order": "desc",
        "convert": True,
        "percent": False,
        "description": "Shareholder Equity"
    },
    "Dív.Brut/ Patrim.": {
        "numeric": True,
        "order": "asc",
        "convert": True,
        "percent": False,
        "description": "Debt-to-Equity"
    },
    "Cresc. Rec.5a": {
        "numeric": True,
        "order": "desc",
        "convert": True,
        "percent": True,
        "description": "Revenue Growth (5y, %)"
    }
}
