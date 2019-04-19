import csv

class City:
  def __init__(self, name, latitude, longitude):
    self.name = name
    self.lat = latitude
    self.lon = longitude

cities = []

def cityreader(cities=[]):
  with open('./cities.csv', newline='') as csvfile:
    city_rows = csv.reader(csvfile, delimiter=',')
    for idx, row in enumerate(city_rows):
      if idx != 0:
        city, _, _, lat, lng = row[:5]
        cities.append(City(city, float(lat), float(lng)))

  return cities

cityreader(cities)

# for c in cities:
#   print(c.name, c.lat, c.lon)


# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  # within will hold the cities that fall within the specified region
  within = []

  min_lat, max_lat = min(lat1, lat2), max(lat1, lat2)
  min_lon, max_lon = min(lon1, lon2), max(lon1, lon2)

  for c in cities:
    if min_lat < c.lat < max_lat and min_lon < c.lon < max_lon:
      print(c.name, c.lat, c.lon)
      within.append(c)

  return within

cityreader_stretch(45, -100, 32, -120, cities)