#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import os

import jinja2
from bs4 import BeautifulSoup

INDEX_HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
	<title>{{book_name}}</title>
	<style>
		body {
			display: flex;
			flex-direction: row;
			height: 100vh;
			margin: 0;
			padding: 0;
		}

		#nav {
			flex: 1;
            position: relative;
			top: 0;
			left: 0;
			height: 100%;
			overflow-y: auto; /* 添加滚动条 */
		}

		#content {
			flex: 4;
			border: none;
			height: 100%;
            position: relative;
			overflow-y: auto; /* 添加滚动条 */
		}
	</style>
</head>
<body>
	<div id="nav">
		<ul>
		    {% for (text, url) in items %}
			<li><a href="{{url}}" target="content">{{text}}</a></li>
			{% endfor %}
		</ul>
	</div>
	<iframe id="content" name="content" src="{{first_page}}"></iframe>
</body>
</html>

"""


def handle_directory(dir):
    book_name = os.path.split(dir)[-1]
    old_index = dir + '/_index.html'
    new_index_template = jinja2.Template(INDEX_HTML_TEMPLATE)
    bs = BeautifulSoup(open(old_index).read(), 'html.parser')
    links = bs.find_all('a')
    items = []
    for link in links:
        text = link.text
        url = link.attrs['href']
        items.append((text, url))
    ctx = {
        'items': items,
        'first_page': items[0][1],
        'book_name': book_name
    }
    data = new_index_template.render(**ctx)
    new_index = dir + '/index.html'
    with open(new_index, 'w') as fh:
        fh.write(data)

def main():
    import sys
    for dir in sys.argv[1:]:
        handle_directory(dir)

if __name__ == '__main__':
    main()
