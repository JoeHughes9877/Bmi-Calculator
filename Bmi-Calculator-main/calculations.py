class bmiCalculator():
    def __init__(self, weight, height, textboxDisplay):
        self.textboxDisplay = textboxDisplay
        self.weight = weight 
        self.height = height

    def calculateBmi(self, weight, height):
        try:
            return weight / (height ** 2)
        except ValueError:
            return None