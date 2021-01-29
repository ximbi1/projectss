import arcade

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "My arcade game"

# Constants used to scale our sprites from their original size
CHARACTER_SCAÑING = 0.8
TILE_SCALING = 0.5
COIN_SCALING = 0.7

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 20

# How many pixels to keep as a minimum margin between the character
# And the edge of the screen
LEFT_VIEWPORT_MARGIN = 250
RIGHT_VIEWPORT_MARGIN = 250
BOTTOM_VIEWPORT_MARGIN = 50
TOP_VIEWPORT_MARGIN = 100

class MyGame(arcade.Window):
    """
    Main application class.
    """
    
    def init(self) :
        
        # Call the  parent class and set up the window
        super().init(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # These are 'lists' thet keep track of our sprites. Each sprite should go into list
        self.coin_list = None
        self.wall_list = None
        self.player_list = None
        self.exit_list = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        # Our physics engine
        self.physics_engine = None

        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0

        # Keep track of a score
        self.score = 0

        # Load sounds
        self.collect_coin_sound = arcade.load_sound(":resources:sounds/coin1.wav")

        arcade.set_background_color(arcade.csscolor.POWDER_BLUE)

        def setup(self):
            """[set the game here. Call this function to restart the game]
            """

            # Used to keep track of our scrolling
            self.view_bottom = 0
            self.view_left = 0

            # Keep track of the score
            self.score = 0

            # Create the Sprite lists
            self.player_list = arcade.SpriteList()
            self.wall_list = arcade.SpriteList()
            self.coin_list = arcade.SpriteList()
            self.exit_list = arcade.SpriteList()

            # Set up the player , specifically placing it at these coordinates.
            image_source = ":resource:images/animated_characters/male_adventurer/maleAdventurer_walk1.png"

            
