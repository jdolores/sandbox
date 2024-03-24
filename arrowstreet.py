# Arrowstreet Capital Paired Coding Exam 3/21/24
# Given a Name and a City, store the max credit and max debit in an array of strings.

import urllib
import json
from urllib.request import urlopen

def amount_as_float(amt_str):
    no_dollar = amt_str.strip("$")
    no_comma = no_dollar.replace(",", "")
    return float(no_comma)

def maximum_transfer(name, city):

    # Initialize json data object to read.
    url = "https://jsonmock.hackerrank.com/api/transactions"
    response = urlopen(url)
    data_json = json.loads(response.read())
    data_obj = data_json['data']

    # Initialize output variables.
    output = []
    max_credit = 0.0
    max_debit = 0.0
    max_credit_str = ""
    max_debit_str = ""

    # Iterate through data object and filter only on name and city passed in.
    for datum in data_obj:
        if datum["userName"] == name and datum["location"]["city"] == city:

            # Get the amount string as a float for numeric comparison.
            amt_float = amount_as_float(datum["amount"])

            # Only keep the maximum credit and debit
            if datum["txnType"] == "debit" and amt_float > max_debit:
                max_debit = amt_float
                max_debit_str = datum["amount"]
            if datum["txnType"] == "credit" and amt_float > max_credit:
                max_credit = amt_float
                max_credit_str = datum["amount"]
    
    # Return the output array
    output.append(max_credit_str)
    output.append(max_debit_str)
    return output

#Test Cases
print(maximum_transfer("Bob Martin", "Ilchester"))
print(maximum_transfer("Bob Martin", "Murillo"))
print(maximum_transfer("John Oliver", "Bourg"))
