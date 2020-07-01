from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import pandas as pd
import datetime
import moosegesture

adminUser = False
normalUser = False


class ActionCredentials(Action):
    def name(self) -> Text:
        return "action_ask_about_credentials"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user = next(tracker.get_latest_entity_values('user'), None)
        print(user)
        if "admin" in str(user):
            adminUser = True
        elif "normal" in str(user):
            normalUser = True

        return []


class ActionPulse(Action):
    def name(self) -> Text:
        return "action_ask_about_pulse"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        file = open("output.csv", "a")
        data = pd.read_csv("date.csv", sep=',')
        dataDf = pd.DataFrame(data)
        print(dataDf.at[0,'pulse'])

        last_message = tracker.latest_message.get("text", "")
        file.write(str(last_message))
        file.write(",")

        pulse = next(tracker.get_latest_entity_values('pulse'), None)
        today = next(tracker.get_latest_entity_values('today'), None)
        yesterday = next(tracker.get_latest_entity_values('yesterday'), None)
        display = next(tracker.get_latest_entity_values('display_actions'), None)
        say = next(tracker.get_latest_entity_values('say_actions'), None)
        target = next(tracker.get_latest_entity_values('target'), None)

        if ("my" not in str(target) or "I" not in str(target)) and normalUser is True:
            dispatcher.utter_message(template="utter_incorrect_credentials")
            return []

        if (today is None or today is not None) and yesterday is None:
            if pulse is not None:
                if display is not None:
                    #dispatcher.utter_message("Display")
                    dispatcher.utter_message("Your pulse is " + str(dataDf.at[0, 'pulse']))
                    file.write("\n")
                    file.close()
                elif say is not None:
                    #dispatcher.utter_message("Say")
                    dispatcher.utter_message("Your pulse is " + str(dataDf.at[0, 'pulse']))
                    file.write("Your pulse is " + str(dataDf.at(0, 'pulse')))
                    file.write("\n")
                    file.close()
                else:
                    #dispatcher.utter_message("Display + Say")
                    print(dataDf.at[0,'pulse'])
                    dispatcher.utter_message("Your pulse is " + str(dataDf.at[0, 'pulse']))
                    file.write("Your pulse is " + str(dataDf.at(0, 'pulse')))
                    file.write("\n")
                    file.close()
                return []
            today = None
        elif yesterday is not None:
            if pulse is not None:
                if display is not None:
                    #dispatcher.utter_message("Display")
                    dispatcher.utter_message("Your pulse was " + str(dataDf.at[1, 'pulse']))
                    file.write("Your pulse was " + str(dataDf.at[1, 'pulse']))
                    file.write("\n")
                    file.close()
                elif say is not None:
                    #dispatcher.utter_message("Say")
                    dispatcher.utter_message("Your pulse was " + str(dataDf.at[1, 'pulse']))
                    file.write("Your pulse was " + str(dataDf.at[1, 'pulse']))
                    file.write("\n")
                    file.close()
                else:
                    #dispatcher.utter_message("Display + Say")
                    dispatcher.utter_message("Your pulse was " + str(dataDf.at[1, 'pulse']))
                    file.write("Your pulse was " + str(dataDf.at[1, 'pulse']))
                    file.write("\n")
                    file.close()
                return []

        dispatcher.utter_message(template="utter_repeat")
        file.write(template="utter_repeat")
        file.write("\n")

        return []


class ActionHealth(Action):
    def name(self) -> Text:
        return "action_ask_about_health"

    def __init__(self):
        pass

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        file = open("output.csv", "a")
        data = pd.read_csv("date.csv", sep=',')
        dataDf = pd.DataFrame(data)

        last_message = tracker.latest_message.get("text", "")
        file.write(str(last_message))
        file.write(",")

        health = next(tracker.get_latest_entity_values('health'), None)
        today = next(tracker.get_latest_entity_values('today'), None)
        yesterday = next(tracker.get_latest_entity_values('yesterday'), None)
        display = next(tracker.get_latest_entity_values('display_actions'), None)
        say = next(tracker.get_latest_entity_values('say_actions'), None)
        target = next(tracker.get_latest_entity_values('target'), None)

        if ("my" not in str(target) or "I" not in str(target)) and normalUser is True:
            dispatcher.utter_message(template="utter_incorrect_credentials")
            return []

        if (today is None or today is not None) and yesterday is None:
            if health is not None:
                if display is not None:
                    #dispatcher.utter_message("Display")
                    dispatcher.utter_message("Your health is " + str(dataDf.at[0, 'health']))
                    file.write("Your health is " + str(dataDf.at[0, 'health']))
                    file.write("\n")
                    file.close()
                elif say is not None:
                    #dispatcher.utter_message("Say")
                    dispatcher.utter_message("Your health is " + str(dataDf.at[0, 'health']))
                    file.write("Your health is " + str(dataDf.at[0, 'health']))
                    file.write("\n")
                    file.close()
                else:
                    #dispatcher.utter_message("Display + Say")
                    dispatcher.utter_message("Your health is " + str(dataDf.at[0, 'health']))
                    file.write("Your health is " + str(dataDf.at[0, 'health']))
                    file.write("\n")
                    file.close()
                return []
            today = None
        elif yesterday is not None:
            if health is not None:
                if display is not None:
                    #dispatcher.utter_message("Display")
                    dispatcher.utter_message("Your health was " + str(dataDf.at[1, 'health']))
                    file.write("Your health was " + str(dataDf.at[1, 'health']))
                    file.write("\n")
                    file.close()
                elif say is not None:
                    #dispatcher.utter_message("Say")
                    dispatcher.utter_message("Your health was " + str(dataDf.at[1, 'health']))
                    file.write("Your health was " + str(dataDf.at[1, 'health']))
                    file.write("\n")
                    file.close()
                else:
                    #dispatcher.utter_message("Display + Say")
                    dispatcher.utter_message("Your health was " + str(dataDf.at[1, 'health']))
                    file.write("Your health was " + str(dataDf.at[1, 'health']))
                    file.write("\n")
                    file.close()
                return []

        dispatcher.utter_message(template="utter_repeat")
        file.write(template="utter_repeat")
        file.write("\n")

        return []


