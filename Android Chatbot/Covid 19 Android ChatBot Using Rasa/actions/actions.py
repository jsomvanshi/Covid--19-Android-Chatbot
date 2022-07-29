# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# import requests, datetime


# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/
# This is a simple example for a custom action which utters "Hello World!"

from email import header
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests, datetime
import json

class CoronaCasesInfo(Action):
    def name(self) -> Text:
        return "corona_cases_action"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain : Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        user_message_entity = tracker.latest_message["entities"]
        context =""
        for entity in user_message_entity:
            
            if entity["entity"] == "country":
                try:
                    # url = "https://covid-19-data.p.rapidapi.com/country"
                    url = "https://covid-193.p.rapidapi.com/statistics"
                    country = entity["value"].lower()
                    print(country)
                    querystring = {"country": country}
                    headers = {
                        #"x-rapidapi-host": "covid-19-data.p.rapidapi.com",
                        #"x-rapidapi-key": "439afa9e0bmsh7c94f437839d80ep1393adjsna157e4ae8d1f",
                        'x-rapidapi-host': "covid-193.p.rapidapi.com",
                        'x-rapidapi-key': "439afa9e0bmsh7c94f437839d80ep1393adjsna157e4ae8d1f"
                    }
                    response = requests.get(url, headers=headers, params=querystring)
                    res = json.loads(response.text)
                    context = "Country : " + res['parameters']['country'] + "\nPopulation :" + str(res['response'][0]['population']) + "\nActive cases :" + str(res['response'][0]['cases']['active']) + "\nCritical cases :" + str(res['response'][0]['cases']['critical']) + "\nRecovered cases :" + str(res['response'][0]['cases']['recovered']) + "\nTotal cases : " +str(res['response'][0]['cases']['total']) + "\nNew Cases : " + str(res['response'][0]['deaths']['new']) +"\nTotal Deaths : " + str(res['response'][0]['deaths']['total']) + "\nTotal Tests : " + str(res['response'][0]['tests']['total']) + "\nDay : " + str(res['response'][0]['day']) + "\nTime Recorded : "+ str(res['response'][0]['time'])
                    print(context)
                except Exception as e:
                    print("error in reponse fetching")
        
        dispatcher.utter_message(context)
        return []

class vaccine_news_info(Action):
    def name(self) -> Text:
        return "vaccine_news_action"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain : Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        user_message_entity = tracker.latest_message["entities"]
        context =""
        try:
            url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/news/get-vaccine-news/0"
            headers = {
                "X-RapidAPI-Host": "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com",
                "X-RapidAPI-Key": "439afa9e0bmsh7c94f437839d80ep1393adjsna157e4ae8d1f"
            }
    
            response = requests.request("GET", url, headers=headers)
            res = json.loads(response.text)
            a=0
            for i in range(0,10):
                a=i+1
                context = str(context) + "#" + str(a) + "\nTitle : " + str(res['news'][i]['title']) + "\nLink : " + str(res['news'][i]['link']) + "\nPub Date : " + str(res['news'][i]['pubDate']) + "\nContent : " + str(res['news'][i]['content']) + "\nReference : " + str(res['news'][i]['reference']) +"\n\n"
            print(context)
        except Exception as e:
            print("error in reponse fetching")
    
        dispatcher.utter_message(context)
        return []

class health_news_info(Action):
    def name(self) -> Text:
        return "health_news_action"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain : Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        user_message_entity = tracker.latest_message["entities"]
        context =""
        try:
            url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/news/get-health-news/1"
            headers = {
                "X-RapidAPI-Host": "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com",
                "X-RapidAPI-Key": "439afa9e0bmsh7c94f437839d80ep1393adjsna157e4ae8d1f"
            }
    
            response = requests.request("GET", url, headers=headers)
            res = json.loads(response.text)
            a=0
            for i in range(0,10):
                a=i+1
                context = str(context) + "#" + str(a) + "\nTitle : " + str(res['news'][i]['title']) + "\nLink : " + str(res['news'][i]['link']) + "\nPub Date : " + str(res['news'][i]['pubDate']) + "\nContent : " + str(res['news'][i]['content']) + "\nReference : " + str(res['news'][i]['reference']) +"\n\n"
            print(context)
        except Exception as e:
            print("error in reponse fetching")
    
        dispatcher.utter_message(context)
        return []

