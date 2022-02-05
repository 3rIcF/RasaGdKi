import pickle
import os
import datetime 
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google.auth.transport.requests import Request
from pprint import pprint
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError




def main(entryname, date, starttime, duration):
    
    CLIENT_SECRET_FILE="client_secret.json"
    API_SERVICE_NAME = 'Calender'
    API_VERSION = 'v3'
    SCOPES=['https://www.googleapis.com/auth/calendar']

    starttime = str(starttime)[:2]
    endtime = str(int(starttime) + int(duration))
    endtime = endtime
    print(starttime)
    print(duration)
    print(endtime)
    

    cred = None

    #initial pickle name
    pickle_file = f'token_{API_SERVICE_NAME}_{API_VERSION}.pickle'
    #pickle_file = f'token.json'

    print('Picklefilename is:'+ pickle_file)

    #check if file exist
    if os.path.exists(pickle_file):
        with open(pickle_file, 'rb') as token:
            cred = pickle.load(token)
    

    # If there are no (valid) credentials available, let the user log in.
    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            cred = flow.run_local_server()

        with open(pickle_file, 'wb') as token:
            pickle.dump(cred, token)


    number_of_aps = "2"
    print("number_of_aps: ",number_of_aps)
    
    try:
        service = build(API_SERVICE_NAME, API_VERSION, credentials=cred)
        print('Name von API Service: ')
        print(API_SERVICE_NAME, 'service created successfully')
        
##Hier kommt der Code rein
         # Call the Calendar API
        #now = datetime.datetime.now(timezone.gmt).isoformat()  # 'Z' indicates UTC time
        now = datetime.datetime.utcnow.isoformat() + 'Z'  # 'Z' indicates UTC time

        ###hier insert
        event = {
            'summary': entryname,
            'description': 'A chance to hear more about Google\'s developer products.',
            'start': {
                'dateTime': date + 'T' + starttime + ':00:00-00:00',
                'timeZone': 'Europe/Berlin',
            },
            'end': {
                'dateTime': date + 'T' + endtime + ':00:00-00:00',
                'timeZone': 'Europe/Berlin',
            },

        }
        


        event = service.events().insert(calendarId='primary', body=event).execute()
        print('Event created: %s' % (event.get('htmlLink')))



    except Exception as e:
        print('Unable to connect.')
        print(e)
        return None



if __name__ == '__main__':
    main()