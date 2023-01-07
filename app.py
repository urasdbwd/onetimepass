from flask import Flask, request, render_template
import pyotp

app = Flask(__name__)
# Generate a new random secret key
# The secret key should be shared between the user and the server
secret_key = pyotp.random_base32()


from flask import jsonify


@app.route('/generate', methods=['POST'])
def generate_otp():
    # Generate a new OTP for the current time
    jsondata = request.get_json()
    secret_key = jsondata['otp']

    totp = pyotp.TOTP(secret_key)
    otp = totp.now()

    # Return the OTP to the client as a JSON object
    response = jsonify({'otp': otp})
    response.headers['Access-Control-Allow-Origin'] = '*'

    return response
@app.route('/')
def hi():
    return render_template('index.html')


@app.route('/things.png')
def bye():
    return render_template('things.png')

if __name__ == '__main__':
    app.run()
