import sys, time, os
import requests
import random

if len(sys.argv) < 2:
    print('error: no username')
    exit(-1)

username = sys.argv[1]
stop = False
offset = 0
s = requests.Session()

if len(sys.argv) == 4:
    # it comes with username and password
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    payload = { 'username': sys.argv[2], 'password': sys.argv[3], 'remember': 'on', 'challenge': 0, 'referer': 'https://www.deviantart.com/', 'csrf_token': 'XPnfEonyYbhjcFvB.q39n6v.R3mJwhoRPQJVieydoFspqZQZlnYhz-TV7UA_915TRUs' }
    r = s.post('https://www.deviantart.com/_sisu/do/signin', data=payload, headers=headers)
    if r.status_code != 301:
        with open('403.html', 'wb') as handler:
            handler.write(r.content)
            print('request failed')

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

while not stop:
    r = s.get('https://www.deviantart.com/_napi/da-user-profile/api/gallery/contents?username={}&offset={}&limit=24&all_folder=true&mode=newest'.format(username, offset))
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