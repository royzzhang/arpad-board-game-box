import random

import streamlit as st


class Card:
    face_value_rank = list(range(3, 11)) + ['J', 'Q', 'K', 'A', 2, '小王', '大王']

    def __init__(self, face_value):
        self.face_value = face_value

    def __str__(self):
        return str(self.face_value)

    def __gt__(self, other):
        return self.face_value_rank.index(self.face_value) > self.face_value_rank.index(other.face_value)

    def __eq__(self, other):
        return self.face_value_rank.index(self.face_value) == self.face_value_rank.index(other.face_value)

    def __lt__(self, other):
        return self.face_value_rank.index(self.face_value) < self.face_value_rank.index(other.face_value)


class Pile:
    def __init__(self, cards):
        self.cards = cards
        self.cards.sort()

    def __str__(self):
        result = []
        for i in range(len(self.cards)):
            result.append(self.cards[i].__str__())
        return ' '.join(result)


class Deck:
    def __init__(self):
        self.cards = [Card('小王'), Card('大王')]
        for i in list(range(2, 11)) + ['J', 'Q', 'K', 'A']:
            for j in range(4):
                self.cards.append(Card(i))

    def shuffle(self):
        random.shuffle(self.cards)
        return self

    def distribute(self):
        pile_1 = Pile(self.cards[:17])
        pile_2 = Pile(self.cards[17:34])
        pile_3 = Pile(self.cards[34:51])
        pile_4 = Pile(self.cards[51:])
        return pile_1, pile_2, pile_3, pile_4


with st.sidebar:
    player_count = 3
    player_names = [''] * player_count
    for i in range(player_count):
        player_names[i] = st.text_input(f'玩家{i + 1}')

st.title('斗地主发牌器')

deck = Deck()
deck.shuffle()
player_pile = [None] * player_count
player_pile[0], player_pile[1], player_pile[2], reserved = deck.distribute()

output_string = ''
for i in range(player_count):
    output_string += f'{i + 1}({player_names[0]}): {player_pile[i]}\n'
output_string += f'地主牌: {reserved}'

st.subheader('发牌结果')
st.write('请点击下方文本框右上角直接复制发牌结果。')
st.code(output_string, language=None)
