# Twilio SMS Proxy

A simple Flask server to securely relay SMS messages to Twilio's API.

## Usage

POST to `/send-sms` with a JSON body:
```json
{
  "To": "+1234567890",
  "From": "+13479527212",
  "Body": "Your message here"
}
