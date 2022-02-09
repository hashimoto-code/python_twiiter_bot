#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      YUTO
#
# Created:     02/09/2021
# Copyright:   (c) YUTO 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    name = "Hello World"
    return name

@app.route('/good')
def good():
    name = "Good"
    return name


if __name__ == '__main__':
    app.run(debug=True)

