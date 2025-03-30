from userInput import userInput
from calculations import bmiCalculator
import json
from pathlib import Path
from json.decoder import JSONDecodeError 

class buttonLogic:
    def __init__(self, buttons, textboxDisplay, userData):
        self.buttons = buttons         
        self.textboxDisplay = textboxDisplay  
        self.userData = userData

    def buttonEvent(self):
        #Collects user inputs, calculates BMI, and updates userData
        self.userInput = userInput(self.buttons, self.textboxDisplay)
        name, age, height, weight, steps, water, heartRate = self.userInput.getUserInputs()

        self.bmiCalculation = bmiCalculator(weight, height, self.textboxDisplay)
        bmi = round(self.bmiCalculation.calculateBmi(weight, height), 2)


        self.userData.update({
            "Name": name,
            "Age": age,
            "Height": height,
            "Weight": weight,
            "Steps": steps,
            "Water intake": water,
            "Heart rate": heartRate,
            "Bmi": bmi,
        })
        name = name.lower().title()

        self.filePath = Path("jsonFiles") / f"{self.userData["Name"]}.json" #after "name" is defined i am declaring the file path, this will be used later

        self.fileHandling()


    def displayMetrics(self):
        #opens the users file so that it can be printed
        with open(self.filePath, "r") as file:  
            data = json.load(file)
        
        #formatting the users print so it looks pretty
        formattedUserData = json.dumps(data, indent=4, separators=(',', ': '))
        formattedUserData = formattedUserData.replace("}", "").replace("{", "").replace("[", " ").replace("]", "").replace(",", "")

        self.textboxDisplay.insert("1.0", formattedUserData)

    def fileHandling(self):
        data = [] #initialize data

        try:
            with open(self.filePath, "r") as file: #opening the file for reading  
                data = json.load(file) #loading existing data in the file
                data.append(self.userData) #appending new data to existing data 
        
        except (FileNotFoundError, JSONDecodeError): 
                data = [self.userData] # If the file doesn't exist/Error, initialize data with just the userData (as the file contains no data nothing needs appending)
    
        with open(self.filePath, "w") as file: #opening file for writing data 
            json.dump(data, file, indent=4) #writing the saved data to the jsonfile 
            file.write("\n") #formatting (makes file look pretty)