class all_coronavirus_news_info(Action):
    def name(self) -> Text:
        return "all_coronavirus_news_action"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain : Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        user_message_entity = tracker.latest_message["entities"]
        context =""
        try:
            url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/news/get-coronavirus-news/0"
            headers = {
                "X-RapidAPI-Host": "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com",
                "X-RapidAPI-Key": "439afa9e0bmsh7c94f437839d80ep1393adjsna157e4ae8d1f"
            }
    
            response = requests.request("GET", url, headers=headers)
            res = json.loads(response.text)
            a=0
            for i in range(0,10):
                a=i+1
                context = str(context) + "#" + str(a) + "\nTitle : " + str(res['news'][i]['title']) + "\nLink : " + str(res['news'][i]['link']) + "\nPub Date : " + str(res['news'][i]['pubDate']) + "\nContent : " + str(res['news'][i]['content']) + "\nReference : " + str(res['news'][i]['reference']) +"\n\n"
            print(context)
        except Exception as e:
            print("error in reponse fetching")
    
        dispatcher.utter_message(context)
        return []

#for data in response:
#                     date = data['lastUpdate']
#                     dt = date.split('T')
#                     dat = datetime.datetime.strptime(dt[0], '%Y-%m-%d').strftime('%d-%m-%Y')
#                    context = "Confirmed cases: "+str(data["confirmed"])+"\nCritical cases: "+str(data["critical"])+"\nDeaths: "+str(data["deaths"])+"\nRecovered cases: "+str(data["recovered"])+"\nLast Update: "+dat
# -------------- error code -----------------------

# class CoronaCasesInfo(Action):

#      def name(self) -> Text:
#          return "corona_cases_action"

#      def run(self, dispatcher: CollectingDispatcher,
#              tracker: Tracker,
#              domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#          user_message_entity = tracker.latest_message['entities']
#          context = ""
#          for entity in user_message_entity:
#             #if (entity['entity'] == "state"):
#             #   url = "https://api.covid19india.org/data.json"
#             #     response = requests.get(url).json()
#             #     state = entity['value'].title()
#             #     for data in response["statewise"]:
#             #         if (data["state"] == state):
#             #             print("confirmed cases: ", data["confirmed"])
#             #             context = "Confirmed cases: "+data["confirmed"]+"\nActive cases: "+data["active"]+"\nDeaths: "\
#             #                      +data["deaths"]+"\nRecovered cases: "+data["recovered"]+"\n TimeStamp: "+data["lastupdatedtime"]
#             if(entity['entity']=="country"):
                
#                  url = "https://covid-19-data.p.rapidapi.com/country"
#                  country = entity['value'].lower()
#                  querystring = { "name": country, "format": "json"}
#                  headers = {
#                      'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
#                      'x-rapidapi-key': "439afa9e0bmsh7c94f437839d80ep1393adjsna157e4ae8d1f"
#                  }
#                  response = requests.get(url, headers=headers, params=querystring).json



#                  #for data in response:
#                   #   date = data['lastUpdate']
#                    #  dt = date.split('T')
#                    #  dat = datetime.datetime.strptime(dt[0], '%Y-%m-%d').strftime('%d-%m-%Y')
#                     # context = "Confirmed cases: "+str(data["confirmed"])+"\nCritical cases: "+str(data["critical"])+"\nDeaths: "+str(data["deaths"])+"\nRecovered cases: "+str(data["recovered"])+"\nLast Update: "+dat
#          dispatcher.utter_message(response.text)
#          return []