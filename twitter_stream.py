from pattern.web import Twitter
import time

s = Twitter().stream('#college')
for i in range(25):
    time.sleep(1)
    s.update(bytes=1024)
    print s[-1].text if s else ''
    s.clear()
