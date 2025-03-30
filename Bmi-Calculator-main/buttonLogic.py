from userInput import userInput
from calculations import bmiCalculator
from fileHandler import saveToJson
import json

class buttonLogic:
    def __init__(self, buttons, textboxDisplay, userData):
        self.buttons = buttons         
        self.textboxDisplay = textboxDisplay  
        self.userData = userData
        self.saveToJson = saveToJson

    def buttonEvent(self):
        #Collects user inputs, calculates BMI, and updates userData
        self.userInput = userInput(self.buttons, self.textboxDisplay)
        name, age, height, weight, steps, water, heartRate = self.userInput.getUserInputs()

        self.bmiCalculation = bmiCalculator(weight, height, self.textboxDisplay)
        bmi = self.bmiCalculation.calculateBmi(weight, height)

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

        save_instance = self.saveToJson(self.userData) 
        save_instance.savingToJSON(self.userData) 

            #trying to display the json file here 
    def displayMetrics(self):
        print("") #hre to stop err