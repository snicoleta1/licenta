## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## say goodbye
* goodbye
  - utter_goodbye

## action + pulse
* pulseIntent
  - action_ask_about_pulse
  
## action + steps
* stepsIntent
  - action_ask_about_steps
  
## action + health
* healthIntent
  - action_ask_about_health
  
## action + calendar
* calendarIntent
  - action_ask_about_calendar
  
## action + blood_pressure
* blood_pressureIntent
  - action_ask_about_blood_pressure
  
## action + sleep
* sleepIntent
  - action_ask_about_sleep
  
## action + time
* timeIntent
  - action_ask_about_time
  
## action + weather
* weatherIntent
  - action_ask_about_weather
  
## action + weight
* weightIntent
  - action_ask_about_weight
  
## action + person
* personIntent
  - action_ask_about_person
  
## action + page_type
* pageIntent
  - action_ask_about_page_type

## action + food
* foodIntent
  - action_ask_about_food

## action + stress
* stressIntent
  - action_ask_about_stress


## action + credentials
* credentialsIntent
  - action_ask_about_credentials

