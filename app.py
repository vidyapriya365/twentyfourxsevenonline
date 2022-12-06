"""						   :~)
Application Name: HBD Fireworks
Designed and Developed by: Raghav, Kendriya Vidyalaya, Coimbatore. [2021]
Created On: @ August 2021
Last Modified On: % August 2021
Version Info: 1.0
"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Importing Required Libraries
from flask import Flask, render_template
from flask import request, jsonify
from requests import get

import requests
import json


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Routes
app = Flask(__name__)


# Default Home Route
@app.route("/")
def home():
    return render_template("index.html")


# Fireworks Route
@app.route("/Boom", methods=["POST"])
def greet():

    # Initalization
    name = request.form.get("Name")
    name_s = name.strip()
    name_l = name_s.lower()

    # Counter
    VC_File = open("Visitor_Count.txt", "r")
    Counter = VC_File.read()
    Counter = int(Counter)
    Counter += 1

    VCI_File = open("Visitor_Count.txt", "w")
    VCI_File.write(str(Counter))

    # User data
    ip = get("https://api.ipify.org").text
    print(f"NAME~~~{name_l}")

    # Check
    name_list = [
        "24x7 online",
        "poorve",
        "poorvekka",
        "poorvika",
        "poorvekka r",
        "poorvekka rajesh",
    ]

    if name_l in name_list:
        return render_template("Boom.html", NAME="24x7 Online")
    else:
        return render_template("Boom.html", NAME=name_l, VISITOR_COUNT=Counter)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main
if __name__ == "__main__":
    app.run(debug=True)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
