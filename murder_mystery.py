print("""


 ██▓███   █    ██  ██▓     ██▓███      ███▄ ▄███▓ █    ██  ██▀███  ▓█████▄ ▓█████  ██▀███     
▓██░  ██▒ ██  ▓██▒▓██▒    ▓██░  ██▒   ▓██▒▀█▀ ██▒ ██  ▓██▒▓██ ▒ ██▒▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒   
▓██░ ██▓▒▓██  ▒██░▒██░    ▓██░ ██▓▒   ▓██    ▓██░▓██  ▒██░▓██ ░▄█ ▒░██   █▌▒███   ▓██ ░▄█ ▒   
▒██▄█▓▒ ▒▓▓█  ░██░▒██░    ▒██▄█▓▒ ▒   ▒██    ▒██ ▓▓█  ░██░▒██▀▀█▄  ░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄     
▒██▒ ░  ░▒▒█████▓ ░██████▒▒██▒ ░  ░   ▒██▒   ░██▒▒▒█████▓ ░██▓ ▒██▒░▒████▓ ░▒████▒░██▓ ▒██▒   
▒▓▒░ ░  ░░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒▓▒░ ░  ░   ░ ▒░   ░  ░░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░ ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░   
░▒ ░     ░░▒░ ░ ░ ░ ░ ▒  ░░▒ ░        ░  ░      ░░░▒░ ░ ░   ░▒ ░ ▒░ ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░   
░░        ░░░ ░ ░   ░ ░   ░░          ░      ░    ░░░ ░ ░   ░░   ░  ░ ░  ░    ░     ░░   ░    
            ░         ░  ░                   ░      ░        ░        ░       ░  ░   ░        
                                                                    ░                         

                                                                                  
                                                      ^?J7^                        
                         ^G&&BY.                   :&@@@@@#^.                     
                        ^#@@@@@@@.                  :@@@@@@@@@J                    
                        P@@@@@@@J                    .@@@@@@@@&J.                  
                     .:JB@@@@@@@.                     .?G5G@@@@@@5                 
                  .7&@@@@@@@@B^!                          G@@@@@@@&:               
               !B@@@@@@@@@@@@@.       .~?.        :!&B!  ~@@@@@@@@@#               
              ^@@@@@@@@@@@@@@@#.    ~G@&G        .&@@@@@G@@@@@@@@@@&               
               Y@@@@@@@@@@@&@@@@J5#&B7.           ~:^&@@@@@@@@@@@@@@               
               Y@@@@@@@@@&: ~B@@@&@J                  :^#@@@@@@@@@@@7              
              P@@@@@@@@@@:    ..                        &@@@@@@@@@@@&              
             5@@@@@@@@@@!                              7@@@@@@@@@@@@@J             
             #@@@@@@@@@@^                            ^P@@@@@@@@@@@@@@&             
              P@@@@@@@@@P                          7&@@@@@@@@@@@@@@&G7             
               ~&@@@@@@@J                         #@@@@@@@@@@@@&5~.                
                 Y@@@@@@@^                        &@@@@5P@@@@@@.                   
                  .&@@@@@@:                       Y@@@@P#@@@@@^                    
                   .@@@@@@&                       :@@@@@@@@@@#                     
                   7@@@@@@#                        #@@@@Y@@@@@#:                   
                   &@@@@@@7                        ^@@@@G~@@@@@@!                  
                  ^@@@@@@@                          JB@@@~:&@@@@@7                 
                  Y@@@@#@&                           !@@Y.  5@@@@@^                
                  &@7?J.J@5                          B@^     .7@@@@7               
                 P@@B^   ~!                          Y^       ~@@&5.               
                 ~7?YY?:                                    ^7Y5!                  
                 
""")

import random

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
   def prepend(self, value):
        new_node = Node(value)

        if self.head != None:
            new_node.next = self.head
            self.head = new_node
            return 

        else:
            self.head = new_node
            return

   def __init__(self):
        self.head = None

   def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        node = self.head
        while node.next is not None:
            node = node.next

        node.next = new_node


suspect1_list = LinkedList()
suspect1_list.append("Vincent Vega")
suspect1_list.append("The suspect has a close relationship to mob boss Marsellus Wallace.")
suspect1_list.append("The suspect has a history as a hit man.")
suspect1_list.append("The suspect enjoys eating his fries in Holland with mayonnaise.")



