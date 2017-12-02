# RESTful Geocoding Proxy Server API

### Description
RESTful implementations of a Server API are provided here in Python. For a given address, the Server API uses JSON serializatoin to return the lat, long, status, and the service provider that was utilized. The Server API uses [Google Maps API](https://developers.google.com/maps/documentation/geocoding/start) as the primary service. If the the call is not successful, it then uses [Mapquest API](https://developer.mapquest.com/documentation/geocoding-api/address/get/) as a secondary fallback.  
  
Two implementations are provided herein for the aforementioned tasks:  
  * `geocoder_flask.py`:  This version uses the Flask framework.
  * `geocoder_base.py`: This version only uses the base Python libraries.

### How to Download
Run the following code to clone the repo:
```
https://github.com/khalilia2000/RESTful_Geocoder_API.git
cd RESTful_Geocoder_API
```
### How to Initiate and Run Server API Using The Base Implementation
Use the following syntax to run the `geocoder_base.py` in a terminal:
```
usage: python geocoder_base.py [-h] [--host HOST] [--port PORT]

optional arguments:
  -h, --help   show this help message and exit
  --host HOST  Host server ip address.
  --port PORT  Port to use.
```
if `--host`, `--port` paramters are not specified, '0.0.0.0' (i.e. localhost) and 5000 are used by default. 

### How to Initiate and Run Server API Using The Flask Implementation
Use the following syntax to run the `geocoder_flask.py` in a terminal:
```
usage: python geocoder_flask.py [-h] [--host HOST] [--port PORT]

optional arguments:
  -h, --help   show this help message and exit
  --host HOST  Host server ip address.
  --port PORT  Port to use.
```
if `--host`, `--port` paramters are not specified, '0.0.0.0' (i.e. localhost) and 5000 are used by default. 

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

### How to Use the Server API
The Server API can be querried by using a GET method and specifying the `address` field, using the following URL syntax:  
`HOST:PORT/geocode?address=ADDRESS`
where, 
`HOST`: is the Host Server IP address that is specified during initiating the Server API. By default both implementations map to localhost (http://0.0.0.0) if HOST parameter is not specified during the initiation of the Server API.
`PORT`: is the Port that is specified during initiating the Server API. By default both implementations use Port 5000 if PORT parameter is not specified during the initiation of the Server API.  
`ADDRESS`: is the address that will be geocoded.

The API returns a JSON object similat to below with `lat`, `long`, `status`, and `service_provider` fields.
```
{
  "lat": 49.2827291, 
  "lng": -123.1207375, 
  "service_provider": "google", 
  "status": "OK"
}
```
