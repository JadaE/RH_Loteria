#Made by Jada Ebong with assistance from Leon Yuan
import random, os
from fpdf import FPDF
count = 0
boards = []
while count!=5:
    #all possible cards
    cards = ["El_gallo","El_diablito","La_dama","El_catrín",
            "El_paraguas","La_sirena","La_escalera","La_botella",
            "El_barril","El_árbol","El_melón","El_valiente",
            "El_gorrito","La_muerte","La_pera","La_bandera","El_bandolón",
            "El_violoncello","La_garza","El_pájaro","La_mano","La_bota",
            "La_luna","El_cotorro","El_Rowdy","El_corazón",
            "La_sandía","El_tambor","El_camarón","Las_jaras","El_músico",
            "La_araña","El_soldado","La_estrella","El_cazo","El_mundo",
            "El_Roadrunner","El_nopal","El_alacrán","La_rosa","La_calavera",
            "La_campana","El_cantarito","El_venado","El_Sol","La_corona",
            "La_chalupa","El_pino","El_pescado","La_palma","La_maceta",
            "El_arpa","La_rana"]
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
        pdf = FPDF('P','cm','A4')
        pdf.add_page()
        pdf.set_font('Arial','',12)
        pdf.set_margins(2,1,2)
#TODO: learn how to pass images into a cell
        #here instead of words, pass the image
        #header = pdf.image("LoteriaBoardHeaderTextured.png", x = None, y = None, w = 19, h = 6, type = 'png', link = '')
        pdf.image("LoteriaBoardHeaderTextured.png", x = None, y = None, w = 19, h = 6, type = 'png', link = '')
        #pdf.cell(19,6,header,1,1)
        pdf.cell(20,1,"",0,1)
        for x in range(0,16):
            if (x %4)-3==0 and x!=0:
                #pdf.cell(3.5,4,str(slot[x]),1,1)
                pdf.image(images(slot[x]), x = None, y = None, w = 19, h = 6, type = 'png', link = '')
                if x != 15:
                 pdf.cell(20,1,"",0,1)
            else:
                pdf.cell(3.5,4,str(slot[x]),1,0)
                pdf.cell(1,4,"",0)
                            
#for images, use call a def and send in slot[x]
# then in def return slot[x].pdf
        pdf.output(extPath,'F')

    print(filename)
    print(slot)

    #increments count for the next board
    count = count +1

def images(name):




#static folder holding all images, find image in folder
#image files have to be consistant, all certain size
#python libraries for dropping pics onto other pics
#make a list of lists instead of a dictionary
#500 boards not 400