from flask import Flask, request, render_template, session, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

from app import routes
