# OCR Service

testing OCR API using FastAPI to demonstrate asyncio, async, and queueing

### Dependencies
1. Docker
2. Docker-compose


### AsyncIO
Using:
1. aiofile
2. aiopytesseract
3. miniopy_async

### Sync

1. pytesseract


 

### AsyncIO with queue
Using:
1. aiofile
2. aiopytesseract
3. miniopy_async
4. RQ


### Start the service

```
docker-compose build
docker-compose up
```

### API request

Sync
```
curl --location --request POST 'http://127.0.0.1:8000/upload' \
--form 'image=@"/${path}.png"'
```
AsyncIO
```
curl --location --request POST 'http://127.0.0.1:8001s/upload' \
--form 'image=@"/${path}.png"'
```
AsyncIO with queue
```
curl --location --request POST 'http://127.0.0.1:8002/upload' \
--form 'image=@"/${path}.png"'
```


### Stress test

```
 locust -f stress.py
```