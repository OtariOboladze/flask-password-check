
import sys
import json
from flask import Flask
app = Flask(__name__)


@app.route('/password_check/<password>', methods=['GET', 'POST'])

def password_check(password):

    json_initial_data = '{"length": 10,"must_have_numbers": true,"must_have_caps": true }'
    json_parse = json.loads(json_initial_data)

    if (len(password) <= json_parse["length"]) or (any(char.isdigit() for char in password) is not json_parse["must_have_numbers"]) or (any(char.isupper() for char in password) is not json_parse["must_have_caps"]):
        return False
    else:
        return True


if __name__ == "__main__":
    return password_check()
    app.run(debug=True)
