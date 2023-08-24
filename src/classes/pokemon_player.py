class Player:
    """
    A class used to represent a PLAYER

    Attributes
    ----------
    name : str
        the name of the Player
    location : str
        the location of the Player. Used to describe the COMPUTER PLAYER
    player_descript : str
        used to describe the COMPUTER PLAYER
    num_pots : int
        the number of health potions the player has (default 1)

    Methods
    -------
    deplete_pot():
        depletes number of health potions by 1.
    """
    
    def __init__(self, input_name, input_location="", input_descript="", num_pots=1):
        self.name = input_name
        self.location = input_location
        self.player_descript = input_descript
        self.num_pots = num_pots

    def __str__(self) -> str:
        return f'{self.name} is in {self.location}. {self.player_descript}'

    def deplete_pot(self):
        """Increment the use of potions by Player."""
        self.num_pots -= 1