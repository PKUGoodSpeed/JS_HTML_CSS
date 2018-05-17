import os
import sys
import numpy as np
import pandas as pd

sys.path.append("../utils")
import basic
import html_utils as hu
import plotly_utils as pu

def _drop_consecutive_dups(df, col):
    # Drop consecutive duplicated rows
    jdg = (df[col[0]].shift() != df[col[0]])
    for i in range(1, len(col)):
        jdg |= (df[col[i]].shift() != df[col[i]])
    return df.loc[jdg]


df = pd.read_csv('../../data/trading/status.csv', dtype={
    'time': np.int64,
    'ask_price': np.float64,
    'bid_price': np.float64
})
df = df[['time', 'ask_price', 'bid_price']]
df = _drop_consecutive_dups(df, ['time', 'ask_price', 'bid_price'])
df.time = df.time
df.ask_price = df.ask_price/1.E8
df.bid_price = df.bid_price/1.E8
df = df.append(
    pd.DataFrame({
        'time': list(np.array(df.time.tolist()[1: ]) - 1),
        'ask_price': df.ask_price.tolist()[: -1],
        "bid_price": df.bid_price.tolist()[: -1]
    })
)
df.sort_values(by='time', inplace=True)
x = df.time.tolist()
y_ap = df.ask_price.tolist()
y_bp = df.bid_price.tolist()
data = "data = [\n"
data += pu.getLineObj(x, y_ap, "ask_price", color="cyan") + ",\n"

df = pd.read_csv("../../data/trading/new.csv", dtype={
    'time': np.int64,
    'order_id': str,
    'side': str,
    'price': np.float64,
    'qty': str
})
df.side = df.side.apply(lambda x: x[0])
df['text'] = df.order_id + "," + df.side + "," + df.qty
data += pu.getScattorObj(df.time.tolist(), df.price.tolist(), df.text.tolist(), "order_new", color="blue", size=8) + ",\n"
id2price = dict([(key, val) for key, val in df[['order_id', 'price']].values])
id2side = dict([(key, val) for key, val in df[['order_id', 'side']].values])
id2qty = dict([(key, val) for key, val in df[['order_id', 'qty']].values])

df = pd.read_csv("../../data/trading/filled.csv", dtype={
    'time': np.int64,
    'order_id': str,
    'side': str,
    'price': np.float64,
    'qty': str
})
df.side = df.side.apply(lambda x: x[0])
df['text'] = df.order_id + "," + df.side + "," + df.qty
data += pu.getScattorObj(df.time.tolist(), df.price.tolist(), df.text.tolist(), "order_filled", color="red") + ",\n"

df = pd.read_csv("../../data/trading/cancel.csv", dtype={
    'time': np.int64,
    'order_id': str
})
df['side'] = df.order_id.apply(lambda x: id2side[x])
df['price'] = df.order_id.apply(lambda x: id2price[x])
df['qty'] = df.order_id.apply(lambda x: id2qty[x])
df['text'] = df.order_id + "," + df.side + "," + df.qty
data += pu.getScattorObj(df.time.tolist(), df.price.tolist(), df.text.tolist(), "order_cancel", color="yellow") + ",\n"

df = pd.read_csv("../../data/trading/canceled.csv", dtype={
    'time': np.int64,
    'order_id': str
})
df['side'] = df.order_id.apply(lambda x: id2side[x])
df['price'] = df.order_id.apply(lambda x: id2price[x])
df['qty'] = df.order_id.apply(lambda x: id2qty[x])
df['text'] = df.order_id + "," + df.side + "," + df.qty
data += pu.getScattorObj(df.time.tolist(), df.price.tolist(), df.text.tolist(), "order_canceled", color="orange") + ",\n"

data += pu.getLineObj(x, y_bp, "bid_price", color="grey") + "\n]\n"
layout = {
    "title": "stgy log",
    "width": 1500,
    "height": 400,
    "margin": {
        'l': 50,
        'r': 50,
        't': 100,
        'b': 50,
        'pad': 10
    }
}
body = hu.getDivision(div_id="stgy_log")
body += hu.getDivision(div_id="integer_pnl")
body += hu.getScript(data)
body += hu.getScript(pu.getLayOut("layout", layout))
body += hu.getScript(pu.getPlotlyPlot(hu.getElement("stgy_log"), "data", "layout"))

df = pd.read_csv("../../data/trading/filled.csv", dtype={
    'time': np.int64,
    'pnl': np.float64
})
df = df[['time', 'pnl']]
df = _drop_consecutive_dups(df, ['time', 'pnl'])

data = "data = [\n"
data += pu.getLineObj(df.time.tolist(), df.pnl.tolist(), "pnl", color="magenta") + "\n]\n"
layout = {
    "title": "integer pnl",
    "width": 1500,
    "height": 400,
    "margin": {
        'l': 50,
        'r': 50,
        't': 100,
        'b': 50,
        'pad': 10
    }
}
body += hu.getScript(data)
body += hu.getScript(pu.getLayOut("layout", layout))
body += hu.getScript(pu.getPlotlyPlot(hu.getElement("integer_pnl"), "data", "layout"))
pu.makeHTML(body, "./test.html", page_name="test_page")