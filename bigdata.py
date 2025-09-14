# Step 1: Import the required libraries
# 'requests' is used to make HTTP requests (accessing the URL)
# 'json' is used to pretty-print JSON data (optional, but very useful)
import requests
import json

# Step 2: Define the API endpoint
# I chose 'routes_prop_stats_geo.json' because its description says
# "contains a list of all routes... along with the latest statistics."
# This seems to be the most interesting and dynamic dataset.
API_URL = "http://data.addinsight.com/ACT/routes_prop_stats_geo.json"

print(f"Trying to fetch data from: {API_URL}")

# Step 3: Use 'try...except' block for error handling
# This is good practice in case your internet connection drops
# or the server is temporarily unavailable.
try:
    # Send a GET request to the API URL
    response = requests.get(API_URL)

    # Check if the request was successful (status code 200 means 'OK').
    # If there’s an error (like 404 Not Found), this will raise an exception.
    response.raise_for_status()

    # Convert the response from JSON (text) into a Python object (list/dictionary)
    data = response.json()

    print("✅ Data successfully fetched!")
    print("-" * 20)

    # Step 4: Process and display the received data
    
    # Check the data type and the available keys
    print(f"Response data type: {type(data)}")
    print(f"Available keys: {list(data.keys())}")

    # If the data is a dict and contains 'features', extract it
    if isinstance(data, dict) and "features" in data:
        routes = data["features"]
    elif isinstance(data, list):
        routes = data
    else:
        print("⚠️ Data format not recognized.")
        routes = []

    print(f"Found traffic data for {len(routes)} routes.")

    # Show a raw example of the first route
    if routes:
        print("\nHere is a raw example of the first route data:")
        print(json.dumps(routes[0], indent=2))
        print("-" * 20)

    # Show some traffic stats
    print("\nLatest traffic statistics for a few routes:")
    for route in routes[:5]:
        # For GeoJSON, properties are usually stored in route['properties']
        props = route.get("properties", route)
        route_name = props.get("Name", "Name not available")
        travel_time = props.get("TT", 0)
        delay = props.get("Delay", 0)
        travel_time_minutes = travel_time // 60
        travel_time_seconds = travel_time % 60

        print(
            f"\n📍 Route: {route_name}\n"
            f"   - Current Travel Time: {travel_time_minutes} minutes {travel_time_seconds} seconds\n"
            f"   - Delay: {delay} seconds compared to normal conditions"
        )

# Error handling
except requests.exceptions.HTTPError as errh:
    print(f"❌ HTTP Error: {errh}")
except requests.exceptions.ConnectionError as errc:
    print(f"❌ Connection Error: {errc}")
except requests.exceptions.Timeout as errt:
    print(f"❌ Timeout Error: {errt}")
except requests.exceptions.RequestException as err:
    print(f"❌ An unexpected error occurred: {err}")
