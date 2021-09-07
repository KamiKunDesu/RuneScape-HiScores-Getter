# from osrs_highscores import Highscores

# #Initializes player object
# user = Highscores("pgpgreen")

# #saves overall scores
# user_overall = user.overall

# #saves dictionary of skills
# user_skill = user.skill

# #saves dictionary of bosses
# user_boss = user.boss

# #initialize two empty dictionaries store the results of bosses and skills
# bosses = {}
# skills = {}

# #print(user_skill)

# #iterates over bosses dictionary in player object to make a more accessible dictionary of bosses vs kills
# for key, value in user_boss.items():
#     bosses[key] = value['kills']

# #iterates over skills dictionary in player object to make a more accessible dictionary of skills vs level
# for key, value in user_skill.items():
#     skills[key] = value['level']

# #print both dictionaries for check
# print(skills)
# print("\n")
# print(bosses)

from OSRSBytes import Hiscores
import http.client

# user = Hiscores('georgedubya')

# print(user)

def _parseData(data):
        data = data.replace('\n', ',')
        data = data.split(',')
        print(data)
        # subset = {}
        # # Totals
        # info = {}
        # info['rank'] = self.data[0]
        # info['level'] = self.data[1]
        # info['experience'] = self.data[2]
        # subset['total'] = info
        # skills = [
        #     'attack',
        #     'defense',
        #     'strength',
        #     'hitpoints',
        #     'ranged',
        #     'prayer',
        #     'magic',
        #     'cooking',
        #     'woodcutting',
        #     'fletching',
        #     'fishing',
        #     'firemaking',
        #     'crafting',
        #     'smithing',
        #     'mining',
        #     'herblore',
        #     'agility',
        #     'thieving',
        #     'slayer',
        #     'farming',
        #     'runecrafting',
        #     'hunter',
        #       #     info['next_level_exp'] = math.floor(sum((math.floor(level + 300 * (2 ** (level / 7.0))) for level in range(1, level)))/4)
        #     info['exp_to_next_level'] = int(info['next_level_exp'] - info['experience'])
        #  'construction'
        #     ]
        # counter = 0
        # for i in range(len(skills)):
        #     info = {}
        #     info['rank'] = int(self.data[counter+3])
        #     info['level'] = int(self.data[counter+4])
        #     info['experience'] = int(self.data[counter+5])
        #     level = int(info['level']+1)
         #subset[skills[i]] = info
        #     counter += 3
        #     # set stats dictionary
        #     self.stats = {}
        #     self.stats[self.username] = subset
        #     self.stats[self.username]['cache_ttl'] = time.time() + self.cacheTTL
        #     # Check for caching
        #     if self.caching:
        #         self._cacheData()


def _getHTTPResponse(username: str, accountType='N'):
        conn = http.client.HTTPSConnection('secure.runescape.com')
        if accountType == 'N':
            conn.request("GET", "/m=hiscore_oldschool/index_lite.ws?player={}".format(username.replace(' ', '%20')))
            response = conn.getresponse()
            status = response.status
            response = response.read().decode('ascii')
            response = response.replace('\n', ',')
            response = response.split(',')
            return response
        elif accountType == 'IM':
            conn.request("GET", "/m=hiscore_oldschool_ironman/index_lite.ws?player={}".format(username.replace(' ', '%20')))
            response = conn.getresponse()
            status = response.status
        elif accountType == "UIM":
            conn.request("GET", "/m=hiscore_oldschool_ultimate/index_lite.ws?player={}".format(username.replace(' ', '%20')))
            response = conn.getresponse()
            status = response.status
        elif accountType == "HIM":
            conn.request("GET", "/m=hiscore_oldschool_hardcore_ironman/index_lite.ws?player={}".format(username.replace(' ', '%20')))
            response = conn.getresponse()
            status = response.status
            _processResponse(status, response)

def returnskillsandmonstersdict(user: str, accountType: str = 'N'):
    user_data = _getHTTPResponse(user, accountType)
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
    final_dict = {
        "Skills": skills,
        "Bosses": bosses
    }
    return final_dict


user_data = returnskillsandmonstersdict('georgedubya')

print(user_data["Skills"])
print("\n")
print(user_data["Bosses"])
