#!/usr/bin/env python
#coding:utf-8
#Copyright (C) dirlt

import glob
import string
import re
import os
import datetime

domain = 'dirtysalt.github.io'

site = 'https://%s/html/' % (domain)

r1 = re.compile(r'^<meta name="generated" content="')
r2 = re.compile(r'^<p class="date">Date: ')
r3 = re.compile(r'^<a href="http://validator.w3.org/check')
r4 = re.compile(r'^<!-- \d{4}-\d{2}\-\d{2} ')

HTML_DIR = './html/'
ORG_DIR = './org/'
html_files = glob.glob(HTML_DIR + '*.html') + glob.glob(HTML_DIR + 'blogs/*.html')
org_files = glob.glob(ORG_DIR + '*.org') + glob.glob(ORG_DIR + 'blogs/*.org')

codes_link = 'https://github.com/dirtysalt/codes/tree/master/'
invalid_codes_refs = (
    'file:///Users/{user}/repo/dirtysalt.github.io/codes/',
    'file:///Users/{user}/mysite/codes/',
    'file:///home/{user}/repo/dirtysalt.github.io/codes/',
    'file:///home/{user}/mysite/codes/',
    'https://github.com/dirtysalt/dirtysalt.github.io/tree/master/codes/'
)
valid_codes_refs = (
    './codes/',
    'codes/'
)


# ============================================================

HEAD_BEGIN = ''
BODY_BEGIN = ''
HEAD_END = ''
BODY_END = ''

# ========== HEAD BEGIN: google sites (deprecated) ==========
X_HEAD_BEGIN = """<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-31377772-3"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-31377772-3');
</script>
""".replace('\n','')

setup_profile = 'simple'
# setup_profile = 'emacs'
# setup_profile = 'yinwang'
# setup_profile = 'org'
with open('./themes/%s-setup.txt' % setup_profile) as fh:
    HEAD_END = fh.read().replace('root/','/').replace('\n','')

# ========== BODY END: disqus page (deprecated) ==========

DISQUS_BODY_END = """
<div id="content">
<!-- DISQUS BEGIN -->
<div id="disqus_thread"></div>
<script>

/**
*  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
*  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables*/
var disqus_config = function () {
this.page.url = 'https://%(domain)s/html/%(site_id)s';
this.page.identifier = '%(site_id)s';
};
(function() {
var d = document, s = d.createElement('script');
s.src = 'https://dirlt.disqus.com/embed.js';
s.setAttribute('data-timestamp', +new Date());
(d.head || d.body).appendChild(s);
})();
</script>
<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
<!-- DISQUS END -->
</div>
""".replace('\n','')

# ========== BODY END: giscus ==========
GISGUS_BODY_END = """
<script src="https://giscus.app/client.js"
        data-repo="dirtysalt/dirtysalt.github.io"
        data-repo-id="MDEwOlJlcG9zaXRvcnk3MjYxNjc3Mw=="
        data-category="Announcements"
        data-category-id="DIC_kwDOBFQLRc4CPQvg"
        data-mapping="pathname"
        data-reactions-enabled="1"
        data-emit-metadata="0"
        data-input-position="bottom"
        data-theme="light"
        data-lang="zh-CN"
        data-loading="lazy"
        crossorigin="anonymous"
        async>
</script>
""".replace('\n', '')

BODY_END = GISGUS_BODY_END

# disable giscus
BODY_END = ""

# ============================================================
def replace_codes_link(x):
    user = os.environ.get('USER', 'dirlt')
    for r in invalid_codes_refs + valid_codes_refs:
        r = r.replace('{user}', user)
        x = x.replace('<a href="' + r, '<a href="' + codes_link)
    return x

for f in html_files:
    xs = open(f).readlines()
    site_id = f[len(HTML_DIR):]
    site_title = site_id

    data=[]
    for x in xs:
        x = x[:-1] # strip trailing \n
        if x.find('<head>') != -1 and not x == '<head>' + HEAD_BEGIN + '\n':
            data.append('<head>' + HEAD_BEGIN)
        elif x.find('<body>') != -1 and not x == '<body>' + BODY_BEGIN + '\n':
            data.append('<body>' + BODY_BEGIN)
        elif x.find('</head>') != -1 and not x == HEAD_END + '</head>' + '\n':
            data.append(HEAD_END + '</head>')
        elif x.find('</body>') != -1 and not x == BODY_END%(locals()) + '</body>' + '\n':
            data.append(BODY_END%(locals()) + '</body>')
        elif r1.match(x) or r2.match(x) or r3.match(x) or r4.match(x):
            pass
        else:
            data.append(x)
        if x.find('<title>') !=-1 and x.find('</title>') != -1:
            site_title = x[len('<title>'):-len('</title>')].replace("'", '')
    print('add code to \'%s\''%(f))
    data = map(replace_codes_link, data)

    with open(f, 'w') as fh:
        fh.writelines(map(lambda x: x + '\n', data))


with open('./sitemap.txt', 'w') as fh:
    lines = [site + x[len(HTML_DIR):-4] + 'html\n' for x in html_files]
    lines.sort()
    fh.writelines(lines)

with open('./sitemap.xml', 'w') as fh:
    fh.write("""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">""")
    lines = ['<url><loc>{}</loc></url>\n'.format(
        site + x[len(HTML_DIR):-4] + 'html') for x in html_files]
    lines.sort()
    fh.writelines(lines)
    fh.write('</urlset>\n')
