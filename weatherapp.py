import urllib2
import json


api_key = '1425f1537d442803'


def tendayforecast(city, state):
	weather_api = api_key
	itemcounter = 0
	#this is the url of the website it basically goes to... varies by location
	#sample: http://api.wunderground.com/api/1425f1537d442803/forecast10day/q/CA/San_Francisco.json
	#replacing all the spaces with underscores because thats how the url syntax is for the weather.com api
	cityurl = city.replace(' ','_')
	stateurl = state.replace(' ', '_')
	url = 'http://api.wunderground.com/api/' + weather_api + '/' + 'forecast10day/q/' + stateurl +'/'+ cityurl + '.json'
	json_obj = urllib2.urlopen(url)
	data = json.load(json_obj)
	for item in data['forecast']['simpleforecast']['forecastday']:
		print item['forecast']['simpleforecast']['forecastday'][itemcounter]['high']
		print item['forecast']['simpleforecast']['forecastday'][itemcounter]['low']
		itemcounter = itemcounter + 1



url = 'http://api.wunderground.com/api/1425f1537d442803/forecast10day/q/California/San_Fransisco.json'
json_obj = urllib2.urlopen(url)
data = json.load(json_obj)

#for item in data['forecast']['simpleforecast']['forecastday'][0]['high']:
#	print item
itemcounter = 0
for item in data['forecast']['simpleforecast']['forecastday']:
	itemcounter = itemcounter + 1
	print data['forecast']['simpleforecast']['forecastday'][itemcounter]['high']
	print data['forecast']['simpleforecast']['forecastday'][itemcounter]['low']