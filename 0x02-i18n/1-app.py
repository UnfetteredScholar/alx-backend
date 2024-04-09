#!/usr/bin/env python3
"""Task 1: A Basic Flask app.
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Flask Babel configuration class"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route("/")
def get_index() -> str:
    """Returns the index (home) page"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
