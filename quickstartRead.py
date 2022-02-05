from __future__ import print_function
from calendar import c

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token2.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def main():
#def main(number_of_aps):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    number_of_aps = "2"
    print("number_of_aps: ",number_of_aps)
    creds = None
    # # The file token2.json stores the user's access and refresh tokens, and is
    # # created automatically when the authorization flow completes for the first
    # # time.
    # if os.path.exists('token2.json'):
    #     creds = Credentials.from_authorized_user_file('token2.json', SCOPES)
    # # If there are no (valid) credentials available, let the user log in.
    # if not creds or not creds.valid:
    #     if creds and creds.expired and creds.refresh_token:
    #         creds.refresh(Request())
    #     else:
    #         print("number_of_aps: ",number_of_aps)
    #         client_json = os.path.dirname(os.path.realpath(__file__) + '/client_secret.json')
    #         print("open client *.json: ", client_json)
    #         flow = InstalledAppFlow.from_client_secrets_file(
    #             client_json, SCOPES)
    #         creds = flow.run_local_server(port=0)
    #     # Save the credentials for the next run
    #     with open('token2.json', 'w') as token:
    #         token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the upcoming X events')
        #hole nächsten 3 Termine
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=number_of_aps, singleEvents=True,
                                              #maxResults=3, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return

        # Prints the start and name of the next X events
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])

        return events



    except HttpError as error:
        print('An error occurred: %s' % error)




if __name__ == '__main__':
    main()