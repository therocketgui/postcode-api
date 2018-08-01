# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request, redirect, send_file, make_response, jsonify
import io
import csv
import json
import os
from postcode import Postcode
# from cStringIO import StringIO

app = Flask(__name__)

#
@app.route('/postcode', methods=['GET', 'POST'])
def view_index():
    try:
      # data = request.get_json()
      postcode = Postcode(request.form['company'] + ' ' + request.form['city'])
      response = postcode.run()

      data = {'company': request.form['company'],
              'city': request.form['city'],
              'address': response}

      if response is not None:
        return jsonify(success=True,
                       data=data)

      else:
        return jsonify(success=True,
                       data=None)
    except Exception as e:
      return jsonify(success=False,
                     data=None,
                     error=str(e))

if __name__ == '__main__':
    app.run(debug=True, port=12345)
