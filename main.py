#make it here
import random
count = 0
dictOfBoards = dict.fromkeys(range(5),[])
print(dictOfBoards)
while count!=1:
    #dictOfBoards[count]
    #all possible cards
    cards = ["El gallo","El diablito","La dama","El catrín",
            "El paraguas","La sirena","La escalera","La botella",
            "El barril","El árbol","El melón","El valiente",
            "El gorrito","La muerte","La pera","La bandera","El bandolón",
            "El violoncello","La garza","El pájaro","La mano","La bota",
            "La luna","El cotorro","El borracho","El Rowdy","El corazón",
            "La sandía","El tambor","El camarón","Las jaras","El músico",
            "La araña","El soldado","La estrella","El cazo","El mundo",
            "El Roadrunner","El nopal","El alacrán","La rosa","La calavera",
            "La campana","El cantarito","El venado","El Sol","La corona",
            "La chalupa","El pino","El pescado","La palma","La maceta",
            "El arpa","La rana"]
            #change? : el negrito(Rowdy), el apache(Roadrunner), el borracho?

    #slot = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    #Two options: Randomize and check all other card combos if it already happened 
    #OR go through in order until 400 but everyones first couple will be same - this wont work bc everyone could get same bingo

    slot = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    for x in slot:
        newS = random.choice(cards)
        cards.remove(newS)
        #for y in cards:
        #    if newS == y:
        #        cards.remove(newS)
        slot[x] = newS
    #print(slot)
    dictOfBoards[count].update(slot)
    dictOfBoards[count].append('*********************')
    count = count +1

print(str(dictOfBoards))
#static folder holding all images, find image in folder
#image files have to be consistant, all certain size
#python libraries for dropping pics onto other pics
#make a list of lists instead of a dictionary
#500 boards not 400