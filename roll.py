import random
import json
def roll(self):
    dpos = self.index('d')
    try: pluspos = self.index('+')
    except:
        self = self + '+0'
        pluspos = self.index('+')
    d = self[:dpos]
    s = self[dpos+1:pluspos]
    b = self[pluspos+1:]
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
        
class DiceRoll(SlashCommand):
    def post_handler(self):
        return self.data.get("text",[""])[0]
        return Falcon.HTTP_200, self.roll()

app = falcon.API()
roll = roll()
app.add_route('/roll', roll)
