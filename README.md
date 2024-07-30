# cards
A simulation for playing cards and the market for purchasing

### Card game
This is a card game inspired heavily from Magic the Gathering. This has roughly similar rules and terminology but is simplified to cater the needs of this game. The purpose of creating actual "game" is to create an AI to choose good decks to fight other AIs. This then creates desireability of a card to be chosen to a deck.

## Game mechanics
Each player act on their turn. They are able to play cards from their hands and act with the cards on the table. There are 3 types of cards currently: monsters, enchantments, and mana cards. Monsters are cards that can be used from the table to attack the opponent and their cards. Enchantments give abilities and boosts to players. Mana used as currency to play the cards.

## Cards
TBD


### Market simulationi
The idea is to run multiple games along with market simulation. The market is similar to stock market and relies on the values of the cards. Many things affect the value: effectiveness in game play, the rarity of the card, the printing, artist, etc.

## Market mechanics
TBD

## Data gathering
In the beginning stages, create the game framework so that it can generate data to cover thousands of games and generate effectiveness score for each card on a scale of 0...1 and the average amount of that card chosen in a deck. The data is collected and saved into csv-file that is used later as a base for choosing decks.