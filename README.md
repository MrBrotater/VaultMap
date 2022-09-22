# Acknowledgements
This game was adapted from concepts presented in Clear Code's Zelda Style RPG tutorial https://www.youtube.com/watch?v=QU1pPzEGrqw, which is published under the Creative Commons Zero (CC0) license.

project files: https://github.com/clear-code-projects/Zelda

The art assets and the soundtrack have been done by Pixel-boy and AAA and can be found here: https://pixel-boy.itch.io/ninja-adventure-asset-pack They are also published under a CC0 license.  Art and sounds will be changed eventually, but I am using these for testing and development.


# Learning Objectives
The game will consist of a large maze that changes periodically (e.g. maze runner) with a safe area in the middle.  The safe middle zone will close off at night and monsters will spawn in the maze.  At the start of the next day the maze will change before the doors to the safe area open.  The player wins by escaping the maze.

1) Implement a moving camera that follows the player around
2) Develop an algorithm to randomize the maze, while ensuring there is a valid solution
3) Implement some basic pathfinding/AI for the monsters in the maze
4) Add some unique/interesting things to find in the maze that may help or harm the player
5) If I am not bored by this point, possibly work on implementing a line of sight so that objects outside the player's field of view are darker and do not update on the screen.

# Planned Monster Classes:
Zombie: Wanders around randomly until spotting the player.  If zombie sees the player he moans loudly and attracts the attention of other zombies nearby.  Can be killed with a melee weapon, if the player has found one.

Ghost: Moves slowly, but can pass through walls.  Can be destroyed using a flashlight, if the player has found one.

Something: Rare, but a virtual death sentence if encountered.

# Planned Items:
1) Baseball bat - defence against zombies
2) Flashlight - defence against ghosts
3) Energy Drink - doubles movement speed for a while
