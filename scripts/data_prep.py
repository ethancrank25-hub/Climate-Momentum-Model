import requests

print("Starting NOAA data prep...")

url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/datasets"

headers = {
    "token": "YOUR_NOAA_TOKEN"
}

print("Sending request...")

response = requests.get(url, headers=headers)

print("Request finished")

print("Status code:", response.status_code)

print("Raw response:")
print(response.text)
