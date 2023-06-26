#python program to display the weather forecast using openweathermap.org#
import requests

def printResult(data): #now data contains list of nested dictionaries# extract the relevant information and store it in variables
    city = data['city']['name']
    country = data['city']['country']
    latitude = data['city']['coord']['lat']
    longitude = data['city']['coord']['lon']
    pressure = data['list'][0]['main']['pressure']
    humidity = data['list'][0]['main']['humidity']
    temp = data['list'][0]['main']['temp']
    temp_min = data['list'][0]['main']['temp_min']
    temp_max = data['list'][0]['main']['temp_max']
    wind_speed = data['list'][0]['wind']['speed']
    description = data['list'][0]['weather'][0]['description']# display the result
    print('Weather forecast for {}, {}:'.format(city, country))
    print('Latitude: {}'.format(latitude))
    print('Longitude: {}'.format(longitude))
    print('Pressure: {}'.format(pressure))
    print('Humidity: {}'.format(humidity))
    print('Temperature: {}'.format(temp))
    print('Minimum Temperature: {}'.format(temp_min))
    print('Maximum Temperature: {}'.format(temp_max))
    print('Wind Speed: {}'.format(wind_speed))
    print('Description: {}'.format(description))


# get city name from user and update the url
city = input("Enter city name: ")
app_id = '98c4b8427da39b49ff700bc3526bd005'
url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&mode=json&APPID={}'.format(city, app_id)
res = requests.get(url)
if res.status_code == 200: #checking the status code of the request and handling error
    data = res.json()
    printResult(data)
elif res.status_code == 404:
    print("City not found")
elif res.status_code == 401:
    print("Invalid API key")
elif res.status_code == 429:
    print("API key blocked")
elif res.status_code == 500:
    print("Internal server error")
elif res.status_code == 503:
    print("Service unavailable")
elif res.status_code == 504:
    print("Gateway timeout")
elif res.status_code == 505:
    print("HTTP version not supported")
elif res.status_code == 511:
    print("Network authentication required")
elif res.status_code == 400:
    print("Bad request")
else :
    print("Error in the HTTP request")