import pygame,json,sys,random
#from controller import *

#symbols = ["spades", "clubs", "diamonds", "hearts"]


class Spritesheet:
    def __init__(self, filename):
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert()
        self.meta_data = self.filename.replace("jpeg","json")
        with open(self.meta_data) as f:
            self.data = json.load(f)
        f.close()

    def get_sprite(self,x,y,w,h):
        sprite = pygame.Surface((w,h))
        sprite.blit(self.sprite_sheet,(0,0),(x,y,w,h))
        return sprite
    
    def parse_sprite(self,name):
        sprite = self.data["frames"][name]["frame"]
        x,y,w,h = sprite["x"],sprite["y"],sprite["w"],sprite["h"]
        image = self.get_sprite(x,y,w,h)
        return image

class Card:
    def __init__(self, number, symbol, sprite, back):
        self.number = number
        self.symbol = symbol
        self.sprite = sprite
        self.back = back


class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()

    def create_deck(self):
        back = pygame.image.load("../sprites/backcard.jpeg").convert()
        back = pygame.transform.scale(back,(65,85))
        spritesheet = Spritesheet("../sprites/cards_sprites.jpeg")
        numeros = ["a","2","3","4","5","6","7","8","9","10","j","q","k"]
        palos = ["spades", "clubs", "diamonds", "hearts"]
        for palo in palos:
            for numero in numeros:
                card = Card(numero,palo,spritesheet.parse_sprite(numero+"_"+palo),back)
                self.cards.append(card)



class FullDeck:
    def __init__(self,quantity):
        self.cards = []
        self.create_full_deck(quantity)

    def create_full_deck(self,quantity):
        for i in range(quantity):
            deck = Deck()
            self.cards.extend(deck.cards)
        self.shuffle()
    
    def shuffle(self):
        random.shuffle(self.cards)

class main():
    pygame.init()
    fondo = pygame.image.load("../sprites/mesa1.jpeg")
    rect = fondo.get_rect()
    fondo = pygame.transform.scale(fondo,(rect.width*2,rect.height*2))
    ventana = pygame.display.set_mode((rect.width*2,rect.height*2))
    pygame.display.set_caption("Prueba")
    fuente = pygame.font.Font(None,30)
    
    deck = FullDeck(2)
    indice = 0
    cards = []
    cards1 = []
    cards2 = []
    cards3 = []
    
    own_cards = pygame.Surface((715,85))
    own_cards1 = pygame.Surface((715,85))
    own_cards2 = pygame.Surface((715,85))
    own_cards3 = pygame.Surface((715,85))
    for i in range(11):
        cards.append(deck.cards.pop(0))
        cards1.append(deck.cards.pop(0))
        cards2.append(deck.cards.pop(0))
        cards3.append(deck.cards.pop(0))
        own_cards.blit(cards[i].sprite,(65*i,0))
        own_cards1.blit(cards1[i].sprite,(65*i,0))
        own_cards2.blit(cards2[i].sprite,(65*i,0))
        own_cards3.blit(cards3[i].sprite,(65*i,0))
    while True:
        numdeck = fuente.render(str(len(deck.cards)),0,(0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    indice = (indice + 1) % len(deck.cards)
                elif event.key == pygame.K_LEFT:
                    indice = (indice - 1) % len(deck.cards)
            elif event.type == pygame.MOUSEBUTTONUP:
                if len(deck.cards) > 0:
                    deck.cards.pop()
        
        ventana.blit(fondo,(0,0))
        for i in range(len(deck.cards)):
            deck.cards[i].back.set_colorkey((255,255,255))
            ventana.blit(deck.cards[i].back,(rect.width-32,rect.height-42))
        ventana.blit(numdeck,(rect.width+38,rect.height-5))
        ventana.blit(own_cards,(0,0))
        ventana.blit(own_cards1,(0,86))
        ventana.blit(own_cards2,(0,172))
        ventana.blit(own_cards3,(0,258))
        pygame.display.update()

if __name__ == "__main__":
    main()