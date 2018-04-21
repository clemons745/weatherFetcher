#! /usr/bin/python3

# Please input your information in the variables below


#####Weather Imformation#####

# List of zip codes
# Format is 'zipcode,countrycode'
zipcodes = ['12345,us', '12345,us']

# apikey for openweathermap.org
# If you don't have one, you can sign up for a free one on their website
# This program only pulls free information, so no need for a paid api key
apiKey = ''

# Set the unit measurement
# imperial for Fahrenheit
# metric for Celsius
# standard for Kelvin
units = 'imperial'


#####Email Information#####

# If using gmail, you must enable sign in with less secure apps
smtpServer = 'smtp.example.com'

smtpPort = 587

# This is the email address the email will come from
fromEmailAddress = 'example@example.com'

# Email password
emailPassword = 'examplePassword'

# List of emails you would like the email from this program to go to
toEmailAddresses = ['example@example.com', 'example2.example.com']
