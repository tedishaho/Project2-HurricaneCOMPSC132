import math

class Hurricane:
    # Categorizes various aspects of a hurricane (category, location, damage)
    def __init__(self, name, category, wind_speed, pressure, location, affected_areas):
        """
        Initialize the Hurricane object with key attributes.

        :param name: Name of the hurricane.
        :param category: Category of the hurricane (e.g., 1 to 5).
        :param wind_speed: Wind speed in mph or km/h.
        :param pressure: Central pressure in millibars (mb).
        :param location: Current location of the hurricane (e.g., latitude and longitude).
        :param affected_areas: List of affected areas (e.g., cities, states).
        """
        self.name = name
        self.category = category
        self.wind_speed = wind_speed
        self.pressure = pressure
        self.location = location
        self.affected_areas = affected_areas

    def update_location(self, new_location):
        """
        Update the location of the hurricane.

        :param new_location: New location as a tuple (latitude, longitude).
        """
        self.location = new_location
        print(f"The location of Hurricane {self.name} has been updated to {self.location}.")

    def add_affected_area(self, area):
        """
        Add a new area to the list of affected areas.

        :param area: Name of the area to add.
        """
        if area not in self.affected_areas:
            self.affected_areas.append(area)
            print(f"{area} has been added to the affected areas for Hurricane {self.name}.")
        else:
            print(f"{area} is already listed as affected by Hurricane {self.name}.")

    def display_info(self):
        """
        Display key information about the hurricane.
        """
        info = (
            f"Hurricane {self.name} Information:\n"
            f"Category: {self.category}\n"
            f"Wind Speed: {self.wind_speed} mph\n"
            f"Pressure: {self.pressure} mb\n"
            f"Location: {self.location}\n"
            f"Affected Areas: {', '.join(self.affected_areas) if self.affected_areas else 'None'}"
        )
        print(info)

    def calculate_damage_potential(self):
        """
        Calculate the potential damage based on the hurricane's category.

        :return: Description of the potential damage.
        """
        damage_potential = {
            1: "Minimal damage, primarily to unanchored structures.",
            2: "Moderate damage, risk to mobile homes and trees.",
            3: "Extensive damage, risk to buildings and infrastructure.",
            4: "Catastrophic damage, severe structural damage.",
            5: "Devastating damage, widespread destruction."
        }
        return damage_potential.get(self.category, "Unknown damage potential.")
    
    def forecast(self, speed, direction, hours):
        """
        Forecast the future location of the hurricane based on speed, direction, and time.

        :param speed: Speed of the hurricane in mph.
        :param direction: Direction of movement in degrees (0° is north, 90° is east).
        :param hours: Time in hours for the forecast.
        :return: New forecasted location as (latitude, longitude).
        """
        # Convert speed from mph to degrees latitude/longitude per hour
        miles_per_degree_lat = 69  # Approximate miles per degree of latitude
        miles_per_degree_lon = 69.172  # At the equator; varies with latitude

        # Calculate distance traveled in miles
        distance = speed * hours

        # Convert direction to radians
        direction_rad = math.radians(direction)

        # Calculate changes in latitude and longitude
        delta_lat = (distance * math.cos(direction_rad)) / miles_per_degree_lat
        delta_lon = (distance * math.sin(direction_rad)) / miles_per_degree_lon

        # Update location
        new_lat = self.location[0] + delta_lat
        new_lon = self.location[1] + delta_lon

        forecasted_location = (round(new_lat, 2), round(new_lon, 2))
        print(f"In {hours} hours, Hurricane {self.name} is forecasted to be at {forecasted_location}.")
        return forecasted_location
    def classification(self, wind_speed):
        if wind_speed >= 74 and wind_speed < 95:
            self.category = 1
        elif wind_speed >= 96 and wind_speed < 110:
            self.category = 2
        elif wind_speed >= 111 and wind_speed < 129:
            self.category = 3
        elif wind_speed >= 130 and wind_speed < 156:
            self.category = 4
        elif wind_speed > 157:
            self.category = 5
        return self.category
    def evacuation_planning(self):

        print("Evacuation measures need to be taken accordingly.")
        print("Please refer to the extended hurricane classificaton below")
        print("to determine if evacuation is immediately required.")
        print("")
        print("Power loss expectancy:")
        x = 1
        for n in self.power_loss:
            print(f"For category {x} hurricane; Expect {n} power loss")
            x += 1
        print("")
        print(f"Evacuation threshold: If category is {x - 4} or higher, you must evacuate!")
        print("")
        y = 1
        print("Property Damage:")
        for n in self.property_damage:
            print(f"For category {y} hurricane; Expect {n} property damage")
            y += 1
        print("")
        print(f"Evacuation threshold: If category is {y - 3} or higher, you must evacuate!")
        print("Damage and/or removal of roof decking is very likely")
        print("")
        z = 1
        print("Habitability of Area:")
        for n in self.habitability:
            print(f"If category {z}; area is considered {n}")
            z += 1
        print("")
        print(f"Evacuation threshold: If category is {z - 4} or higher, you must evacuate!")
        print("Access to water and electricity will be unavailable for prolonged time.")
        print("")

    def resource_distribution(self):
        area_assistance = None
        print("Distribution of resources")
        print("The distribution of resources will depend on the severity of the hurricane")
        print("Some areas are prioritized depending on the respective category")
        print("")
        print(f"Category: {self.category} (Hurricane Ian)")
        if self.category == 4 or self.category == 5:
            print("Victims in area are prioritized and require immediate assistance.")
            print("Area is considered uninhabitable")
            area_assistance = ['Water','Clothes','Food','Medicine','Transportation for medical care']
        elif self.category == 3:
            print("Access to water or electricity is very limited;")
            print("Area is considered very dangerous")
            area_assistance = ['Water','Food', 'Transportation for medical care']
        elif self.category == 2:
            print("Area is dangerous.")
            area_assistance = ['Water','Food']

        print(f"Resources for area: {area_assistance}")

# Example Usage:
hurricane_ian = Hurricane(
    name="Ian",
    category=4,
    wind_speed=150,
    pressure=937,
    location=(25.0, -80.0),  # Example coordinates
    affected_areas=["Florida", "Cuba"]
)

# Display information
hurricane_ian.display_info()

# Update location
hurricane_ian.update_location((27.0, -82.0))

# Add a new affected area
hurricane_ian.add_affected_area("South Carolina")

# Calculate damage potential
damage_potential = hurricane_ian.calculate_damage_potential()
print(f"Damage Potential: {damage_potential}")

# Forecast the future location
forecasted_location = hurricane_ian.forecast(speed=15, direction=90, hours=5)
# Output: In 5 hours, Hurricane Ian is forecasted to be at (25.0, -78.91)


print("")
hurricane_ian.classification(wind_speed=150)
hurricane_ian.evacuation_planning()
hurricane_ian.resource_distribution()

