from pprint import pprint
from Google import Create_Service



#Einmal startetn, damit Token für die Google API erstellt werden kann.
CLIENT_SECRET_FILE="client_secret.json"
API_NAME = 'calender'
API_VERSION = 'v3'
SCOPES=['https://www.googleapis.com/auth/calendar']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)