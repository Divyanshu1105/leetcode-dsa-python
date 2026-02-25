class RailwayNode:
    def __init__(self, name, node_type):
        self.name = name
        self.type = node_type
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.children.append(child)
        child.parent = self
    
    def get_all_stations(self):
        stations = []
        if self.type == "Station":
            stations.append(self.name)
        for child in self.children:
            stations.extend(child.get_all_stations())
        return stations
    
    def get_path_to_root(self):
        path = []
        current = self
        while current:
            path.append(current.name)
            current = current.parent
        return " → ".join(reversed(path))
    
    def get_all_path_root_normal(self):
        path = []
        current = self
        while current:
            path.append(current.name)
            current = current.parent
        return " → ".join(path)


    def get_all_stations_count(self):
        count = 1

        for child in self.children:
            count += child.get_all_stations_count()
        return count
    

railways = RailwayNode("Indian Railways","HQ")

#Zones
north = RailwayNode("Nothern Zone","HQ")
south = RailwayNode("Southern Zone","HQ")
east = RailwayNode("Eastern Zone","HQ")
west = RailwayNode("Western Zone","HQ")

railways.add_child(north)
railways.add_child(south)
railways.add_child(east)
railways.add_child(west)

delhi = RailwayNode("Delhi HQ","City HQ")
lucknow = RailwayNode("Lucknow HQ","City HQ")

north.add_child(delhi)
north.add_child(lucknow)

#stations under delhi
delhi.add_child(RailwayNode("New Delhi Station", "Station"))
delhi.add_child(RailwayNode("Old Delhi Station", "Station"))

lucknow.add_child(RailwayNode("Agra Station", "Station"))
lucknow.add_child(RailwayNode("Mathura Station", "Station"))

print("All stations under Northern Zone")
print(north.get_all_stations())


print("\n Path from New Delhi to Railways")
new_delhi = delhi.children[0]
print(new_delhi.get_path_to_root())


print("\n Root to Agra station to Railways : ")
agra = lucknow.children[0]
print(agra.get_all_path_root_normal())


print("\n Station count : ")
print(railways.get_all_stations_count())