class ActionSteps(Action):
    def name(self) -> Text:
        return "action_ask_about_steps"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        file = open("output.csv", "a")
        data = pd.read_csv("date.csv", sep=',')
        dataDf = pd.DataFrame(data)

        last_message = tracker.latest_message.get("text", "")
        file.write(str(last_message))
        file.write(",")

        steps = next(tracker.get_latest_entity_values('steps'), None)
        today = next(tracker.get_latest_entity_values('today'), None)
        yesterday = next(tracker.get_latest_entity_values('yesterday'), None)
        display = next(tracker.get_latest_entity_values('display_actions'), None)
        say = next(tracker.get_latest_entity_values('say_actions'), None)
        target = next(tracker.get_latest_entity_values('target'), None)

        if ("my" not in str(target) or "I" not in str(target)) and normalUser is True:
            dispatcher.utter_message(template="utter_incorrect_credentials")
            return []

        if (today is None or today is not None) and yesterday is None:
            if steps is not None:
                if display is not None:
                    #dispatcher.utter_message("Display")
                    dispatcher.utter_message("Your number of steps are " + str(dataDf.at[0, 'steps']))
                    file.write("Your number of steps are " + str(dataDf.at[0, 'steps']))
                    file.write("\n")
                    file.close()
                elif say is not None:
                    #dispatcher.utter_message("Say")
                    dispatcher.utter_message("Your number of steps are " + str(dataDf.at[0, 'steps']))
                    file.write("Your number of steps are " + str(dataDf.at[0, 'steps']))
                    file.write("\n")
                    file.close()
                else:
                    #dispatcher.utter_message("Display + Say")
                    dispatcher.utter_message("Your number of steps are " + str(dataDf.at[0, 'steps']))
                    file.write("Your number of steps are " + str(dataDf.at[0, 'steps']))
                    file.write("\n")
                    file.close()
                return []
            today = None
        elif yesterday is not None:
            if steps is not None:
                if display is not None:
                    #dispatcher.utter_message("Display")
                    dispatcher.utter_message("Your number of steps was " + str(dataDf.at[1, 'steps']))
                    file.write("Your number of steps was " + str(dataDf.at[1, 'steps']))
                    file.write("\n")
                    file.close()
                elif say is not None:
                    #dispatcher.utter_message("Say")
                    dispatcher.utter_message("Your number of steps was " + str(dataDf.at[1, 'steps']))
                    file.write("Your number of steps was " + str(dataDf.at[1, 'steps']))
                    file.write("\n")
                    file.close()
                else:
                    #dispatcher.utter_message("Display + Say")
                    dispatcher.utter_message("Your number of steps was " + str(dataDf.at[1, 'steps']))
                    file.write("Your number of steps was " + str(dataDf.at[1, 'steps']))
                    file.write("\n")
                    file.close()
                return []

        dispatcher.utter_message(template="utter_repeat")
        file.write(template="utter_repeat")
        file.write("\n")

        return []


