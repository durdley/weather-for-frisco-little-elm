import datetime
from datetime import timedelta, date, time
import bs4
from bs4 import BeautifulSoup
import requests
url= 'https://www.localconditions.com/weather-little-elm-texas/75068/forecast.php'
#frisco url='https://www.localconditions.com/weather-frisco-texas/75034/forecast.php'
page = requests.get(url)
soup =  BeautifulSoup(page.text, 'html.parser')

#parse url to obtain location
url_split = url.split('/')
ugly_location = url_split[3]
parse_location = ugly_location.split('-')
list_location = parse_location[1::]

location = ' '.join(list_location)
location = location.title()

todayWeather = soup.div.find_all("div",attrs={"class":"col-xs-12 col-md-6"})
futureWeather = soup.div.find_all("div",attrs={"class":"btn-group dropup"})

dayWeather = todayWeather[0].text
nightWeather = todayWeather[1].text
tomorrowDay = futureWeather[0].text
tomorrowNight = futureWeather[1].text
nextDay1 = futureWeather[2].text
nextNight1 = futureWeather[3].text
nextDay2 = futureWeather[4].text
nextNight2 = futureWeather[5].text
nextDay3 = futureWeather[6].text
nextNight3 = futureWeather[7].text

today = date.today()
tmrw = date.today() + timedelta(days=1)
next1 = date.today() + timedelta(days=2)
next2 = date.today() + timedelta(days=3)
next3 = date.today() + timedelta(days=4)
todayDate = today.strftime("%B %d, %Y")
tmrwDate = tmrw.strftime("%B %d, %Y")
next1Date = next1.strftime("%B %d, %Y")
next2Date = next2.strftime("%B %d, %Y")
next3Date = next3.strftime("%B %d, %Y")

def splitter(s):
    where_period = s.find('.')
    if where_period == -1:
        return s
    return s[:where_period]

dayWeather = splitter(dayWeather)
nightWeather = splitter(nightWeather)
tomorrowDay = splitter(tomorrowDay)
tomorrowNight = splitter(tomorrowNight)
nextDay1 = splitter(nextDay1)
nextNight1 = splitter(nextNight1)
nextDay2 = splitter(nextDay2)
nextNight2 = splitter(nextNight2)
nextDay3 = splitter(nextDay3)
nextNight3 = splitter(nextNight3)

print (f"\nFive day forecast for {location}")
print (f"\nWeather for {todayDate}:\nDaytime weather: {dayWeather[5:len(dayWeather)]}")
print (f"Nighttime weather: {nightWeather[7:len(nightWeather)]}\n")
print (f"Weather for {tmrwDate}:\nDaytime weather: {tomorrowDay[9:len(tomorrowDay)]}")
print (f"Nighttime weather: {tomorrowNight[13:len(tomorrowNight)]}\n")
print (f"Weather for {next1Date}:\nDaytime weather: {nextDay1[9:len(nextDay1)]}")
print (f"Nighttime weather: {nextNight1[13:len(nextNight1)]}\n")
print (f"Weather for {next2Date}:\nDaytime weather: {nextDay2[9:len(nextDay2)]}")
print (f"Nighttime weather: {nextNight2[13:len(nextNight2)]}\n")
print (f"Weather for {next3Date}:\nDaytime weather: {nextDay3[9:len(nextDay3)]}")
print (f"Nighttime weather: {nextNight3[13:len(nextNight3)]}\n")




#<div class="col-xs-12 col-md-6">
#<p><b>Day</b><br/>
#<div class="col-xs-12 col-md-6">
#<p><b>Night</b><br/>
#<div class="btn-group dropup">
#<button aria-label="Daytime..." or ="Nighttime..."
#<b>Day</b>
#<td><img alt="Little Elm, TX  weather condition is Clear and 63°F." src="https://www.localconditions.com/images/fcicons/sunnyn.png" 