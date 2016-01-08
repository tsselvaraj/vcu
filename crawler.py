from pattern.web import Crawler

class Wally(Crawler):
    def visit(self, link, source=None):
        print 'visited:', repr(link.url), 'from:', link.referrer

    def fail(self, link):
        print 'failed:', repr(link.url)

p = Wally(links=['http://www.cnn.com/'], delay=1)
while not p.done:
    p.crawl(method=2, cached=False, throttle=1)
