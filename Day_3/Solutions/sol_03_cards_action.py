from sol_01_card import Card, VALUES, SUITS


cards = []
# TODO-1: в список cards добавьте ВСЕ карты всех мастей
for suit in SUITS:
    for value in VALUES:
        cards.append(Card(value, suit))

# TODO-2: Выведите карты в формате: cards[кол-во]2♠, 3♠, 4♠ ... A♠, ..., 2♦, 3♦ ... A♦, 2♥, 3♥, 4♥ ... A♥
out_cards = []
for card in cards:
    out_cards.append(card.to_str())

result = f"cards[{len(cards)}] {', '.join(out_cards)}"
print(result)
