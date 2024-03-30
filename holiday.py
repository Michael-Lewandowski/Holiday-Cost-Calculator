'holiday.py'

"""
Calculate and return the hotel cost based on number of nights
Calculate and return the plane cost based on the city
Calculate and return the car rental cost based on number of days
Calculate and return the total cost by summing hotel, plane, and car costs
Get user inputs for city_flight, num_nights, rental_days
Call the respective functions and calculate the total holiday cost
Print the total cost
"""

# Define the hotel cost function
def hotel_cost(num_nights):
    # Assuming a fixed rate per night
    rate_per_night = 100
    return num_nights * rate_per_night

# Define the plane cost function
def plane_cost(city_flight):
    # Flight costs vary by city
    city_costs = {"CityA": 200, "CityB": 250, "CityC": 300}
    return city_costs.get(city_flight, 0)

# Define the car rental function
def car_rental(rental_days):
    # Assuming a fixed daily rental cost
    daily_cost = 40
    return rental_days * daily_cost

# Define the total holiday cost function
def holiday_cost(hotel, plane, car):
    return hotel + plane + car

# Get user inputs
city_flight = input("Enter the city you are flying to: ")
num_nights = int(input("Enter the number of nights for the hotel stay: "))
rental_days = int(input("Enter the number of days for car rental: "))

# Calculate costs
total_cost = holiday_cost(hotel_cost(num_nights), plane_cost(city_flight), car_rental(rental_days))

# Print the total holiday cost
print(f"Total holiday cost: ${total_cost}")
