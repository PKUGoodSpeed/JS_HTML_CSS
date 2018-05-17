"""
@author: PKUGoodSpeed
Creating HTML page for plotly
"""
from basic import *


def parseDate(date):
    yyyy = str(date)[: 4]
    mm = str(int(str(date)[4: 6]) - 1)
    dd = str(date)[6:]
    return "new Date({Y}, {M}, {D})".format(Y=yyyy, M=mm, D=dd)


def getLineObj(x, y, name, color):
    """ Getting a plotly line object """
    obj = {
        'x': x,
        'y': y,
        'type': 'scatter',
        'name': name,
        'line': {
            'color': color
        }
    }
    return dictToString(obj)


def getScattorObj(x, y, text, name, color, size=8):
    """ Getting a plotly scatter object """
    obj = {
        'x': x,
        'y': y,
        'text': text,
        'type': 'scatter',
        'mode': 'markers',
        'name': name,
        'marker': {
            'size': size,
            'color': color
        }
    }
    return dictToString(obj)


def getBarObj(x, y, name, color):
    """ Getting a plotly bar object """
    obj = {
        'x': x,
        'y': y,
        'name': name,
        'type': 'bar',
        'line': {
            'color': color
        }
    }
    return dictToString(obj)


def getPieObj(vals, labels, colors):
    obj = {
        "values": vals,
        "labels": labels,
        "colors": {
            "colors": colors
        }
    }
    return dictToString(obj)


def getLayOut(layout_name, layout_map):
    """
    Getting plotly layout settings
    :param layout_map: layout options
    :return: a string with a layout name
    """
    out_str = str(layout_name) + " = " + dictToString(layout_map)
    return out_str


def getPlotlyPlot(where, content, layout):
    """
    Getting a plotly plot
    :param where: where to show the plot
    :param content: variable to plot
    :param layout: plot layout settings
    :return: script in form of string
    """
    return "Plotly.plot({W_VAR}, {C_VAR}, {L_VAR})".format(W_VAR=where, C_VAR=content, L_VAR=layout)


def makeHTML(body, html_file, page_name="Simulation"):
    """ Creating html page by passing in a body block """
    with open(html_file, "w") as f:
        f.write("""
<html>
<head>
<title>{PNM}</title>
<style>
table.sortable thead {{
background-color:#eee;
color:#666666;
font-weight: bold;
cursor: default;
}}
table.sortable td {{
text-align: right;
}}
a {{
color: cyan;
}}
a:visited {{
color: gray;
}}
</style>
<script src="https://kryogenix.org/code/browser/sorttable/sorttable.js"></script>
<!-- Plotly.js -->
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
{BODY}
</body>
</html>
        """.format(PNM=page_name, BODY=body))


if __name__ == "__main__":
    import html_utils as hu
    body = hu.getHeader("Test Page")
    body += hu.getParagraph(hu.getBoldText("testing"))
    body += hu.getDivision(div_id="test_div")
    data = "data = [\n"
    data += getBarObj([1, 2, 3], [2, 1, 2], "case#1", color="blue") + ",\n"
    data += getBarObj([1, 2, 3], [4, 2, 1], "case#2", color="red") + ",\n"
    data += getBarObj([1, 2, 3], [3, 3, 3], "case#3", color="orange") + "\n]\n"
    body += hu.getScript(data)
    layout = {
        "title": "test plot",
        "width": 500,
        "height": 300,
        "margin": {
            'l': 50,
            'r': 50,
            't': 100,
            'b': 50,
            'pad': 10
        }
    }

    body += hu.getScript(getLayOut("layout", layout))
    body += hu.getScript(getPlotlyPlot(hu.getElement("test_div"), "data", "layout"))
    makeHTML(body, "./test.html", page_name="test_page")
