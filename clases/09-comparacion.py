class Coordenadas:
    def __init__(self, lat, lon):
       self.lat = lat
       self.lon = lon
    
    def __eq__(self, other):
        return self.lat == other.lat and self.lon == other.lon
    
    def __ne__(self, other):
        return self.lat != other.lat or self.lon != other.lon

    def __lt__(self, other):
        return self.lat + other.lat < self.lon + other.lon
    
    def __le__(self, other):
        return self.lat + other.lat <= self.lon + other.lon

coord = Coordenadas(45, 27) 
coord2 = Coordenadas(45, 27)
print(coord <= coord2)
