class Area:
    def __init__(self, name):
        self.name = name
        self.subareas = []

    # TODO: Define the add_subarea method to add a subarea to a given area
    def add_subarea(self, area):
        self.subareas.append(Area(area))

    # TODO: Define the dfs_traversal method to perform a depth-first search traversal over the areas
    def dfs_traversal(self, visited=None):
        if visited is None:
            visited = set()
        visited.add(self.name)
        print(self.name, end='->')
        for area in self.subareas:
            if area not in visited:
                area.dfs_traversal()


# TODO: Construct a tree to represent areas of a city

town = Area('Accra')
town.add_subarea('Kaneshi')
town.add_subarea('Amasaman')
town.add_subarea('Kasoa')
town.subareas[0].add_subarea('Abossey Okai')
town.subareas[0].add_subarea('Pramprom')
town.subareas[1].add_subarea('Ashalaja')
town.subareas[1].add_subarea('Obeeyie')
town.subareas[2].add_subarea('Denkyira')
town.subareas[2].add_subarea('Ofankor')

#Conduct a DFS traversal to print all areas
print("Areas and its subareas in Accra include")
town.dfs_traversal()
print('end')