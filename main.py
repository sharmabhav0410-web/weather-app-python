city = input("Enter city name: ")

if city.lower() == "pune":
    print("Temperature: 28°C")
    print("Weather: Cloudy")

elif city.lower() == "mumbai":
    print("Temperature: 31°C")
    print("Weather: Humid")

elif city.lower() == "delhi":
    print("Temperature: 35°C")
    print("Weather: Sunny")

else:
    print("Weather data not available")
