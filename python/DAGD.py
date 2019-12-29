import sys, time, os
import requests
import random
from my_cookie import cookie

if len(sys.argv) < 2:
    print('error: no username')
    exit(-1)

username = sys.argv[1]
stop = False
offset = 0

def setup_cookie(cookie):
    c = {}
    
    sessions = cookie.split('; ')
    for s in sessions:
        o = s.split('=')
        c[o[0]] = o[1]
    
    return c

def image_link(uri, token):
    '''
    get the image link by merging uri and one of the token
    '''
    t = random.choice(token)
    return '{}?token={}'.format(uri, t)

def image_filename(uri, name):
    '''
    merge the image extension and name
    '''
    extension = uri.split('.')[-1]
    return '{}.{}'.format(name, extension)

da_cookie = setup_cookie(cookie)
print(da_cookie)
while not stop:
    r = requests.get('https://www.deviantart.com/_napi/da-user-profile/api/gallery/contents?username={}&offset={}&limit=24&all_folder=true&mode=newest'.format(username, offset), cookies=da_cookie)
    if r.status_code != 200:
        # quit if http request failed
        break

    print('offset - {}'.format(offset))
    json = r.json()
    if json['hasMore'] == False:
        break

    try:
        json = json['results']
        for result in json:
            media = result['deviation']['media']
            website_link = result['deviation']['url']
            base_uri = media['baseUri']
            token = media['token']

            img_url = image_link(base_uri, token)
            img_name = 'gallery' + image_filename(base_uri, website_link)

            if (os.path.exists(img_name)):
                continue

            image = requests.get(img_url).content
            with open(img_name, 'wb') as handler:
                handler.write(image)
                print(img_name + ' has been downloaded')
    except Exception:
        print('Failed to download image')
        pass
    
    offset += 24
    # rest a little bit
    time.sleep(0.2)

print('\n\nThank you for using DeviantArt Gallery Downloader')