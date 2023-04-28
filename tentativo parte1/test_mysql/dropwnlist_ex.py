        self.options_day = ['1', '2', '3', '4', '5',
                       '6' ,'7' ,'8' ,'9' ,'10' ,
                       '11' ,'12' ,'13' ,'14' ,'15' ,
                       '16' ,'17' ,'18' ,'19' ,'20' ,
                       '21', '22', '23', '24', '25', 
                       '26', '27', '28', '29', '30',
                       '31']
        self.sel_dropdown = StringVar()
        self.sel_dropdown.set(self.options_day[0])
        self.options_day_images = {
            '1' : self.relative_to_assets('image71.png'), 
            '2':self.relative_to_assets('image72.png'), 
            '3':self.relative_to_assets('image73.png'),
            '4':self.relative_to_assets('image74.png'),
            '5':self.relative_to_assets('image75.png'),
            '6' :self.relative_to_assets('image76.png'),
            '7' :self.relative_to_assets('image77.png'),
            '8' :self.relative_to_assets('image78.png'),
            '9' :self.relative_to_assets('image79.png'),
            '10' :self.relative_to_assets('image710.png'),
            '11' :self.relative_to_assets('image711.png'),
            '12' :self.relative_to_assets('image712.png'),
            '13' :self.relative_to_assets('image713.png'),
            '14' :self.relative_to_assets('image714.png'),
            '15' :self.relative_to_assets('image715.png'),
            '16' :self.relative_to_assets('image716.png'),
            '17' :self.relative_to_assets('image717.png'),
            '18' :self.relative_to_assets('image718.png'),
            '19' :self.relative_to_assets('image719.png'),
            '20' :self.relative_to_assets('image720.png'),
            '21':self.relative_to_assets('image721.png'), 
            '22':self.relative_to_assets('image722.png'), 
            '23':self.relative_to_assets('image723.png'), 
            '24':self.relative_to_assets('image724.png'), 
            '25':self.relative_to_assets('image725.png'), 
            '26':self.relative_to_assets('image726.png'), 
            '27':self.relative_to_assets('image727.png'), 
            '28':self.relative_to_assets('image728.png'), 
            '29':self.relative_to_assets('image729.png'), 
            '30':self.relative_to_assets('image730.png'),
            '31':self.relative_to_assets('image731.png')
        }
        self.dropdown = OptionMenu(self, self.sel_dropdown, *self.options_day, command = self.custom_option_menu)
        self.dropdown.pack(ipadx=500, ipady=100)
        self.sel_dropdown.trace('w', self.custom_option_menu)


    def custom_option_menu(self, *args):
        selected_value = self.sel_dropdown.get()
        
        # Remove the existing label, if any
        for widget in self.winfo_children():
            if isinstance(widget, Label):
                widget.destroy()
        
        # Create a label with the image corresponding to the selected option
        image_path = self.options_day_images.get(selected_value)
        if image_path:
            image = PhotoImage(file=image_path)
            label = Label(self, image=image)
            label.image = image  # Store a reference to the image to prevent it from being garbage collected
            label.pack()
\