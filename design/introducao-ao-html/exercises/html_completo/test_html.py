from pathlib import Path
import re
from html.parser import HTMLParser


PWD = Path(__file__).parent
arquivo_html = PWD / 'exemplo.html'


def clear_spaces(s):
    return re.sub(r'\s+', ' ', s).strip()


class TreeNode:
    def __init__(self, parent=None):
        self.parent = parent
        self.closed = True
        self.children = []
        self.text = None

    def get_text(self):
        return self.text

    def valid(self):
        return True

    def find(self, *args, **kwargs):
        return None

    def find_all(self, *args, **kwargs):
        return []

    def to_str(self, indent):
        return f'{indent * " "}{self}'


class Text(TreeNode):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.text = text

    def __str__(self):
        return self.text


class HTMLElement(TreeNode):
    def __init__(self, tag=None, attrs=None, parent=None):
        super().__init__(parent)
        self.tag = tag
        self.self_closing = tag in [None, 'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr']
        self.closed = self.self_closing
        self.attrs = attrs

        if self.attrs:
            self.attrs = dict(self.attrs)

    def add_child(self, tag, attrs):
        new_element = HTMLElement(tag, attrs, self)
        self.children.append(new_element)
        return new_element

    def add_text(self, text):
        self.children.append(Text(clear_spaces(text), self))

    def get_text(self):
        return ' '.join([c.get_text() for c in self.children]).strip()

    def to_str(self, indent=0):
        s = ' ' * indent

        children_str = ''
        if self.children:
            children_str = '\n' + '\n'.join(c.to_str(indent + 2) for c in self.children)

        return f'{s}[{self.tag}{f"({self.attrs})" if self.attrs else ""}{children_str}\n{s}]'

    def find(self, tag):
        if self.tag == tag:
            return self
        for c in self.children:
            found = c.find(tag)
            if found:
                return found
        return None

    def find_all(self, tag):
        found = []
        if self.tag == tag:
            found.append(self)
        for c in self.children:
            found += c.find_all(tag)
        return found

    def valid(self):
        if not self.closed:
            return False
        for c in self.children:
            if not c.valid():
                return False
        return True

    def __str__(self):
        return self.to_str()


class TreeHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.root = HTMLElement()
        self.cur_element = self.root
        self.errors = []

    def handle_starttag(self, tag, attrs):
        self.cur_element = self.cur_element.add_child(tag, attrs)

    def handle_endtag(self, tag):
        while self.cur_element and tag != self.cur_element.tag and self.cur_element.self_closing:
            self.cur_element = self.cur_element.parent
        if tag != self.cur_element.tag:
            self.errors.append(f'A tag {tag} não foi fechada corretamente')
        else:
            self.cur_element.closed = True
            self.cur_element = self.cur_element.parent

    def handle_data(self, data):
        self.cur_element.add_text(data)

    def valid(self):
        return self.root.valid()

    def __str__(self):
        return str(self.root)


def carrega_html():
    with open(arquivo_html) as f:
        return f.read()


def parse_html(html):
    tree = TreeHTMLParser()
    tree.feed(html)
    assert len(tree.errors) == 0, '\n'.join(tree.errors)
    return tree


def test_corrige_titulo():
    tree = parse_html(carrega_html())
    h1s = tree.root.find_all('h1')
    assert len(h1s) > 0,'Não encontrei a tag h1'
    assert len(h1s) < 2,'Deveria ter apenas uma tag h1 no documento'
    text = h1s[0].get_text().lower()
    assert 'senoura' not in text and 'cenoura' in text, 'Não corrigiu o erro de grafia'


def test_html_valido():
    tree = parse_html(carrega_html())
    assert tree.valid(), 'Alguma tag não foi fechada corretamente'


def test_src_correto():
    tree = parse_html(carrega_html())
    imgs = tree.root.find_all('img')
    assert len(imgs) > 0,'Não encontrei a tag img'
    assert len(imgs) < 2,'Você não deveria ter adicionado outra tag img neste documento'
    img = imgs[0]
    assert img.attrs['src'] == 'img/exemplo.png', 'Não corrigiu o erro de grafia'