class ActionBloodPressure(Action):
    def name(self) -> Text:
        return "action_ask_about_blood_pressure"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        file = open("output.csv", "a")
        data = pd.read_csv("date.csv", sep=',')
        dataDf = pd.DataFrame(data)

        last_message = tracker.latest_message.get("text", "")
        file.write(str(last_message))
        file.write(",")

        blood_pressure = next(tracker.get_latest_entity_values('blood_pressure'), None)
        today = next(tracker.get_latest_entity_values('today'), None)
        yesterday = next(tracker.get_latest_entity_values('yesterday'), None)
        tomorrow = next(tracker.get_latest_entity_values('tomorrow'), None)
        display = next(tracker.get_latest_entity_values('display_actions'), None)
        say = next(tracker.get_latest_entity_values('say_actions'), None)
        target = next(tracker.get_latest_entity_values('target'), None)

        if ("my" not in str(target) or "I" not in str(target)) and normalUser is True:
            print("intra aici")
            print(str(target))
            dispatcher.utter_message(template="utter_incorrect_credentials")
            return []

        if (today is None or today is not None) and yesterday is None and tomorrow is None:
            if blood_pressure is not None:
                if "diastolic" in str(blood_pressure):
                    if display is not None:
                        #dispatcher.utter_message("Display")
                        dispatcher.utter_message(
                            "Your diastolic pressure is " + str(dataDf.at[0, 'diastolic_pressure']))
                        file.write("Your systolic pressure is " + str(dataDf.at[0, 'diastolic_pressure']))
                        file.write("\n")
                        file.close()
                    elif say is not None:
                        #dispatcher.utter_message("Say")
                        dispatcher.utter_message(
                            "Your diastolic pressure is " + str(dataDf.at[0, 'diastolic_pressure']))
                        file.write("Your systolic pressure is " + str(dataDf.at[0, 'diastolic_pressure']))
                        file.write("\n")
                        file.close()
                    else:
                        #dispatcher.utter_message("Display + Say")
                        dispatcher.utter_message(
                            "Your diastolic pressure is " + str(dataDf.at[0, 'diastolic_pressure']))
                        file.write("Your systolic pressure is " + str(dataDf.at[0, 'diastolic_pressure']))
                        file.write("\n")
                        file.close()
                    return []
                elif "systolic" in str(blood_pressure):
                    if display is not None:
                        #dispatcher.utter_message("Display")
                        dispatcher.utter_message(
                            "Your systolic pressure is " + str(dataDf.at[0, 'systolic_pressure']))
                        file.write("Your systolic pressure is " + str(dataDf.at[0, 'systolic_pressure']))
                        file.write("\n")
                        file.close()
                    elif say is not None:
                        #dispatcher.utter_message("Say")
                        dispatcher.utter_message(
                            "Your systolic pressure is " + str(dataDf.at[0, 'systolic_pressure']))
                        file.write("Your systolic pressure is " + str(dataDf.at[0, 'systolic_pressure']))
                        file.write("\n")
                        file.close()
                    else:
                        #dispatcher.utter_message("Display + Say")
                        dispatcher.utter_message(
                            "Your systolic pressure is " + str(dataDf.at[0, 'systolic_pressure']))
                        file.write("Your systolic pressure is " + str(dataDf.at[0, 'systolic_pressure']))
                        file.write("\n")
                        file.close()
                    return []
                else:
                    if display is not None:
                        #dispatcher.utter_message("Display")
                        dispatcher.utter_message("Your blood pressure is " + str(dataDf.at[0, 'blood_pressure']))
                        file.write("Your blood pressure is " + str(dataDf.at[0, 'blood_pressure']))
                        file.write("\n")
                        file.close()
                    elif say is not None:
                        #dispatcher.utter_message("Say")
                        dispatcher.utter_message("Your blood pressure is " + str(dataDf.at[0, 'blood_pressure']))
                        file.write("Your blood pressure is " + str(dataDf.at[0, 'blood_pressure']))
                        file.write("\n")
                        file.close()
                    else:
                        #dispatcher.utter_message("Display + Say")
                        dispatcher.utter_message("Your blood pressure is " + str(dataDf.at[0, 'blood_pressure']))
                        file.write("Your blood pressure is " + str(dataDf.at[0, 'blood_pressure']))
                        file.write("\n")
                        file.close()
                    return []

            today = None
        elif yesterday is not None:
            if blood_pressure is not None:
                if "diastolic" in str(blood_pressure):
                    if display is not None:
                        #dispatcher.utter_message("Display")
                        dispatcher.utter_message(
                            "Your diastolic pressure was " + str(dataDf.at[1, 'diastolic_pressure']))
                        file.write("Your systolic pressure was " + str(dataDf.at[1, 'diastolic_pressure']))
                        file.write("\n")
                        file.close()
                    elif say is not None:
                        #dispatcher.utter_message("Say")
                        dispatcher.utter_message(
                            "Your diastolic pressure was " + str(dataDf.at[1, 'diastolic_pressure']))
                        file.write("Your systolic pressure was " + str(dataDf.at[1, 'diastolic_pressure']))
                        file.write("\n")
                        file.close()
                    else:
                        #dispatcher.utter_message("Display + Say")
                        dispatcher.utter_message(
                            "Your diastolic pressure was " + str(dataDf.at[1, 'diastolic_pressure']))
                        file.write("Your systolic pressure was " + str(dataDf.at[1, 'diastolic_pressure']))
                        file.write("\n")
                        file.close()
                    return []
                elif "systolic" in str(blood_pressure):
                    if display is not None:
                        #dispatcher.utter_message("Display")
                        dispatcher.utter_message(
                            "Your systolic pressure was " + str(dataDf.at[1, 'systolic_pressure']))
                        file.write("Your systolic pressure was " + str(dataDf.at[1, 'systolic_pressure']))
                        file.write("\n")
                        file.close()
                    elif say is not None:
                        #dispatcher.utter_message("Say")
                        dispatcher.utter_message(
                            "Your systolic pressure was " + str(dataDf.at[1, 'systolic_pressure']))
                        file.write("Your systolic pressure was " + str(dataDf.at[1, 'systolic_pressure']))
                        file.write("\n")
                        file.close()
                    else:
                        #dispatcher.utter_message("Display + Say")
                        dispatcher.utter_message(
                            "Your systolic pressure was " + str(dataDf.at[1, 'systolic_pressure']))
                        file.write("Your systolic pressure was " + str(dataDf.at[1, 'systolic_pressure']))
                        file.write("\n")
                        file.close()
                    return []
                else:
                    if display is not None:
                        #dispatcher.utter_message("Display")
                        dispatcher.utter_message(
                            "Your blood pressure was " + str(dataDf.at[1, 'blood_pressure']))
                        file.write("Your blood pressure was " + str(dataDf.at[1, 'blood_pressure']))
                        file.write("\n")
                        file.close()
                    elif say is not None:
                        #dispatcher.utter_message("Say")
                        dispatcher.utter_message(
                            "Your blood pressure was " + str(dataDf.at[1, 'blood_pressure']))
                        file.write("Your blood pressure was " + str(dataDf.at[1, 'blood_pressure']))
                        file.write("\n")
                        file.close()
                    else:
                        #dispatcher.utter_message("Display + Say")
                        dispatcher.utter_message(
                            "Your blood pressure was " + str(dataDf.at[1, 'blood_pressure']))
                        file.write("Your blood pressure was " + str(dataDf.at[1, 'blood_pressure']))
                        file.write("\n")
                        file.close()
                    return []

        dispatcher.utter_message(template="utter_repeat")
        file.write(template="utter_repeat")
        file.write("\n")

        return []


