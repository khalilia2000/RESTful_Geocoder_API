# RESTful Geocoding Proxy Services API

## Description
RESTful implementations of a Geocoding Services API in Python are provided herein. For a given address, the Services API uses JSON serialization to return the lat, long, status, and the service provider that was utilized. The Services API uses [Google Maps API](https://developers.google.com/maps/documentation/geocoding/start) as the primary service. If the call is not successful, it then uses [Mapquest API](https://developer.mapquest.com/documentation/geocoding-api/address/get/) as a secondary fallback.  
  
Two implementations are provided herein for the aforementioned tasks:  
  * `geocoder_flask.py`:  This version uses the Flask framework.
  * `geocoder_base.py`: This version only uses the base Python libraries.

## Initiate the Services API
### Download:
Run the following code to clone the repo:
```
https://github.com/khalilia2000/RESTful_Geocoder_API.git
cd RESTful_Geocoder_API
```
### Use The Base Implementation:
Use the following syntax to run the `geocoder_base.py` in a terminal:
```
usage: python geocoder_base.py [-h] [--host HOST] [--port PORT]

optional arguments:
  -h, --help   show this help message and exit
  --host HOST  Host Server IP address.
  --port PORT  Port to use.
```
if `--host`, `--port` parameters are not specified, 'http://0.0.0.0' (i.e. localhost) and 5000 are used by default. 

### Use The Flask Implementation:
Use the following syntax to run the `geocoder_flask.py` in a terminal:
```
usage: python geocoder_flask.py [-h] [--host HOST] [--port PORT]

optional arguments:
  -h, --help   show this help message and exit
  --host HOST  Host Server IP address.
  --port PORT  Port to use.
```
if `--host`, `--port` parameters are not specified, 'http://0.0.0.0' (i.e. localhost) and 5000 are used by default. 

### Dependencies
`geocoder_base.py` uses the following standard Python 3.x libraries to implement the API:
  * argparse
  * http.server
  * json
  * urllib.request

`geocoder_flask.py` uses the Flask framework and the following libraries, and requires Python 3.x:
  * argparse
  * json
  * urllib.request
  * flask

## Usage and Querying
The Services API can be queried by using a GET method and specifying the `address` field, using the following URL syntax:  
`HOST:PORT/geocode?address=ADDRESS`. 
where,   
  * `HOST`: is the Host Server IP address that is specified during the initiation of the Services API. By default, both implementations map to localhost (http://0.0.0.0) if HOST parameter is not specified during the initiation of the Services API.  
  * `PORT`: is the Port that is specified during the initiation of the Services API. By default, both implementations use Port 5000 if PORT parameter is not specified during the initiation of the Server API.    
  * `ADDRESS`: is the address that will be geocoded.  

The API returns a JSON object similar to below with `lat`, `long`, `status`, and `service_provider` fields.
```
{
  "lat": 49.2827291, 
  "lng": -123.1207375, 
  "service_provider": "google", 
  "status": "OK"
}
```

## License
This repository is published under MIT License, except that the API keys that are included in the codes shall not be used without contacting the author.

Copyright (c) 2017 Ali Khalili

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

