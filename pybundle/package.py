from lxml import html
from .fetch import fetch
from .memoize import memoize

def getAllPkgs():
    tree = html.fromstring(fetch("https://pypi.org/simple"))
    return tree.xpath('//a/text()')