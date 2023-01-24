import random
import globals

class Playground:
    def __init__(self, deck):
        self.__deck = deck.cardList
        self.__securityArea = self.__setSecurityArea()
        self.__hand = self.__setHand()
        self.__deepOcean = self.__setDeepOcean()
        self.__darkArea = []
        self.__breedengArea = []
        self.__battleArea = []
        self.__memory = 0
        print(f'Deep Ocean {self.__deepOcean}')
        print(f'Secuiyty {self.__securityArea}')
        print(f'Hand {self.__hand}')

    def __setSecurityArea(self):
        unlocated = filter()
        sample_list = random.sample(unlocated, 3)
        for card in sample_list:
            card.setLocation(globals.PLAYMATE_SECURITY_AREA)
        print(sample_list)
        self.__securityArea = sample_list
        
    def __setHand(self):
        unlocated = filter()
        sample_list = random.sample(unlocated, 5)
        for card in sample_list:
            card.setLocation(globals.PLAYMATE_HAND)
        print(sample_list)
        self.__hand = sample_list
        
    def __setDeepOcean(self):
        unlocated = filter()
        for card in unlocated:
            card.setLocation(globals.PLAYMATE_DEEP_OCEAN)
        print(sample_list)
        self.__hand = sample_list

    def __draw(self, count = 1):
        sample_list = random.sample(self.__deepOcean, count)
        for card in sample_list:
            card.setLocation(globals.PLAYMATE_HAND)
            self.__hand.append(card)
        print(sample_list)
        self.__deepOcean = filter(globals.PLAYMATE_DEEP_OCEAN)

    def 
    
    def filter(self, search = globals.PLAYMATE_UNLOCATED):
        list( filter(lambda check: card.checkLocation(search), self.__deck))