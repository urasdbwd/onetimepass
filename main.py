import pyotp

# Generate a new random secret key
# The secret key should be shared between the user and the server
secret_key = "NL3HOZVFFAHD3NQQKCDA3LZEWABKPSAI" #pyotp.random_base32()
print (secret_key)
# Generate a new OTP for the current time
totp = pyotp.TOTP(secret_key)
otp = totp.now()

# Print the OTP
print(otp)