import customtkinter as ctk
import darkdetect
from buttons import Buttons
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
        self.iconbitmap('cal2.ico')
        
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