import customtkinter as ctk
import darkdetect
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
        
        self.mainloop()

        
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
    def __init__(self, parent, row):
        super().__init__(
            parent,
            text= '4+9',
            fg_color= 'blue'
            )
        self.grid(row = row, column = 0, columnspan = 4)
        
        
if __name__ == '__main__':
    Calculator(darkdetect.isDark())