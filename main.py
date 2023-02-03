from PIL import Image, ImageDraw, ImageFont
import textwrap
from e import center, bottom


sizeImageUser = input('Format de l\'image souhaité ? > ')
i = Image.open('R.jpg')
width, height = i.size
draw = ImageDraw.Draw(i)

run = True

while run:
    selection = int(input("""

    [1] Text [2] Image [3] Soon..

    Que voulez vous insérer >> """))

    if selection in [1, 2, 3]:
        if selection == 1:
            phrase = input('Inscrivez votre phrase souhaité >> ')
            wrapper = textwrap.wrap(phrase, width=35)
            myFont = ImageFont.truetype('Montserrat-Italic-VariableFont_wght.ttf', 50)
            parameter = int(input("""
            
            [1] Top [2] Middle [3] Bottom

            Choisissez votre emplacement sur l'image >> """))
            if parameter in [1, 2, 3]:
                if parameter == 3:
                    bottom(40, wrapper, draw, width, height, myFont)
                if parameter == 2:
                    center(40, wrapper, draw, width, height, myFont)
            run = False
        else:
            pass
    else:
        print('Veuillez sélectionné entre 1 et 3')






    

i.show()