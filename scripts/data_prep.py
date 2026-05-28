scripts/data_prep.py
import requests
print("Starting NOAA data prep...")
url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/datasets"
headers = {
  "token": "YOUR_NOAA_TOKEN"
}
response = request.get(url, headers=headers)
print("Status code:", response.status_code)
print(response.text[:200])
