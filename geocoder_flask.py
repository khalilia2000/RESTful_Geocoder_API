"""
Created on Friday Dec 1, 2017 19:53:37 2017

@author: ali khalili
"""

# import starndard libraries
import json
import urllib
import argparse

# Use flask framework
from flask import Flask, request, jsonify
app = Flask(__name__)

# google api code - not a good practice to have it exposed, but OK for this api
google_api_key = "AIzaSyAXNj1dI0hX41ekKNJIYk9zE09-7n-_9S0"
# mapquest api code - not a good practice to have it exposed, but OK for this api
mapquest_api_key = "SP0GUfBbmngjpLBShIq0YObi1PDZan9g"


def geocode_by_google(input_location):
    '''
    Use google map api to get the lat and long for the input_loation.
    
    Parameters:
        input_location: A string specifyign the address.
    
    Return:
        return a dictionary with keys: 'lat' and 'lng' with corresponding lat/long values
    '''
    
    # replace all spaces with + to be compliant with google maps api
    location_string = input_location.replace(" ", "+")
    # insert the location string and the google api key
    raw_url = 'https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'
    url = raw_url.format(location_string, google_api_key)
    
    try: 
        # send a GET request and process the response into a json dictionary
        response = urllib.request.urlopen(url)
        result = json.loads(response.read())
    except Exception:
        print('Exception raised in geocode_by_google()')
        return False
    
    if result['status'] != 'OK':
        # not successful response
        return False
    else:
        # successful response
        lat_long_dict = result['results'][0]['geometry']['location']
        return lat_long_dict


def geocode_by_mapquest(input_location):
    '''
    Use mapquest api to get the lat and long for the input_loation.
    
    Parameters:
        input_location: A string specifyign the address.
    
    Return:
        return a dictionary with keys 'lat' and 'lng' with corresponding lat/long values.
    '''

    # replace all spaces with + to be compliant with google maps api
    location_string = input_location.replace(" ", "+")
    # insert the location string and the mapquest api key
    raw_url = 'http://www.mapquestapi.com/geocoding/v1/address?key={}&location={}'
    url = raw_url.format(mapquest_api_key, location_string)
    
    try:
        # send a GET request and process the response into a json dictionary
        response = urllib.request.urlopen(url)
        result = json.loads(response.read())
    except Exception:
        print('Exception raised in geocode_by_mapquest().')
        return False
    
    if result['info']['statuscode'] != 0:
        # not successful response
        return False
    else:
        # successful response
        lat_long_dict = result['results'][0]['locations'][0]['latLng']
        return lat_long_dict
  

def get_lat_long(input_location):
    '''
    Use google maps api as primary service to return the lat and long of the input_location.
    if not successful, use mapquest api as secondary fallback to get lat and long
    
    Parameters:
        input_location: A string specifying the address.
        
    Return:
        return a dictionary with keys 'lat' and 'lng' with corresponding lat/long values.
    '''
    
    # use google maps api first
    result_g = geocode_by_google(input_location)
    if result_g:
        # success
        result_g['service_provider'] = 'google'
        return result_g
    else:
        # use mapquest api as secondary fallback
        result_m = geocode_by_mapquest(input_location)
        if result_m:
            result_m['service_provider'] = 'mapquest'
        return result_m
        

@app.route('/')
def provide_help():
    '''
    send an api syntax error status and show the correct usage of the api.
    '''
    # syntax
    syntax_str = 'HOST:PORT/geocode?address=ADDRESS'
    # description of parameters
    description_str = 'Use the correct syntax in which, '
    description_str += ' HOST is the host server ip address - '
    description_str += ' PORT is the port to use - '
    description_str += ' ADDRESS is the address to be geocoded.'
    # result dictionary
    result =  {'syntax': syntax_str, 'status': 'api syntax error', 'description': description_str}
    # encode in utf-8 before returning
    return jsonify(result)


@app.route('/geocode')
def geocode_address():
    '''
    handle the GET request at /geocode.
    isolate the "address" field in the GET parameters and pass on to get_lat_long function.
    add a status code to the result and retun a json object
    
    Return:
        A jasonified dictionary with the following keys:
            status: "OK", "not successful", or "address is missing"
            service_provider: the 3rd party service provider that was used.
            lat: latitude of the address
            lng: longitude of the address
    '''
    
    # parse the GET arguments and isolate the address
    args = request.args
    if 'address' in args:
        # address argument is passed on
        result = get_lat_long(args['address'])
        if result:
            # success
            result['status'] = 'OK'
        else:
            # no success
            result = {'status': 'not successful'}
        return jsonify(result)
    else:
        # no address argument is passed on
        result = {'status': 'address is missing'}
        return jsonify(result)


def run_server(host, port):
    # initate and run the server
    app.debug = True
    app.run(host=host, port=port)


if __name__ == '__main__':
    
    # parse commandline arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str,
                      default='0.0.0.0', help='Host server ip address.')
    parser.add_argument('--port', type=int, default=5000, help='Port to use.')
    FLAGS, unparsed = parser.parse_known_args()
    
    # initiate and run server
    run_server(FLAGS.host, FLAGS.port)