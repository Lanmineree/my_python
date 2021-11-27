import random
class Deck:
    def __init__(self):
        self.symbol = ["♠","♥","♦","♣"]
        self.point = ['A','2','3','4','5','6','7','8','9','10','J','K',"Q"]
        self.box =[]
        for i in self.symbol:
            for j in self.point:
                self.box.append(i+j)
    def shuffle(self):
        random.shuffle(self.box)
    def deal_game(self):
        self.dealcards=[self.box[0],self.box[1]]
        self.recard=[self.box.pop(0),self.box.pop(0)]
        return self.dealcards
class Player:
    def __init__(self,box2):
        self.box2 = box2
    def hit(self):
        self.hitcard=[self.box2.pop[0]]
        return self.hitcard
    def stand(self):
        pass
    def hit_or_stand(self):
        ans=input("Hit or Stand: ")
        if ans=="Hit":
            self.hit()
        if ans=="Stand":
            self.stand()

deck=Deck()
deck.shuffle()
player=Player(deck.box)
play1 = player(player.hit())