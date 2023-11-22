# Summarizer-API

**Get the container on Dockerhub**: https://hub.docker.com/repository/docker/lovewaffle/summarizer-api/general

```
import requests
import json

myurl = r"http://<ip>:<port>/summary"
mytext = """<Some big block of text from Wikipedia or whatever>"""

x = requests.post(myurl, json.dumps({'text':mytext}))

## Gotta unpack the JSON response and do work on it
print(x.text)
```
