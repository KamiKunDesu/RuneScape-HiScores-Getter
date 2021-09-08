import http.client

"""
_getHTTPResponse is a function which handles making a request to the JaGex runescape hiscores api.

It also handles the csv format that it returns the data in, reads
it and processes so that it's in a useable format
It then returns the usable format (list) for use processing to make some
dictionaries of relevant data
It takes the username and account type as an argument and raises an error
if the username is wrong.
"""
def _getHTTPResponse(username: str, accountType='N'):
    #This raises an http connection to the Runescape api
    conn = http.client.HTTPSConnection('secure.runescape.com')
    '''
    Each of these if statements handles a different account type and
    N = "normal", "IM" = Iron Man, "UIM" = "Ultimate Iron Man",
    "HIM" = Hardcore Iron Man
    '''
    if accountType == 'N':
        #handles the specific api request
        conn.request("GET", "/m=hiscore_oldschool/index_lite.ws?player={}".format(username.replace(' ', '%20')))
    elif accountType == 'IM':
        conn.request("GET", "/m=hiscore_oldschool_ironman/index_lite.ws?player={}".format(username.replace(' ', '%20')))
    elif accountType == "UIM":
        conn.request("GET", "/m=hiscore_oldschool_ultimate/index_lite.ws?player={}".format(username.replace(' ', '%20')))
    elif accountType == "HIM":
        conn.request("GET", "/m=hiscore_oldschool_hardcore_ironman/index_lite.ws?player={}".format(username.replace(' ', '%20')))
    #gets response and stores it in variable
    response = conn.getresponse()
    #stores the status i.e. 404, 403 errors etc
    status = response.status
    #Raises exception if error status, most likely due to wrong user name or account type
    if status != 200:
        raise Exception("Player name given not found in account type provided. Valid account types are, 'N' (Normal), 'IM' (Iron Man), 'UIM' (Ultimate Iron Man), 'HIM' (Hardcore Iron Man)")
    #Decodes and reads the response object into ascii and saves it to a variable
    response = response.read().decode('ascii')
    #Next two lines get rid of new lines in the returned response and split them by comma delimiter into a list (since the response is csv)
    response = response.replace('\n', ',')
    response = response.split(',')
    #return list of each field in the request for further processing
    return response
            
         


'''
This is the function that processes the request from the osrs api and makes
two separate dictionaries, one for skills and one for bosses (by pulling through from the
appropriate indexes) and then it returns a dictionary with those two dictionaries as
sub dictionaries
it takes username and account type as parameters (since it needs to pass these params
through to the request function)
'''
def returnskillsandmonstersdict(user: str, accountType: str = 'N'):
    #get the user data by calling the _getHTTPResponse function
    user_data = _getHTTPResponse(user, accountType)
    #initiate the skills dictionary by pulling the correct indexes from the data
    skills = {
        "Overall": user_data[1],
        "Attack": user_data[4],
        "Defence": user_data[7],
        "Strength": user_data[10],
        "Hitpoints": user_data[13],
        "Ranged": user_data[16],
        "Prayer": user_data[19],
        "Magic": user_data[22],
        "Cooking": user_data[25],
        "Woodcutting": user_data[28],
        "Fletching": user_data[31],
        "Fishing": user_data[34],
        "Firemaking": user_data[37],
        "Crafting": user_data[40],
        "Smithing": user_data[43],
        "Mining": user_data[46],
        "Herblore": user_data[49],
        "Agility": user_data[52],
        "Thieving": user_data[55],
        "Slayer": user_data[58],
        "Farming": user_data[61],
        "Runecraft": user_data[64],
        "Hunter": user_data[67],
        "Construction": user_data[70]
    }
    #initiate bosses dictionary by pulling through the right indexes from the data
    bosses = {
        "Bounty Hunter - Hunter": user_data[75],
        "Bounty Hunter - Rogue": user_data[77],
        "Clue Scrolls (all)": user_data[79],
        "Clue Scrolls (beginner)": user_data[81],
        "Clue Scrolls (easy)": user_data[83],
        "Clue Scrolls (medium)": user_data[85],
        "Clue Scrolls (hard)": user_data[87],
        "Clue Scrolls (elite)": user_data[89],
        "Clue Scrolls (master)": user_data[91],
        "LMS - Rank": user_data[93],
        "Soul Wars Zeal": user_data[95],
        "Abyssal Sire": user_data[97],
        "Alchemical Hydra": user_data[99],
        "Barrow Chests": user_data[101],
        "Bryophyta": user_data[103],
        "Callisto": user_data[105],
        "Cerberus": user_data[107],
        "Chambers of Xeric": user_data[109],
        "Chambers of Xeric: Challenge Mode": user_data[111],
        "Chaos Elemental": user_data[113],
        "Chaos Fanatic": user_data[115],
        "Commander Zilyana": user_data[117],
        "Corporeal Beast": user_data[119],
        "Crazy Archaeologist": user_data[121],
        "Dagannoth Prime": user_data[123],
        "Dagannoth Rex": user_data[125],
        "Dagannoth Supreme": user_data[127],
        "Deranged Archaeologist": user_data[129],
        "General Graador": user_data[131],
        "Giant Mole": user_data[133],
        "Grotesque Guardians": user_data[135],
        "Hespori": user_data[137],
        "Kalphite Queen": user_data[139],
        "King Black Dragon": user_data[141],
        "Kraken": user_data[143],
        "Kree'Arra": user_data[145],
        "K'ril Tsutsaroth": user_data[147],
        "Mimic": user_data[149],
        "Nightmare": user_data[151],
        "Phosani's Nightmare": user_data[153],
        "Obor": user_data[155],
        "Sarachnis": user_data[157],
        "Scorpia": user_data[159],
        "Skotizo": user_data[161],
        "Tempoross": user_data[163],
        "The Gauntlet": user_data[165],
        "The Corrupted Gauntlet": user_data[167],
        "Theatre of Blood": user_data[169],
        "Theatre of Blood: Hard Move": user_data[171],
        "Thermonuclear Smoke Devil": user_data[173],
        "TzKal-Zuk": user_data[175],
        "TzKal-Jad": user_data[177],
        "Venenatis": user_data[179],
        "Vet'ion": user_data[181],
        "Vorkath": user_data[183],
        "Wintertodt": user_data[185],
        "Zalcano": user_data[187],
        "Zulrah": user_data[189]
    }

    #finally initiate and return final dictionary as sub dictionary
    final_dict = {
        "Skills": skills,
        "Bosses": bosses
    }
    return final_dict


user_data = returnskillsandmonstersdict('pgp green')

print(user_data["Skills"])
print("\n")
print(user_data["Bosses"])