suspect2_list = LinkedList()
suspect2_list.append("Jules Winnfield")
suspect2_list.append("The suspect has a close relationship to mob boss Marsellus Wallace.")
suspect2_list.append("The suspect has a history as a hit man.")
suspect2_list.append("The suspect left a burger wrapper at the scene or as he calls it 'a Royale with cheese'.")

suspect3_list = LinkedList()
suspect3_list.append("Butch Coolidge")
suspect3_list.append("The suspect was looking for money.")
suspect3_list.append("The suspect narrowly escaped death once thanks to a pair of toaster pastries.")
suspect3_list.append("Police report that the only object missing from the crime scene is a gold watch.")

suspect4_list = LinkedList()
suspect4_list.append("Mia Wallace")
suspect4_list.append("The suspect has a close relationship to mob boss Marsellus Wallace.")
suspect4_list.append("The suspect has a favorite joke that ends with the punch line 'Catch up'.")
suspect4_list.append("The last words Mr. Tarantino heard were 'I said goddamn! I said goddamn, goddamn, goddamn.'")

suspect5_list = LinkedList()
suspect5_list.append("Marsellus Wallace")
suspect5_list.append("The suspect was looking for money.")
suspect5_list.append("The suspect believes that 'Pride only hurts; it never helps.'")
suspect5_list.append("The suspect has taken away the L.A. privileges of someone that has wronged him.")

suspect6_list = LinkedList()
suspect6_list.append("Pumpkin and Yolanda")
suspect6_list.append("The suspect was looking for money.")
suspect6_list.append("The suspect has been referred to as a Beatle.")
suspect6_list.append("The suspect was interested in finding out the contents of a briefcase that was in Mr. Tarantino’s possession.")

suspect7_list = LinkedList()
suspect7_list.append("Winston Wolf")
suspect7_list.append("The suspect has a close relationship to mob boss Marsellus Wallace.")
suspect7_list.append("The suspect was looking for money.")
suspect7_list.append("The suspect is referred to as a land mammal or as the scientific name, Canis lupus.")




weapon1_list = LinkedList()
weapon1_list.append("Rope")
weapon1_list.append("Has been used since prehistoric times.")
weapon1_list.append("Has tensile strength.")
weapon1_list.append("It is of paramount importance in fields as diverse as construction, seafaring, exploration, sports, theatre, and communications.")

weapon2_list = LinkedList()
weapon2_list.append("Lead Pipe")
weapon2_list.append("The federal government banned the use of them.")
weapon2_list.append("A dull, silver-gray color that is easily scratched with a coin.")
weapon2_list.append("Can enter drinking water through corrosion.")

weapon3_list = LinkedList()
weapon3_list.append("Knife")
weapon3_list.append("Has been used since prehistoric times.")
weapon3_list.append("Originally made of wood, bone, and stone.")
weapon3_list.append("Usually attached to a handle.")

weapon4_list = LinkedList()
weapon4_list.append("Wrench")
weapon4_list.append("In the UK, Ireland, Australia, and New Zealand spanner is the standard term.")
weapon4_list.append("Frequently chrome-plated to resist corrosion and for ease of cleaning.")
weapon4_list.append("Used to provide grip and mechanical advantage in applying torque to turn objects.")

weapon5_list = LinkedList()
weapon5_list.append("Candlestick")
weapon5_list.append("Has been used since prehistoric times.")
weapon5_list.append("This is a style of a financial chart used to describe price movements of a security, derivative, or currency.")
weapon5_list.append("Can provide a method of keeping time.")

weapon6_list = LinkedList()
weapon6_list.append("Revolver")
weapon6_list.append("A Beatles album.")
weapon6_list.append("Popular model patented in 1836.")
weapon6_list.append("Also called a six shooter or a wheel gun.")

weapon7_list = LinkedList()
weapon7_list.append("Chainsaw")
weapon7_list.append("A common accident arises from 'kickback'.")
weapon7_list.append("Sometimes used for cutting ice.")
weapon7_list.append("Portable gasoline-, electric-, or battery-powered options.")



