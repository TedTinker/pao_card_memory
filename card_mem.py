from itertools import product
from random import shuffle

class Card():
    
    def __init__(self, p = "person", a = "action", o = "object"):
        self.p = p; self.a = a; self.o = o
        
    def __str__(self):
        return(
            "{} | {} | {}.".format(self.p, self.a, self.o))
    
    def __repr__(self):
        return(self.__str__())
    
    
        
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["♡", "♢", "♣", "♠"] # "♠♤♥♡♦♢♣♧"





class Deck():

    def __init__(self):
        self.deck = {value + suit : None for suit, value in product(suits, values)}
        self.value_suits = []
        
    def update(self, suit, value, card):
        self.deck[value + suit] = card
        if(not value + suit in self.value_suits):
            self.value_suits.append(value + suit)
        
    def shuffle_deck(self):
        value_suits = [_ for _ in self.value_suits]
        shuffle(value_suits)
        i = 0
        for value_suit in value_suits:
            card = self.deck[value_suit]
            if i%3 == 0: print("\n" + card.p, end = " | ")
            if i%3 == 1: print(card.a, end = " | ")
            if i%3 == 2: print(card.o, end = ".")
            if(i == len(value_suits)-1): 
                if(i%3 == 0): print("{} | {}.".format(card.a, card.o))
                if(i%3 == 1): print("{}.".format(card.o))
            i += 1

    def __str__(self):
        to_return = ""
        current_suit = suits[0]
        for value_suit, card in self.deck.items():
            if(current_suit != value_suit[-1]): to_return += "\n"
            to_return += "\n{}: {}".format(value_suit, card)
            current_suit = value_suit[-1]
        return(to_return)
    
    def __repr__(self):
        return(self.__str__())
        
deck = Deck()

hearts = [
    Card("Link",    "finds () in a chest",              "an ocarina"),
    Card("Sonic",   "eats () and poops",                "a chili-dog"),
    Card("Olimar",  "digs up () and throws it",         "a bunch of pikmin"),
    Card("Kirby",   "sucks up",                         "metaknight"),
    Card("Bowser",  "breaths fire on",                  "a goomba"),
    Card("Koopa",   "is jumped on and turns into",      "a green shell"),
    Card("Wario",   "steals () from a garlic guy",      "garlic"),
    Card("Toad",    "takes the mask off",               "a Shyguy"),
    Card("Yoshi",   "eats () and lays an egg",          "Baby Mario"),
    Card("Daisy",   "gets () in a Mario-Kart item",     "a red shell"),
    Card("Luigi",   "vacuums up",                       "Boo"),
    Card("Peach",   "floats hanging from",              "an umbrella"),
    Card("Mario",   "eats () and gets bigger",          "a mushroom")
    ]

diamonds = [
    Card("Ed, Edd, and Eddy",    "",              "jawbreakers"),
    Card("Mr Krabs",    "",              "one dollar"),
    Card("Plankton",    "",              "Plankton's wife"),
    Card("Sandy",    "",              ""),
    Card("Patrick",    "",              ""),
    Card("Chowder",    "",              ""),
    Card("Ben Tennason",    "slaps his wristwatch to become",              ""),
    Card("Squidward",    "yelling out his window, shaking",              "a clarinet"),
    Card("Timmy Turner",    "",              ""),
    Card("Jimmy Neutron",    "",              ""),
    Card("Powerpuff Girls",    "",              ""),
    Card("Dexter",    "",              ""),
    Card("Spongebob",    "pressing () on a grill",      "a jellyfish"),
    ]

clubs = [
    Card("Red Scout",       "whacks () with a fish",    "Blu Scout"),
    Card("Red Soldier",     "fires a rocket at",        "Blu Soldier"),
    Card("Red Pyro",        "fires a firework at",      "Blu Pyro"),
    Card("Red Demoman",     "throws a grenade at",      "Blu Demoman"),
    Card("Red Heavy",       "fires a machine-gun at",   "Blu Heavy"),
    Card("Red Engineer",    "whacks () with a wrench",  "Blu Engineer"),
    Card("Red Medic",       "ubers",                    "Blu Medic"),
    Card("Red Sniper",      "pees on",                  "Blu Sniper"),
    Card("Red Spy",         "stabs () with a knife",    "Blu Spy"),
    Card("Bayonetta",       "picks up {} with their hair", "Satan"),
    Card("",                "",                         ""),
    Card("Chell",           "uses portals to fire",     "space personality core"),
    Card("Gordan Freeman",  "uses gravity gun on",      "the G-Man"),
    ]

spades = [
    
    ]

for heart, value in zip(hearts, values):
    deck.update("♡", value, heart)
for diamond, value in zip(diamonds, values):
    deck.update("♢", value, diamond)
for club, value in zip(clubs, values):
    deck.update("♣", value, club)
for spade, value in zip(spades, values):
    deck.update("♠", value, spade)

print(deck)

deck.shuffle_deck()