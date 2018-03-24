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
**Writing unit test cases for REST API's with out authentication:**

- Step-1: Importing pyRest_lib
```
from rest_lib import pyRest_lib
```

- Step-2: Writing the **setUp** method
```
def setUp(self):
        self.rest = pyRest_lib.PyRestLib(url='https://httpbin.org')
        self.log = self.rest.get_logObj()
        self.json = self.rest.get_jsonObj()
 ```
* Creating object for `PyRestLib` class and passing `URL` as parameter.
* Getting logger & Json object

- Step-3: Writing unittests for GET,POST,PUT,DELETE requests.
##### GET
```
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
```
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
```
    def test_put_request(self):
        response = self.rest.send_request('/put',method_name='PUT')
        code = response['code']
        self.assertEqual(code, 200)
```
##### DELETE
```
def test_delete_request(self):
        response = self.rest.send_request('/delete',method_name='DELETE')
        code = response['code']
        self.assertEqual(code, 200)
```