def storyline():
   print("\nBREAKING NEWS: \n")
   print("Last night, at approximately 8:05pm on October 14, 1994, Quentin Tarantino was murdered at his Hollywood mansion. We currently do not have a motive but there are rumors that Mr. Tarantino had had a dispute with a wealthy mob boss by the name of Marsellus Wallace.")
   
   input("\nPress ENTER to continue...\n")

   print("Mr. Tarantino was last seen on October 14, 1994 with 8 people. All 8 suspects are in custody.")

   input("\nPress ENTER to continue...\n")

   print("8 suspects in custody: Vincent Vega, Jules Winnfield, Butch Coolidge, Mia Wallace, Marsellus Wallace, Husband and wife duo Pumpkin and Yolanda, and Winston Wolf")

   input("\nPress ENTER to continue...\n")

   print("The suspect will be boarding a flight out of the country in 3 hours, you must identify the suspect and murder weapon before he/she boards the flight. Each clue adds 1 hour.")

   input("\nPress ENTER to continue...\n")


def show_suspect_menu():
      print("---------------------------------------------------------------------")
      print("                       === MENU ===                                  ")
      print("---------------------------------------------------------------------")
      print("                         Suspects                                    ")  
      print("---------------------------------------------------------------------")
      print("| 1. Vincent Vega  | 2. Jules Winnfield   | 3. Butch Coolidge      | ")
      print("---------------------------------------------------------------------")
      print("| 4. Mia Wallace   | 5. Marsellus Wallace | 6. Pumpkin and Yolanda | ")
      print("---------------------------------------------------------------------")
      print("                   | 7. Winston Wolf |                               ")
      print("---------------------------------------------------------------------")
      print("---------------------------------------------------------------------")
      print("| 0. View Murderer Clue                   | 8. Guess the Murderer  | ")
      print("=====================================================================")

def show_bio(selection):
   if selection == 1:
      print("\nVincent is a hitman who has been working for mob boss Marsellus Wallace in Amsterdam for over three years and recently returned to Los Angeles, where he has been partnered with Jules Winnfield. He wears a bola tie with his suit, has long hair pulled back into a ponytail, rolls his own cigarettes and orders his steak 'bloody as hell'. He expresses scrupulous loyalty towards his boss Marsellus. However, he can be a cold, selfish bully, and sometimes strongly resents what he sees as authority, to the point of stubborn foolishness.\n")
   elif selection == 2:
      print("\nJules is a hitman working alongside Vincent Vega for Marsellus Wallace. Jules seems to value friendships and loyalty, appears to be thoughtful, can be gregarious and talkative but has a slow temper, is a remorseless professional killer and is capable of psychologically tormenting a victim before 'popping a cap in his ass.' After narrowly avoiding death, Jules is stunned and swiftly re-evaluates his life, deciding to retire as a hitman.\n")
   elif selection == 3:
      print("\nButch is an aging boxer who agrees to lose a boxing match in exchange for a bribe from Marsellus Wallace. Butch betrays Marcellus by betting on his own victory (with presumably long odds) and wins the match by accidentally killing his opponent in the ring. Butch has a temper but this seems to be dampened by his feelings for others.\n")
   elif selection == 4:
      print("\nMia is the wife of wealthy mob boss Marsellus Wallace. Her behavior with Marsellus is sophisticated, reserved and sleek, but with Vincent she is very talkative, articulate and somewhat more casually dressed.\n")
   elif selection == 5:
      print("\nMarsellus is a wealthy Los Angeles mob boss married to Mia, a former aspiring actress. Marsellus is intelligent, straightforward, and loyal but when confronted with a problem may quickly resort to violence and murder, hence all of the characters who know Marsellus are wary of him.\n")
   elif selection == 6:
      print("\nPumpkin and Yolanda are a pair of small-time crooks who have been robbing liquor stores.\n")
   elif selection == 7:
      print("\nWinston drives fast, thinks fast and talks fast to swiftly, calmly and professionally solve problems, presumably those which arise from criminal activities. Wolf wears a tuxedo, carries large sums of cash, drinks his coffee with lots of cream and sugar and may have a penchant for private, high stakes gambling.\n")



def weapon_menu():
      print("=====================================================================")
      print("                      Murder Weapons                                 ")  
      print("---------------------------------------------------------------------")
      print("| 1. Rope          | 2. Lead Pipe         | 3. Knife    |            ")
      print("---------------------------------------------------------------------")
      print("| 4. Wrench        | 5. Candlestick       | 6. Revolver |            ")
      print("---------------------------------------------------------------------")
      print("                   | 7. Chainsaw |                                   ")
      print("---------------------------------------------------------------------")


