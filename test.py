#Initial test of python functionality in PyCharm

#Prompt for battle cry input; 'YOLO' preferred
battleCry = raw_input('Declare your battle cry:')

def rallyTroops(battleCry):
    print(battleCry + "!!!11!?!")
    return 0

if __name__ == "__main__":
    rallyTroops(battleCry)