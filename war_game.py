from deck_of_cards import deck_of_cards
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.draw = []
        self.discard = []

#Test to make sure list imported correctly; code was run twice, and each time a card name and a card value were printed.
# card = random.choice(deck_of_cards)
# print(card.name, card.value)

random.shuffle(deck_of_cards)

player1 = Player("Player 1")
player2 = Player("Player 2")

# Test Code for Deck of Cards - deck was shuffled and a random card was pulled from index 0
# card = deck_of_cards.pop(0)
# print(card.name, card.value)

for x in range(52):
    if x < 26:
        card = deck_of_cards.pop(0)
        player1.draw.append(card)
    else:
        card = deck_of_cards.pop(0)
        player2.draw.append(card)

# Test Code for Draw Piles - each player's draw pile now has 26 random cards
# for card in player1.draw:
#     print(player1.name, card.name, card.value)

# for card in player2.draw:
#     print(player2.name, card.name, card.value)

# print(len(player1.draw))
# print(len(player2.draw))

war_cards = []

def war(player1_card, player2_card):
    if len(war_cards) == 0:
        war_cards.append(player1_card)
        war_cards.append(player2_card)

    if len(war_cards) != 0:
        if len(player1.draw) < 5:
            discard_to_draw(player1)
            if len(player1.draw) < 5:
                for x in range(0, len(player1.draw), 1):
                    card = player1.draw.pop(0)
                    war_cards.append(card)
                player1_card5 = war_cards[len(war_cards) - 1]
        
        if len(player1.draw) >= 5:
            for x in range(0, 5, 1):
                card = player1.draw.pop(0)
                war_cards.append(card)
            player1_card5 = war_cards[len(war_cards) - 1]
            print("The length of the war cards list is:", len(war_cards))

        if len(player2.draw) < 5:
            discard_to_draw(player2)
            if len(player2.draw) < 5:
                for x in range(0, len(player2.draw), 1):
                    card = player2.draw.pop(0)
                    war_cards.append(card)
                player2_card5 = war_cards[len(war_cards) - 1]
    
        if len(player2.draw) >= 5:
            for x in range(0, 5, 1):
                card = player2.draw.pop(0)
                war_cards.append(card)
            player2_card5 = war_cards[len(war_cards) - 1]
            print("The length of the war cards list is:", len(war_cards))

    if player1_card5.value > player2_card5.value:
        print("Your " + player1_card5.name + " beats the " + player2_card5.name + "!")
        print("The length of " + player1.name + "'s discard pile was:", len(player1.discard))
        for card in war_cards:
            player1.discard.append(card)
        war_cards.clear()
        print(player1.name + " has", len(player1.draw), "cards in their draw pile and", len(player1.discard), "cards in their discard pile.")
        print(player2.name + " has", len(player2.draw), "cards in their draw pile and", len(player2.discard), "cards in their discard pile.")
        return

    elif player1_card5.value < player2_card5.value:
        print("Your " + player1_card5.name + " loses to the " + player2_card5.name + ".")
        print("The length of " + player2.name + "'s discard pile was:", len(player2.discard))
        for card in war_cards:
            player2.discard.append(card)
        war_cards.clear()
        print(player1.name + " has", len(player1.draw), "cards in their draw pile and", len(player1.discard), "cards in their discard pile.")
        print(player2.name + " has", len(player2.draw), "cards in their draw pile and", len(player2.discard), "cards in their discard pile.")
        return

    elif player1_card5.value == player2_card5.value:
        print("Your " + player1_card5.name + " ties with the " + player2_card5.name + "! You and the computer enter into another War.")
        # war(player1_card, player2_card)
        while True:
            choice = input(player1.name + ", select P to play your card or Q to quit the game: ")
            if choice.upper() == "P":
                war(player1_card, player2_card)
            elif choice.upper() == "Q":
                print("Thank you for playing! Your final point total is:", len(player1.draw) + len(player1.discard), "- We hope you play again soon!")
                break
            else: 
                print("You have not selected a valid option. Please select P to play or Q to quit.")


def discard_to_draw(player):
    if len(player.discard) > 0:
        random.shuffle(player.discard)
        for card in player.discard:
            player.draw.append(card)
        player.discard.clear()
        print(player.name + " has shuffled their discard pile and now has a new draw pile. Their card total is:", len(player.draw))
    else:
        print(player.name + " has run out of cards!")
        return False


