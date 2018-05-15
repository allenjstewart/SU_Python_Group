################################################################################
#
#   Playing with API: Number Facts
#
#       http://numbersapi.com/#42
#
#  http://numbersapi.com/number/type to get a plain text response, where
#
# type is one of trivia, math, date, or year. Defaults to trivia if omitted.
# number is
# an integer, or
# the keyword random, for which we will try to return a random available fact, or
# a day of year in the form month/day (eg. 2/29, 1/09, 04/1), if type is date
# ranges of numbers
#
# Include the query parameter json or set the HTTP header Content-Type to
# application/json to return the fact and associated meta-data as a JSON object,
 # with the properties:
# text: A string of the fact text itself.
# found: Boolean of whether there was a fact for the requested number.
# number: The floating-point number that the fact pertains to. This may be
# useful for, eg. a /random request or notfound=floor.
# For a date fact, this is the 1-indexed day of a leap year
# (eg. 61 would be March 1st).
# type: String of the category of the returned fact.
# date (sometimes): A day of year associated with some year facts, as a string.
# year (sometimes): A year associated with some date facts, as a string.
#
################################################################################

import requests
import json
from pprint import pprint



response = requests.get("http://numbersapi.com/57?json")
response2 = requests.get("http://numbersapi.com/79?json")

trivia57 = response.json()
trivia79 = response2.json()

print("\nHere are some number facts:\n")
print(trivia57["text"])
print(trivia79["text"])

# Now try Wunderground:
#
# https://www.wunderground.com/weather/api/d/docs?d=resources/code-samples
#   The wunderground documentation isn't great...
#       (needs more ascii kittens!)
#

My_Key = "b1d80cef351d91cd"

weather_response = requests.get("http://api.wunderground.com/api/"+My_Key+"/conditions/q/WA/Seattle.json")
weather = weather_response.json()



city = weather['current_observation']['display_location']["city"]
state = weather['current_observation']['display_location']["state"]
temp_f = str(weather['current_observation']['temp_f']) + " F"
condition = weather['current_observation']['icon']
forecast_link = weather['current_observation']['forecast_url']

print("\n\nNow let's check the weather!\n")
print("The temperature in %s, %s is currently %s and %s." % (city, state, str(temp_f), condition))
print("\nFor a full report, see: \n%s" % (forecast_link))

print("\nHere is the full JSON record:\n")
pprint(weather)
