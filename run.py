from flask import Flask, request
app = Flask(__name__)
from twilio import twiml
from twilio.twiml.messaging_response import MessagingResponse
import random
from draw_hangman import *
from twilio.rest import Client

@app.route('/sms', methods=['POST'])
def sms():

    #message_body = request.form['Body']

    #resp = MessagingResponse()
    #resp.message('Hello hacker! You guessed: {}'.format(message_body))
    #return str(resp)
    return 0


if __name__ == '__main__':
    app.run()
