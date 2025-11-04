"""
Lab 3.1 – Simple Datasets and Aggregates

Goals:
- Create and manipulate Python lists and dictionaries.
- Compute aggregates such as sum, average, max, and min.

Instructions:
1. Create a list `temperatures` with daily temperatures for one week.
2. Create a dictionary `city_population` with at least 5 cities and their populations.
3. Compute:
   - The average temperature.
   - The maximum and minimum population.
   - The total population of all cities.
4. Print your results in a clear, formatted way.
"""

# Create the datasets
temperatures = [15.2, 16.8, 14.9, 17.5, 18.0, 16.1, 15.7]  # daily temps for one week
city_population = {
    "Riga": 632614,
    "Daugavpils": 82357,
    "Liepaja": 68106,
    "Jelgava": 55711,
    "Jurmala": 48001,
}

# Compute aggregates
average_temperature = sum(temperatures) / len(temperatures) if temperatures else 0.0
total_population = sum(city_population.values())
largest_city = max(city_population, key=city_population.get)
largest_population = city_population[largest_city]
smallest_city = min(city_population, key=city_population.get)
smallest_population = city_population[smallest_city]

# Print results
print(f"Temperatures (week): {temperatures}")
print(f"Average temperature: {average_temperature:.2f}°C")
print()
print("City populations:")
for city, pop in city_population.items():
    print(f" - {city}: {pop:,}")
print()
print(f"Largest city: {largest_city} - {largest_population:,}")
print(f"Smallest city: {smallest_city} - {smallest_population:,}")
print(f"Total population (all cities): {total_population:,}")
