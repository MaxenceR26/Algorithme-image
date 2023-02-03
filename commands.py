from PIL import Image, ImageFont, ImageDraw
import textwrap

def center(padding, wrap, text, width, height, font):
    pad = padding
    for line in wrap:
        w, h = text.textsize(line, font=font)
        h += int(h*0.21)
        
        text.text(((width - w) / 2, ((height - h) / 2) - h*(len(wrap) / 4)), line, font=font) 
            
        height += h + pad

def bottom(padding, wrap, text, width, height, font):
    pad = padding
    for line in wrap:
        w, h = text.textsize(line, font=font)
        h += int(h*0.21)

        text.text(((width - w) / 2, ((height - h))), line, anchor='mb', font=font) 

        height += h + pad
            
        

# Center au milieu de l'image, horizontalement et verticalement