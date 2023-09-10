# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 16:53:54 2023

@author: Emin
"""

from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)

URL = "https://kur.doviz.com/"
DECIMAL_PRECISION = 4


def get_currency_value(curr):
    try:
        html_content = requests.get(URL).content
        soup = BeautifulSoup(html_content, 'html.parser')
        currency_value = soup.find('td', {'data-socket-attr': 'ask', 'data-socket-key': curr})
        if currency_value != None:
            return (float(currency_value.text.strip().replace(',', '.')))
        else:
            raise ValueError("Currency code not found on the web page.")
    except (requests.exceptions.RequestException, ValueError, AttributeError) as e:
        raise Exception(f"Error fetching currency value: {e}")
        

def get_currency_rate(curr_from, curr_to):
    try:
        html_content = requests.get(URL).content
        soup = BeautifulSoup(html_content, 'html.parser')
        currency_value1 = soup.find('td', {'data-socket-attr': 'ask', 'data-socket-key': curr_from})
        currency_value2 = soup.find('td', {'data-socket-attr': 'ask', 'data-socket-key': curr_to})
        if currency_value1 != None and currency_value2 != None:
            return (float(currency_value1.text.strip().replace(',', '.')))/(float(currency_value2.text.strip().replace(',', '.')))
        else:
            raise ValueError("Currency codes not found on the web page.")
    except (requests.exceptions.RequestException, ValueError, AttributeError) as e:
        raise Exception(f"Error fetching currency rate: {e}")


@app.route('/convert', methods=['POST'])
def convert_currency():
    try:
        data = request.get_json()
        curr_from = data.get('curr_from').upper()
        curr_to = data.get('curr_to').upper()
        amount = data.get('amount')
        
        if not curr_from or not curr_to or not amount:
            return jsonify({"error": "Missing input data"}), 400
        
        if curr_from == "TRY":
            curr_to_value = get_currency_value(curr_to)
            rate = 1 / curr_to_value
        elif curr_to == "TRY":
            curr_from_value = get_currency_value(curr_from)
            rate = curr_from_value
        else:
            rate = get_currency_rate(curr_from, curr_to)
        
        converted_amount = round(amount * rate, DECIMAL_PRECISION)
        
        return jsonify({"converted_amount": converted_amount}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

