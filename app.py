from flask import Flask, jsonify, send_from_directory
import random
import os

app = Flask(__name__, static_folder='static')