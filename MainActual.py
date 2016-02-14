import time
import random
pickupchains = 0

health = 100
meleeAttack = 5
kickAttack = 8
zombieHealth = 50
zombieScratchAttack = 8
prompt_0 = 0
morale = 20

    
foodDict = {'Apple':30, 'Purified Water':25, 'Energy Bar':35, 'Raw Potatoes':-5, 'Bag of chips':10, 'Bread':15, 'Carrot':20, 'Vitamins':40, 'Apple with a worm':-10}
foodList = ['Apple','Purified Water', 'Energy Bar', 'Raw Potatoes', 'Bag of chips', 'Bread', 'Carrot', 'Vitamins', 'Apple with a worm']

chains = False

x = random.randint(0,8)
y = random.randint(0,8)
while(y == x):
    y = random.randint(0,8)
firstItem = foodList[x]
secondItem = foodList[y]

def start():
    global health
    global prompt_0
    health = 100
    print ('''Zzzzzz Zzzzzz Zzzz...... uhh where.. where am I?????''')
    time.sleep(2.5)
    print ('''You move around on the bed and chains clink together.''')
    print ('''Do you wait for help(1) or do you break the chains and lose 75 health(2)''')
    prompt_chains()
    print('')
    time.sleep(1)
    print ('You sit up on the edge of the bed and let your eyes adjust to whatever light is in the room.')
    #Make screen less black
    time.sleep(2)
    print('Do you want to wrap chains around your hand(1) or leave them behind(2)')
    prompt_wrapchains()
    print('')
    print ('''If you\'re curious, you can explore the facility(1). You can refill your health by finding food(2), but who knows what else you might find.
If you wanna play it safe, you could search for a phone and call 911(3).''')
    prompt_survival()
    print('')
    if(prompt_0 == '1'):
        prompt_explorefacility()
        print('')
    if(prompt_0 == '2'):
        prompt_findfood()
    if(prompt_0 == '3'):
        print('You see a fire escape you could get onto(1) or you could continue to look for a phone(2)')
        prompt_phonedecision()
        print('')
        

def prompt_chains():
    global health
    global prompt_0
    prompt_0 = input("Type your choice: ")
    if prompt_0 == '1':
        for x in range(0,5):
            print('.')
            time.sleep(0.7)
        print ('You wait but no help arrives')
        time.sleep(2)
        print ('You have to break the chains yourself. However, waiting has made you calm down and you will only lose 55 health(3).')
        prompt_chains()

    elif prompt_0 == '2':
        print ('You panic realizing someone put you in these chains and break out furiously hurting yourself in the process')
        print ('You lost 75 health')
        health = health - 75
        print("Your health: "+ str(health))

    elif prompt_0 == '3':
        print ('You lost only 55 health')
        health = health - 55
        print("Your health: "+ str(health))


def prompt_wrapchains():
    global meleeAttack
    global pickupchains
    prompt_0 = input('Type your choice: ')
    if prompt_0 == '1':
        global attack
        print('You have wrapped chains around your hand. Your attack has been boosted!')
        pickupchains = 1
        meleeAttack = meleeAttack + 3
        print('Your attack: ' + str(meleeAttack))
        time.sleep(2)
                
    if prompt_0 != '1':
        print('You left a very useful item behind!')
        global attack
        print('Your attack: ' + str(meleeAttack))
        time.sleep(2)


def prompt_survival():
    global prompt_0
    prompt_0 = input("Type your choice: ")
    if prompt_0 == '1':
        print ('You get up from the bed and go out into a dark hallway.')
        time.sleep(2)
        print ('You let your eyes adjust to the dark. You can see a little better.')
        time.sleep(2)
        #make screen even less black
    elif prompt_0 == '3':
        print ('You walk to the other end of the room and feel along the wall for a phone.')
        time.sleep(2)
        print ('You don\'t find a phone')
                

def prompt_explorefacility():
    print('You can barely make out the outline of 1 door on both sides of the hallway.')
    time.sleep(2)
    print("Do you want to go to go through one of the doors(1) or head down the hallway to go down the stairs(2)")
    prompt_0 = input("Type your choice: ")
    if prompt_0 == '1':
        print('Do you want to the room on the left(1) or the right(2)?')
        prompt_choosedoor()
    elif prompt_0 == '2':
        print("You walk down the stairs cautiously because you hear a noise that sounds like approaching footsteps.")
        time.sleep(2.5)
        print("You see a face of another human and you rush over to open the door, but realize it is locked.")
        time.sleep(2)
        print('Do you open the door and let the man in(1) or do you leave the unknown person locked out(2)?')
        prompt_opendoor()

def prompt_choosedoor():
    prompt_0 = input('Type your choice: ')
    if prompt_0 == '1':
        print('You enter the room slowly, and suddenly notice you\'re not the only one in the room.')
        time.sleep(2)
        print('You walk to the person.')
        time.sleep(1.5)
        print('You ask \"Excuse me, where am I?\" and then the person turns around.')
        time.sleep(2)
        print('Before you can react, the person grabs you by the throat and begins to strangle you.')
        time.sleep(2)
        print('You realize you\'re staring into the bloodthirsty eyes of a zombie.')
        time.sleep(2)
        print('Do you punch(1) or kick(2) the zombie?')
        prompt_attackzombie()
                
