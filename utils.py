import json

def getGameMap():
    print("Select a game map:")
    with open('data/availableMaps.json', 'r') as maps_file:
        available_maps = json.load(maps_file)
    for index, map_name in enumerate(available_maps["maps"], start=1):
        print(f"{index}. {map_name["name"]}")
    choice = input("Game map number: ")
    while(not choice.isdigit() or not (1 <= int(choice) <= len(available_maps["maps"]))):
        print("Invalid game map number. Please try again.")
        choice = input("Game map number: ")
    selectedMap = available_maps["maps"][int(choice)-1]
    return loadGameMap(selectedMap)

def loadGameMap(map):
    with open('data/'+map["jsonName"]+'Rules.json', 'r') as rules_file:
        rules = json.load(rules_file)
    with open('data/'+map["jsonName"]+'Map.json', 'r') as map_file:
        game_map = json.load(map_file)
    return {"rules": rules, "map": game_map}

def getGameMode():
    print("Select a game mode:")
    print("1. Play as AI")
    choice = input("Game mode number: ")
    while(not choice.isdigit() or not (1 <= int(choice) <= 1)):
        print("Invalid game map number. Please try again.")
        choice = input("Game map number: ")
    if choice == "1":
        return "AI"
    
def getTotalPlayers(playerRange):
    choice = input("Select the number of players ("+playerRange+"):")
    while(not choice.isdigit() or not (int(playerRange.split("-")[0]) <= int(choice) <= int(playerRange.split("-")[1]))):
        print("Invalid number of players. Please try again.")
        choice = input("Number of players: ")
    return int(choice)

def getAIPlayers(numPlayers):
    choice = input("Select the number of AI players (0-"+str(numPlayers)+"):")
    while(not choice.isdigit() or not (0 <= int(choice) <= numPlayers)):
        print("Invalid number of AI players. Please try again.")
        choice = input("Number of AI players: ")
    return int(choice)