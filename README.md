# Reverse Geocoding and Geolocation Service MCP Server

## Overview

The **Reverse Geocoding and Geolocation Service** is designed to provide comprehensive geographical insights. By leveraging latitude and longitude coordinates, this server offers a variety of functionalities including city identification, distance calculation, timezone retrieval, and water location checks. It efficiently translates GPS coordinates into human-readable location data, making it invaluable for applications requiring geographical context.

### Key Features

- **City Identification**: Discover the nearest or largest cities based on a specific geographical point. The service identifies cities within a defined radius, providing details such as city name, population, and distance.

- **Distance Calculation**: Determine the distance between two geographical points in meters, kilometers, and miles. The service also provides compass direction and bearing between the two points, along with the names of the start and destination countries.

- **Timezone Information**: Retrieve timezone details for any given coordinate. This includes the timezone name, ID, and the current local time at the specified location.

- **Water Location Check**: Assess whether a specific geographical point is located on water, such as a sea or lake. The service returns a simple true/false response indicating the presence of water.

## Detailed Tool Usage

### Reverse Geocoding (City Places Lookup)

- **Get Nearest Cities**: Returns the three nearest cities to a specified latitude and longitude. Provides details such as city name, population, country, and distance.

- **Get Largest Cities**: Identifies the five largest cities within a specified radial range from a given point. Returns information including city name, population, country, and distance.

### Distance Measurement

- **Get Distance**: Calculates the distance between two sets of latitude and longitude coordinates. Outputs the distance in multiple units along with the compass direction and bearing, including country information for both points.

### Timezone Retrieval

- **Get Timezone**: Finds and returns timezone information for a specified geographical location, including the timezone name, ID, and current local time.

### Water Location Verification

- **Is On Water**: Checks if a given geographical coordinate is situated on water. Determines whether the coordinate is on a sea or lake and returns the result as true or false.

## Database Information

This service utilizes a comprehensive database that includes worldwide cities with a population greater than 5,000. All city population data is updated as of 2023, ensuring accurate and reliable geographical insights.

With these tools, the Reverse Geocoding and Geolocation Service MCP Server provides essential geographical data that can enhance applications across various domains, from navigation and logistics to location-based services and beyond.