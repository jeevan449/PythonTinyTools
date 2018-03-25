pyRestAuto
==========
<a href="https://codebeat.co/projects/github-com-qaautomation-in-pyrestauto-master"><img alt="codebeat badge" src="https://codebeat.co/badges/5a1193d5-7a47-4a1d-8a0e-a8cd93dbac34" /></a>
[![Build Status](https://travis-ci.org/qaautomation-in/pyRestAuto.svg?branch=master)](https://travis-ci.org/qaautomation-in/pyRestAuto)

Framework for automating WEBSERVICES (REST API's).

#### Introduction
Framework/libraries to automate Webservice's API's.
Development engineers, automation engineers should be able to leverage
`pyRestAuto` for automating their webservices.

#### Features
Few features of `pyRestAuto` Package .
-   light weight and easy of use
-   Modular and reusable libraries
-   REST Authentication & Authorization support
    - HTTPBasicAuth
    - HTTPDigestAuth
    -   jwt
    -   oauth2
-   REST MIME Support
-   HTML Test Reports
-   Better Logging
-   Json parsing capabilities

#### Usage
**Writing unit test cases for REST API's (No authentication):**

- Step-1: Importing pyRest_lib
```python
from rest_lib import pyRest_lib
```

- Step-2: Writing the **setUp** method
```python
def setUp(self):
        self.rest = pyRest_lib.PyRestLib(url='https://httpbin.org')
        self.log = self.rest.get_logObj()
        self.json = self.rest.get_jsonObj()
 ```
* Creating object for `PyRestLib` class and passing `URL` as parameter.
* Getting logger & Json object

- Step-3: Writing unittests for GET,POST,PUT,DELETE requests.
`send_request` single method for sending GET/POST/PUT/DELETE request types.
##### GET
<dl> <dt> HTTP GET request: </dt>
  <dd> https://httpbin.org/get</dd>
<dt>Response:</dt>
 <dd>{
  "args": {},
  "headers": {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "close",
    "Cookie": "_gauges_unique_year=1; _gauges_unique=1; _gauges_unique_month=1; _gauges_unique_hour=1; _gauges_unique_day=1",
    "Host": "httpbin.org",
    "Referer": "https://httpbin.org/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0"
  },
  "origin": "36.255.85.10",
  "url": "https://httpbin.org/get"
}</dd></dl>

* Passing `path` and request `method type` as passing parameters to send_request.
* return object `response` contains response data,code and headers and that can be accessed by `response['data'],response['code'] & response['headers']`.

```python
def test_get_request(self):
        response =  self.rest.send_request('/get',method_name='GET')
        response_code = response['code']
        response_data = response['data']
        verify_host = self.json.get_key_value(response_data,'Host')
        response_headers = response['headers']
        self.assertEqual(response_code,200)
        self.assertEqual(verify_host,'httpbin.org')
```

##### POST
```python
def test_post_request(self):
        data = {'test':'post'}
        json_data = self.json.dump_json_data(data)
        response = self.rest.send_request('/post',method_name='POST',
                                          parameters=json_data)
        response_code = response['code']
        response_data = response['data']
        verify_response_data = self.json.get_key_value(response_data,'test')
        self.assertEqual(response_code, 200)
        self.assertEqual(verify_response_data,'post')
```
##### PUT
```python
    def test_put_request(self):
        response = self.rest.send_request('/put',method_name='PUT')
        code = response['code']
        self.assertEqual(code, 200)
```
##### DELETE
```python
def test_delete_request(self):
        response = self.rest.send_request('/delete',method_name='DELETE')
        code = response['code']
        self.assertEqual(code, 200)
```

