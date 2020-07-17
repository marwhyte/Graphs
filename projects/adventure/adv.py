from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


trackPrevRoom = [None]
dirOpposite = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}
visited = {}
roomMaster = {}
# check each direction                    dict_keys(['s', 'e', 'w'])
print(room_graph[6][1])


def possibleOptions(roomID):
    options = []
    # print(room_graph[room_id][1].keys()) This is kinda op gets the keys
    if 'n' in room_graph[roomID][1].keys():
        options.append('n')
    if 'e' in room_graph[roomID][1].keys():
        options.append('e')
    if 's' in room_graph[roomID][1].keys():
        options.append('s')
    if 'w' in room_graph[roomID][1].keys():
        options.append('w')
    return options


while len(visited) < len(room_graph):
    roomID = player.current_room.id
    # check room_id is in our Master
    if roomID not in roomMaster:
        # add to visited
        visited[roomID] = roomID
        # add all directions using OP function
        roomMaster[roomID] = possibleOptions(roomID)

    # check if there are any more directions to travel.
    if len(roomMaster[roomID]) < 1:
        prevRoom = trackPrevRoom.pop()
        traversal_path.append(prevRoom)
        # send player object in that direction
        player.travel(prevRoom)

    else:
        # What direction i wanna go next out of the direction master
        nextDirection = roomMaster[roomID].pop(0)
        traversal_path.append(nextDirection)
        # add what going back is to prev room
        trackPrevRoom.append(dirOpposite[nextDirection])
        player.travel(nextDirection)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
