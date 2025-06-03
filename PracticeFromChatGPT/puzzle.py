import requests
import json
import base64

# --- Your Name and Email (kept for context) ---
your_name = "Ankit Kumar" # Keep your name for context
your_email = "ankitveer54@gmail.com" # Keep your email for context

# --- The Endpoint for Initial Submission (replace with the correct one you found) ---
# This URL is the one that successfully gave you the JWT token.
submission_url = "https://workwithus.lucioai.com/get-started" # Example: "https://workwithus.lucioai.com/api/register"

# --- Manually paste the JWT token you received ---
# Ensure this is the exact token from your last successful run
jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiQW5raXQgS3VtYXIiLCJlbWFpbCI6ImFua2l0dmVlcjU0QGdtYWlsLmNvbSIsImRhdGUiOiIyMDI1LTA1LTI3IDE2OjQzOjQyIn0.clhncI5wk9xAEafZjzbk2-O1ySG4_tGaINd4VHHkaJ4"


print("\n--- Decoding the JWT Token (from previous step's output) ---")
try:
    header_encoded, payload_encoded, signature = jwt_token.split('.')
    def base64url_decode(input_string):
        decoded_bytes = base64.urlsafe_b64decode(input_string + '==')
        return decoded_bytes.decode('utf-8')

    header_decoded_json = json.loads(base64url_decode(header_encoded))
    payload_decoded_json = json.loads(base64url_decode(payload_encoded))

    print("JWT Header (Decoded):")
    print(json.dumps(header_decoded_json, indent=2))
    print("\nJWT Payload (Decoded):")
    print(json.dumps(payload_decoded_json, indent=2))

except Exception as e:
    print(f"Error decoding JWT: {e}")
    exit()

# --- NEW STEP: Interact with the "Bouncer" ---
# Common endpoint guesses: /bouncer, /club, /entrance, /next_stage
# If this fails, you MUST re-examine the website (source code, network tab)
# for a specific endpoint hint.
bouncer_url = "https://workwithus.lucioai.com/bouncer" # Common guess for the next stage

print(f"\n--- Attempting to enter the club via: {bouncer_url} ---")
print(f"Sending JWT in Authorization header: Bearer {jwt_token[:30]}...") # Print first 30 chars

headers = {
    "Authorization": f"Bearer {jwt_token}",
    # Content-Type is usually not needed for a GET request with only headers,
    # but won't hurt if kept.
    # "Content-Type": "application/json"
}

try:
    bouncer_response = requests.get(bouncer_url, headers=headers)
    bouncer_response.raise_for_status() # Raise an exception for HTTP errors (4xx or 5xx)

    print("\n--- Response from the Bouncer ---")
    print(bouncer_response.text)

except requests.exceptions.RequestException as e:
    print(f"Error accessing the bouncer: {e}")
    if hasattr(e, 'response') and e.response is not None:
        print(f"Bouncer Server response text: {e.response.text}")
    print("\nPossible issues:")
    print("- The 'bouncer_url' might be incorrect. This is the most likely issue.")
    print("- The JWT token might be invalid or expired (less likely given it was just issued).")
    print("- Other required headers are missing (less likely for initial bouncer step).")