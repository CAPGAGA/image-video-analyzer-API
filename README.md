# Video frames analyzer API

## How to use:

### Setup and run

Clone this repository with `git clone git@github.com:CAPGAGA/image-video-analyzer-API.git`

Setup with docker compose via `docker-compose up -d`

After that, you can access API via `localhost/docs` or `127.0.0.1/docs` depending on your local DNS setup

## API endpoints and what they do

To submit your video for analysis use `POST` request to the `/analysis` endpoint with fields media file in request body

example:

```
curl -X 'POST' \
  'http://127.0.0.1:8000/analysis/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'media=@855538-hd_1920_1080_25fps.mp4;type=video/mp4'
```

example of successful respond:

```
{"requestId": 18}
```

`requestId` is an id of submitted file, which can be used to analysis data about of each frame of the video as shown in next example

To get information of each frame use `GET` request with `reuqestId` in URL as shown: 

example:

```
curl -X 'GET' \
  'http://127.0.0.1:8000/analysis/18/' \
  -H 'accept: application/json'
```

example of successful respond:

```
[
  {
    "file_id": 18,
    "result": "African elephant, Loxodonta africana",
    "id": 1,
    "created": null
  },
  {
    "file_id": 18,
    "result": "African elephant, Loxodonta africana",
    "id": 2,
    "created": null
  },
  {
    "file_id": 18,
    "result": "African elephant, Loxodonta africana",
    "id": 3,
    "created": null
  },
  ...
]
```

Keep in mind that analysis is done in background, so results might not be accessible right away!

To delete analysis results send `DELETE` request with `requestId` in URL as shown:

example:

```
curl -X 'DELETE' \
  'http://127.0.0.1:8000/analysis/18/' \
  -H 'accept: application/json'
```

there will be no response here if all is successful


