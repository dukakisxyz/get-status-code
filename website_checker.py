#!/usr/local/bin/python
import urllib
from status_codes import check_status

#21 imports
from two1.wallet import Wallet
from two1.bitserv.flask import Payment
import yaml

app1 = flask.Flask(__name__)
payment = Payment(app1, Wallet())

#get website
@app.route('/check_website/<string:website_url>')
@payment.required(500)
def make_password(website_url = None):
	website_url = website_url
	url = "http://"+website_url

	#get status code:
	a = urllib.urlopen(url)
	status = a.getcode()

	try:
		result = check_status(status)
		message = " %s %s" %(website,result)
		return (message)
	except:
		exception = " %s doesn't exist" % (website)
		return (exception)

if __name__ == "__main__":
    app1.run(host="0.0.0.0", port=3000)