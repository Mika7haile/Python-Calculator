import customtkinter as ctk
import darkdetect
from buttons import Buttons, ImageButton, NumButton, MathButton, MathImageButton
from PIL import Image
from settings import *
try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass
class Calculator(ctk.CTk):
    def __init__(self,isDark):
        
        # window setup
        super().__init__(fg_color= (WHITE, BLACK))
        self.geometry(f'{APP_SIZE[0]}x{APP_SIZE[1]}')
        ctk.set_appearance_mode(f'{"dark" if isDark else "light"}')
        self.resizable(False,False)
        self.change_title_bar_color(isDark)
        self.title('')
        if isDark:
            self.iconbitmap('app_icon_dark.ico')
        else:
            self.iconbitmap('app_icon_light.ico')
            
        
        # Layout
        self.rowconfigure(list(range(MAIN_ROWS)), weight= 1, uniform= 'a')
        self.columnconfigure(list(range(MAIN_COLUMNS)), weight= 1, uniform= 'a')
        
        # data
        self.result_string = ctk.StringVar(value= '')
        self.formula_string = ctk.StringVar(value= '0')
        
        
        # widgets
        self.create_widgets()
        
        self.mainloop()

    def create_widgets(self):
        # fonts
        main_font = ctk.CTkFont(family= FONT, size = NOTMAL_FONT_SIZE)
        result_font = ctk.CTkFont(family= FONT, size = OUTPUT_FONT_SIZE)
        # OUTPUT LABELS  
        OutputLabel(self, 0, 'se', main_font, self.result_string)
        OutputLabel(self, 1, 'e', result_font, self.formula_string)
        
        # clear (AC) button
        Buttons(
            parent = self,
            func= self.clear,
            text =OPERATORS['clear']['text'],
            col = OPERATORS['clear']['col'],
            row = OPERATORS['clear']['row'],
            font= main_font
            )
        # percent (%)button
        Buttons(
            parent = self,
            func= self.percent,
            text =OPERATORS['percent']['text'],
            col = OPERATORS['percent']['col'],
            row = OPERATORS['percent']['row'],
            font= main_font
            )
        # invert button 
        invert_image = ctk.CTkImage(
            light_image = Image.open(OPERATORS['invert']['image path']['light']),
            dark_image= Image.open(OPERATORS['invert']['image path']['dark']),
            size= (50,50)
            )
        ImageButton(
            parent = self,
            func= self.invert,
            col = OPERATORS['invert']['col'],
            row = OPERATORS['invert']['row'],
            image = invert_image
        )
        # Number buttons
        for num, data, in NUM_POSITIONS.items():
            NumButton(
            parent = self,
            func = self.num_press,
            text = num,
            col = data['col'],
            row = data['row'],
            span = data['span'],
            font = main_font,
            )
        divide_image = ctk.CTkImage(
            light_image = Image.open(MATH_POSITION['/']['image path']['light']),
            dark_image= Image.open(MATH_POSITION['/']['image path']['dark']),
            size= (50,50)
            )
        # the math buttons
        for operator, data in MATH_POSITION.items():
            if data['image path']:
                MathImageButton(
                parent = self,
                func = self.math_press,
                operator = operator,
                col= data['col'],
                row = data['row'],
                image = divide_image,
                )
            else:
                MathButton(
                    parent = self,
                    operator= operator,
                    func= self.math_press,
                    text =data['character'],
                    col = data['col'],
                    row = data['row'],
                    font= main_font,
                    )
            

    def math_press(self, value):
        self.result_string.set(value=value)
             
    def num_press(self, value):
        print(value)
        
    def invert(self):
        print('invert')
        
    def percent(self):
        print('%')   
          
    def clear(self):
        print('clear')
           
    def change_title_bar_color(self, isDark):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            title_bar_color =TITLE_BAR_HEX_COLORS['dark'] if isDark else TITLE_BAR_HEX_COLORS['light']
            windll.dwmapi.DwmSetWindowAttribute(
                HWND,
                35,
                byref(c_int(title_bar_color)),
                sizeof(c_int)
                )        
        except: 
            pass
class OutputLabel(ctk.CTkLabel):
    def __init__(self, parent, row, anchor, font, textvariable):
        super().__init__(
            parent,
            textvariable = textvariable,
            font= font
            )
        self.grid(row = row, column = 0, columnspan = 4,padx = 10, sticky = anchor)
        
        
if __name__ == '__main__':
    Calculator(darkdetect.isDark())