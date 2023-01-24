# import globals

class Card:
    def __init__(self, name = "", type = 1, color = 1, stage = 1, attribute = 1, level = 0, play_cost = 0, evolution_cost = 0, rarity = 1, dp = 0, digi_type = 1, card_number = "", main_effect = "", soure_effect = "", original_set = "", sets = [], image = ""):
        if isinstance(name, str):
            self.name = name
            self.type = type
            # self.type = globals.CARD_TYPE[type]
            self.color = color
            # self.color = globals.DIGIMON_COLOR[color]
            self.stage = stage
            # self.stage = globals.STAGE[stage]
            self.attribute = attribute
            # self.attribute = globals.ATTRIBUTE[attribute]
            self.level = level
            self.play_cost = play_cost
            self.evolution_cost = evolution_cost
            self.rarity = rarity
            # self.rarity = globals.RARITY[rarity]
            self.dp = dp
            self.digi_type = digi_type
            # self.digi_type = globals.DIGIMON_TYPE[digi_type]
            self.card_number = card_number
            self.main_effect = main_effect
            self.soure_effect = soure_effect
            self.original_set = original_set
            self.image = image
            self.sets = sets
        else:
            self.name = name["name"]
            self.type = name["type"]
            # self.type = globals.CARD_TYPE[type]
            self.color = name["color"]
            # self.color = globals.DIGIMON_COLOR[color]
            self.stage = name["stage"]
            # self.stage = globals.STAGE[stage]
            self.attribute = name["attribute"]
            # self.attribute = globals.ATTRIBUTE[attribute]
            self.level = name["level"]
            self.play_cost = name["play_cost"]
            self.evolution_cost = name["evolution_cost"]
            self.rarity = name["cardrarity"]
            # self.rarity = globals.RARITY[rarity]
            self.dp = name["dp"]
            self.digi_type = name["digi_type"]
            # self.digi_type = globals.DIGIMON_TYPE[digi_type]
            self.card_number = name["cardnumber"]
            self.main_effect = name["maineffect"]
            self.soure_effect = name["soureeffect"]
            self.original_set = name["set_name"]
            self.image = name["image_url"]
            self.sets = name["card_sets"]
        self.__location = 0

    def __repr__(self):
        return "Card()"

    def __str__(self):
        return f' Name: {self.name}\n Type: {self.type}\n Color: {self.color}\n Stage: {self.stage}\n Attribute: {self.attribute}\n Level: {self.level}\n Play Cost: {self.play_cost}\n Evolution Cost: {self.evolution_cost}\n Rarity: {self.rarity}\n DP: {self.dp}\n DigimonType: {self.digi_type}\n Card Number: {self.card_number}\n Main Effect: {self.main_effect}\n Soure Effect: {self.soure_effect}\n Original Set: {self.original_set}\n Image: {self.image}\n Sets: {self.sets}\n '
            
    def getCard(name = "", desc = "", color = "", type = "", attribute = "", card = "", pack = "", sort = "", sortDirection = "desc", series = ""):
        print(f'https://digimoncard.io/api-public/search.php?n={name}&desc={desc}&color={color}&type={type}&attribute={attribute}&card={card}&pack={pack}&sort={sort}&sortdirection={sortDirection}&series={series}')
        

    def getAllCards( sort = "name", series = "", sortDirection = "asc"):
        print(f'https://digimoncard.io/api-public/getAllCards.php?sort={sort}&series={series}&sortdirection={sortDirection}')


    def setLocation(self, location = 0):
        self.__location = location
        
    def getLocation(self):
        self.__location
        
    def checkLocation(self, location = 0 ):
        self.__location == location
        