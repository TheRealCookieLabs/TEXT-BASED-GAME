import time
import random

pickupchains = 0
health = 100
foodList = {'Apple':15, 'Purified Water':25, 'Energy Bar':30, 'Raw Potatoes':-5, 'Bag of chips':10, 'Bread':20, 'Carrot':35, 'Vitamins':40, 'Apple with a worm':-10}
randomx = foodList[random.randrange(foodList.values())]
randomy = foodList[random.randrange(foodList.values())]
def start():
    print ('''Zzzzzz Zzzzzz Zzzz...... uhh where.. where am I?????''')
    time.sleep(2.5)
    print ('''You move around on the bed and chains clink together.''')
    print ('''Do you wait for help(1) or do you break the chains and lose 75 health(2)''')
    prompt_chains()
    time.sleep(1)
    print ('You sit up on the edge of the bed and let your eyes adjust to whatever light is in the room.')
    #Make screen less black
    time.sleep(2)
    print('Do you want to wrap chains around your hand(1) or leave them behind(2)')
    prompt_wrapchains()
    print ('''If you\'re curious, you can explore the facility(1). You can refill your health by finding food(2), but who knows what else you might find.
If you wanna play it safe, you could search for a phone and call 911(3).''')
    prompt_survival()
           
def prompt_chains():
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
        time.sleep(2)
        
    elif prompt_0 == '3':
        print ('You lost only 55 health')
        health = health - 55


def prompt_wrapchains():
    prompt_0 = input('Type your choice: ')
    if prompt_0 == '1':
        print('You have wrapped chains around your hand. Your attack has been boosted!')
        time.sleep(2)
    if prompt_0 != '1':
        print('You left a very useful item behind!')
        time.sleep(2)
    
        
def prompt_survival():
    prompt_0 = input("Type your choice: ")
    if prompt_0 == '1':
        print ('You get up from the bed and go out into a dark hallway.')
        time.sleep(2)
        print ('You let your eyes adjust to the dark. You can see a little better.')
        time.sleep(2)
        #make screen even less black
    elif prompt_0 == '2':
         
        
        print ("You have found a refrigerator")
        print ("Do you want to eat 1 food item(1) or 2 food items(2). (Warning: There\'s a chance of getting poisoned)")

def prompt_numfood():
    prompt_0 = input("Type your choice: ")
    if prompt_0 == '1':
        xvalue = foodList[x]
        yvalue = foodList[y]
        

    
start()
