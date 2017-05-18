
import os
import flask, flask.views
from flask import Markup
from flask import jsonify
import app.evaluate
import sys

def getInput():
	sentence = input("Enter a sentence: ");
	percentage = evaluate.tweetscore(str(sentence));
	print("Sarcasm score is : (range of -100 to 100) : " + str(percentage));
	
	choice = input("Do you want to continue? (y/n) : ");
	if choice is 'Y' or choice is 'y':
		getInput();

#print("running");
getInput();

