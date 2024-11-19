from mcpi.minecraft import Minecraft
from mcpi import block
import time

# Connect to Minecraft
mc = Minecraft.create()
game = True

# Get the player's initial position
x, y, z = mc.player.getTilePos()

# Build a fully enclosed stone room (8x8x8) with no escape
# Player will be trapped inside the room

# Clear the area first for building the house (create space)
for dx in range(10):
    for dz in range(10):
        mc.setBlock(x + dx, y, z + dz, block.AIR.id)

# Build walls (stone)
for dx in range(10):
    for dz in range(10):
        if dx == 0 or dx == 9 or dz == 0 or dz == 9:
            for dy in range(5):  # Stone walls from the floor to just below the roof
                mc.setBlock(x + dx, y + dy, z + dz, 7)

# Build the ceiling (stone)
for dx in range(10):
    for dz in range(10):
        mc.setBlock(x + dx, y + 5, z + dz, 7)

# Build the floor (stone)
for dx in range(10):
    for dz in range(10):
        mc.setBlock(x + dx, y - 1, z + dz, 7)

# Create a door space at one side
mc.setBlock(x + 4, y, z, block.AIR.id)

# Place torches for lighting
mc.setBlock(x + 1, y + 1, z + 1, block.TORCH.id)
mc.setBlock(x + 8, y + 1, z + 1, block.TORCH.id)
mc.setBlock(x + 1, y + 1, z + 8, block.TORCH.id)
mc.setBlock(x + 8, y + 1, z + 8, block.TORCH.id)

# Place wood blocks with instructions for the challenges
mc.setBlock(x + 2, y + 1, z + 2, block.WOOD.id)  # Hint 1
mc.setBlock(x + 5, y + 1, z + 2, block.WOOD.id)  # Hint 2

# Hide the lever behind a stone wall (secret)
mc.setBlock(x + 4, y + 1, z + 4, 69, 8)  # Lever (upside down)

# Function to handle block hits
def handle_block_hits(game):
    blockEvents = mc.events.pollBlockHits()

    for blockEvent in blockEvents:
        # Check if the player hits any of the wood blocks for instructions
        if blockEvent.pos.x == x + 2 and blockEvent.pos.y == y + 1 and blockEvent.pos.z == z + 2:
            mc.postToChat("Hint 1: Hit the wood block to find your first clue.")
        elif blockEvent.pos.x == x + 5 and blockEvent.pos.y == y + 1 and blockEvent.pos.z == z + 2:
            mc.postToChat("Hint 2: The lever is hidden, look around carefully.")
        
        # Check if the player hits the lever (exit)
        if blockEvent.pos.x == x + 4 and blockEvent.pos.y == y + 1 and blockEvent.pos.z == z + 4:
            # Remove all the blocks to free the player
            for dx in range(10):
                for dy in range(6):
                    for dz in range(10):
                        # Remove all blocks except for the air space where the player is and the door space
                        if not (dx == 4 and dy == 0 and dz == 0):  # Keep the door space
                            mc.setBlock(x + dx, y + dy, z + dz, block.AIR.id)

            # Post a message to the player
            game = False
            mc.postToChat("Congratulations! You've escaped!")
    return False

# Place the player inside the room
mc.player.setTilePos(x + 1, y + 1, z + 1)


# Loop to check for block hit events
while game ==True:
    handle_block_hits(game)  # Handle any block hit events
    time.sleep(0.5)  # Delay to prevent high CPU usage