class ActionCalendar(Action):
    def name(self) -> Text:
        return "action_ask_about_calendar"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        file = open("output.csv", "a")
        data = pd.read_csv("date.csv", sep=',')
        dataDf = pd.DataFrame(data)

        last_message = tracker.latest_message.get("text", "")
        file.write(str(last_message))
        file.write(",")

        calendar = next(tracker.get_latest_entity_values('calendar'), None)
        today = next(tracker.get_latest_entity_values('today'), None)
        yesterday = next(tracker.get_latest_entity_values('yesterday'), None)
        tomorrow = next(tracker.get_latest_entity_values('tomorrow'), None)
        display = next(tracker.get_latest_entity_values('display_actions'), None)
        say = next(tracker.get_latest_entity_values('say_actions'), None)
        target = next(tracker.get_latest_entity_values('target'), None)

        if ("my" not in str(target) or "I" not in str(target)) and normalUser is True:
            dispatcher.utter_message(template="utter_incorrect_credentials")
            return []

        if (today is None or today is not None) and yesterday is None and tomorrow is None:
            if calendar is not None:
                if "plans" in str(calendar):
                    if display is not None:
                        #dispatcher.utter_message("Display")
                        dispatcher.utter_message(
                            "Your plans are: " + str(dataDf.at[0, 'plans']))
                        file.write("Your plans are: " + str(dataDf.at[0, 'plans']))
                        file.write("\n")
                        file.close()
                    elif say is not None:
                        #dispatcher.utter_message("Say")
                        dispatcher.utter_message(
                            "Your plans are: " + str(dataDf.at[0, 'plans']))
                        file.write("Your plans are: " + str(dataDf.at[0, 'plans']))
                        file.write("\n")
                        file.close()
                    else:
                        #dispatcher.utter_message("Display + Say")
                        dispatcher.utter_message(
                            "Your plans are: " + str(dataDf.at[0, 'plans']))
                        file.write("Your plans are: " + str(dataDf.at[0, 'plans']))
                        file.write("\n")
                        file.close()
                    return []
                elif "meetings" in str(calendar):
                    if display is not None:
                        #dispatcher.utter_message("Display")
                        dispatcher.utter_message(
                            "Your meetings are: " + str(dataDf.at[0, 'meetings']))
                        file.write("Your meetings are: " + str(dataDf.at[0, 'meetings']))
                        file.write("\n")
                        file.close()
                    elif say is not None:
                        #dispatcher.utter_message("Say")
                        dispatcher.utter_message(
                            "Your meetings are: " + str(dataDf.at[0, 'meetings']))
                        file.write("Your meetings are: " + str(dataDf.at[0, 'meetings']))
                        file.write("\n")
                        file.close()
                    else:
                        #dispatcher.utter_message("Display + Say")
                        dispatcher.utter_message(
                            "Your meetings are: " + str(dataDf.at[0, 'meetings']))
                        file.write("Your meetings are: " + str(dataDf.at[0, 'meetings']))
                        file.write("\n")
                        file.close()
                    return []
                else:
                    if display is not None:
                        #dispatcher.utter_message("Display")
                        dispatcher.utter_message(
                            "Your calendar activities are: " + str(dataDf.at[0, 'calendar']))
                        file.write("Your calendar activities are: " + str(dataDf.at[0, 'calendar']))
                        file.write("\n")
                        file.close()
                    elif say is not None:
                        #dispatcher.utter_message("Say")
                        dispatcher.utter_message(
                            "Your calendar activities are: " + str(dataDf.at[0, 'calendar']))
                        file.write("Your calendar activities are: " + str(dataDf.at[0, 'calendar']))
                        file.write("\n")
                        file.close()
                    else:
                        #dispatcher.utter_message("Display + Say")
                        dispatcher.utter_message(
                            "Your calendar activities are: " + str(dataDf.at[0, 'calendar']))
                        file.write("Your calendar activities are: " + str(dataDf.at[0, 'calendar']))
                        file.write("\n")
                        file.close()
                    return []
            today = None
        elif yesterday is not None:
            if calendar is not None:
                if "plans" in str(calendar):
                    if display is not None:
                        #dispatcher.utter_message("Display")
                        dispatcher.utter_message(
                            "Your plans were: " + str(dataDf.at[0, 'plans']))
                        file.write("Your plans were: " + str(dataDf.at[0, 'plans']))
                        file.write("\n")
                        file.close()
                    elif say is not None:
                        #dispatcher.utter_message("Say")
                        dispatcher.utter_message(
                            "Your plans were: " + str(dataDf.at[0, 'plans']))
                        file.write("Your plans were: " + str(dataDf.at[0, 'plans']))
                        file.write("\n")
                        file.close()
                    else:
                        #dispatcher.utter_message("Display + Say")
                        dispatcher.utter_message(
                            "Your plans were: " + str(dataDf.at[0, 'plans']))
                        file.write("Your plans were: " + str(dataDf.at[0, 'plans']))
                        file.write("\n")
                        file.close()
                    return []
                elif "meetings" in str(calendar):
                    if display is not None:
                        #dispatcher.utter_message("Display")
                        dispatcher.utter_message(
                            "Your meetings were: " + str(dataDf.at[0, 'meetings']))
                        file.write("Your meetings were: " + str(dataDf.at[0, 'meetings']))
                        file.write("\n")
                        file.close()
                    elif say is not None:
                        #dispatcher.utter_message("Say")
                        dispatcher.utter_message(
                            "Your meetings were: " + str(dataDf.at[0, 'meetings']))
                        file.write("Your meetings were: " + str(dataDf.at[0, 'meetings']))
                        file.write("\n")
                        file.close()
                    else:
                        #dispatcher.utter_message("Display + Say")
                        dispatcher.utter_message(
                            "Your meetings were: " + str(dataDf.at[0, 'meetings']))
                        file.write("Your meetings were: " + str(dataDf.at[0, 'meetings']))
                        file.write("\n")
                        file.close()
                    return []
                else:
                    if display is not None:
                        #dispatcher.utter_message("Display")
                        dispatcher.utter_message(
                            "Your calendar activities were: " + str(dataDf.at[0, 'calendar']))
                        file.write("Your calendar activities were: " + str(dataDf.at[0, 'calendar']))
                        file.write("\n")
                        file.close()
                    elif say is not None:
                        #dispatcher.utter_message("Say")
                        dispatcher.utter_message(
                            "Your calendar activities were: " + str(dataDf.at[0, 'calendar']))
                        file.write("Your calendar activities were: " + str(dataDf.at[0, 'calendar']))
                        file.write("\n")
                        file.close()
                    else:
                        #dispatcher.utter_message("Display + Say")
                        dispatcher.utter_message(
                            "Your calendar activities were: " + str(dataDf.at[0, 'calendar']))
                        file.write("Your calendar activities were: " + str(dataDf.at[0, 'calendar']))
                        file.write("\n")
                        file.close()
                    return []
        elif tomorrow is not None:
            if calendar is not None:
                if "plans" in str(calendar):
                    if display is not None:
                        #dispatcher.utter_message("Display")
                        dispatcher.utter_message(
                            "Your plans will be: " + str(dataDf.at[0, 'plans']))
                        file.write("Your plans will be: " + str(dataDf.at[0, 'plans']))
                        file.write("\n")
                        file.close()
                    elif say is not None:
                        #dispatcher.utter_message("Say")
                        dispatcher.utter_message(
                            "Your plans will be: " + str(dataDf.at[0, 'plans']))
                        file.write("Your plans will be: " + str(dataDf.at[0, 'plans']))
                        file.write("\n")
                        file.close()
                    else:
                        #dispatcher.utter_message("Display + Say")
                        dispatcher.utter_message(
                            "Your plans will be: " + str(dataDf.at[0, 'plans']))
                        file.write("Your plans will be: " + str(dataDf.at[0, 'plans']))
                        file.write("\n")
                        file.close()
                    return []
                elif "meetings" in str(calendar):
                    if display is not None:
                        #dispatcher.utter_message("Display")
                        dispatcher.utter_message(
                            "Your meetings will be: " + str(dataDf.at[0, 'meetings']))
                        file.write("Your meetings will be: " + str(dataDf.at[0, 'meetings']))
                        file.write("\n")
                        file.close()
                    elif say is not None:
                        #dispatcher.utter_message("Say")
                        dispatcher.utter_message(
                            "Your meetings will be: " + str(dataDf.at[0, 'meetings']))
                        file.write("Your meetings will be: " + str(dataDf.at[0, 'meetings']))
                        file.write("\n")
                        file.close()
                    else:
                        #dispatcher.utter_message("Display + Say")
                        dispatcher.utter_message(
                            "Your meetings will be: " + str(dataDf.at[0, 'meetings']))
                        file.write("Your meetings will be: " + str(dataDf.at[0, 'meetings']))
                        file.write("\n")
                        file.close()
                    return []
                else:
                    if display is not None:
                        #dispatcher.utter_message("Display")
                        dispatcher.utter_message(
                            "Your calendar activities will be: " + str(dataDf.at[0, 'calendar']))
                        file.write("Your calendar activities will be: " + str(dataDf.at[0, 'calendar']))
                        file.write("\n")
                        file.close()
                    elif say is not None:
                        #dispatcher.utter_message("Say")
                        dispatcher.utter_message(
                            "Your calendar activities will be: " + str(dataDf.at[0, 'calendar']))
                        file.write("Your calendar activities will be: " + str(dataDf.at[0, 'calendar']))
                        file.write("\n")
                        file.close()
                    else:
                        #dispatcher.utter_message("Display + Say")
                        dispatcher.utter_message(
                            "Your calendar activities will be: " + str(dataDf.at[0, 'calendar']))
                        file.write("Your calendar activities will be: " + str(dataDf.at[0, 'calendar']))
                        file.write("\n")
                        file.close()
                    return []

        dispatcher.utter_message(template="utter_repeat")
        #file.write(template="utter_repeat")
        #file.write("\n")

        return []


