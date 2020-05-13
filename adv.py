from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

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
traversal_path = []
reversed_path = []
reversed_directions = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
visited = set()  # rooms we've visited

# while there are still unvisited rooms
while len(visited) < len(room_graph):

    # initialize next move as None
    next_move = None

    # for each exit (n,s,w,e) in the room (i.e. neighbors)
    for direction in player.current_room.get_exits():
        # for each exit direction, if it hasn't been visited, set it as the next_move
        if player.current_room.get_room_in_direction(direction) not in visited:
            next_move = direction
    # if there is a viable move...
    if next_move is not None:
        # append the move to the traversal_path
        traversal_path.append(next_move)
        # breadcrumb trail to get back out
        # append the reversed direction to the reversed_path
        reversed_path.append(reversed_directions[next_move])
        player.travel(next_move)  # travel to next_move
        visited.add(player.current_room)  # add the room to visited
    else:
        # if there is no next move, use reversed_path to go back
        next_move = reversed_path.pop()  # pop the reversed_path's last element
        traversal_path.append(next_move)  # add that to traversal path
        player.travel(next_move)  # travel back to that room


# TRAVERSAL TEST - DO NOT MODIFY
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
