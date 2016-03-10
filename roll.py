import random
import json
import falcon


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
	def roll(text):
		dpos = text.index('d')
		try: pluspos = text.index('+')
		except:
			text = text + '+0'
			pluspos = text.index('+')
		d = text[:dpos]
		s = text[dpos+1:pluspos]
		b = text[pluspos+1:]
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
		return output

	def post_handler(self):
		text = self.data.get("text",[""])[0]
		return Falcon.HTTP_200, self.roll(text)
	
class Test(SlashCommand):
    def get_kv(self, log_date):
        """Gets the key / value output for the POSTed data."""
        updt = {  
            "slackup_notes":    self.data.get("text",[""])[0],
            "user_name":        self.data["user_name"][0],
            "user_id":          self.data["user_id"][0],
            "team_id":          self.data["team_id"][0],
            "timestamp":        log_date.isoformat(),
            "date":             log_date.date().isoformat()
        }
        upkey = ':'.join([updt["team_id"], updt["user_id"], "slackup", updt["date"]])
        return upkey, updt

    def post_handler(self):
        """Handles POST requests for Slackup."""
        k, v = self.get_kv(datetime.now())
        return falcon.HTTP_200, v

class SaveRoll(SlashCommand):
	def post_handler():
    		roll = random.randint(1,20)
		if roll == 1:
        		return Falcon.HTTP_200, 'Double Fail!'
    		if roll > 1 and roll < 10:
        		return Falcon.HTTP_200, 'Fail'
    		if roll > 9 and roll < 20:
        		return Falcon.HTTP_200, 'Success'
    		if roll == 20:
        		return Falcon.HTTP_200, 'Critical Success! +1 HP'

app = falcon.API()
diceroll = DiceRoll()
test = Test()
save = SaveRoll()
app.add_route('/roll', test)
app.add_route('/save', save)
