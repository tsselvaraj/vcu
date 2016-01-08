from pattern.web import Crawler
from pattern.web import download
from pattern.web import plaintext

class Polly(Crawler):
    def visit(self, link, source=None):
        print 'visited:', repr(link.url), 'from:', link.referrer
        print plaintext(download(link.url))

    def fail(self, link):
        print 'failed:', repr(link.url)

p = Polly(links=['http://www.cnn.com/'], delay=1)
while not p.done:
    p.crawl(method=2, cached=False, throttle=1)
