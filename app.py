from flask import Flask, request, render_template
import pyotp

app = Flask(__name__)

# Generate a new random secret key
# The secret key should be shared between the user and the server
secret_key = pyotp.random_base32()


from flask import jsonify


@app.route('/generate/<secret_key>', methods=['POST','GET'])
def generate_otp(secret_key):
    # Generate a new OTP for the current time
    totp = pyotp.TOTP(secret_key)
    otp = totp.now()

    # Return the OTP to the client as a JSON object
    response = jsonify({'otp': otp})
    response.headers['Access-Control-Allow-Origin'] = '*'

    return response
@app.route('/')
def gen():
    return render_template('index.html')
if __name__ == '__main__':
    app.run()
