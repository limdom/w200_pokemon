import sys
import os
import time
import random
#### ASCIIArt: #### 
from assets import pokemon_ascii
#### Classes:  ####
from classes import pokemon_player
from classes import pokemon_monster

class NotPokemon:
    """
    A class used to represent the main game.

    Methods
    -------
    slowprint(): 
        Makes use of sys.stdout.write/flush and time.sleep to give effect of printing one character at a time.

    splash_screen(): 
        Inital splash sequence to start game. Calls intro method.

    intro(): 
        NOT POKEMON backstory. Calls choose_pokemon method.

    choose_pokemon(): 
        User input to be use for Player instance name and Pokemon instance in gameplay method. Calls gameplay method. with player name and pokemon arguments.

    gameplay(player_name, pokemon_choice): 
        Takes player name and pokemon parameters to instantiate human player and human pokemon.
        Instantiates one of each pokemon types (lightning, fire, ice), and 3 Player instances. 
        The computer is then randomly assigned one of these pokemon and one of these player instances.
        Main game loop to battle pokemon until terminating condition: HP(hitpoints) is >= 0 or player surrenders.
        Calls one of four "Out-tro" sequences based on game outcome.

    win(player_name, pokemon_name, computer_name, computer_location): 
        "Out-tro" scenario if winning against computer. Calls choose_pokemon is player chooses to restart game, or exits outright.
    
    win_surrender(player_name, pokemon_name, computer_name, computer_location): 
        "Out-tro" scenario if surrendering against computer but "surviving". Calls choose_pokemon is player chooses to restart game, or exits outright.

    lose(player_name, pokemon_name, computer_name, computer_location): 
        "Out-tro" scenario if losing against computer. Calls choose_pokemon is player chooses to restart game, or exits outright.

    lose_surrender(player_name, pokemon_name, computer_name, computer_location): 
        "Out-tro" scenario if surrendering against computer but not "surviving". Calls choose_pokemon is player chooses to restart game, or exits outright.
    """

    def slowprint(s,t=0.05):
        """ 
        prints one character at a time in a string
        source: https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
        """
        for c in s:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(t)

    def splash_screen():
        """Splash screen with ASCII image."""
        # os.system('cls' if os.name == 'nt' else 'clear')
        os.system('cls||clear') # Clears terminal, Source: https://stackoverflow.com/questions/2084508/clear-terminal-in-python
        
        for line in pokemon_ascii.splash_screen:
            time.sleep(0.04)
            print(line)

        # time.sleep(0.5)
        print("==========================================================================")
        print("Not_Pokemon\n")  
        NotPokemon.slowprint("A POKEMON inspired post-apocalypse by DOMINIC LIM.")
        print("\nNOTE: PLEASE MAXIMIZE TERMINAL WINDOW AND ZOOM OUT FOR BEST EXPERIENCE")
        print("\n==========================================================================")
        time.sleep(0.5)
        input("Press [any key] to continue.")
        os.system('cls||clear') 
        
        NotPokemon.intro()

    def intro():
        """Introduces the Not_Pokemon backstory."""
        
        print("=============================================================================================================================================")
        print("In 2031, the world marveled as scientists from Nintendo invented POKEMON, animals that are genetically modified to a persons' will.")
        time.sleep(2)
        print("\nPOKEMON quickly proliferated as the hottest commodity. POKEMON not only became dear pets but also an essential component of the workforce.")
        time.sleep(2)
        print("\nHumankind reaches a golden age as POKEMON were applied to tackling humanity's greatest challenges.")
        time.sleep(2)
        print("\n\nIt wasn't very long until that technology began seeing military applications....")

        input("Press [any key] to continue.")
        os.system('cls||clear')
        print("=============================================================================================================================================")
        print("It's 2061. After decades of inaction by the World's governments, climate change is realized as a global catastrophe.")
        time.sleep(2)
        print("\nGovernments around the world desperately fight over habitable zones and increasingly scarce resources.")
        time.sleep(2)
        print("\nCritical municipal services are cut with citizens left fending for themselves.")
        time.sleep(2)
        print("\nRoving gangs prowl the streets with their killer POKEMON, looking to loot any unsuspecting victims.")
        time.sleep(2)
        print("\n\n\nWELCOME to NOT_POKEMON... \n\n")
        input("Press [any key] to continue.")
        # os.system('cls||clear')

        NotPokemon.choose_pokemon()    

    # def pre_choose():
    #     """
    #     Allows player to quit the game or to move on. Works as the splash screen after finishing the battle for replay."""
    #     NotPokemon.choose_pokemon() 

    def choose_pokemon():
        """
        Allows player option to input player name.  
        Gives player choice for pokemon type or to quit the game outright.
        Updated: Also provides additional information about POKEMON attacks and abilities.
        """

        os.system('cls||clear')
        
        name_bool = True
        
        while name_bool:
            print("==========================================================================")
            player_name = input("Enter player name: ").title()
            if len(player_name) >= 1:
                name_bool = False
            else:
                print("Enter a player name with at least 1 character.")
            
        choices_bool = True
        while choices_bool: # Only accept one of the specified

            print("==========================================================================")
            print("\t[L]ightning - LIGHTNING POKEMON are effective against FIRE POKEMON.")
            print("\t[F]ire - FIRE POKEMON are effective against ICE POKEMON.")
            print("\t[I]ce - ICE POKEMON are effective against LIGHTNING POKEMON.")
            print("\t[H]elp - For additional information about the POKEMON.")
            print("\t[Q]uit - End the game.\n")
            pokemon_choice = input(f"Choose your POKEMON, {player_name.title()}.\n")
            print("==========================================================================")
            
            if pokemon_choice in ["lightning", "l", "L"]:
                os.system('cls||clear') 
                NotPokemon.slowprint(f"{player_name}: ZAPDOS, I choose you!!\n")
                for line in pokemon_ascii.lightmonster_portrait: 
                    print(line)
                time.sleep(2)
                choices_bool = False
                NotPokemon.gameplay(player_name.title(), pokemon_choice)

            elif pokemon_choice in ["ice", "i", "I"]:
                os.system('cls||clear') 
                NotPokemon.slowprint(f"{player_name}: ARTICUNO, I choose you!!:\n")
                for line in pokemon_ascii.icemonster_portrait: 
                    print(line)
                time.sleep(2)
                choices_bool = False
                NotPokemon.gameplay(player_name.title(), pokemon_choice)

            elif pokemon_choice in ["fire", "f", "F"]:
                os.system('cls||clear') 
                NotPokemon.slowprint(f"{player_name}: CHARIZARD, I choose you!!:\n")
                for line in pokemon_ascii.firemonster_portrait: 
                    print(line)
                time.sleep(2)
                choices_bool = False
                NotPokemon.gameplay(player_name.title(), pokemon_choice)
                
            elif pokemon_choice == "help" or pokemon_choice == "h" or pokemon_choice == "H":
                print("\tLIGHTNING POKEMON have the highest potential damage ouput. \
                \n\t However, LIGHTNING STRIKE damage output is highly variable..\n")
                print("\tFIRE POKEMON have medium damage output. \
                \n\t With each subsequent attach, FIREBALL gains a 15 % base damage bonus.\n")
                print("\tICE POKEMON have the lowest damage output. \
                \n\t FROZEN ORB has a 40 % chance of freezing the opponent for 1 turn.")
                print("")
                print("==========================================================================")
                input("Press [any key] to continue.")

            elif pokemon_choice == "quit" or pokemon_choice == "q" or pokemon_choice == "Q":
                print(f"\nTry your luck in NOT_POKEMON another time, {player_name.title()}..")
                time.sleep(3) # Wait for 3 seconds before quitting.
                sys.exit()

            else:
                print("Entire a valid key entry:")
                print("Choose your POKEMON.\n")
                print("\t[L]ightning - LIGHTNING POKEMON are stronger than FIRE POKEMON.")
                print("\t[F]ire - FIRE POKEMON are stronger than ICE POKEMON.")
                print("\t[I]ce - ICE POKEMON are stronger than LIGHTNING POKEMON.")
                print("\t[H]elp - For additioanl information about the POKEMON.")
                print("\t[Q]uit - End the game.\n")
                print("==========================================================================")


    def gameplay(player_name, pokemon_choice):
        """
        Initialize Computer Instances: computer, pokemon2
        Initalize Player Instances: player1, pokemon1
        """

        # Define computer player (enemy):
        gangland = pokemon_player.Player("Immortan Joe", 
                        input_location="Desert Wasteland", 
                        input_descript="A ruthless enslaver and leader of the 'WarBoys', Immortan Joe uses his battle hardened POKEMON to great effect. Immortan Joe summons his POKEMON to attack!!")
        militant = pokemon_player.Player("Bane", 
                            input_location="Remnants of Gotham City", 
                            input_descript="Bane, having dispatched Batman, has total control over the smoldering ruins of Gotham City. Sensing a challenger, Bane summons his POKEMON to attack!!")
        wanderer = pokemon_player.Player("The Crazed Raider", 
                            input_location="Ruins of Back Bay, MA", 
                            input_descript="The Crazed Raider, having just looted an unsuspecting victim, senses another opportunity. The Crazed Raider immediately summons his POKEMON to attack!!")

        # Instantiate computer's pokemon (enemy):
        light,fire,ice = pokemon_monster.LightMonster(), pokemon_monster.FireMonster(), pokemon_monster.IceMonster()
        
        # Randomly choose computer Player and Pokemon:
        computer = random.choice([gangland,militant,wanderer])
        pokemon2 = random.choice([light,fire,ice])
        
        # Instantiate player's Player and Pokeman from choose_pokemon method.
        player1 = pokemon_player.Player(player_name)

        if pokemon_choice in ["lightning", "l", "L"]:
            pokemon1 = pokemon_monster.LightMonster()
        elif pokemon_choice in ["fire", "f", "F"]:
            pokemon1 = pokemon_monster.FireMonster()
        elif pokemon_choice in ["ice", "i", "I"]:
            pokemon1 = pokemon_monster.IceMonster()

        # Introduces player to Computer match-up (Computer name, description):
        os.system('cls||clear') 
        print("===================================================================================================================================")
        print(f"{player1.name} wanders in the {computer.location} when {player1.name} encounters {computer.name}!")
        time.sleep(1)
        print(f"\n{computer.player_descript}")
        time.sleep(1)
        NotPokemon.slowprint(f"\n{computer.name}: {pokemon2.name}! I choose you! \n\n")
        time.sleep(3)

        # Actual battle:
        input("Press [any key] to continue.")

        while (pokemon1.hp > 0) and (pokemon2.hp > 0):
                
            # Main game interface: header for player/pokemon stats.
            # Computer's Pokemon ASCII art is represented in top right corner.
            # Center panel contains battle stats for both the Computer and Human player.
            # Player's Pokemon ASCII art is represented in bottom left corner.
            os.system('cls||clear') 

            # ASCII represenation for Computer Player.
            if pokemon2.state == 'Frozen':
                for line in pokemon_ascii.ice_scaled_computer:
                    print(line)
            elif pokemon2.state != 'Frozen':
                if pokemon2.type == 'light':
                    for line in pokemon_ascii.lightmonster_scaled_computer:
                        print(line)
                elif pokemon2.type == 'fire':
                    for line in pokemon_ascii.firemonster_scaled_computer:
                        print(line)
                elif pokemon2.type == 'ice':
                    for line in pokemon_ascii.icemonster_scaled_computer:
                        print(line)

            # Battle stats for Computer Player. These are updated after the END of every turn.
            print(f"\nComputer: {computer.name: <30}\t \
            Pokemon: {pokemon2.name.upper(): <10} \t\t HP:{pokemon2.hp: <10} \t Type: {pokemon2.type.title(): <10} \t Strong Against: {pokemon2.strong_against.title(): <10}\
            \t State: {pokemon2.state: <10} \t # Potions:{computer.num_pots: <10}")
            
            # Battle stats for Human Player. These are updated after the END of every turn.                   
            print(f"Player: {player1.name: <30}\t\t \
            Pokemon: {pokemon1.name.upper(): <10} \t\t HP:{pokemon1.hp: <10} \t Type: {pokemon1.type.title(): <10} \t Strong Against: {pokemon1.strong_against.title(): <10}\
            \t State: {pokemon1.state: <10} \t # Potions:{player1.num_pots: <10}\n")
            
            # ASCII representation for Human Player.
            if pokemon1.state == 'Frozen':
                for line in pokemon_ascii.iced_scaled:
                    print(line)
            elif pokemon1.state != 'Frozen':
                if pokemon1.type == 'light':
                    for line in pokemon_ascii.lightmonster_scaled:
                        print(line)
                elif pokemon1.type == 'fire':
                    for line in pokemon_ascii.firemonster_scaled:
                        print(line)
                elif pokemon1.type == 'ice':
                    for line in pokemon_ascii.icemonster_scaled:
                        print(line)            

            # Main game loop. The human player plays first, followed by the computer player.
            player_choice = True
            while player_choice:

                # If human player is frozen, player skips one turn.
                if pokemon1.state == "Frozen":
                    print(f"{pokemon1.name} is frozen!")
                    player_move = input("Press [any key] to continue.")
                    pokemon1.state = "NotFrozen"
                    pokemon1.set_turn_counter()
                    player_choice = False

                # The player has two types of sets of decisions. 1) Attack, use potion or surrender, 2) Attack or Surrender (if used potions)
                elif player1.num_pots > 0:
                    player_move = input("[A]ttack, use [p]otion, or [s]urrender.").lower()
                    
                    # The player attacks, use the appropriate method. Light attack for lightmonster class, Fire attack for firemonster class, ice attack for icemonster class.
                    if player_move in ['a','attack']:
                        NotPokemon.slowprint(f"{player1.name}: {pokemon1.name.upper()}, use {pokemon1.attack_name}!\t{pokemon1.attack_str} \n",0.02)
                        pokemon1.attack(pokemon2)
                        print(pokemon1)
                        print("==========================================================================\n")
                        pokemon1.set_turn_counter()

                        # Terminates loop if the human player wins before Turn ends (i.e before computer player has a chance to play)
                        if pokemon2.hp <= 0:
                            time.sleep(2)
                            NotPokemon.win(player1.name, pokemon1.name, computer.name, computer.location)
                        else:
                            player_choice = False
                    
                    # The use of potion revives HP and depletes potion count on the Player class.
                    elif player_move in ['p','potion'] and player1.num_pots > 0:
                        NotPokemon.slowprint(f"{player1.name}: {pokemon1.name.upper()}! take a health potion!\n")
                        pokemon1.use_pot()
                        player1.deplete_pot()
                        pokemon1.set_turn_counter()
                        player_choice = False
                    
                    elif player_move in ['s','surrender']:
                        lose_or_win = random.choice(["lose","win"])
                        if lose_or_win == "lose":
                            NotPokemon.lose_surrender(player1.name, pokemon1.name, computer.name, computer.location)
                        elif lose_or_win == "win":
                            NotPokemon.win_surrender(player1.name, pokemon1.name, computer.name, computer.location)
                
                # Set of actions (attack or surrender) if potions are used.
                else:
                    player_move = input("[A]ttack or [s]urrender.").lower()
                    
                    if player_move in ['a','attack']:
                        NotPokemon.slowprint(f"{player1.name}: {pokemon1.name.upper()}, use {pokemon1.attack_name}!\t{pokemon1.attack_str} \n",0.02)
                        pokemon1.attack(pokemon2)
                        print(pokemon1)
                        print("==========================================================================\n")
                        pokemon1.set_turn_counter()

                        # Terminates loop if the human player wins before Turn ends (i.e before computer player has a chance to play)
                        if pokemon2.hp <= 0:
                            time.sleep(2)
                            NotPokemon.win(player1.name, pokemon1.name, computer.name, computer.location)
                        else:
                            player_choice = False
                    
                    # Surrendering randomly calls lose/surrender or win/surrender outros methods.
                    elif player_move in ['s','surrender']:
                        lose_or_win = random.choice(["lose","win"]) # If player chooses to surrender, player has a 50% chance of retreating and surviving the battle (win_surrender)
                        if lose_or_win == "lose":
                            NotPokemon.lose_surrender(player1.name, pokemon1.name, computer.name, computer.location)
                        elif lose_or_win == "win":
                            NotPokemon.win_surrender(player1.name, pokemon1.name, computer.name, computer.location)
            time.sleep(1)    

            # Computer moves 2nd. Computer skips turn if frozen. Computer by default uses potion if HP <= 100, else attack.
            # Because computer plays 2nd and at the end of the iterative loop, turn_counter is used to keep the computer frozen for the subsequent round.
            if pokemon2.state == "Frozen":
                if pokemon2.turn_counter == int(pokemon2.turn_frozen) +1:
                    print(f"{pokemon2.name} is frozen!")
                    pokemon2.state = "NotFrozen"
                    pokemon2.set_turn_counter()
                else: 
                    print(f"{pokemon2.name} is frozen!")
                    pokemon2.set_turn_counter()
            
            elif pokemon2.hp <= 100 and computer.num_pots > 0:
                NotPokemon.slowprint(f"{computer.name}: {pokemon2.name.upper()}! take a health potion!\n")
                pokemon2.use_pot()
                computer.deplete_pot()
                pokemon2.set_turn_counter()
            
            else:
                NotPokemon.slowprint(f"{computer.name}: {pokemon2.name.upper()}, use {pokemon2.attack_name}!\t{pokemon2.attack_str} \n",0.02)
                pokemon2.attack(pokemon1)
                print(pokemon2)
                print("==========================================================================\n")
                pokemon2.set_turn_counter()

            time.sleep(2)

        
        # Win or lose, outro methods are called with player name, pokemon name, computer name, and location parameters.
        if pokemon1.hp <= 0:
            time.sleep(2)
            NotPokemon.lose(player1.name, pokemon1.name, computer.name, computer.location)
        
        if pokemon1.hp > 0:
            time.sleep(2)
            NotPokemon.win(player1.name, pokemon1.name, computer.name, computer.location)

    def win(player_name, pokemon_name, computer_name, computer_location):
        """Win outro sequence if human player wins."""

        os.system('cls||clear') 
        print(f"\n{player_name}, you and your {pokemon_name.upper()} survive another day in the wasteland!")
        print(f"\nHaving vanquished {computer_name}, you can't help but feel a brief respite in the {computer_location}.")
        print(f"\nHaving just scraped by your last encounter, {player_name}, you wonder what danger lurks around the corner..")
        
        for line in pokemon_ascii.success:
            print(line)
        
        print("\n==========================================================================")
        print("[R]estart - To play the game again.")
        print("[Q]uit - End the game.\n")
        print("==========================================================================")
        
        restart_bool = True
        while restart_bool:
            restart_choice = input(f"Make your choice, {player_name}").lower()
            if restart_choice == "restart" or restart_choice == "r":
                NotPokemon.choose_pokemon() # returns back to game-start
                time.sleep(1)
            elif restart_choice == "quit" or restart_choice == "q":
                print(f"\nCome back another time, {player_name.title()}!!")
                time.sleep(1)
                sys.exit()
            else:
                print(f"Enter a valid entry.\n[R]estart - To play the game again.\n[Q]uit - End the game.")
    def win_surrender(player_name, pokemon_name, computer_name, computer_location):
        """Win outro sequence if human player surrenders and survives."""

        os.system('cls||clear')
        print(f"\nYour appeals to {computer_name}'s humanity somehow worked!!")
        print(f"\n{computer_name}: Skip town and never come back!") 
        print(f"\n{player_name}, you and your companion {pokemon_name.upper()} cheat death. You swallow your pride and leave the {computer_location}...")
        
        for line in pokemon_ascii.success:
            print(line)
        
        print("\n==========================================================================")
        print("[R]estart - To play the game again.")
        print("[Q]uit - End the game.\n")
        print("==========================================================================")
        
        restart_bool = True
        while restart_bool:
            restart_choice = input(f"Make your choice, {player_name}").lower()
            if restart_choice == "restart" or restart_choice == "r":
                NotPokemon.choose_pokemon() # returns back to game-start
                time.sleep(1) 
            elif restart_choice == "quit" or restart_choice == "q":
                print(f"\nCome back another time, {player_name.title()}!!")
                sys.exit()
            else:
                print(f"Enter a valid entry.\n[R]estart - To play the game again.\n[Q]uit - End the game.")

    def lose(player_name, pokemon_name, computer_name, computer_location):
        """Lose outro sequence if computer player wins."""

        os.system('cls||clear') 
        print(f"\n{player_name}, you have failed your entrusted {pokemon_name.upper()}...")
        print(f"\n{computer_name} continues to rule the {computer_location} with impunity.") 
       
        for line in pokemon_ascii.tomb_stone:
            print(line)
        
        NotPokemon.slowprint(f"\n\nTry your luck in NOT_POKEMON another time, {player_name}..")
        print("\n==========================================================================")
        print("[R]estart - To play the game again.")
        print("[Q]uit - End the game.\n")
        print("==========================================================================")
        
        restart_bool = True
        while restart_bool:
            restart_choice = input(f"Make your choice, {player_name}").lower()
            if restart_choice == "restart" or restart_choice == "r":
                NotPokemon.choose_pokemon() # returns back to game-start
                time.sleep(1)
            elif restart_choice == "quit" or restart_choice == "q":
                print(f"\nCome back another time, {player_name.title()}!!")
                time.sleep(1)
                sys.exit()
            else:
                print(f"Enter a valid entry.\n[R]estart - To play the game again.\n[Q]uit - End the game.")

    def lose_surrender(player_name, pokemon_name, computer_name, computer_location):
        """Lose outro sequence if human player surrenders and dies."""

        os.system('cls||clear')
        print(f"\nDespite your appeals to {computer_name}'s humanity, you were destroyed anyways.")
        print(f"\n{computer_name} continues to rule the {computer_location} with impunity.") 
        print(f"\n{player_name}, you have failed your entrusted {pokemon_name.upper()}...")
        
        for line in pokemon_ascii.tomb_stone:
            print(line)
        
        NotPokemon.slowprint(f"\n\nTry your luck in NOT_POKEMON another time, {player_name}..\n")
        print("==========================================================================")
        print("[R]estart - To play the game again.")
        print("[Q]uit - End the game.\n")
        print("==========================================================================")
        
        restart_bool = True
        while restart_bool:
            restart_choice = input(f"Make your choice, {player_name}").lower()
            if restart_choice == "restart" or restart_choice == "r":
                NotPokemon.choose_pokemon() # returns back to game-start
                time.sleep(1)
            elif restart_choice == "quit" or restart_choice == "q":
                print(f"\nCome back another time, {player_name.title()}!!")
                time.sleep(1)
                sys.exit()
            else:
                print(f"Enter a valid entry.\n[R]estart - To play the game again.\n[Q]uit - End the game.")

if __name__ == "__main__":
    NotPokemon.splash_screen()