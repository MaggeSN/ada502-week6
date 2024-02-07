import requests

class TemperatureRetriever:

    def retrieve(self, lat, long, ts):
        """
        This method retrieves a temperature observation.
        """

        #do api calling here
        return 42

class TemperatureStore:
    


    def __init__(self):
        self.locations = {}


    def store(self, lat, long, ts, temp):
        """
        This method stores a temperature observation.
        """
        if (lat, long) in self.locations:
            location_map = self.locations[(lat, long)]
        else:
            location_map = {}
            self.locations[(lat, long)] = location_map
        location_map[ts] = temp
        

    def retrieve(self, lat, long, ts):
        if (lat, long) in self.locations:
            location_map = self.locations[(lat, long)]
            if ts in location_map:
                return location_map[ts]
        return None

