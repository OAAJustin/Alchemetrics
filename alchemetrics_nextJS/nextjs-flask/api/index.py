from flask import Flask, jsonify

app = Flask(__name__)

def home():
    return