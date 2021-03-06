# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from cgitb import text
import datetime as dt
import imp
from typing import Any, Text, Dict, List

from actions import Cal_Read
from actions import Cal_Write





from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

#Gib die aktuelle ZEit zurück
class ActionGetCurrentTime(Action):

    def name(self) -> Text:
        return "action_show_time"
        

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print(dt.datetime.now)
        dispatcher.utter_message(text=f"{dt.datetime.now()}")

        return []

##safe aname
class ActionSaveName(Action):

    def name(self) -> Text:
        return "action_recieve_name"
        

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        name = tracker.get_slot("name")
        if(name=="None"):
            
            dispatcher.utter_message(f"I couldn`t understand your name!?")
            return[]
        
        dispatcher.utter_message(f"Ahhh! Hello, {name}!")
        
        return [SlotSet("name", name)]

## Actuin get Next Appointment
class ActionShowNextAppointment(Action):

    def name(self) -> Text:
        return "action_show_next_appointment"
        

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        entry_number_of_aps = tracker.get_slot("number_of_aps")
        print(entry_number_of_aps)

        #if not numeric format to numeric
        if not entry_number_of_aps.isnumeric():
            
           
            help_dict = {
                'one': '1',
                'two': '2',
                'three': '3',
                'four': '4',
                'five': '5',
                'six': '6',
                'seven': '7',
                'eight': '8',
                'nine': '9',
                'zero' : '0'
            }

            
            # printing original string
            print("The original string is : " + entry_number_of_aps)

            # Convert numeric words to numbers
            # Using join() + split()
            entry_number_of_aps = ''.join(help_dict[ele] for ele in entry_number_of_aps.split())



        
        app = Cal_Read.main(entry_number_of_aps)
        for event in app:
            start = event['start'].get('dateTime', event['start'].get('date'))
            dispatcher.utter_message(text=f"{start, event['summary']}")
            print(start, event['summary'])

        

        return []

##repeate my name
class ActionSayName(Action):
    print("Ich bin in SayName")
    print("Action", Action)
    def name(self) -> Text:
        return "action_say_name"
        

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        name = tracker.get_slot("name")
        print("name: ",name)
        if not name:
            dispatcher.utter_message(text=f"I don`t know your name!")
        else:
            dispatcher.utter_message(text=f"Your name is {name}")
        return []


class ActionMakeEntry(Action): 

    def name(self) -> Text:
        return "action_make_entry"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entryname = tracker.get_slot("entryname")
        date = tracker.get_slot("date")
        starttime = tracker.get_slot("starttime")
        duration = tracker.get_slot("duration")
        Cal_Write.main(entryname, date, starttime, duration)
        return []