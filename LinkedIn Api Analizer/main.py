import requests

CLIENT_ID = "***"
CLIENT_SECRET = "***"
AUTORITHATION_URL = "https://www.linkedin.com/oauth/v2/authorization"

parameters = {
    "response_type": "code",
    "client_id": CLIENT_ID,
    "redirect_uri": "https://dev.example.com/auth/linkedin/callback",
    "scope": "r_emailaddress"
}

response = requests.get(AUTORITHATION_URL, params=parameters)
response.raise_for_status()
auth = response.text
print(auth)
