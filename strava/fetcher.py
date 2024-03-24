import requests
import json 
import os
from dotenv import load_dotenv

# define constants
PATH = '/data/private'
PER_PAGE=20
STRAVA_API_URL = "https://www.strava.com/api/v3"

# fetch env vars
load_dotenv()

STRAVA_ACCESS_TOKEN = os.getenv("STRAVA_ACCESS_TOKEN")
START_DATE=os.getenv("START_DATE")
END_DATE=os.getenv("END_DATE")

# fetches activities from strava
def fetch_activities():
  session = requests.Session()
  session.headers.update({"Authorization": f"Bearer {STRAVA_ACCESS_TOKEN}"})
  page = 1
  while True:
    response = session.get(
      f"{STRAVA_API_URL}/athlete/activities",
      # params={"after": START_DATE, "before": END_DATE, "per_page": PER_PAGE, "page": page},
      params={"after": START_DATE, "per_page": PER_PAGE, "page": page},
     )
    response.raise_for_status()
    activities = response.json()
    if not activities:
      break
    for activity in activities:
      yield activity
    page += 1
    
# store activity data in json file
def store_activity(activity):
  with open(f"strava/data/private/activities/{activity['id']}.json", "w") as file:
    json.dump(activity, file)

# fetch and store stream from strava
def fetch_and_store_stream_for_activity(activity):
  session = requests.Session()
  session.headers.update({"Authorization": f"Bearer {STRAVA_ACCESS_TOKEN}"})
  response = session.get(
    f"{STRAVA_API_URL}/activities/{activity['id']}/streams",
    params={"keys": "time,heartrate,latlng,distance,altitude,velocity_smooth,cadence,watts,temp,moving,grade_smooth"},
  )
  response.raise_for_status()
  stream = response.json()
  with open(f"strava/data/private/streams/{activity['id']}.json", "w") as file:
    json.dump(stream, file)

print('Fetching activities from Strava...')

# fetches activity data from strava and stores it in json file
for activity in fetch_activities():
  store_activity(activity)
  fetch_and_store_stream_for_activity(activity)


print('Activities fetched and stored')
