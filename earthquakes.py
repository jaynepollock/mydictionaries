'''
the eq_data file is a json file that contains detailed information about
earthquakes around the world for a period of a month.

NOTE: No hard-coding allowed except for keys for the dictionaries

1) print out the number of earthquakes '''


''''
2) iterate through the dictionary and extract the location, magnitude, 
   longitude and latitude of the location and put it in a new
   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a 
   magnitude > 6. Print out the new dictionary.
'''

import json

infile = open('eq_data.json','r')

eq = json.load(infile)


print('Number of earthquakes', len(eq["features"]))

eq_dict= {"earthquakes":[]}

for i in eq['features']:
   magnitude = i['properties']["mag"]
   if magnitude > 6:
      location = i['properties']['place']
      magnitude = i['properties']['mag']
      longitude = i['geometry']['coordinates'][0]
      latitude = i["geometry"]["coordinates"][1]

      earthquakes = {'Location:': location, 'Magnitude': magnitude, 
                     "Latitude": latitude, 'Longitude': longitude}
      eq_dict["earthquakes"].append(earthquakes)
      
 

print(eq_dict)




'''
3) using the eq_dict dictionary, print out the information as shown below (first three shown):

Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364


Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604


Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628

'''



