'''
Copyright 2023 Sebastian Feiert

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''
__author__ = 'Sebastian Feiert'

import tkinter as tk
from tkinter import ttk
from datetime import datetime
from PIL import ImageTk, Image

from gui.window_main.Window_Main_CaseFrame_Manager import CaseFrameManagerMW
from gui.window_main.Window_Main_Status import MainWindowStatus
from gui.Window_Additionals import InfoWindow
from gui.Gui_OptionMenu import GuiOptionMenu
from gui.Window_Additionals import CreateInfo

from style_classes import MyFrame
from style_classes import MyLabelPixel
from style_classes import MyLabel

class MainWindow(tk.Toplevel):
    def __init__(self, main_app, root, gui, *args, **kwargs):
        tk.Toplevel.__init__(self, root)
        self.gui = gui
        self.root = root
        self.root.bind('<FocusIn>', self.on_root_deiconify)
        self.overrideredirect(1)
        self.geometry('1200x600+100+100')

        self.main_app = main_app
        self.data_manager = self.main_app.get_data_manager()

        self.style_dict = self.data_manager.get_style_dict()
        self.language_dict = self.data_manager.get_language_dict()

        self.x_win = None
        self.y_win = None
        self.start_x = None
        self.start_y = None

        self.highlight_main_window = False

        self.option_menu = GuiOptionMenu(self,self.main_app,self.gui)

        # run the main frame of this layer
        self.create_main_frame()

    def create_main_frame(self):

        # Create A Main Frame
        self.main_frame = MyFrame(self, self.data_manager)
        self.main_frame.pack(side = "top", fill = "both",expand = True)
        self.main_frame.configure(highlightbackground=self.style_dict["border_color"], highlightcolor=self.style_dict["border_color"], highlightthickness=1)
        self.main_frame.bind("<Leave>", self.main_window_leave)

        # make a frame for the title bar
        self.title_bar = MyFrame(self.main_frame,self.data_manager)
        self.title_bar.configure(background=self.style_dict["titlebar_color"],highlightcolor=self.style_dict["titlebar_color"],highlightbackground=self.style_dict["titlebar_color"])
        self.title_bar.pack(side='top', fill = "x")
        self.title_bar.bind('<B1-Motion>', self.move_window)
        self.title_bar.bind('<Button-1>', self.get_pos)
        self.title_bar.bind("<Button-3>", self.bar_right_clicked)

        image = Image.open("images/Logo_image.png")
        photo = ImageTk.PhotoImage(image.resize((30, 30), Image.ANTIALIAS))
        self.lbl_icon = MyLabel(self.title_bar, self.data_manager, image=photo)
        self.lbl_icon.configure(background=self.style_dict["titlebar_color"])
        self.lbl_icon.image = photo
        self.lbl_icon.pack(side='left')
        self.lbl_icon.bind('<Button-1>', self.show_about)
        self.lbl_icon.bind("<Button-3>", self.bar_right_clicked)
        icon_text = self.language_dict["about_EasyTARC"]
        self.about_easytarc_ttp = CreateInfo(self.lbl_icon, self.data_manager, 30, 25, icon_text)
        self.lbl_icon.bind("<Enter>", self.icon_enter)
        self.lbl_icon.bind("<Leave>", self.icon_leave)

        dt = datetime.now()
        str_today = dt.strftime("%d") + "." + dt.strftime("%m") + "." + dt.strftime("%Y") + "  "+ self.language_dict["week"] + str(dt.isocalendar()[1])
        self.lbl_title = MyLabelPixel(self.title_bar, self.data_manager, text='   ' + self.main_app.app_name + '                     ' + str_today)
        self.lbl_title.configure(background=self.style_dict["titlebar_color"],height=30)
        self.lbl_title.pack(side='left')
        self.lbl_title.bind('<B1-Motion>', self.move_window)
        self.lbl_title.bind('<Button-1>', self.get_pos)
        self.lbl_title.bind("<Button-3>", self.bar_right_clicked)

        self.close_button = MyLabelPixel(self.title_bar, self.data_manager, text='      X      ')
        self.close_button.configure(background=self.style_dict["titlebar_color"],height=30)
        self.close_button.pack(side='right')
        self.close_button.bind('<Button-1>', self.close_window)
        self.close_button.bind("<Button-3>", self.bar_right_clicked)
        self.close_button.bind("<Enter>", self.enter_close)
        self.close_button.bind("<Leave>", self.leave_close)

        self.minimize_button = MyLabelPixel(self.title_bar, self.data_manager, text='   ___   ')
        self.minimize_button.configure(background=self.style_dict["titlebar_color"],height=30)
        self.minimize_button.pack(side='right',padx = 5)
        self.minimize_button.bind('<Button-1>', self.minimize_window)
        self.minimize_button.bind("<Button-3>", self.bar_right_clicked)
        self.minimize_button.bind("<Enter>", self.enter_minimize)
        self.minimize_button.bind("<Leave>", self.leave_minimize)

        # bind title bar motion to the move window function

        self.root.bind("<Map>", self.on_root_deiconify)
        self.root.bind("<Unmap>", self.on_root_iconify)

        self.bottom_status = MainWindowStatus(self.main_frame, self.main_app,self.gui,self)

        self.case_frame = CaseFrameManagerMW(self.main_frame, self.main_app, self.gui)
        self.case_frame.pack(side = "top", fill = "both", expand = True)

##################################################

    def on_root_iconify(self, event):
        # print('unmap')
        if self.gui.on_window_switch == False:
            self.gui.minimise()
            self.withdraw()
        
    def on_root_deiconify(self, event):
        # print('map')
        if self.gui.on_window_switch == False:
            self.gui.unminimise()
            self.deiconify()

    def main_window_leave(self,e):
        if self.highlight_main_window == True:
            self.highlight_main_window = False
            self.main_frame.configure(highlightbackground=self.style_dict["border_color"], highlightcolor=self.style_dict["border_color"], highlightthickness=1)

##################################################

    def get_pos(self, event):
        self.x_win = self.winfo_x()
        self.y_win = self.winfo_y()
        self.start_x = event.x_root
        self.start_y = event.y_root
        self.y_win = self.y_win - self.start_y
        self.x_win = self.x_win - self.start_x

    def move_window(self, event):
        if type(event.x_root) == int and type(event.y_root) == int:
            self.geometry('+{0}+{1}'.format(event.x_root + self.x_win, event.y_root + self.y_win))
            self.start_x = event.x_root
            self.start_y = event.y_root

    def reset_window_pos(self):
        w = 1200
        h = 600
        self.start_x = 100
        self.start_y = 100
        self.geometry('%dx%d+%d+%d' % (w, h, self.start_x, self.start_y))

    def pos_window_central_and_highlight(self):
        ws = self.winfo_screenwidth() # width of the screen
        hs = self.winfo_screenheight() # height of the screen
        w = self.winfo_width()
        h = self.winfo_height()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        #self.wm_geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.highlight_main_window = True
        self.main_frame.configure(highlightbackground=self.style_dict["selected_color"], highlightcolor=self.style_dict["selected_color"], highlightthickness=1)

##################################################

    def bar_right_clicked(self,e):
        self.option_menu.popup(e)

##################################################

    def icon_enter(self,e):
        self.lbl_icon.configure(background=self.style_dict["highlight_color"])
        self.about_easytarc_ttp.scheduleinfo()

    def icon_leave(self,e):
        self.lbl_icon.configure(background=self.style_dict["titlebar_color"])
        self.about_easytarc_ttp.hideinfo()

##################################################

    def enter_close(self,e):
        self.close_button.configure(background=self.style_dict["notification_color"])

    def leave_close(self,e):
        self.close_button.configure(background=self.style_dict["titlebar_color"])

    def close_window(self,event):
        self.work_clock = self.main_app.data_manager.get_work_clock()
        if self.data_manager.times_saved == True:
            self.root.quit()
        elif str(self.work_clock.str_timedelta(self.work_clock.get_total_time())) == '00:00:00':
            self.root.quit()
        else:
            self.gui.exit_saving_warning()

##################################################

    def enter_minimize(self,e):
        self.minimize_button.configure(background=self.style_dict["highlight_color"])

    def leave_minimize(self,e):
        self.minimize_button.configure(background=self.style_dict["titlebar_color"])

    def minimize_window(self,event=None):
        self.root.iconify()

##################################################

    def show_about(self,event):
        text = self.language_dict['about_EasyTARC_text_1'] 
        text = text + "\n\n" + self.language_dict['about_EasyTARC_text_2']
        text = text + "\n\n" + self.language_dict['about_EasyTARC_text_3']
        text = text + "\n\n" + self.language_dict['about_EasyTARC_text_4']

        info_window = InfoWindow(self.main_app, self.gui, self.main_frame ,text,600,400)

##################################################

    def refresh(self):
        self.style_dict = self.data_manager.get_style_dict()
        self.language_dict = self.data_manager.get_language_dict()

        self.title_bar.refresh_style()
        self.lbl_title.refresh_style()
        self.lbl_icon.refresh_style()
        self.close_button.refresh_style()
        self.minimize_button.refresh_style()
        self.option_menu.refresh()
        self.about_easytarc_ttp.refresh()

        self.main_frame.configure(highlightbackground=self.style_dict["border_color"], highlightcolor=self.style_dict["border_color"], highlightthickness=1)
        self.title_bar.configure(background=self.style_dict["titlebar_color"],highlightcolor=self.style_dict["titlebar_color"],highlightbackground=self.style_dict["titlebar_color"])
        self.lbl_icon.configure(background=self.style_dict["titlebar_color"])
        self.lbl_title.configure(background=self.style_dict["titlebar_color"])
        self.close_button.configure(background=self.style_dict["titlebar_color"])
        self.minimize_button.configure(background=self.style_dict["titlebar_color"])

        self.case_frame.refresh()
        self.bottom_status.refresh()

        dt = datetime.now()
        str_today = dt.strftime("%d") + "." + dt.strftime("%m") + "." + dt.strftime("%Y") + "  "+ self.language_dict["week"] + str(dt.isocalendar()[1])
        self.lbl_title.configure(text='   ' + self.main_app.app_name + '                     ' + str_today)

        icon_text = self.language_dict["about_EasyTARC"]
        self.about_easytarc_ttp.text = icon_text
        return







