# OTP Generator

This project uses Flask and PyOTP to generate one-time passwords (OTPs) for authenticating users.

## Requirements
pip install -r requirements.txt

- Flask (1.1.2 or later)
- PyOTP (2.3.1 or later)

## Usage

1. Install the required packages using `pip`:
pip install pyotp
pip install Flask

2. Run the Flask app:


2. Run the Flask app:


The server will generate a new OTP and return it as a JSON object. The OTP will be valid for only a short time (typically 30 seconds), so you should generate a new OTP each time you need to authenticate the user.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