def prompt_opendoor():
    global morale
    print("")
    prompt_0 = input("Type your choice: ")
    if prompt_0 == '1':
        print('He runs in and mumbles \"Thank you,\" and he runs up the stairs quickly')
        time.sleep(2)
        print('''Do you want to find out what the man was running away from by exploring the second floor of the asylum(1)
or go up to the third floor and see if you can get more info from the man(2).''')
        prompt_choosingfloors()
    elif prompt_0 == '2':
        print('''Realizing that you don\'t know this guy at all or what his intent is, you stay on the stairs watching his face through the small glass
window of the door. He looks panicked and keeps pounding on the door whilst looking over his shoulders intermittently.''')
        time.sleep(4)
        print('He looks at you solemnly, then stops pounding on the door as you make out pale hands dragging his face away from your line of sight.')
        time.sleep(2)
        print('You realize that you are going to have to be alot more careful as you walk around this odd place.')
        time.sleep(3)
        print('You have lost 5 morale because you let the man die instead of helping him. If you lose all the morale, you will lose the will to continue going.')
        morale = morale - 5
        print("YOUR MORALE: " + str(morale))
        time.sleep(2)
        print('Now do you go up to the third floor to search for more items(1), or you can head all the way down to the first floor(2).')
        prompt_returnfloor()
                
                
def prompt_phonedecision():
    prompt_0 = input("Type your choice: ")
    if prompt_0 == '1':
        print('You get out onto the fire escape, thinking you can go down to the ground and get off.')
        time.sleep(2)
        print('As you go down the fire escape, you realize that it ends at the bottom of the second level, so you are ten feet off the ground.')
        time.sleep(3)
        print('You can get into the window of the second floor and see what is in there(1), or you can jump down to the ground, risking your safety(2).')
        prompt_jumpexplore()

            
def prompt_jumpexplore():
    prompt_0 = input("Type your choice: ")
    if prompt_0 == '1':
        print('You enter the hallway, and suddenly notice you\'re not the only one there.')
        time.sleep(2)
        print('You walk up to the person.')
        time.sleep(1.5)
        print('You ask \"Excuse me, where am I?\" and then the person turns around.')
        time.sleep(2)
        print('Before you can react, the person grabs you by the throat and begins to strangle you.')
        time.sleep(2)
        print('You, then, realize you\'re staring into the bloodthirsty eyes of a zombie.')
        time.sleep(2)
        print('Do you punch(1) or kick(2) the zombie?')
        prompt_attackzombie()




def prompt_choosingfloors():
    global health
    prompt_0 = input("Type your choice: ")
    if prompt_0 == '1':
        print('You head into the gloom of the hallway, and peer left then right. You see something that looks like an exit sign, and begin to head for it.')
        for x in range(0,5):
            print('.')
            time.sleep(1)
        print('As you walk towards the exit, you feel relief wash over you knowing you\'ll be out of this creepy place.')
        time.sleep(3)
        print('You are about to reach the exit when something, someone, grabs you by the feet and you can\'t move, and then they begin to scratch and claw at your flesh.')
        time.sleep(3)
        print('You realize it is a zombie, and he begins dragging you to a herd of zombies in one of the rooms on the second floor. Your screams never even reach the ends of the hallways before your demise.')
        time.sleep(3)
        while(health > 0):
              print("Your health: " + str(health))
              health = health - 10
              time.sleep(1.25)
        if health <= 0:
              print('You are dead. GAME OVER.')
              time.sleep(5)
              
              
def prompt_returnfloor():
    global health
    prompt_0 = input("Type your choice: ")
    if prompt_0 == '1':
        print('You walk back up the stairs slowly and you are still traumatized from the zombie. You are scared that you might die in this facility.')
        time.sleep(3)
        print('You head back onto the third floor.')
        time.sleep(1.5)
        
    if prompt_0 == '2':
         print('You walk down the stairs and can\'t help but feel sorry for the guy you just watched get killed.')
         time.sleep(2)
         print('You make it to the first floor and check both ways now, not knowing when you might find the same fate as the man on the second floor.')
         time.sleep(2.5)
         print('You look out into the hallway, and notice the gleam of moon light washing over the floor. That has to be an exit.')
         time.sleep(2.25)
         print('You can examine the possible exit(1), or you can go search for items on the rest of the first floor(2).')
         prompt_exit1stfloor()
         
                
