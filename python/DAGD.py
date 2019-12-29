import sys, time
import requests

if len(sys.argv) < 2:
    print('error: no username')
    exit(-1)

username = sys.argv[1]
stop = False
offset = 0

while not stop:
    r = requests.get('https://www.deviantart.com/_napi/da-user-profile/api/gallery/contents?username={}&offset={}&limit=24&all_folder=true&mode=newest'.format(username, offset))
    if r.status_code != 200:
        # quit if http request failed
        break


    json = r.json()
    print(json)
    break
    
    # rest a little bit
    time.sleep(200)