# RESTful Geocoding Proxy Server API

## Description
RESTful implementations of a Server API are provided here in Python. For a given address, the server api uses JSON serializatoin to return the lat, long, status, and the service provider that was utilized. The Server API uses [Google Maps API](https://developers.google.com/maps/documentation/geocoding/start) as the primary service. If the the call is not successful, it then uses [Mapquest API](https://developer.mapquest.com/documentation/geocoding-api/address/get/) as a secondary fallback.  
2 RESTful implementations of the Server API are provided here in this repo to implement a RESTful API for the aforementioned tasks:  
  * `geocoder_flask.py`:  This version uses the Flask framework.
  * `geocoder_base.py`: This version only uses the base Python libraries.

## Installation and Run
