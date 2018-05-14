"""
@author: PKUGoodSpeed
Creating Simple HTML elements and make HTML files
"""

def getHeader(content, level=1):
    """ Getting HTML Header """
    return "<h{L}>{CONTENT}</h{R}>\n".format(L=level, CONTENT=content, R=level)


def getNewLine():
    """ Getting HTML line breaker """
    return "<br>"


def getUnderLine(content):
    """ Getting underline text """
    return "<u>{C}</u>".format(C=content)


def getComments(content):
    """ Getting HTML comments """
    return "<!--{C}-->\n".format(C=content)


def getBoldText(content):
    """ Getting bold text """
    return "<b>{C}</b>".format(C=content)


def getParagraph(content):
    """ Getting an HTML paragraph """
    return "<p>{C}</p>\n".format(C=content)


def getSection(content):
    """ Getting an HTML section """
    return "<section>\n{C}\n</section>".format(C=content)


def getDivision(div_id, content="", width=500, height=500, color="white"):
    """ Getting an HTML division """
    return "<div id=\"{ID}\" style=\"width:{W}px;height:{H}px;background-color:{COL}\" onshow></div>\n".format(
        ID=str(div_id), W=str(width), H=str(height), COL=color
    )

def getAbbr(content, abbr):
    """ Getting an HTML Abbr element """
    return "<abbr title=\"{C}\">{AB}</abbr>".format(C=content, AB=abbr)


def getFigure(fig_content, newline=False):
    """ Getting a figure section of HTML """
    s = "<figure>\n{FC}\n</figure>\n".format(FC=fig_content)
    if not newline:
        return s
    return s + "<br>\n"


def getFigureCaption(content):
    """ Getting an HTML figure captions """
    return "\n<figcaption>{C}<figcaption>".format(C=content)


def getImage(src, width=500, height=500):
    """ Getting an HTML image section """
    return "<img src=\"{SRC}\" width=\"{W}\" height=\"{H}\"".format(SRC=src, W=width, H=height)


def getInput(type="text", name="input", value="value"):
    """ Getting an HTML input section """
    return "<input type=\"{T}\" name=\"{N}\" value=\"{V}\">".format(T=type, N=name, V=value)


def getTextArea(rows, cols, msg="Input text here"):
    """ Getting an HTML text block """
    return "<textarea rows=\"{R}\" cols=\"{C}\">\n{M}\n</textarea>".format(R=rows, C=cols, M=msg)


def getOption(key, value):
    """ Getting an HTML option section """
    if type(value) is str:
        return "\t<option value=\"{V}\">{K}</option>\n".format(V=value, K=str(key))
    return "\t<option value={V}>{K}</option>\n".format(V=value, K=str(key))


def getSelection(option_map, newline=False):
    """
    Getting an HTML section element
    :param option_map: mapping from key (display) to value
    :return: return an HTML section
    """
    out_str = "<section>\n"
    for key, val in option_map.items():
        out_str += getOption(key, val)
    out_str += "<section>\n"
    if not newline:
        return out_str
    return out_str + "<br>\n"


def getButton(action, display):
    """ Getting an HTML button """
    return "<button onclick=\"{A}\">{D}</button>".format(A=action, D=display)


def getHyperLink(src, s, style="blank", new_line=False):
    """ Getting an HTML hyperlink """
    s = "<a href=\"{SRC}\" target=\"_{T}\">{S}</a>".format(
        SRC=src, T=style, S=s)
    if not new_line:
        return s
    return s + "\n<br>\n"


def getScript(s):
    """ Getting a JAVA script block"""
    return "<script>\n" + s + "\n</script>\n"


def getElement(name):
    """ Getting an HTML element object in js script """
    return "document.getElementById(\"{NAME}\")".format(NAME=name)
