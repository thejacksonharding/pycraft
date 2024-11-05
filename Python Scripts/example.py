from mcpi import minecraft, block 
import time
X=266 # coordinates of the escape room corner
Y=69
Z=10
WIDTH = 10 #size of the escape room
ORANGE = 1 #id of of a wool colour
YELLOW = 4 #id of of a wool colour
BLUE = 11 #id of of a wool colour
mc = minecraft.Minecraft.create ()

# Create a connection to Minecraft


# Set player starting position
mc.player.setTilePos(0, -10, 0)

# Define room layout
def create_room():
    # Create walls using stone blocks
    mc.setBlocks(-5, 0, -5, 5, 3, 5, block.STONE.id)
    mc.setBlocks(-4, 0, -4, 4, 3, 4, block.AIR.id)  # Empty space inside the room

    # Create a door
    mc.setBlock(0, 1, -5, block.WOODEN_SLAB.id, 1)  # Upper part of door
    mc.setBlock(0, 0, -5, block.WOODEN_SLAB.id, 0)  # Lower part of door

    # Create a 'key' item (represented by a block)
    mc.setBlock(2, 1, 0, block.GOLD_BLOCK.id)  # Key position
    mc.postToChat("Find the key to unlock the door!")

# Function to check for interaction with the key
def check_key():
    player_tile_pos = mc.player.getTilePos()
    if player_tile_pos.x == 2 and player_tile_pos.y == 1 and player_tile_pos.z == 0:
        mc.postToChat("You've found the key!")
        unlock_door()

# Function to unlock the door
def unlock_door():
    mc.setBlock(0, 0, -5, block.AIR.id)  # Remove the door block to unlock it
    mc.setBlock(0, 1, -5, block.AIR.id)  # Remove the upper door block
    mc.postToChat("The door is now unlocked!")

# Create the room
create_room()

# Game loop to check for key interaction
while True:
    check_key()
    time.sleep(0.5)  # Check every half second
