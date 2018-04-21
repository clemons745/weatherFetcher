#! /usr/bin/python3

from var import *
from urllib.request import urlopen
import json
import smtplib


def fetchWeatherData(dataType, locationZip):
    # Ensure units variable is set correctly
    try:
        assert (units == 'imperial' or
                units == 'standard' or
                units == 'metric')
    except AssertionError:
        raise Exception('Units variable not set correctly.')

    # Build the URL
    url = 'http://api.openweathermap.org/data/2.5/\
%s?zip=%s&units=%s&appid=%s' % (dataType, locationZip, units, apiKey)

    # login and download weather data
    response = urlopen(url).read().decode('utf-8')
    weather = json.loads(response)

    # Ensure successful connection
    # 'cod' should be 200 if successful
    if weather['cod'] == 200 or weather['cod'] == '200':
        return weather
    else:
        raise Exception('Error Code "%s" while feching \
weather data with message "%s"' % (weather['cod'], weather['message']))


def sendEmail(emailText):
    # Sign in to email
    conn = smtplib.SMTP(smtpServer, smtpPort)
    conn.ehlo()
    conn.starttls()
    conn.login(fromEmailAddress, emailPassword)

    # Send email to all email address specified in var.py
    for email in toEmailAddresses:
        conn.sendmail(fromEmailAddress, email, emailText)

    # Finished with emailing, close the connection
    conn.quit()


def getWindDirection(deg):
    # The API returns wind direction in degrees.
    # This function converts it to a human readable direction
    if deg == 0:
        return 'N'
    elif deg > 0 and deg < 45:
        return 'NNE'
    elif deg == 45:
        return 'NE'
    elif deg > 45 and deg < 90:
        return 'ENE'
    elif deg == 90:
        return 'E'
    elif deg > 90 and deg < 135:
        return 'ESE'
    elif deg == 135:
        return 'SE'
    elif deg > 135 and deg < 180:
        return 'SSE'
    elif deg == 180:
        return 'S'
    elif deg > 180 and deg < 225:
        return 'SSW'
    elif deg == 225:
        return 'SW'
    elif deg > 225 and deg < 270:
        return 'WSE'
    elif deg == 270:
        return 'W'
    elif deg > 270 and deg < 315:
        return 'WNW'
    elif deg == 315:
        return 'NW'
    elif deg > 315 and deg < 360:
        return 'NNW'
    elif deg == 360:
        return 'N'
    else:
        raise Exception('Error occured calculating wind speed, \
deg is %s' % deg)


def createDailyEmail(currentWeather, forecastWeather):
    # This function creates the text of the email that will be sent
    return '''Subject: Daily Weather Report for %s\n\n\
Current Conditions
###################

City: %s
Condition: %s
Temperature: %sF
Humidity: %s%%
Pressure: %s
Wind Speed: %smph
Wind Direction: %s

Forecast
###################

Date: %s
Condition: %s
Temperature: %sF
Humidity: %s%%
Pressure: %s
Wind Speed: %smph
Wind Direction: %s

Date: %s
Condition: %s
Temperature: %sF
Humidity: %s%%
Pressure: %s
Wind Speed: %smph
Wind Direction: %s

Date: %s
Condition: %s
Temperature: %sF
Humidity: %s%%
Pressure: %s
Wind Speed: %smph
Wind Direction: %s

Date: %s
Condition: %s
Temperature: %sF
Humidity: %s%%
Pressure: %s
Wind Speed: %smph
Wind Direction: %s

Date: %s
Condition: %s
Temperature: %sF
Humidity: %s%%
Pressure: %s
Wind Speed: %smph
Wind Direction: %s

''' % (currentWeather['name'],
       currentWeather['name'],
       currentWeather['weather'][0]['main'],
       currentWeather['main']['temp'],
       currentWeather['main']['humidity'],
       currentWeather['main']['pressure'],
       currentWeather['wind']['speed'],
       getWindDirection(currentWeather['wind']['deg']),
       forecastWeather['list'][0]['dt_txt'],
       forecastWeather['list'][0]['weather'][0]['main'],
       forecastWeather['list'][0]['main']['temp'],
       forecastWeather['list'][0]['main']['humidity'],
       forecastWeather['list'][0]['main']['pressure'],
       forecastWeather['list'][0]['wind']['speed'],
       getWindDirection(forecastWeather['list'][0]['wind']['deg']),
       forecastWeather['list'][8]['dt_txt'],
       forecastWeather['list'][8]['weather'][0]['main'],
       forecastWeather['list'][8]['main']['temp'],
       forecastWeather['list'][8]['main']['humidity'],
       forecastWeather['list'][8]['main']['pressure'],
       forecastWeather['list'][8]['wind']['speed'],
       getWindDirection(forecastWeather['list'][8]['wind']['deg']),
       forecastWeather['list'][16]['dt_txt'],
       forecastWeather['list'][16]['weather'][0]['main'],
       forecastWeather['list'][16]['main']['temp'],
       forecastWeather['list'][16]['main']['humidity'],
       forecastWeather['list'][16]['main']['pressure'],
       forecastWeather['list'][16]['wind']['speed'],
       getWindDirection(forecastWeather['list'][16]['wind']['deg']),
       forecastWeather['list'][24]['dt_txt'],
       forecastWeather['list'][24]['weather'][0]['main'],
       forecastWeather['list'][24]['main']['temp'],
       forecastWeather['list'][24]['main']['humidity'],
       forecastWeather['list'][24]['main']['pressure'],
       forecastWeather['list'][24]['wind']['speed'],
       getWindDirection(forecastWeather['list'][24]['wind']['deg']),
       forecastWeather['list'][32]['dt_txt'],
       forecastWeather['list'][32]['weather'][0]['main'],
       forecastWeather['list'][32]['main']['temp'],
       forecastWeather['list'][32]['main']['humidity'],
       forecastWeather['list'][32]['main']['pressure'],
       forecastWeather['list'][32]['wind']['speed'],
       getWindDirection(forecastWeather['list'][32]['wind']['deg']))


def main():
    for locationZip in zipcodes:
        currentWeather = fetchWeatherData('weather', locationZip)
        forecastWeather = fetchWeatherData('forecast', locationZip)
        sendEmail(createDailyEmail(currentWeather, forecastWeather))


if __name__ == '__main__':
    main()
