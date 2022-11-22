import json
states_and_capitals = { "Karnataka":"Bengaluru","Maharashtra": "Mumbai",
"Goa" : "Panji","Punjab":"Chandigarh","Jharkhand":"Ranchi","Bihar": "Patna", "Rajasthan": "Jaipur"}

with open("states.json","w") as file: # creating json file
    json.dump(states_and_capitals,file)

with open("states.json","r") as new_file: #reading json file and storing it
    new = json.load(new_file)

for k,v in new.items(): #printing the States and their Capital individually
    print(k,v)