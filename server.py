import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/Noggle/api/reverse-geocoding-and-geolocation-service'

mcp = FastMCP('reverse-geocoding-and-geolocation-service')

@mcp.tool()
def get_nearest_cities(latitude: Annotated[Union[int, float], Field(description='latitude in decimal degrees (wgs84) Default: 53.55196')],
                       longitude: Annotated[Union[int, float], Field(description='longitude in decimal degrees (wgs84) Default: 9.98558')],
                       range: Annotated[Union[int, float], Field(description='max radial range for lookup in meter (0=no range) Default: 0')]) -> dict: 
    '''Returns a readable place name as nearest 3 cities with population, country and distance based on given latitude/longitude pair.'''
    url = 'https://geocodeapi.p.rapidapi.com/GetNearestCities'
    headers = {'x-rapidapi-host': 'geocodeapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'latitude': latitude,
        'longitude': longitude,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_largest_cities(latitude: Annotated[Union[int, float], Field(description='latitude in decimal degrees (wgs84) Default: 53.55196')],
                       longitude: Annotated[Union[int, float], Field(description='longitude in decimal degrees (wgs84) Default: 9.98558')],
                       range: Annotated[Union[int, float], Field(description='radial lookup range in meters (max 100.000) Default: 50000')]) -> dict: 
    '''Returns 5 largest cities within a given radial range with name, population, country and distance.'''
    url = 'https://geocodeapi.p.rapidapi.com/GetLargestCities'
    headers = {'x-rapidapi-host': 'geocodeapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'latitude': latitude,
        'longitude': longitude,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_distance(lat1: Annotated[Union[int, float], Field(description='latitude in decimal degrees (wgs84) Default: 53.55196')],
                 lon1: Annotated[Union[int, float], Field(description='longitude in decimal degrees (wgs84) Default: 9.98558')],
                 lat2: Annotated[Union[int, float], Field(description='max radial range for lookup in meter (0=no range) Default: 48.87443216181037')],
                 lon2: Annotated[Union[int, float], Field(description='Default: 2.3304897319025466')]) -> dict: 
    '''Distance between two GPS latitude and longitude positions in meters, kilometers and miles. Retrieves compass direction and bearing. Information about start and destination country.'''
    url = 'https://geocodeapi.p.rapidapi.com/GetDistance'
    headers = {'x-rapidapi-host': 'geocodeapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'lat1': lat1,
        'lon1': lon1,
        'lat2': lat2,
        'lon2': lon2,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_timezone(latitude: Annotated[Union[int, float], Field(description='Default: 40.63380384389354')],
                 longitude: Annotated[Union[int, float], Field(description='Default: -74.40753570369408')]) -> dict: 
    '''Finds the local timezone for any given geo-location point by lat and long and returns timezone information with Timezone name, Timezone id and current local time.'''
    url = 'https://geocodeapi.p.rapidapi.com/GetTimezone'
    headers = {'x-rapidapi-host': 'geocodeapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'latitude': latitude,
        'longitude': longitude,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def is_on_water(lat: Annotated[Union[int, float], Field(description='Default: 53.71381')],
                lon: Annotated[Union[int, float], Field(description='Default: 11.45935')]) -> dict: 
    '''Checks whether a GPS coordinate is on water (sea or lake) or not.'''
    url = 'https://geocodeapi.p.rapidapi.com/isonwater'
    headers = {'x-rapidapi-host': 'geocodeapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'lat': lat,
        'lon': lon,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
