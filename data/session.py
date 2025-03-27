trade_data = []

def add_trade(pair, entry, sl, tp, rr):
    trade_data.append({
        "pair": pair,
        "entry": entry,
        "sl": sl,
        "tp": tp,
        "rr": rr
    })

def get_trades():
    return trade_data

def reset_trades():
    trade_data.clear()