class ActionWeight(Action):
    def name(self) -> Text:
        return "action_ask_about_weight"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        file = open("output.csv", "a")
        data = pd.read_csv("date.csv", sep=',')
        dataDf = pd.DataFrame(data)

        last_message = tracker.latest_message.get("text", "")
        file.write(str(last_message))
        file.write(",")

        weight = next(tracker.get_latest_entity_values('weight'), None)
        today = next(tracker.get_latest_entity_values('today'), None)
        yesterday = next(tracker.get_latest_entity_values('yesterday'), None)
        display = next(tracker.get_latest_entity_values('display_actions'), None)
        say = next(tracker.get_latest_entity_values('say_actions'), None)
        target = next(tracker.get_latest_entity_values('target'), None)

        if ("my" not in str(target) or "I" not in str(target)) and normalUser is True:
            dispatcher.utter_message(template="utter_incorrect_credentials")
            return []

        if (today is None or today is not None) and yesterday is None:
            if weight is not None:
                if display is not None:
                    #dispatcher.utter_message("Display")
                    dispatcher.utter_message("Your weight is " + str(dataDf.at[0, 'weight']))
                    file.write("Your weight is " + str(dataDf.at[0, 'weight']))
                    file.write("\n")
                elif say is not None:
                    #dispatcher.utter_message("Say")
                    dispatcher.utter_message("Your weight is " + str(dataDf.at[0, 'weight']))
                    file.write("Your weight is " + str(dataDf.at[0, 'weight']))
                    file.write("\n")
                else:
                    #dispatcher.utter_message("Display + Say")
                    dispatcher.utter_message("Your weight is " + str(dataDf.at[0, 'weight']))
                    file.write("Your weight is " + str(dataDf.at[0, 'weight']))
                    file.write("\n")
                file.close()
                return []

        dispatcher.utter_message(template="utter_repeat")
        file.write(template="utter_repeat")
        file.write("\n")

        file.close()
        return []


