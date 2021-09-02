import time
import numpy as np
import sys

# Delay printing
def delay_print(s):
    # print one character at a time
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

# Create the class
class Fighter():
    def __init__(self, name, types, moves, stats, health='==================='):
        # save variables as attributes
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = stats['ATTACK']
        self.defense = stats['DEFENSE']
        self.health = health
        self.bars = 20


    def fight(self, Fighter2):
        # Allow two fighters to fight each other

        # Print fight information
        print("-----BATTLE-----")
        print(f"\n{self.name}")
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("\nVS")
        print(f"\n{Fighter2.name}")
        print("TYPE/", Fighter2.types)
        print("ATTACK/", Fighter2.attack)
        print("DEFENSE/", Fighter2.defense)

        time.sleep(2) #To show it slower

        # Consider type advantages
        version = ['Siege', 'Shinobi', 'Horse Rider']
        for i,k in enumerate(version):
            if self.types == k:
                # Both are same type, son de el mismo tipo
                if Fighter2.types == k:
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts not very effective...'

                # Fighter2 is STRONG
                if Fighter2.types == version[(i+1)%3]:
                    Fighter2.attack *= 2
                    Fighter2.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts super effective!'

                # Fighter2 is WEAK
                if Fighter2.types == version[(i+2)%3]:
                    self.attack *= 2
                    self.defense *= 2
                    Fighter2.attack /= 2
                    Fighter2.defense /= 2
                    string_1_attack = '\nIts super effective!'
                    string_2_attack = '\nIts not very effective...'


        # Now for the actual fighting...
        # Continue while fihter still have health
        while (self.bars > 0) and (Fighter2.bars > 0):
            # Print the health of each fighter
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{Fighter2.name}\t\tHLTH\t{Fighter2.health}\n")

            print(f"Go {self.name}!")
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"\n{self.name} used {self.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_1_attack)

            # Determine damage
            Fighter2.bars -= self.attack
            Fighter2.health = ""

            # Add back bars plus defense boost
            for j in range(int(Fighter2.bars+.1*Fighter2.defense)):
                Fighter2.health += "="

            time.sleep(1)
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{Fighter2.name}\t\tHLTH\t{Fighter2.health}\n")
            time.sleep(.5)

            # Check to see if fighter fainted
            if Fighter2.bars <= 0:
                delay_print("\n..." + Fighter2.name + ' fainted.')
                break

            # Fighter2 turn

            print(f"Go {Fighter2.name}!")
            for i, x in enumerate(Fighter2.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"\n{Fighter2.name} used {Fighter2.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_2_attack)

            # Damage
            self.bars -= Fighter2.attack
            self.health = ""

            # Add back bars plus defense boost
            for j in range(int(self.bars+.1*self.defense)):
                self.health += "="

            time.sleep(1)
            print(f"{self.name}\t\tHLTH\t{self.health}")
            print(f"{Fighter2.name}\t\tHLTH\t{Fighter2.health}\n")
            time.sleep(.5)

            # Check to see if Fighter fainted
            if self.bars <= 0:
                delay_print("\n..." + self.name + ' fainted.')
                break

        xp = np.random.choice(5000)
        delay_print(f"\nYou got {xp} xp.\n")






if __name__ == '__main__':
    #Create Fighters
    Siege_Lv3 = Fighter('Siege Lv.3', 'Siege', ['Fire ball', 'Rock ball', 'Oil', 'Hit'], {'ATTACK':12, 'DEFENSE': 8})
    Shinobi_Lv3 = Fighter('Shinobi Lv.3', 'Shinobi', ['Sword Strike', 'Charge Hit', 'Silent Attack', 'Fast Attack'],{'ATTACK': 10, 'DEFENSE':10})
    Horse_Rider_Lv3 = Fighter('Horse Rider Lv.3', 'Horse Rider', ['Charge Hit', 'Run Hit', 'Fast Hit', 'Frenezy Attack'],{'ATTACK':8, 'DEFENSE':12})

    Siege_Lv1 = Fighter('Siege Lv.1', 'Siege', ['Fire ball', 'Rock ball', 'Oil', 'Hit'],{'ATTACK':4, 'DEFENSE':2})
    Shinobi_Lv2 = Fighter('Shinobi Lv.1', 'Shinobi', ['Sword Strike', 'Charge Hit', 'Silent Attack', 'Fast Attack'],{'ATTACK': 3, 'DEFENSE':3})
    Horse_Rider_Lv2 = Fighter('Horse Rider Lv.1', 'Horse Rider', ['Charge Hit', 'Run Hit', 'Fast Hit', 'Frenezy Attack'],{'ATTACK':2, 'DEFENSE':4})

    Siege_Lv2 = Fighter('Siege Lv.2', 'Siege', ['Fire ball', 'Rock ball', 'Oil', 'Hit'],{'ATTACK':6, 'DEFENSE':5})
    Shinobi_Lv2 = Fighter('Shinobi Lv.2', 'Shinobi', ['Sword Strike', 'Charge Hit', 'Silent Attack', 'Fast Attack'],{'ATTACK': 5, 'DEFENSE':5})
    Horse_Rider_Lv2 = Fighter('Horse Rider Lv.3\t', 'Horse Rider', ['Charge Hit', 'Run Hit', 'Fast Hit', 'Frenezy Attack'],{'ATTACK':4, 'DEFENSE':6})


    Siege_Lv3.fight(Shinobi_Lv3) # Get them to fight

    #pudeo usar self fihther2 para que el usiario escoja