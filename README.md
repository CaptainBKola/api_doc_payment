# Public Rest API for Viddatech Twitter API Consumption

## General API Information

* The base endpoint is: /
* All endpoints return JSON objects

## HTTP Return Codes

* HTTP 4XX return codes are used for malformed requests; the issue is on the sender's side
* HTTP 5XX return codes are used for internal errors; the issue is on Viddatech's side. It is important to NOT treat this as a failure operation; the execution status is UNKNOWN and could have been a success

## General Information on Endpoints

* For GET, POST endpoints, parameters must be sent along the request body
* Parameters may be sent in any order
* All endpoints returns success flag

Sample Payload below:

```JSON
{
    "success": true,
    "message": ""
}
```

## API Error

* Any endpoint can return an ERROR

Sample Payload below:

```JSON
{
    "success": false,
    "message": ""
}
```

## General endpoints

### Say hello

GET `/`

Says hello to the Rest API to test connectivity.

**Response**

```JSON
{
    "success": true,
    "message": "Hello World!"
}
```

### Post Tweet

POST `/post-tweet/`

Create a new transaction

**Parameters**

| Name      | Type    | Mandatory |
| --------- | ------- | --------- |
| consumer_key    | STRING  | YES       |
| consumer_secret    | STRING | YES       |
| access_token | STRING  | YES       |
| access_token_secret | STRING  | YES       |
| tweet | STRING  | YES       |



**Response**

```JSON
{
    "success": true,
    "Name": "",
    "Location": "",
    "Friend": ""
}
```

### Get Tweets

GET `/get-tweet/`

Get all account transactions

**Parameters**

| Name      | Type    | Mandatory |
| --------- | ------- | --------- |
| consumer_key    | STRING  | YES       |
| consumer_secret    | STRING | YES       |
| access_token | STRING  | YES       |
| access_token_secret | STRING  | YES       |
| username | STRING  | YES       |
**Response**

```JSON
{
    "success": true,
    "tweet": "",
    "created_at": "",
    "username": "",
    "headshot_url": "",
   
}
```
