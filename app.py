import requests
import json

token = 'XXX'



# send_msg
# Function that will send the message to the channel
def send_msg(msg):

    headers = {
        'authority': 'discord.com',
        'x-super-properties': 'eyJvcyI6IkxpbnV4IiwiYnJvd3NlciI6IkNocm9tZSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk5LjAuNDg0NC41MSBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTkuMC40ODQ0LjUxIiwib3NfdmVyc2lvbiI6IiIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxNTM2NTUsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
        'dnt': '1',
        'x-discord-locale': 'en-US',
        'x-debug-options': 'bugReporterEnabled',
        'authorization': token,
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
        'accept': '*/*',
        'sec-gpc': '1',
        'origin': 'https://discord.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://discord.com/channels/1015095797689360444/1033419953564561408',
        'accept-language': 'en-US,en;q=0.9',
    }

    json_data = {
        'content': msg,
        'tts': False,
    }

    response = requests.post('https://discord.com/api/v9/channels/1033419953564561408/messages', headers=headers, json=json_data)

    return response

def main():
    # Prompt user to enter it's message
    inputMsg = input('Enter your message: ')
    
    # Send the message
    responseBack = send_msg(inputMsg)
    
    # resopnseBack is a response object
    # Parse the response to json
    responseBack = json.loads(responseBack.text)

main()
