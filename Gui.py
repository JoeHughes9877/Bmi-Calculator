import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("590x500")
        self.title("Body Mass Index (BMI) Calculator")

        self.userData = {}

        self.textboxError = customtkinter.CTkTextbox(self, width=250, height=30)
        self.textboxError.grid(row=0, column=1, columnspan=2, padx=10, pady=5, sticky="ew")

        self.textboxDisplay = customtkinter.CTkTextbox(self, width=250, height=400)
        self.textboxDisplay.grid(row=1, column=2, rowspan=7, padx=10, pady=5, sticky="nsw")

        label_options = {"fg_color": "transparent"}

        labelName = customtkinter.CTkLabel(self, text="Name", **label_options)
        labelName.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.textboxName = customtkinter.CTkTextbox(self, width=200, height=30)
        self.textboxName.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        labelAge = customtkinter.CTkLabel(self, text="Age", **label_options)
        labelAge.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.textboxAge = customtkinter.CTkTextbox(self, width=200, height=30)
        self.textboxAge.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        labelHeight = customtkinter.CTkLabel(self, text="Height", **label_options)
        labelHeight.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.textboxHeight = customtkinter.CTkTextbox(self, width=200, height=30)
        self.textboxHeight.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

        labelWeight = customtkinter.CTkLabel(self, text="Weight", **label_options)
        labelWeight.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.textboxWeight = customtkinter.CTkTextbox(self, width=200, height=30)
        self.textboxWeight.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

        labelSteps = customtkinter.CTkLabel(self, text="Steps", **label_options)
        labelSteps.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.textboxSteps = customtkinter.CTkTextbox(self, width=200, height=30)
        self.textboxSteps.grid(row=5, column=1, padx=10, pady=5, sticky="ew")

        labelWaterIntake = customtkinter.CTkLabel(self, text="Water intake", **label_options)
        labelWaterIntake.grid(row=6, column=0, padx=10, pady=5, sticky="w")
        self.textboxWaterIntake = customtkinter.CTkTextbox(self, width=200, height=30)
        self.textboxWaterIntake.grid(row=6, column=1, padx=10, pady=5, sticky="ew")

        labelHeartRate = customtkinter.CTkLabel(self, text="Heart rate", **label_options)
        labelHeartRate.grid(row=7, column=0, padx=10, pady=5, sticky="w")
        self.textboxHeartRate = customtkinter.CTkTextbox(self, width=200, height=30)
        self.textboxHeartRate.grid(row=7, column=1, padx=10, pady=5, sticky="ew")

        def userInputs():
            try:
                name = self.textboxName.get("1.0", "end-1c")
                age = self.textboxAge.get("1.0", "end-1c")
                hight = self.textboxHeight.get("1.0", "end-1c")
                weight = self.textboxWeight.get("1.0", "end-1c")
                steps = self.textboxSteps.get("1.0", "end-1c")
                water = self.textboxWaterIntake.get("1.0", "end-1c")
                heartRate = self.textboxHeartRate.get("1.0", "end-1c")

                return name.title(), int(age), float(hight), float(weight), int(steps), int(water), int(heartRate)
            except ValueError:
                self.textboxError.delete("1.0", "end") 
                errorMessage = "Your input was incorrect, please try again :)"
                self.textboxError.insert("end", f"{errorMessage}")

        def button_event():
            name, age, hight, weight, steps, water, heartRate = userInputs()

            self.userData.update({
                "Name": name,
                "Age": age,
                "Height": hight,
                "Weight": weight,
                "Steps": steps,
                "Water intake": water,
                "Heart rate": heartRate,
            })

            self.textboxDisplay.delete("1.0", "end") 
            for key, value in self.userData.items():
                self.textboxDisplay.insert("end", f"{key}: {value}\n")

            #saves data to a txt file
            for key, value in self.userData.items():
                with open("JoesBmiCal.txt", "a") as f:  
                    f.write(f"{key}: {value}\n")

        buttonUpdate = customtkinter.CTkButton(self, text="Update!", command=button_event, width=200)
        buttonUpdate.grid(row=8, column=1, padx=10, pady=10, sticky="ew")

app = App()
app.mainloop()