class ActionTime(Action):
    def name(self) -> Text:
        return "action_ask_about_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        file = open("output.csv", "a")

        last_message = tracker.latest_message.get("text", "")
        file.write(str(last_message))
        file.write(",")

        time = next(tracker.get_latest_entity_values('time'), None)
        today = next(tracker.get_latest_entity_values('today'), None)
        yesterday = next(tracker.get_latest_entity_values('yesterday'), None)
        display = next(tracker.get_latest_entity_values('display_actions'), None)
        say = next(tracker.get_latest_entity_values('say_actions'), None)
        target = next(tracker.get_latest_entity_values('target'), None)

        if ("my" not in str(target) or "I" not in str(target)) and normalUser is True:
            dispatcher.utter_message(template="utter_incorrect_credentials")
            return []

        currentDT = datetime.datetime.now()
        if (today is None or today is not None) and yesterday is None:
            if time is not None:
                if "time" or "hour" in str(time):
                    if display is not None:
                        #dispatcher.utter_message("Display")
                        dispatcher.utter_message("It's " + str(currentDT.strftime("%H:%M:%S")))
                        file.write("It's " + str(currentDT.strftime("%H:%M:%S")))
                        file.write("\n")
                    elif say is not None:
                        #dispatcher.utter_message("Say")
                        dispatcher.utter_message("It's " + str(currentDT.strftime("%H:%M:%S")))
                        file.write("It's " + str(currentDT.strftime("%H:%M:%S")))
                        file.write("\n")
                    else:
                        #dispatcher.utter_message("Display + Say")
                        dispatcher.utter_message("It's " + str(currentDT.strftime("%H:%M:%S")))
                        file.write("It's " + str(currentDT.strftime("%H:%M:%S")))
                        file.write("\n")
                    file.close()
                    return []
                if "day" in str(time):
                    if display is not None:
                        #dispatcher.utter_message("Display")
                        dispatcher.utter_message("It's " + str(currentDT.strftime("%Y/%m/%d")))
                        file.write("It's " + str(currentDT.strftime("%Y/%m/%d")))
                        file.write("\n")
                    elif say is not None:
                        #dispatcher.utter_message("Say")
                        dispatcher.utter_message("It's " + str(currentDT.strftime("%Y/%m/%d")))
                        file.write("It's " + str(currentDT.strftime("%Y/%m/%d")))
                        file.write("\n")
                    else:
                        #dispatcher.utter_message("Display + Say")
                        dispatcher.utter_message("It's " + str(currentDT.strftime("%Y/%m/%d")))
                        file.write("It's " + str(currentDT.strftime("%Y/%m/%d")))
                        file.write("\n")
                    file.close()
                    return []
                if "month" in str(time):
                    if display is not None:
                        #dispatcher.utter_message("Display")
                        dispatcher.utter_message("It's  %d" % currentDT.month)
                        file.write("It's  %d" % currentDT.month)
                        file.write("\n")
                    elif say is not None:
                        #dispatcher.utter_message("Say")
                        dispatcher.utter_message("It's %d" % currentDT.month)
                        file.write("It's %d" % currentDT.month)
                        file.write("\n")
                    else:
                        #dispatcher.utter_message("Display + Say")
                        dispatcher.utter_message("It's %d" % currentDT.month)
                        file.write("It's %d" % currentDT.month)
                        file.write("\n")
                    file.close()
                    return []
                if "year" in str(time):
                    if display is not None:
                        #dispatcher.utter_message("Display")
                        dispatcher.utter_message("It's %d" % currentDT.year)
                        file.write("It's %d" % currentDT.year)
                        file.write("\n")
                    elif say is not None:
                        #dispatcher.utter_message("Say")
                        dispatcher.utter_message("It's %d" % currentDT.year)
                        file.write("It's %d" % currentDT.year)
                        file.write("\n")
                    else:
                        #dispatcher.utter_message("Display + Say")
                        dispatcher.utter_message("It's %d" % currentDT.year)
                        file.write("It's %d" % currentDT.year)
                        file.write("\n")
                    file.close()
                    return []

        dispatcher.utter_message(template="utter_repeat")
        file.write(template="utter_repeat")
        file.write("\n")
        file.close()
        return []


class ActionWeather(Action):
    def name(self) -> Text:
        return "action_ask_about_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        file = open("output.csv", "a")
        data = pd.read_csv("date.csv", sep=',')
        dataDf = pd.DataFrame(data)

        last_message = tracker.latest_message.get("text", "")
        file.write(str(last_message))
        file.write(",")

        weather = next(tracker.get_latest_entity_values('weather'), None)
        today = next(tracker.get_latest_entity_values('today'), None)
        tomorrow = next(tracker.get_latest_entity_values('tomorrow'), None)

        if (today is None or today is not None) and tomorrow is None:
            if weather is not None:
                dispatcher.utter_message("The weather is " + str(dataDf.at[0, 'weather']))
                file.write("The weather is " + str(dataDf.at[0, 'weather']))
                file.write("\n")
                file.close()
                return []
        elif tomorrow is not None:
            if weather is not None:
                dispatcher.utter_message("The weather will be " + str(dataDf.at[2, 'weather']))
                file.write("The weather will be " + str(dataDf.at[2, 'weather']))
                file.write("\n")
                file.close()
                return []

        dispatcher.utter_message(template="utter_repeat")
        file.write(template="utter_repeat")
        file.write("\n")
        file.close()
        return []