storyline()

murderer_list =  None
selected_murderer = random.randint(1, 7)
if selected_murderer == 1:
      murderer_list = suspect1_list
elif selected_murderer == 2:
      murderer_list = suspect2_list
elif selected_murderer == 3:
      murderer_list = suspect3_list
elif selected_murderer == 4:
      murderer_list = suspect4_list
elif selected_murderer == 5:
      murderer_list = suspect5_list
elif selected_murderer == 6:
      murderer_list = suspect6_list
elif selected_murderer == 7:
      murderer_list = suspect7_list

murder_weapon_list = None
selected_murder_weapon = random.randint(1, 7)
if selected_murder_weapon == 1:
   murder_weapon_list = weapon1_list
elif selected_murder_weapon == 2:
   murder_weapon_list = weapon2_list
elif selected_murder_weapon == 3:
   murder_weapon_list = weapon3_list
elif selected_murder_weapon == 4:
   murder_weapon_list = weapon4_list
elif selected_murder_weapon == 5:
   murder_weapon_list = weapon5_list
elif selected_murder_weapon == 6:
   murder_weapon_list = weapon6_list
elif selected_murder_weapon == 7:
   murder_weapon_list = weapon7_list
   

clue = murderer_list.head
clue_counter = 0
murder_weapon_clue = murder_weapon_list.head
murder_weapon_counter = 0


while True:
   show_suspect_menu()  
   choice = int(input("Select a suspect to view their bio. Choose 1-7, 0 to view the murderer clue, or 8 to guess the murderer: "))
   if choice >= 1 and choice <= 7:
      show_bio(choice) 
      continue
   elif choice == 8:
      guess= int(input ("\nEnter the suspect you believe is the murderer: "))
      if guess == selected_murderer:
            print("\nYou have found the murderer! Now you must find the murder weapon.\n")
            while True:
               weapon_menu()
               weapon_choice = int(input ("\nEnter the weapon number (1-7) you believe was used or 0 for a weapon clue: "))
               if weapon_choice == selected_murder_weapon:
                  print("\nCONGRATULATIONS! You have succeeded in finding the murderer and murder weapon!")
                  break
               elif weapon_choice == 0:
                  murder_weapon_counter = murder_weapon_counter + 1 
                  if murder_weapon_counter <= 3:
                     print(f"\nHere's your murder weapon clue number {murder_weapon_counter}: {murder_weapon_clue.next.value}\n")
                     murder_weapon_clue = murder_weapon_clue.next
                     continue
                  else:
                     print("\nThere are no more weapon clues, you must guess the murder weapon\n")
                     continue
               else:
                  print("\nIncorrect weapon guess, the murderer has boarded the flight and got away. GAME OVER!")
                  break
            break
      else: 
         print("\nIncorrect guess, the murderer has boarded the flight and got away. GAME OVER!")
         break
   elif choice == 0:
      clue_counter = clue_counter + 1 
      if clue_counter <= 3:
         print(f"\nClue number {clue_counter}: {clue.next.value}\n")
         clue = clue.next
      else:
         print("\nThere are no more clues, you must guess the murderer\n")
         show_suspect_menu()  
         suspect_murderer = int(input("\nSelect the murderer: Choose 1-7\n"))  
         if suspect_murderer == selected_murderer:
            print("\nYou have found the murderer! Now you must find the murder weapon.\n")
            while True:
               weapon_menu()
               weapon_choice = int(input ("\nEnter the weapon number (1-7) you believe was used or 0 for a weapon clue: "))
               if weapon_choice == selected_murder_weapon:
                  print("\nCONGRATULATIONS! You have succeeded in finding the murderer and murder weapon!")
                  break
               elif weapon_choice == 0:
                  murder_weapon_counter = murder_weapon_counter + 1 
                  if murder_weapon_counter <= 3:
                     print(f"\nHere's your murder weapon clue number {murder_weapon_counter}: {murder_weapon_clue.next.value}\n")
                     murder_weapon_clue = murder_weapon_clue.next
                     continue
                  else:
                     print("\nThere are no more weapon clues, you must guess the murder weapon\n")
                     continue
               else:
                  print("\nIncorrect weapon guess, the murderer has boarded the flight and got away. GAME OVER!")
                  break
            break
         else:
            print("\nIncorrect guess, the murderer has boarded the flight and got away. GAME OVER!")
            break



