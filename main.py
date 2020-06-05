#Made by Jada Ebong with assistance from Leon Yuan
import random, os
from fpdf import FPDF
import hashlib
count = 0
boards = []
while count!=500:
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
            #change? : el negrito(), el apache(), el borracho? 
    
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
    hash_string = f'HowdyRacks{count}';
    hash_object = hashlib.sha1(hash_string.encode('utf-8'))
    filename =  "LoteriaBoard_" + hash_object.hexdigest() + '.pdf' 
    path = str(os.getcwd()) + "/boards/"
    extPath = path + filename
    if not os.path.exists(path):
        os.makedirs(path)
    with (open(os.path.join(path, filename), "w+")):
        #PDF things
        pdf = FPDF('P','cm','A4')
        pdf.add_page()
        pdf.set_font('Arial','',12)
        #pdf.set_fill_color(203, 235, 232)
        pdf.set_margins(2,1,2)
        pdf.image("LoteriaBoardHeader_1.jpg", x = None, y = None, w = 19, h = 6, type = 'jpg', link = '')
        pdf.cell(20,1,"",0,1)
        xaxis=2
        yaxis=8
        for x in range(0,16):
            cardImage = 'cards/' + slot[x] + '.jpeg'
            if (x %4)-3==0 and x!=0:
                pdf.cell(20,1,"",0,0)
                pdf.image(cardImage, x = xaxis, y = yaxis, w = 3.5, h = 4, type = 'jpeg', link = '')
                if x != 15:
                   pdf.cell(20,1,"",0,0)  
                xaxis = 2
                yaxis = yaxis +5
            else :
                pdf.image(cardImage, x = xaxis, y = yaxis, w = 3.5, h = 4, type = 'jpeg', link = '')
                pdf.cell(1,4,"",0)
                xaxis = xaxis + 4.5
                
        pdf.output(extPath,'F')

    print(str(count) + " " +filename)
    print(slot)
    #increments count for the next board
    count = count +1