class ActionPerson(Action):
    def name(self) -> Text:
        return "action_ask_about_person"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        file = open("output.csv", "a")

        last_message = tracker.latest_message.get("text", "")
        file.write(str(last_message))
        file.write(",")

        dispatcher.utter_message(template="utter_person")
        file.write("I am a bot, powered by Rasa.")
        file.write("\n")
        file.close()
        return []


class ActionPage(Action):
    def name(self) -> Text:
        return "action_ask_about_page_type"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        file = open("output.csv", "a")

        last_message = tracker.latest_message.get("text", "")
        file.write(str(last_message))
        file.write(",")

        page_type = next(tracker.get_latest_entity_values('page_type'), None)

        if page_type is not None:
            if "main" in page_type:
                dispatcher.utter_message("Go to the main page")
                file.write("Go to the main page")
                file.write("\n")
            elif "back" in page_type:
                dispatcher.utter_message("Go back")
                file.write("Go back")
                file.write("\n")
            else:
                dispatcher.utter_message("Go forward")
                file.write("Go forward")
                file.write("\n")
            file.close()
            return []

        dispatcher.utter_message(template="utter_repeat")
        file.write(template="utter_repeat")
        file.write("\n")

        file.close()
        return []


class ActionSleep(Action):
    def name(self) -> Text:
        return "action_ask_about_sleep"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        file = open("output.csv", "a")
        data = pd.read_csv("date.csv", sep=',')
        dataDf = pd.DataFrame(data)

        last_message = tracker.latest_message.get("text", "")
        file.write(str(last_message))
        file.write(",")

        sleep = next(tracker.get_latest_entity_values('sleep'), None)
        today = next(tracker.get_latest_entity_values('today'), None)
        yesterday = next(tracker.get_latest_entity_values('yesterday'), None)
        display = next(tracker.get_latest_entity_values('display_action'), None)
        say = next(tracker.get_latest_entity_values('say_action'), None)
        target = next(tracker.get_latest_entity_values('target'), None)

        if ("my" not in str(target) or "I" not in str(target)) and normalUser is True:
            dispatcher.utter_message(template="utter_incorrect_credentials")
            return []

        if (today is None or today is not None) and yesterday is None:
            if sleep is not None:
                if display is not None:
                    #dispatcher.utter_message("Display")
                    dispatcher.utter_message("The number of sleep hours is " + str(dataDf.at[0, 'sleep']))
                    file.write("The number of sleep hours is " + str(dataDf.at[0, 'sleep']))
                    file.write("\n")
                elif say is not None:
                    #ispatcher.utter_message("Say")
                    dispatcher.utter_message("The number of sleep hours is " + str(dataDf.at[0, 'sleep']))
                    file.write("The number of sleep hours is " + str(dataDf.at[0, 'sleep']))
                    file.write("\n")
                else:
                    #dispatcher.utter_message("Display + Say")
                    dispatcher.utter_message("The number of sleep hours is " + str(dataDf.at[0, 'sleep']))
                    file.write("The number of sleep hours is " + str(dataDf.at[0, 'sleep']))
                    file.write("\n")
                file.close()
                return []
            today = None
        elif yesterday is not None:
            if sleep is not None:
                if display is not None:
                    #dispatcher.utter_message("Display")
                    dispatcher.utter_message("The number of sleep hours was " + str(dataDf.at[1, 'sleep']))
                    file.write("The number of sleep hours was " + str(dataDf.at[1, 'sleep']))
                    file.write("\n")
                elif say is not None:
                    #dispatcher.utter_message("Say")
                    dispatcher.utter_message("The number of sleep hours was " + str(dataDf.at[1, 'sleep']))
                    file.write("The number of sleep hours was " + str(dataDf.at[1, 'sleep']))
                    file.write("\n")
                else:
                    #dispatcher.utter_message("Display + Say")
                    dispatcher.utter_message("The number of sleep hours was " + str(dataDf.at[1, 'sleep']))
                    file.write("The number of sleep hours was " + str(dataDf.at[1, 'sleep']))
                    file.write("\n")
                file.close()
                return []

        dispatcher.utter_message(template="utter_repeat")
        file.write(template="utter_repeat")
        file.write("\n")

        file.close()
        return []


