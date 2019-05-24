"""
May 24 2019
cardinalion
"""

from flask import Flask


def create_app():
    app = Flask(__name__)
    return app