import random
import json
def roll(d,s,b):
    total = 0
    d = int(d)
    s = int(s)
    b = int(b)
    while d > 0:
        total = total + random.randint(1,s)
        d = d - 1
    final = total + b
    final = str(final)
    output = 'Roll = '
    output = output + final
    return falcon.HTTP_200, output

app = falcon.API()

class SlashCommand():
    def on_get(self, req, resp):
        resp.status, resp.body = self.get_handler()

    def on_post(self, req, resp):
        try:
            self.data = urlparse.parse_qs(req.stream.read())
        except:
            self.data = None
        resp.status, resp.body = self.post_handler()

    def get_handler(self):
        return dummy_handler()

    def post_handler(self):
        return dummy_handler()

  


dpos = text.index('d')
try: pluspos = text.index('+')
except:
    text = text + '+0'
    pluspos = text.index('+')
d = text[:dpos]
s = text[dpos+1:pluspos]
b = text[pluspos+1:]
roll(d,s,b)
