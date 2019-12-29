# API
~~~
https://www.deviantart.com/_napi/da-user-profile/api/gallery/contents
username: string
offset: number
limit: number
all_folder: boolean
mode: string

e.g. https://www.deviantart.com/_napi/da-user-profile/api/gallery/contents?username=?????&offset=24&limit=24&all_folder=true&mode=newest
~~~
As long as you have the username, all images can be retrieved by this link.

## JSON
### Root object
~~~ts
hasMore: boolean,
nextOffset: number,
results: [], // fixed 24 images per requests
comments: {}
~~~

### result
~~~ts
deviation: {}
~~~

#### deviation
~~~ts
url: string
title: string
publishedTime: string
media: {}
~~~

##### media
~~~ts
baseUri: string
prettyName: string
token: [string]
types: []
~~~

###### types
~~~ts
t: string
c: string
~~~

The goal is to check if media exists, the download link will be `baseUri + ?token= + token` or `baseUri + / + c + ?token= + token`