class ActionFood(Action):
    def name(self) -> Text:
        return "action_ask_about_food"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        file = open("output.csv", "a")
        data = pd.read_csv("date.csv", sep=',')
        dataDf = pd.DataFrame(data)

        last_message = tracker.latest_message.get("text", "")
        file.write(str(last_message))
        file.write(",")

        food = next(tracker.get_latest_entity_values('food'), None)
        today = next(tracker.get_latest_entity_values('today'), None)
        yesterday = next(tracker.get_latest_entity_values('yesterday'), None)
        tomorrow = next(tracker.get_latest_entity_values('tomorrow'), None)
        display = next(tracker.get_latest_entity_values('display_action'), None)
        say = next(tracker.get_latest_entity_values('say_action'), None)
        target = next(tracker.get_latest_entity_values('target'), None)

        if ("my" not in str(target) or "I" not in str(target)) and normalUser is True:
            dispatcher.utter_message(template="utter_incorrect_credentials")
            return []

        if (today is None or today is not None) and yesterday is None and tomorrow is None:
            if food is not None:
                if display is not None:
                    #dispatcher.utter_message("Display")
                    dispatcher.utter_message("You can eat " + str(dataDf.at[0, 'food']))
                    file.write("You can eat " + str(dataDf.at[0, 'food']))
                    file.write("\n")
                elif say is not None:
                    #dispatcher.utter_message("Say")
                    dispatcher.utter_message("You can eat " + str(dataDf.at[0, 'food']))
                    file.write("You can eat " + str(dataDf.at[0, 'sleep']))
                    file.write("\n")
                else:
                    #dispatcher.utter_message("Display + Say")
                    dispatcher.utter_message("You can eat " + str(dataDf.at[0, 'food']))
                    file.write("You can eat " + str(dataDf.at[0, 'sleep']))
                    file.write("\n")
                file.close()
                return []
            today = None
        elif yesterday is not None:
            if food is not None:
                if display is not None:
                    #dispatcher.utter_message("Display")
                    dispatcher.utter_message("You ate " + str(dataDf.at[1, 'food']))
                    file.write("You ate " + str(dataDf.at[1, 'food']))
                    file.write("\n")
                elif say is not None:
                    #dispatcher.utter_message("Say")
                    dispatcher.utter_message("You ate " + str(dataDf.at[1, 'food']))
                    file.write("You ate " + str(dataDf.at[1, 'food']))
                    file.write("\n")
                else:
                    #dispatcher.utter_message("Display + Say")
                    dispatcher.utter_message("You ate " + str(dataDf.at[1, 'food']))
                    file.write("You ate " + str(dataDf.at[1, 'food']))
                    file.write("\n")
                file.close()
                return []
        elif tomorrow is not None:
            if food is not None:
                if display is not None:
                    #dispatcher.utter_message("Display")
                    dispatcher.utter_message("You will eat " + str(dataDf.at[2, 'food']))
                    file.write("You will eat " + str(dataDf.at[2, 'food']))
                    file.write("\n")
                elif say is not None:
                    #dispatcher.utter_message("Say")
                    dispatcher.utter_message("You will eat " + str(dataDf.at[2, 'food']))
                    file.write("You will eat " + str(dataDf.at[2, 'food']))
                    file.write("\n")
                else:
                    #dispatcher.utter_message("Display + Say")
                    dispatcher.utter_message("You will eat " + str(dataDf.at[2, 'food']))
                    file.write("You will eat " + str(dataDf.at[2, 'food']))
                    file.write("\n")
                file.close()
                return []

        dispatcher.utter_message(template="utter_repeat")

        file.close()
        return []

class ActionSleep(Action):
    def name(self) -> Text:
        return "action_ask_about_stress"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        file = open("output.csv", "a")
        data = pd.read_csv("date.csv", sep=',')
        dataDf = pd.DataFrame(data)

        last_message = tracker.latest_message.get("text", "")
        file.write(str(last_message))
        file.write(",")

        stress = next(tracker.get_latest_entity_values('stress'), None)
        today = next(tracker.get_latest_entity_values('today'), None)
        yesterday = next(tracker.get_latest_entity_values('yesterday'), None)
        display = next(tracker.get_latest_entity_values('display_action'), None)
        say = next(tracker.get_latest_entity_values('say_action'), None)
        target = next(tracker.get_latest_entity_values('target'), None)

        if ("my" not in str(target) or "I" not in str(target)) and normalUser is True:
            dispatcher.utter_message(template="utter_incorrect_credentials")
            return []

        if (today is None or today is not None) and yesterday is None:
            if stress is not None:
                if display is not None:
                    #dispatcher.utter_message("Display")
                    dispatcher.utter_message("Your stress level is " + str(dataDf.at[0, 'stress']))
                    file.write("Your stress level is " + str(dataDf.at[0, 'stress']))
                    file.write("\n")
                elif say is not None:
                    #dispatcher.utter_message("Say")
                    dispatcher.utter_message("Your stress level is " + str(dataDf.at[0, 'stress']))
                    file.write("Your stress level is " + str(dataDf.at[0, 'stress']))
                    file.write("\n")
                else:
                    #dispatcher.utter_message("Display + Say")
                    dispatcher.utter_message("Your stress level is " + str(dataDf.at[0, 'stress']))
                    file.write("Your stress level is " + str(dataDf.at[0, 'stress']))
                    file.write("\n")
                file.close()
                return []
            today = None
        elif yesterday is not None:
            if stress is not None:
                if display is not None:
                    #dispatcher.utter_message("Display")
                    dispatcher.utter_message("Your stress level was " + str(dataDf.at[1, 'stress']))
                    file.write("Your stress level was " + str(dataDf.at[1, 'stress']))
                    file.write("\n")
                elif say is not None:
                    #dispatcher.utter_message("Say")
                    dispatcher.utter_message("Your stress level was " + str(dataDf.at[1, 'stress']))
                    file.write("Your stress level was " + str(dataDf.at[1, 'stress']))
                    file.write("\n")
                else:
                    #dispatcher.utter_message("Display + Say")
                    dispatcher.utter_message("Your stress level was " + str(dataDf.at[1, 'stress']))
                    file.write("Your stress level was " + str(dataDf.at[1, 'stress']))
                    file.write("\n")
                file.close()
                return []

        dispatcher.utter_message(template="utter_repeat")
        file.write(template="utter_repeat")
        file.write("\n")

        file.close()
        return []
