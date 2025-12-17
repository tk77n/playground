import random


class Card:
    def __init__(self, suit: str, number: int):
        self.suit = suit
        self.number = number


class Deck:
    def __init__(self):
        self.cards = []  # 委譲か
        # 初期化の時点ででトランプを生成
        for suit in ["ハート", "スペード", "ダイヤ", "クラブ"]:
            for number in range(1, 14):
                card = Card(suit, number)
                self.cards.append(card)

    # シャッフル
    def shuffle(self) -> None:
        random.shuffle(self.cards)

    # ドロー
    def draw_card(self) -> Card:
        return self.cards.pop()


d = Deck()
d.shuffle()

print("全カードの表示")
for card in d.cards:
    print(card.suit, card.number)
print()

print("ドローを試す")
for x in range(5):
    print(f"{x+1}枚目 : {d.draw_card().suit} {d.draw_card().number}")
