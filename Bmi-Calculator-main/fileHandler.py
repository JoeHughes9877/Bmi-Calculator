import json

filename = "jsonFiles"

class saveToJson:
    def __init__(self, userData):
        self.userData = userData

    def savingToJSON(self, userData):
        if 'name' in userData: 
            json_file_name = f"{self.userData['name']}.json"  
            
            with open({name}.json, 'a') as json_file:
                json.dump(userData, json_file, indent=4) 
        else:
            print("poopoo")