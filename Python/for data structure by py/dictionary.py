#py字典练习

locations = {'North America':{'USA':['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia']={'India':['Bangalore']}
locations['Asia']['China']=['Shanghai']
locations['Africa']={'Egypt':['Cairo']}

print(1)
usa_sorted=sorted(locations['North America']['USA'])
for city in usa_sorted:
    print(city)

print(2)
asia_cities = []
for countries,cities in locations['Asia'].items():
    city_country = cities[0]+" - "+countries
    asia_cities.append(city_country)
asia_sorted=sorted(asia_cities)
for city in asia_sorted:
    print(city)

print(3)
locations['Africa']['Penda']=['Dibai']
africa_sorted=sorted(locations['Africa'])
print(africa_sorted)
for country1 in africa_sorted:
    for country2,city in locations['Africa'].items():
        if country1 == country2:
            print(country1+' - '+city[0])
