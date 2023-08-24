import random
from decimal import *

class Monster:
    """
    A class used to represent a POKEMON 

    Attributes
    ----------
    name : str
        Monster name
    hp : int
        The current number of hitpoitns (HP)
    state : str
        Frozen or NotFrozen. Primarily relevant when an IcePokemon is in play.
    turn_frozen : int
        The last turn # when POKEMON was last frozen.
    attack_counter : int
        A running count of total attacks. primarily used for FirePokemon unique ability.
    turn_counter : int
        A running count of total turns taken.

    Methods
    -------
    use_pot():
        Add HP to POKEMON. 30 % chance of FULL REJUVENATION else, 40 HP.
    set_turn_counter():
        Auto increments total turns by 1.
    set_attack_counter():
        Auto increments attacks by 1.
    set_turn_frozen():
        Sets POKEMON state as "Frozen"
        
    """
    def __init__(self, 
                name,
                hp=200,
                state="NotFrozen",
                turn_frozen=0,
                attack_counter=0,
                turn_counter=0):
        self.name = name
        self.hp = hp
        self.state = state # State refers to being frozen or not frozen.
        self.turn_frozen = turn_frozen
        self.attack_counter = attack_counter
        self.turn_counter = turn_counter # Keeps track of num of turns (attack, potion, or being frozen.)

    def use_pot(self):
        """
        Health potions have a 30% chance of a full rejuvenation.
        Otherwise the health potion returns 40 HP.
        """

        rejuv_bool = random.choices([0,1], weights = [30, 70], k=1)
        if 1 in rejuv_bool:
            add_hp = 200 - self.hp # Prevents Pokemon from having over 200 health.
        else:
            add_hp = min(40, 200 - self.hp)
        self.hp += add_hp
        print(f"The Health potion added {add_hp} health points!!")

    def set_turn_counter(self):
        """Increments total # of turns in game."""
        self.turn_counter += 1

    def set_attack_counter(self):
        """Increments total # of attacks. Primarily used for FireMonster subclass."""
        self.attack_counter += 1

    def set_turn_frozen(self):
        """Determines when pokemon is last frozen."""
        self.turn_frozen = self.turn_counter
    
class LightMonster(Monster):
    """
    A sub-class used to represent a LIGHT POKEMON. Inherits from Monster class. 

    Attributes(specific to LightMonster)
    ----------
    name : str
        Zapdos (a lightning type POKEMON)
    type: str
        "light" type.
    strong_against: str
        strong against "fire" type.
    attack_name: str
        attack_name = "Lighning Strike"
    attack_str: str
        An ASCII representation of the "attack", to be used in the main game loop.

    Methods
    -------
    attack(self, Pokemon2):
        Reduces Pokemon2 HP by a calculated amount of damage.
    """
    def __init__(self, 
                hp=200,
                name="Zapdos", 
                type="light", 
                strong_against="fire", 
                attack_name="Lightning Strike",
                attack_str= "_.~'"'~._.~'"'~._.~'"'~._.~'"'~._   _.~'"'~._.~'"'~._.~'"'~._.~'"'~._   _.~'"'~._.~'"'~._.~'"'~._.~'"'~._",
                last_damage=0,
                state="NotFrozen", 
                turn_frozen=0,
                attack_counter=0,
                turn_counter=0):
        super().__init__(hp, state, turn_frozen, attack_counter, turn_counter)
        self.hp = hp
        self.name = name
        self.type = type
        self.strong_against = strong_against
        self.attack_name = attack_name
        self.attack_str = attack_str
        self.last_damage = last_damage
        self.state = state
        self.attack_counter = attack_counter

    def __str__(self) -> str:
        return f'{self.name.upper()} used {self.attack_name}, causing {self.last_damage} damage!!'

    def attack(self, Pokemon2):
        """
        Light attacks are highly variable. Attacks get a bonus to the damage range against fire types.
        """
        light_dmg = random.randrange(1,70)
        if Pokemon2.type == self.strong_against:
            light_dmg = random.randrange(35,100)
        Pokemon2.hp -= Decimal(light_dmg).quantize(Decimal('.01'),rounding=ROUND_UP)
        self.last_damage = Decimal(light_dmg).quantize(Decimal('.01'),rounding=ROUND_UP)
        self.attack_counter += 1
        

