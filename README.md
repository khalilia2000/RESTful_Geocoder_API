# RESTful Geocoding Proxy Server API

## Description
RESTful implementations of a Server API are provided here in Python. For a given address, the Server API uses JSON serializatoin to return the lat, long, status, and the service provider that was utilized. The Server API uses [Google Maps API](https://developers.google.com/maps/documentation/geocoding/start) as the primary service. If the the call is not successful, it then uses [Mapquest API](https://developer.mapquest.com/documentation/geocoding-api/address/get/) as a secondary fallback.  
  
Two implementations are provided herein for the aforementioned tasks:  
  * `geocoder_flask.py`:  This version uses the Flask framework.
  * `geocoder_base.py`: This version only uses the base Python libraries.

## How to Download
Run the following code to clone the repo:
```
https://github.com/khalilia2000/RESTful_Geocoder_API.git
cd RESTful_Geocoder_API
```
## How to Run `geocoder_base.py`
Use the following syntax to run the `geocoder_base.py` in a terminal:
```
usage: python geocoder_base.py [-h] [--host HOST] [--port PORT]

optional arguments:
  -h, --help   show this help message and exit
  --host HOST  Host server ip address.
  --port PORT  Port to use.
```
if `--host`, `--port` paramters are not specified, '0.0.0.0' (i.e. localhost) and 5000 are used by default. 

## How to Run `geocoder_flask.py`
Use the following syntax to run the `geocoder_flask.py` in a terminal:
```
usage: python geocoder_flask.py [-h] [--host HOST] [--port PORT]

optional arguments:
  -h, --help   show this help message and exit
  --host HOST  Host server ip address.
  --port PORT  Port to use.
```
if `--host`, `--port` paramters are not specified, '0.0.0.0' (i.e. localhost) and 5000 are used by default. 

## Dependencies
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
  
