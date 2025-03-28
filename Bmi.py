usrDta = {}

def userInputs():
    while True: 
        try:
            nme = input("Name: ").title()
            age = int(input("Age: "))
            hgt = float(input("Height (M): "))
            wgt = float(input("Weight (Kg): "))
            sps = int(input("Steps: "))
            wtr = int(input("Water Intake (L): "))
            htRt = int(input("Heart rate: "))

            usrDta.update({
                "name": nme,
                "age": age,
                "height": hgt,
                "weight": wgt,
                "steps": sps,
                "water intake": wtr,
                "heart rate": htRt,
            })
            return(hgt, wgt)
        except ValueError:
            print("Invalid input") 

def bmiCalculation(): 
    hgt, wgt = userInputs()
    bmi = wgt / (hgt ** 2)
    
    for key, value in usrDta.items():
        f = open("JoesBmiCal.txt", "a")
        f.write(f'{key}: {value} ')
        f.close()

def main():
    bmiCalculation()

main()