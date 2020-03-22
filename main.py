#Made by Jada Ebong with assistance from Leon Yuan
import random, os
from fpdf import FPDF
pdf = FPDF()
count = 0
boards = []
while count!=5:
    #all possible cards
    cards = ["El gallo","El diablito","La dama","El catrín",
            "El paraguas","La sirena","La escalera","La botella",
            "El barril","El árbol","El melón","El valiente",
            "El gorrito","La muerte","La pera","La bandera","El bandolón",
            "El violoncello","La garza","El pájaro","La mano","La bota",
            "La luna","El cotorro","El HEB Partner","El Rowdy","El corazón",
            "La sandía","El tambor","El camarón","Las jaras","El músico",
            "La araña","El soldado","La estrella","El cazo","El mundo",
            "El Roadrunner","El nopal","El alacrán","La rosa","La calavera",
            "La campana","El cantarito","El venado","El Sol","La corona",
            "La chalupa","El pino","El pescado","La palma","La maceta",
            "El arpa","La rana"]
            #change? : el negrito(Rowdy), el apache(Roadrunner), el borracho?
    
    #slot represents the 16 different locations on a 4x4 loteria board
    slot = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

    #puts a random card into a slot, then deletes it from card pool so it can't be repeated
    for x in slot:
        newS = random.choice(cards)
        cards.remove(newS)
        slot[x] = newS

    #check for repeating boards
    if slot in boards:
        break
    else:
        boards.append(slot)

    #File I/O: creates a unique file for each board in RH_Loteria/boards
    filename =  str(count) + '.pdf' #add "YourLoteriaBoard" + # + .pdf
    path = str(os.getcwd()) + "/boards/"
    extPath = path + filename
    if not os.path.exists(path):
        os.makedirs(path)
    with (open(os.path.join(path, filename), "w+")):
        #PDF things
        pdf.add_page()
        pdf.set_font('Arial','B',8)
        pdf.cell(40,10,str(slot))
        pdf.output(extPath,'')

    print(filename)
    print(slot)

    #increments count for the next board
    count = count +1


#static folder holding all images, find image in folder
#image files have to be consistant, all certain size
#python libraries for dropping pics onto other pics
#make a list of lists instead of a dictionary
#500 boards not 400