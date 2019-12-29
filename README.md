# DAGD - DeviantArt Gallery Downloader
You need to install `requests` for it to work. 

## Setup
You need to create a file called `my_cookie.py` next to `DAGD.py` with one line of code inside
~~~python
cookie = '<INSERT YOUR COOKIE HERE>'
~~~

### How to get Cookie
- `Sign in` inside your browser and launch `dev tools`.
- Go to `Network` and find `https://www.deviantart.com/` (or your current link, if it's not there, simply refresh your webpage)
- Go to `Headers` -> `Request Headers` -> `cookie`
- Copy and paste it inside `my_cookie.py`

## Usage
~~~
./DAGD.py [username]
~~~
It will then download all media from that user until it reaches the `LIMIT`
