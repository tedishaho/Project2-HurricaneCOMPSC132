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
