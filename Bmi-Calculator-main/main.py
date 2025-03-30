import customtkinter
from buttonLogic import buttonLogic

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("Body Mass Index (BMI) Calculator")
        customtkinter.set_appearance_mode("dark")
        
        self.userData = {}
        self.textboxes = {}

        self.textboxDisplay = customtkinter.CTkTextbox(self, width=250, height=400)
        self.textboxDisplay.grid(row=0, column=2, rowspan=7, padx=10, pady=5, sticky="nsw")

        #initializing attributes before use  
        self.logic = buttonLogic(self.textboxes, self.textboxDisplay, self.userData)

        labelOptions = {"fg_color": "transparent"}
        
        #here i am creating the texes and labels defined in the "textboxes" array, this is creating the button and iterating by 1 for formatting 
        for i, key in enumerate(["Name", "Age", "Height", "Weight", "Steps", "WaterIntake", "HeartRate"]):
            label = customtkinter.CTkLabel(self, text=key, **labelOptions)
            label.grid(row=i, column=0, padx=10, pady=5, sticky="w")

            textbox = customtkinter.CTkTextbox(self, width=200, height=30)
            textbox.grid(row=i, column=1, padx=10, pady=5, sticky="ew")
            self.textboxes[key] = textbox
    
            #displays user infomation 
            self.textboxDisplay.delete("1.0", "end") 
            for key, value in self.userData.items():
                self.textboxDisplay.insert("end", f"{key}: {value}\n")

            #saves data to a txt file
            for key, value in self.userData.items():
                with open("JoesBmiCal.txt", "a") as f:  
                    f.write(f"{key}: {value}\n")

        SaveButton = customtkinter.CTkButton(self, text="Update!", command=self.updateButtonOnCLick, width=200, height=30)
        SaveButton.grid(row=7, column=1, padx=15, sticky="ew")

        displayButton = customtkinter.CTkButton(self, text="Display!", command=self.displayButtonOnCLick , width=200, height=30)
        displayButton.grid(row=8, column=1, padx=15, pady=5, sticky="ew")

    def updateButtonOnCLick(self):
        self.logic.buttonEvent()

    def displayButtonOnCLick(self):
        self.logic.displayMetrics()

app = App()
app.mainloop()