def war_one_player():
    while True:
        choice = input(player1.name + ", select P to play your card or Q to quit the game: ")
        if choice.upper() == "P":
            if len(player1.draw) == 0:
                x = discard_to_draw(player1)
                if x == False:
                    print(player2.name + " wins the game!")
                    print(player2.name + " has a final point total of:", len(player2.draw) + len(player2.discard))
                    break
            if len(player2.draw) == 0:
                x = discard_to_draw(player2)
                if x == False:
                    print(player1.name + " wins the game!")
                    print(player1.name + " has a final point total of:", len(player1.draw) + len(player1.discard))
                    break
            
            player1_card = player1.draw.pop(0)
            print("You have played a " + player1_card.name + ".")
            player2_card = player2.draw.pop(0)
            print("The computer has played a " + player2_card.name + ".")

            if player1_card.value > player2_card.value:
                print("Your " + player1_card.name + " beats the " + player2_card.name + "!")
                player1.discard.append(player1_card)
                player1.discard.append(player2_card)
                print(player1.name + " has", len(player1.draw), "cards in their draw pile and", len(player1.discard), "cards in their discard pile.")
                print(player2.name + " has", len(player2.draw), "cards in their draw pile and", len(player2.discard), "cards in their discard pile.")

            elif player1_card.value < player2_card.value:
                print("Your " + player1_card.name + " loses to the " + player2_card.name + ".")
                player2.discard.append(player1_card)
                player2.discard.append(player2_card)
                print(player1.name + " has", len(player1.draw), "cards in their draw pile and", len(player1.discard), "cards in their discard pile.")
                print(player2.name + " has", len(player2.draw), "cards in their draw pile and", len(player2.discard), "cards in their discard pile.")

            elif player1_card.value == player2_card.value:
                print("Your " + player1_card.name + " ties with the " + player2_card.name + "! You and the computer enter into War.")
                war(player1_card, player2_card)

        elif choice.upper() == "Q":
            print("Thank you for playing! Your final point total is:", len(player1.draw) + len(player1.discard), "- We hope you play again soon!")
            break

        else:
            print("You have not selected a valid option. Please select P to play or Q to quit.")


def war_two_players():
    while True:
        choice_player1 = input(player1.name + ", select P to play your card or Q to quit the game.")
        choice_player2 = input(player2.name + "select P to play your card or Q to quit the game.")
        if choice_player1.upper() == "P" and choice_player2.upper() == "P":
            if len(player1.draw) == 0:
                x = discard_to_draw(player1)
                if x == False:
                    print(player2.name + " wins the game!")
                    print(player2.name + " has a final point total of ", len(player2.draw) + len(player2.discard))
                    break
            
            if len(player2.draw) == 0:
                x = discard_to_draw(player2)
                if x == False:
                    print(player1.name + " wins the game!")
                    print(player1.name + " has a final point total of:", len(player1.draw) + len(player1.discard))
                    break
            
            player1_card = player1.draw.pop(0)
            print(player1.name + " has played a " + player1_card.name + ".")
            player2_card = player2.draw.pop(0)
            print(player2.name + " has played a " + player2_card.name + ".")
            
            if player1_card.value > player2_card.value:
                print(player1.name + "'s " + player1_card.name + " beats " + player2.name + "'s " + player2_card.name + "!")
                player1.discard.append(player1_card)
                player1.discard.append(player2_card)

            elif player1_card.value < player2_card.value:
                print(player1.name + "'s " + player1_card.name + " loses to " + player2.name + "'s " + player2_card.name + "!")
                player2.discard.append(player1_card)
                player2.discard.append(player2_card)

            elif player1_card.value == player2_card.value:
                print(player1.name + "'s " + player1_card.name + " ties with " + player2.name + "'s " + player2_card.name + "!" + player1.name + " and " + player2.name + " enter into War.")
                war(player1_card, player2_card)

        elif choice_player1.upper() == "Q" or choice_player2.upper() == "Q":
            print("Thank you for playing!\n" + player1.name + "'s final point total is:", (len(player1.draw) + len(player1.discard)),
                  "\n" + player2.name + "'s final point total is:", len(player2.draw) + len(player2.discard), "\nWe hope you play again soon!")
            break

        else:
            print("You have not selected a valid option. Please select P to play or Q to quit.")



while True:
    print("Welcome to the Game of War!")
    choice = input("Please select the number of players: ")
    if choice == "1":
        player1.name = input("Enter your name: ")
        player2.name = "Computer"
        print("Welcome " + player1.name + "!")
        break
    elif choice == "2":
        player1.name = input("Enter the first player's name: ")
        player2.name = input("Enter the second player's name: ")
        print("Welcome" + player1.name + " and " + player2.name + "!")
        break
    else:
        print("This game only supports up to two players. Please select either one or two players for this game.")

if player2.name == "Computer":
    war_one_player()
elif player2.name != "Computer":
    war_two_players()