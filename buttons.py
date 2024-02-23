from customtkinter import CTkButton
from settings import *

class Buttons(CTkButton):
    def __init__(self, parent,func, text, col, row, font, span = 1, color = 'dark-gray'):
        super().__init__(
            parent,
            command= func,
            text = text, 
            corner_radius= STYLING['corner-radius'],
            font= font,
            fg_color= COLORS[color]['fg'],
            hover_color= COLORS[color]['hover'],
            text_color= COLORS[color]['text']
        )
        self.grid(column = col, columnspan = span, row = row, sticky = 'nswe', padx = STYLING['gap'], pady = STYLING['gap'])
        
class ImageButton(CTkButton):
    def __init__(self, parent,func, col, row, image, text = '' , color = 'dark-gray'):
        super().__init__(
        parent,
        command = func,
        text= text,
        image= image,
        corner_radius= STYLING['corner-radius'],
        fg_color= COLORS[color]['fg'],
        hover_color= COLORS[color]['hover'],
        )
        self.grid(column = col,  row = row, sticky = 'nswe', padx = STYLING['gap'], pady = STYLING['gap'])
            
class NumButton(Buttons):
    def __init__(self, parent,func, span, text, col, row, font, color = 'light-gray'):  
        super().__init__(
            parent = parent,
            func = lambda:func(text),
            text = text,
            col = col,
            row = row,
            font = font,
            color = color,
            span= span
        )

class MathButton(Buttons):
    def __init__(self, parent,func,operator, text, col, row, font, color = 'orange'):
         super().__init__(
            parent = parent,
            text = text,
            func = lambda:func(operator),
            col = col,
            row = row,
            font = font,
            color = color,
        )

class MathImageButton(ImageButton):
    def __init__(self, parent,func,operator, col, row, image, color = 'orange'):
        super().__init__(
        parent = parent,
        func = lambda:func(operator),
        col = col,
        row = row,
        image = image,
        color = color,
    )