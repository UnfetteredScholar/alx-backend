#!/usr/bin/env python3
"""Task 0: A basic flask application"""
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.get("/", strict_slashes=False)
def index() -> str:
    """Gets the index page"""

    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
