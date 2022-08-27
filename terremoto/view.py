import pygame
from controller import *

symbols = ["spades", "clover", "diamond", "heart"]


class Card:
    def __init__(self, number, symbol, sprite, back):
        self.number = number
        self.symbol = symbol
        self.sprite = sprite
        self.back = back


class Deck:
    pass


class FullDeck:
    pass
