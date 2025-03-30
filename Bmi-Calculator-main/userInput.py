class userInput():
    def __init__(self, buttons, textboxDisplay):
        self.buttons = buttons
        self.textboxDisplay = textboxDisplay

    def getUserInputs(self):
            try:
                name = self.buttons["Name"].get("1.0", "end-1c")
                age = int(self.buttons["Age"].get("1.0", "end-1c"))
                height = float(self.buttons["Height"].get("1.0", "end-1c"))
                weight = float(self.buttons["Weight"].get("1.0", "end-1c"))
                steps = int(self.buttons["Steps"].get("1.0", "end-1c"))
                water = int(self.buttons["WaterIntake"].get("1.0", "end-1c"))
                heartRate = int(self.buttons["HeartRate"].get("1.0", "end-1c"))

                return name.title(), int(age), float(height), float(weight), int(steps), int(water), int(heartRate)
            except ValueError:
                self.textboxDisplay.delete("1.0", "end") 
                errorMessage = ("Your input was incorrect, please try again :")
                self.textboxDisplay.insert("end", f"{errorMessage}")