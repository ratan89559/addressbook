### Create virtual environment

```
$ python3 -m venv venv
```

### Activate virtual environment

```
$ source venv/bin/activate
```

### Intall Requirements
```
$ pip install -r requirements.txt
```

### Run Fast api server

```
$ uvicorn main:app --reload
```

### Open address in Browser

```
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc
```

### Example Create Address payload
```
{
  "email": "user@example.com",
  "name": "string",
  "address1": "string",
  "address2": "string",
  "city": "string",
  "state": "string",
  "zip": 0,
  "latitude": "string",
  "longitude": "string"
}
```


### Example Get Address response
```
{
  "email": "user@example.com",
  "name": "string",
  "address1": "string",
  "address2": "string",
  "city": "string",
  "state": "string",
  "zip": 0,
  "latitude": "string",
  "longitude": "string",
  "id": 1
}
```
