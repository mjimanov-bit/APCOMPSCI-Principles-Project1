
import random

# Step 1: Weather dataset
city_list = ["Denver", "New York", "Chicago", "Miami", "Seattle"]
forecast_number_list = [2, 2, 2, 2, 2]

icon_list = ["☀️", "🌧️", "☁️", "⛈️", "🌤️"]
condition_list = [
    "Sunny",
    "Rainy",
    "Cloudy",
    "Thunderstorms",
    "Partly Cloudy"
]

high_temp_list = [75, 62, 58, 84, 68]
low_temp_list = [48, 51, 42, 72, 50]


# Step 2: Create filtered lists
filtered_city_list = []
filtered_icon_list = []
filtered_condition_list = []
filtered_high_temp_list = []
filtered_low_temp_list = []


# Step 3: Traverse the dataset and filter forecasts
def filter_weather():

    for i in range(len(forecast_number_list)):

        if forecast_number_list[i] == 2:

            filtered_city_list.append(city_list[i])
            filtered_icon_list.append(icon_list[i])
            filtered_condition_list.append(condition_list[i])
            filtered_high_temp_list.append(high_temp_list[i])
            filtered_low_temp_list.append(low_temp_list[i])


# Step 4: Generate and display a random forecast
def update_screen():

    index = random.randint(0, len(filtered_city_list) - 1)

    print("\n------ WEATHER FORECAST ------")
    print("City:", filtered_city_list[index])
    print("Weather:", filtered_icon_list[index])
    print("Condition:", filtered_condition_list[index])
    print("High:", filtered_high_temp_list[index], "°F")
    print("Low:", filtered_low_temp_list[index], "°F")
    print("------------------------------")


# Step 5: Filter the weather data
filter_weather()


# Step 6: Allow the user to generate forecasts
while True:

    choice = input("\nPress Enter for a forecast or type 'q' to quit: ")

    if choice.lower() == "q":
        break

    update_screen()