class FireMonster(Monster):
    """
    A sub-class used to represent a FIRE POKEMON. Inherits from Monster class. 

    Attributes(specific to LightMonster)
    ----------
    name : str
        Charizard (a fire type POKEMON)
    type: str
        "fire" type.
    strong_against: str
        strong against "ice" type.
    attack_name: str
        attack_name = "Fireball"
    attack_str: str
        An ASCII representation of the "attack", to be used in the main game loop.

    Methods
    -------
    attack(self, Pokemon2):
        Reduces Pokemon2 HP by a calculated amount of damage.
    """
    
    def __init__(self, 
                hp=200,
                name="Charizard", 
                type="fire", 
                strong_against="ice", 
                attack_name="Fireball",
                attack_str="--~~~~~~~~~~~~~=:>[XXXXXXXXX]>   --~~~~~~~~~~~~~=:>[XXXXXXXXX]>   --~~~~~~~~~~~~~=:>[XXXXXXXXX]>",
                last_damage=0,
                state="NotFrozen", 
                attack_counter=0,
                turn_frozen=0,
                turn_counter=0):
        super().__init__(hp, state, turn_frozen, turn_counter)
        self.hp = hp
        self.name = name
        self.type = type
        self.strong_against = strong_against
        self.attack_name = attack_name
        self.attack_str = attack_str
        self.last_damage = last_damage
        self.state = state
        self.attack_counter = attack_counter

    def __str__(self) -> str:
        return f'{self.name.upper()} used {self.attack_name}, causing {round(self.last_damage,2)} damage!!'

    def attack(self, Pokemon2):
        """
        Fire attacks get 15% stronger for every subsequent attack.
        """
        if self.attack_counter == 0:
            fire_dmg = 30
        else:
            fire_dmg = 30 * (1+ 0.15 * self.attack_counter)
        if Pokemon2.type == self.strong_against: # Attack bonus against ice POKEMON.
            fire_dmg *= 1.15
        Pokemon2.hp -= Decimal(fire_dmg).quantize(Decimal('.01'),rounding=ROUND_UP)
        self.last_damage = Decimal(fire_dmg).quantize(Decimal('.01'),rounding=ROUND_UP)
        self.attack_counter += 1

class IceMonster(Monster):
    """
    A sub-class used to represent a ICE POKEMON. Inherits from Monster class. 

    Attributes
    ----------
    name : str
        Articuno (an ICE type POKEMON)
    type: str
        "ice" type.
    strong_against: str
        strong against "lightning" type.
    attack_name: str
        attack_name = "Frozen Orb"
    attack_str: str
        An ASCII representation of the "attack", to be used in the main game loop.

    Methods
    -------
    attack(self, Pokemon2):
        Reduces Pokemon2 HP by a calculated amount of damage.
        Has a chance of freezing the opposing Pokemon
    """
    def __init__(self, 
                hp=200,
                state="NotFrozen", 
                name="Articuno", 
                type="ice", 
                strong_against="light", 
                attack_name="Frozen Orb",
                attack_str="""_.~"('_.~"('_.~"('_.~"('_.~"('   _.~"('_.~"('_.~"('_.~"('_.~"('   _.~"('_.~"('_.~"('_.~"('_.~"('""",
                last_damage=0,
                attack_counter=0,
                turn_frozen=0,
                turn_counter=0):
        super().__init__(hp, state, turn_frozen, turn_counter)
        self.hp = hp
        self.name = name
        self.type = type
        self.strong_against = strong_against
        self.attack_name = attack_name
        self.attack_str = attack_str
        self.last_damage = last_damage
        self.state = state
        self.attack_counter = attack_counter

    def __str__(self) -> str:
        return f'{self.name.upper()} used {self.attack_name}, causing {round(self.last_damage,2)} damage!!'

    def attack(self, Pokemon2):
        """
        Ice attacks are low in damage but have a 40% chance of freezing the opponent for one turn.
        """
        ice_dmg = 20
        if Pokemon2.type == self.strong_against:
            # print(f'{self.attack_name} was super effective!')
            ice_dmg *= 2
        Pokemon2.hp -= Decimal(ice_dmg).quantize(Decimal('.01'),rounding=ROUND_UP)
        self.last_damage = Decimal(ice_dmg).quantize(Decimal('.01'),rounding=ROUND_UP)
        self.attack_counter += 1
        if self.type != Pokemon2.type:
            freeze_bool = random.choices([1,0], weights = [40, 60], k=1)
            if 1 in freeze_bool:
                Pokemon2.state = "Frozen"
                Pokemon2.turn_frozen = Pokemon2.turn_counter