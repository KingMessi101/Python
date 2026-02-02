import requests
url = "https://uselessfacts.jsph.pl/random.json?language=en"

def get_random_fact():
    try:
        response = requests.get(url, timeout = 5)
        if response.status_code == 200:
            data = response.json()
            print("did You know?", data["text"])
        else:
            print("server Error")
    except requests.exceptions.RequestException:
       print("network issue or API down")

while True:
     user_input = input("Press enter to get random fact or press 'q' to quit: ")

     if user_input.lower() == 'q':
        break 
     get_random_fact()