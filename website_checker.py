import flask
import urllib.request
from status_codes import check_status
import json

#21 imports
from two1.wallet import Wallet
from two1.bitserv.flask import Payment
import yaml

app = flask.Flask(__name__)
payment = Payment(app, Wallet())
app.debug = True


@app.route("/")
def info():
    return "To check a URL run: $ 21 buy 'http://[fcce:a977:ee7d:817b:3380:0000:0000:0001]:4000/check_website/<www.website.com>'"

#get website
@app.route('/check_website/<string:website_url>')
@payment.required(500)
def make_password(website_url = None):
	website_url = website_url
	url = "http://"+website_url

	try:
        #get status code:
        a = urllib.request.urlopen(url)
        status = a.getcode()
		description = check_status(status)
        message = {status : description}
		return json.dumps(message)
	except:
        exception = {"Exception raised" : "Possibly %s doesn't exist" % (url)}
		return json.dumps(exception)


if __name__ == "__main__":
    app.run(host=”::”, port=4000)