def prompt_attackzombie():
    global health
    global zombieHealth
    global meleeAttack
    global kickAttack
    global zombieScratchAttack
    prompt_0 = input("Type your choice: ")
    if prompt_0 == '1':
        while(zombieHealth > 25):
            print("Zombie deals 5 damage by choking you.")
            time.sleep(2)
            health = health - 5
            
            if health <= 0:
                print("You have died. GAME OVER!")
                break
                
            print("YOUR HEALTH: " + str(health))
            time.sleep(2)
            print("You deal " + str(meleeAttack)+ " damage to the zombie")
            time.sleep(2)
            zombieHealth = zombieHealth - meleeAttack
            print("ZOMBIE'S HEALTH: " + str(zombieHealth))
        if(zombieHealth < 25):
            print("Good Job! You have gotten the zombie to half of its health. It has released its grip and let you go.")
            time.sleep(2.5)
            print("You feel adrenaline rush through your veins.")
            time.sleep(2)
            print("You have the option of running away(1) or continue fighting the zombie with new strength(2).")
            prompt_adrenalinerush()

def prompt_adrenalinerush():
    global health
    global zombieHealth
    global meleeAttack
    global kickAttack
    global zombieScratchAttack
    prompt_0 = input("Type your choice: ")
    if prompt_0 == '1':
        print("You get up and run down the hallway, with the zombie following behind you.")
        time.sleep(2)
        print("When you get to the end of the hallway, you see a locker(1) that you could jump into to hide, or you can keep running(2).")      
        prompt_hiderun()
    if prompt_0 == '2':
        print("You continue to attack the zombie, and the zombie starts scratching you.")

def prompt_findfood():
    global health
    print("You come up to a refrigerator and decide to open to see if there's any food in it.")
    time.sleep(3)
    print("You found " + str(firstItem) + " and " + str(secondItem) + ".")
    time.sleep(3)
    print("The " + str(firstItem) + " added " + str(foodDict[firstItem]) + " to your health")
    health = health + foodDict[firstItem]
    if health > 100:
        health = 100
    print("YOUR HEALTH: " + str(health))
    time.sleep(2)
    print("The " + str(secondItem) + " added " + str(foodDict[secondItem]) + " to your health")
    health = health + foodDict[secondItem]
    if health > 100:
        health = 100
    print("YOUR HEALTH: " + str(health))
    time.sleep(2)
    print("After checking the fridge, you decide you have two options.")
    time.sleep(2)            
    print("You can either look around the room for something else(1), or go out in the hallway(2).")          
    prompt_fooddecision()

def prompt_fooddecision():
    global meleeAttack
    prompt_0 = input("Type your choice: ")
    if prompt_0 == '1':
        print("You search around the room and find a couple of items.")
        time.sleep(2)
        print("The items are: A wrench(1), a lead pipe(2), and a pair of crutches(3).")
        prompt_weaponchoice()
    if prompt_0 == '2':
        print('You can barely make out the outline of 1 door on both sides of the hallway.')
    time.sleep(2)
    print("Do you want to go to go through one of the doors(1) or head down the hallway to go down the stairs(2)")
    prompt_0 = input("Type your choice: ")
    if prompt_0 == '1':
        print('Do you want to the room on the left(1) or the right(2)?')
        prompt_choosedoor()
    elif prompt_0 == '2':
        print("You walk down the stairs cautiously because you hear a noise that sounds like approaching footsteps.")
        time.sleep(2.5)
        print("You see a face of another human and you rush over to open the door, but realize it is locked.")
        time.sleep(2)
        print('Do you open the door and let the man in(1) or do you leave the unknown person locked out(2)?')
        prompt_opendoor()
        
def prompt_weaponchoice():
    global meleeAttack
    prompt_0 = input("Type your choice: ")
    if prompt_0 == '1':
        if pickupchains == 1:
            print("Do you want to keep your chains(1) or pick up the wrench(2)?")
            prompt_keepwrench()
        if pickupchains == 0:
            print("You pick up the wrench.")
            time.sleep(1.5)
            print("Your attack is boosted by 5")
            meleeAttack = meleeAttack + 5
            time.sleep(1.5)
            print("YOUR ATTACK: " + str(meleeAttack))
            prompt_afterchoosingnewweapon()
    if prompt_0 == '2':
        if pickupchains == 1:
            print("Do you want to keep your chains(1) or pick up the lead pipe(2)?")
            prompt_keepleadpipe()
        if pickupchains == 0:
            print("You pick up the lead pipe.")
            time.sleep(1.5)
            print("Your attack is boosted by 4")
            meleeAttack = meleeAttack + 4
            time.sleep(1.5)
            print("YOUR ATTACK: " + str(meleeAttack))
            prompt_afterchoosingnewweapon()
    if prompt_0 == '3':
        if pickupchains == 1:
            print("Do you want to keep your chains(1) or pick up the lead crutches(2)?")
            prompt_keepcrutches()
        if pickupchains == 0:
            print("You pick up the crutches.")
            time.sleep(1.5)
            print("Your attack is boosted by 7")
            meleeAttack = meleeAttack + 7
            time.sleep(1.5)
            print("YOUR ATTACK: " + str(meleeAttack))
            prompt_afterchoosingnewweapon()

    
        


start()

