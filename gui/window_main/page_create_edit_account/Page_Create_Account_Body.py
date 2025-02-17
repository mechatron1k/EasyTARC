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

from gui.Scroll_Frame import Scroll_Frame

from style_classes import MyFrame
from style_classes import MyLabel
from style_classes import MyButton
from style_classes import MyEntry 
from style_classes import MyCheckbutton

class CreateEditAccountBody:
    def __init__(self, container, main_app, gui, create_account_page, modus, main_account_dict = None, sub_account_dict = None):

        # get main_app, datamanager, style_dict and language_dict
        self.main_app = main_app
        self.data_manager = self.main_app.get_data_manager()
        self.style_dict = self.data_manager.get_style_dict()
        self.language_dict = self.data_manager.get_language_dict()

        # get gui for additional windows
        # capture tab for updating tab
        self.gui = gui
        self.create_account_page = create_account_page
        self.modus = modus
        self.main_account_dict = main_account_dict
        self.sub_account_dict = sub_account_dict

        self.scroll = Scroll_Frame(self.main_app,self.gui)

        # run the main frame of this layer
        self.create_main_frame(container)

#################################################################

    def create_main_frame(self,container):

        bodyframe = MyFrame(container,self.data_manager)
        bodyframe.pack(side = "top", fill = "both", expand = True)

        self.main_frame = self.scroll.create_scroll_frame(bodyframe)

        if self.modus == 'new_sub' or self.modus == 'edit_sub':
            self.frame_main_name = MyFrame(self.main_frame,self.data_manager)
            self.frame_main_name.pack(side = "top", padx=10, pady=5,fill='x')

            self.lbl_main_name = MyLabel(self.frame_main_name,self.data_manager,width=15,text=self.language_dict['main_account'])
            self.lbl_main_name.pack(side = "left", padx=10)

            self.lbl_main_text = MyLabel(self.frame_main_name,self.data_manager,text=self.main_account_dict.get("name"),width=36)
            self.lbl_main_text.pack(side = "left", padx=10)

            self.separator_frame_0 = MyFrame(self.main_frame,self.data_manager)
            self.separator_frame_0.configure(highlightthickness=1,highlightcolor=self.style_dict["highlight_color"],highlightbackground=self.style_dict["highlight_color"])
            self.separator_frame_0.pack(side = "top",fill='x', pady=10)

        ###################################

        self.frame_name = MyFrame(self.main_frame,self.data_manager)
        self.frame_name.pack(side = "top", padx=10, pady=5,fill='x')

        self.lbl_name = MyLabel(self.frame_name,self.data_manager,width=15,text=self.language_dict['name'] + ':')
        self.lbl_name.pack(side = "left", padx=10)

        self.account_name = tk.StringVar()
        self.textBox_name = MyEntry(self.frame_name,self.data_manager, textvariable=self.account_name, width=36)
        self.textBox_name.pack(side = "left", padx=10)

        self.lbl_name_info = MyLabel(self.frame_name,self.data_manager)
        self.lbl_name_info.pack(side = "left", padx=10)

        if self.modus in ['new_order','new_process','edit_main']:
            self.account_name.set(self.main_account_dict.get("name"))
        elif self.modus in ['edit_sub']:
            self.account_name.set(self.sub_account_dict.get("name"))

        name_text_A = self.language_dict['create_account_name_text_A']
        name_text_B = self.language_dict['create_account_name_text_B']

        if self.modus in ['new_main','new_order','new_process','edit_main']:
            self.lbl_name_info.configure(text=name_text_A,anchor='w',justify='left')
        elif self.modus in ['new_sub','edit_sub']:
            self.lbl_name_info.configure(text=name_text_B,anchor='w',justify='left')

        self.textBox_name.configure(highlightthickness = 1, highlightcolor=self.style_dict["notification_color"],highlightbackground=self.style_dict["notification_color"])
        if self.style_dict['name'] == 'dark':
            self.textBox_name.configure(borderwidth = 0)

        ###################################

        self.frame_description = MyFrame(self.main_frame,self.data_manager)
        self.frame_description.pack(side = "top", padx=10, pady=5,fill='x')

        self.lbl_description = MyLabel(self.frame_description,self.data_manager,width=15,text= self.language_dict['description'] + ':')
        self.lbl_description.pack(side = "left", padx=10)

        self.account_description_text = tk.StringVar()
        self.textBox_description = MyEntry(self.frame_description,self.data_manager, textvariable=self.account_description_text, width=36)
        self.textBox_description.pack(side = "left", padx=10)

        self.lbl_description_info = MyLabel(self.frame_description,self.data_manager,text=self.language_dict['create_account_description_text'],anchor='w',justify='left')
        self.lbl_description_info.pack(side = "left", padx=10)

        if self.modus in ['new_order','new_process','edit_main']:
            self.account_description_text.set(self.main_account_dict.get("description_text"))
        elif self.modus in ['edit_sub']:
            self.account_description_text.set(self.sub_account_dict.get("description_text"))

        self.textBox_description.configure(highlightthickness = 1)
        if self.style_dict['name'] == 'dark':
            self.textBox_description.configure(borderwidth = 0)

        self.separator_frame_2 = MyFrame(self.main_frame,self.data_manager)
        self.separator_frame_2.configure(highlightthickness=1,highlightcolor=self.style_dict["highlight_color"],highlightbackground=self.style_dict["highlight_color"])
        self.separator_frame_2.pack(side = "top",fill='x', pady=10)

        ###################################

        self.frame_group = MyFrame(self.main_frame,self.data_manager)
        self.frame_group.pack(side = "top", padx=10, pady=5,fill='x')

        self.lbl_group = MyLabel(self.frame_group,self.data_manager,width=15,text= self.language_dict['group'] + ':')
        self.lbl_group.pack(side = "left", padx=10)

        self.account_group = tk.StringVar()
        self.group_cbox = ttk.Combobox(self.frame_group, width = 28, textvariable = self.account_group)
        self.group_cbox['values'] = self.data_manager.get_all_account_groups()
        self.group_cbox.pack(side="left", padx=10)

        self.lbl_highlight = MyLabel(self.frame_group,self.data_manager,text='  '+u'\U0001F808'+' ')
        self.lbl_highlight.pack(side = "left")

        self.lbl_group_info = MyLabel(self.frame_group,self.data_manager,text=self.language_dict['create_account_group_text'],anchor='w',justify='left')
        self.lbl_group_info.pack(side = "left", padx=10)

        if self.modus in ['new_order','new_process','edit_main','new_sub','edit_sub'] and str(self.main_account_dict.get("group")) != 'default':
            self.account_group.set(str(self.main_account_dict.get("group")))

        if self.modus in ['new_order','new_process','new_sub','edit_sub']:
            self.group_cbox.configure(state=tk.DISABLED)
        else:
            self.group_cbox.configure(state=tk.NORMAL)
            self.lbl_highlight.configure(foreground=self.style_dict["selected_color"])


        self.separator_frame_4 = MyFrame(self.main_frame,self.data_manager)
        self.separator_frame_4.configure(highlightthickness=1,highlightcolor=self.style_dict["highlight_color"],highlightbackground=self.style_dict["highlight_color"])
        self.separator_frame_4.pack(side = "top",fill='x', pady=10)

        ###################################

        self.frame_project = MyFrame(self.main_frame,self.data_manager)
        self.frame_project.pack(side = "top", padx=10, pady=5,fill='x')

        self.lbl_project = MyLabel(self.frame_project,self.data_manager,width=15,text=self.language_dict['project_nbr'] + ':')
        self.lbl_project.pack(side = "left", padx=10)

        self.account_project = tk.StringVar()
        self.textBox_project = MyEntry(self.frame_project, self.data_manager, textvariable=self.account_project, width=36)
        self.textBox_project.pack(side="left", padx=10)

        self.lbl_project_info = MyLabel(self.frame_project,self.data_manager,text=self.language_dict['create_account_project_nbr_text'],anchor='w',justify='left')
        self.lbl_project_info.pack(side = "left", padx=10)

        if self.modus in ['new_order','new_process','edit_main','new_sub','edit_sub']:
            self.account_project.set(str(self.main_account_dict.get("project_nbr")))

        if self.modus in ['new_order','new_process','new_sub','edit_sub']:
            self.textBox_project.configure(state=tk.DISABLED)
        else:
            self.textBox_project.configure(state=tk.NORMAL, highlightthickness = 1)
            if self.style_dict['name'] == 'dark':
                self.textBox_project.configure(borderwidth = 0)


        ###################################

        self.frame_order = MyFrame(self.main_frame,self.data_manager)
        self.frame_order.pack(side = "top", padx=10, pady=5,fill='x')

        self.lbl_order = MyLabel(self.frame_order,self.data_manager,width=15,text=self.language_dict['order_nbr'] + ':')
        self.lbl_order.pack(side = "left", padx=10)

        self.account_order = tk.StringVar()
        self.textBox_order = MyEntry(self.frame_order, self.data_manager, textvariable=self.account_order, width=36)
        self.textBox_order.pack(side="left", padx=10)

        self.lbl_order_info = MyLabel(self.frame_order,self.data_manager,text=self.language_dict['create_account_order_nbr_text'],anchor='w',justify='left')
        self.lbl_order_info.pack(side = "left", padx=10)

        if self.modus in ['new_process','edit_main','new_sub','edit_sub']:
            self.account_order.set(str(self.main_account_dict.get("order_nbr")))

        if self.modus in ['new_process','new_sub','edit_sub']:
            self.textBox_order.configure(state=tk.DISABLED)
        else:
            self.textBox_order.configure(highlightthickness = 1, state=tk.NORMAL)
            if self.style_dict['name'] == 'dark':
                self.textBox_order.configure(borderwidth = 0)

        ###################################

        self.frame_process = MyFrame(self.main_frame,self.data_manager)
        self.frame_process.pack(side = "top", padx=10, pady=5,fill='x')

        self.lbl_process = MyLabel(self.frame_process,self.data_manager,width=15,text=self.language_dict['process_nbr'] + ':')
        self.lbl_process.pack(side = "left", padx=10)

        self.account_process = tk.StringVar()
        self.textBox_process = MyEntry(self.frame_process, self.data_manager, textvariable=self.account_process, width=36)
        self.textBox_process.pack(side="left", padx=10)

        self.lbl_process_info = MyLabel(self.frame_process,self.data_manager,text=self.language_dict['create_account_process_nbr_text'],anchor='w',justify='left')
        self.lbl_process_info.pack(side = "left", padx=10)

        if self.modus in ['edit_main','new_sub','edit_sub']:
            self.account_process.set(str(self.main_account_dict.get("process_nbr")))

        if self.modus in ['new_sub','edit_sub']:
            self.textBox_process.configure(state=tk.DISABLED)
        else:
            self.textBox_process.configure(highlightthickness = 1, state=tk.NORMAL)
            if self.style_dict['name'] == 'dark':
                self.textBox_process.configure(borderwidth = 0)

        self.separator_frame_1 = MyFrame(self.main_frame,self.data_manager)
        self.separator_frame_1.configure(highlightthickness=1,highlightcolor=self.style_dict["highlight_color"],highlightbackground=self.style_dict["highlight_color"])
        self.separator_frame_1.pack(side = "top",fill='x', pady=10)

        ###################################

        self.frame_bookable = MyFrame(self.main_frame,self.data_manager)
        self.frame_bookable.pack(side = "top", padx=10, pady=5,fill='x')

        self.lbl_bookable = MyLabel(self.frame_bookable,self.data_manager,width=15,text=self.language_dict['bookable'] + ':')
        self.lbl_bookable.pack(side = "left", padx=10)

        self.account_bookable = tk.StringVar()
        self.checkBox_bookable = MyCheckbutton(self.frame_bookable, self.data_manager,
                                                variable=self.account_bookable)
        self.checkBox_bookable.pack(side="left", padx=10)

        self.lbl_empty0 = MyLabel(self.frame_bookable,self.data_manager,text='', width=25)
        self.lbl_empty0.pack(side = "left", padx=10)

        self.lbl_checkBox_bookable_info = MyLabel(self.frame_bookable,self.data_manager,text=self.language_dict['create_account_bookable_text'],anchor='w',justify='left')
        self.lbl_checkBox_bookable_info.pack(side = "left", padx=10)

        if self.modus in ['new_order','new_process','edit_main','new_sub','edit_sub']:
            if self.main_account_dict.get("bookable") == 0:
                self.checkBox_bookable.deselect()
            else:
                self.checkBox_bookable.select()

        elif self.modus in ['new_main']:
            self.checkBox_bookable.deselect()

        if self.modus in ['new_sub','edit_sub']:
            self.checkBox_bookable.configure(state=tk.DISABLED)
        else:
            self.checkBox_bookable.configure(state=tk.NORMAL, selectcolor=self.style_dict["selected_color"],foreground=self.style_dict["font_color_3"] )

        ###################################


        self.frame_autobooking = MyFrame(self.main_frame,self.data_manager)
        self.frame_autobooking.pack(side = "top", padx=10, pady=5,fill='x')

        self.lbl_autobooking = MyLabel(self.frame_autobooking,self.data_manager,width=15,text=self.language_dict['auto_booking'] + ':')
        self.lbl_autobooking.pack(side = "left", padx=10)

        self.account_autobooking = tk.StringVar()
        self.checkBox_autobooking = MyCheckbutton(self.frame_autobooking, self.data_manager,
                                                variable=self.account_autobooking)
        self.checkBox_autobooking.pack(side="left", padx=10)

        self.lbl_empty1 = MyLabel(self.frame_autobooking,self.data_manager,text='', width=25)
        self.lbl_empty1.pack(side = "left", padx=10)

        self.lbl_checkBox_auto_booking_info = MyLabel(self.frame_autobooking,self.data_manager,text=self.language_dict['create_account_auto_booking_text'],anchor='w',justify='left')
        self.lbl_checkBox_auto_booking_info.pack(side = "left", padx=10)

        if self.modus in ['new_order','new_process','edit_main','new_sub','edit_sub']:
            if self.main_account_dict.get("auto_booking") == 0:
                self.checkBox_autobooking.deselect()
            else:
                self.checkBox_autobooking.select()

        elif self.modus in ['new_main']:
            self.checkBox_autobooking.deselect()

        if self.modus in ['new_sub','edit_sub']:
            self.checkBox_autobooking.configure(state=tk.DISABLED)
        else:
            self.checkBox_autobooking.configure(state=tk.NORMAL, selectcolor=self.style_dict["selected_color"],foreground=self.style_dict["font_color_3"] )

        ###################################

        self.frame_response = MyFrame(self.main_frame,self.data_manager)
        self.frame_response.pack(side = "top", padx=10, pady=5,fill='x')

        self.lbl_response = MyLabel(self.frame_response,self.data_manager,width=15,text=self.language_dict['booking_nbr'] + ':')
        self.lbl_response.pack(side = "left", padx=10)

        self.account_response = tk.StringVar()
        self.textBox_response = MyEntry(self.frame_response, self.data_manager, textvariable=self.account_response, width=36)
        self.textBox_response.pack(side="left", padx=10)

        if self.modus in ['edit_main','new_sub','edit_sub']:
            self.account_response.set(str(self.main_account_dict.get("response_nbr")))

        if self.modus in ['new_sub','edit_sub']:
            self.textBox_response.configure(state=tk.DISABLED)
        else:
            self.textBox_response.configure(state=tk.NORMAL,highlightthickness = 1)
            if self.style_dict['name'] == 'dark':
                self.textBox_response.configure(borderwidth = 0)

        ###################################

        self.frame_response_text = MyFrame(self.main_frame,self.data_manager)
        self.frame_response_text.pack(side = "top", padx=10, pady=5,fill='x')

        lbl_response_text = MyLabel(self.frame_response_text,self.data_manager,width=15,text=self.language_dict['booking_text'] + ':')
        lbl_response_text.pack(side = "left", padx=10)

        self.account_response_text = tk.StringVar()
        self.textBox_text = MyEntry(self.frame_response_text,self.data_manager, textvariable=self.account_response_text, width=36)
        self.textBox_text.pack(side = "left", padx=10)

        if self.modus in ['new_order','new_process','edit_main','new_sub','edit_sub']:
            self.account_response_text.set(self.main_account_dict.get("default_text"))

        self.textBox_text.configure(highlightthickness = 1)
        if self.style_dict['name'] == 'dark':
            self.textBox_text.configure(borderwidth = 0)

        self.separator_frame_3 = MyFrame(self.main_frame,self.data_manager)
        self.separator_frame_3.configure(highlightthickness=1,highlightcolor=self.style_dict["highlight_color"],highlightbackground=self.style_dict["highlight_color"])
        self.separator_frame_3.pack(side = "top",fill='x', pady=10)

        ###################################

        self.frame_obligation = MyFrame(self.main_frame,self.data_manager)
        self.frame_obligation.pack(side = "top", padx=10, pady=5,fill='x')

        self.lbl_fill = MyLabel(self.frame_obligation,self.data_manager,width=15,text=self.language_dict['fillable'])
        self.lbl_fill.configure(foreground=self.style_dict["selected_color"])
        self.lbl_fill.pack(side = "left", padx=10)

        self.lbl_obligation = MyLabel(self.frame_obligation,self.data_manager,width=15,text=self.language_dict['mandatory_field'])
        self.lbl_obligation.configure(foreground=self.style_dict["notification_color"])
        self.lbl_obligation.pack(side = "left", padx=10)

        self.lbl_error_info = MyLabel(self.main_frame,self.data_manager, width=100)
        self.lbl_error_info.pack(side = "top", padx=10, pady=5)

        if self.modus in ['edit_main','edit_sub']:
            btn_text = self.language_dict['complete_editing']
        else:
            btn_text = self.language_dict['add']

        self.btn_quit = MyButton(self.main_frame,self.data_manager, text=btn_text, command=self.finish, width=30)
        self.btn_quit.pack(side = "top", padx=10, pady=5)
        return
    
    def finish(self):
        response = self.create_account_page.user_input(self.account_name,
                                                       self.account_description_text,
                                                       self.account_project,
                                                       self.account_order,
                                                       self.account_process,
                                                       self.account_response,
                                                       self.account_response_text,
                                                       self.account_autobooking,
                                                       self.account_group,
                                                       self.account_bookable)
        if response != None:
            self.lbl_error_info.configure(text = str(response))

    def update(self):
        return
    
    def refresh(self):
        # configure style and language of main frame
        self.style_dict = self.data_manager.get_style_dict()
        self.language_dict = self.data_manager.get_language_dict()

        self.main_frame.refresh_style()
        return


