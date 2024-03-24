# Strava Data Exporter

## Prerequisite
- Strava API setup: https://www.strava.com/settings/api
- Postman

## Access

Strava is using 0Auth with access privileges per app. To get access to Strava data a dedicated AccessKey needs to be fetched every 6 hour!

Fetch access key (with Postman & Browser)
1. Open following URL in browser (copy value from Postman): http://www.strava.com/oauth/authorize?client_id={{your-client-id}}&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=activity%3Aread_all
2. Click 'authorize'
3. Copy `code` value from re-directed URL.
4. Copy & paste code into Postman `STRAVA_AUTHORIZATION_CODE` value and execute
5. Observe and copy `access_token` from response

## Run