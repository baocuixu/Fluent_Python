#! -*- coding: utf-8 -*-

import collections

#纸牌类
Card = collections.namedtuple('Card',['rank', 'suit'])

class FrenchDeck:
	ranks = [str(n) for n in range(2, 11) + list('JQKA')]
	suits = 'spades diamonds clubs hearts'.split()

	def __init__(self):
		self._cards = [Card(rank, suit) for suit in self.suits
		                               for rank self.ranks]
	
	def __len__(self):
		return len(self._cards)

	def __getitem__(self, postition)：
		return self._cards[postion]
