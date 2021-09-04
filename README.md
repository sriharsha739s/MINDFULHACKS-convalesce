# convalesce-MINDFULHACK

These are all the modules required to host locally:

from flask import Flask, render_template, request, redirect, url_for
from train import make_prediction
from flask_sqlalchemy import SQLAlchemy
import time
import random

These are all the modules required for machine learning:

import nltk
import random
import json
import pickle
from nltk.stem.lancaster import LancasterStemmer
import numpy
import tflearn
import tensorflow

***Use pip install or other installation methods for module installation

Once you downloaded all files with necessary modules, then you can just run the python file “main.py” which will then return a local port that the website is hosted on. 

You can use the navigation bar on the top to choose between the multiple features that we offer. The home page is the machine learning chatbot where you can interact with a machine learning chatbot that uses NLP to offer valuable responses to the user.

PLEASE DO KEEP IN MIND THE DATASET IS EXTREMELY SMALL AND WE CAME UP WITH IT WITHIN A DAY FOR THE HACKATHON. FOR BETTER ACCURACY, WE WILL BE COLLECTING MORE DATA. THIS IS TO SHOW FUNCTIONALITY. 

The Memory Bank connects the file to a database which you can access by download “DB Browser for SQLite” and then view all the memory banks that the user inputed under the “posts” column. 

