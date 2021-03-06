import random
import time
class Card:
    def __init__(self, value):
        self.__value = value
        self.__suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
        self.__ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

    def getRank(self):
        return self.__ranks[self.__value % 13]

    def getSuit(self):
        return self.__suits[self.__value // 13]

    def getCardValue(self):
        return self.__value % 13 + 1

    def getDeckValue(self):
        return self.__value

    def getNickName(self):
        nickName = ""
        if self.getCardValue() > 1 and self.getCardValue() < 11:
            nickName += str(self.getCardValue())
        else:
            nickName += self.getRank()[0]

        nickName += self.getSuit()[0]

        return nickName

    # Dunder to return a string representation to print() and format()
    def __str__(self):
        return self.getRank() + " of " + self.getSuit()

    # Dunder to return a string representation to other usages
    def __repr__(self):
        return self.__str__()


class Deck:
    def __init__(self):
        self.shuffle()

    def shuffle(self):
        self.__deck = []
        for i in range(52):
            self.__deck.append(Card(i))
        random.shuffle(self.__deck)

    def draw(self):
        return self.__deck.pop()


def main():
    print("Welcome to the Jacob's BlackJack Table")
    #Number of players
    number_of_players = int(input("How many players are there today?: "))
    player_list = []
    for i in range(number_of_players):
        player_list.append(i + 1)

    balance = starting_balance(number_of_players)
    keep_playing = True
    while keep_playing == True:
        z = 0
        bets = take_bets(number_of_players, balance, player_list)
        #creates deck
        mydeck = Deck()

        print("\nPlease wait while cards are dealt...")
        time.sleep(3)

        players_hands = []
        done = False
        round = 1
        while not done:
            #deals another card to each player
            dealhand(number_of_players, mydeck, players_hands, round, player_list)
            second = True if round == 2 else False
            if second is True:
                print("\nThe dealers second card is: " + str(players_hands[len(player_list)][1]))
                done = True
            round += 1




        y = 0
        playernumber = player_list[y]
        done = False
        x = 0
        while not done:
            if playernumber - 1 == number_of_players:
                if x == 0:
                    print("\nDealers Turn")
                    time.sleep(1)
                    x += 1
                time.sleep(1)
                print("\nDealers Hand....")
                for i in range(len(players_hands[len(player_list)])):
                    print(players_hands[len(player_list)][i])
                time.sleep(1)
                if check_hand_value(len(player_list), players_hands, number_of_players) == 'dealerstop':
                    done = True
                    print("\nDealer Holds")
                    time.sleep(1)
                elif check_hand_value(len(player_list), players_hands, number_of_players) == 'bust':
                    done = True
                    print("\nDealer Busts!")
                    time.sleep(1)
                elif find_hand_value(len(player_list), players_hands, number_of_players) >= 17:
                    done = True
                    print("\nDealer Holds")
                    time.sleep(1)
                else:
                    players_hands[len(player_list)].append(mydeck.draw())
                    print("\nDealer Draws")

                    time.sleep(1)

            else:
                bust = False
                round = 3
                print("\nPlayer " + str(playernumber) + " your hand is...")
                for i in range(round - 1):
                    print(players_hands[y][i])
                playerturndone = False
                round = 2
                while not playerturndone:

                    playerAction = int(input("\nType 1 for hit\nType 2 for hold\nUser Input: "))
                    if playerAction == 1:
                        players_hands[y].append(mydeck.draw())
                        round += 1
                        print("\nPlayer number " + str(playernumber) + " your hand is...")

                        for i in range(round):
                            print(players_hands[y][i])


                        if check_hand_value(player_list.index(player_list[z]), players_hands, len(player_list) - 1) == 'bust':
                            print("\nPlayer " + str(playernumber) + " you Bust!")
                            time.sleep(1)
                            playerturndone = True




                    elif playerAction == 2:
                        print("\nPlayer " + str(playernumber) + " Holds")
                        time.sleep(1)
                        playerturndone = True
                    else:
                        print("Invalid input please try again")


                if player_list[y] == player_list[-1]:
                    playernumber = number_of_players + 1
                else:
                    y += 1
                    playernumber = player_list[y]
                    z += 1



        payouts(len(player_list), players_hands, bets, balance, player_list)

        playerout(number_of_players, balance, player_list)
        if len(player_list) == 0:
            print("All Players Lose!!!")
            break


        playagain = int(input("\nType 1 to play again or Type 2 to end game: "))
        again = None
        while again is None:
            again = None
            if playagain == 1:
                again = True
            elif playagain == 2:
                keep_playing = False
            else:
                print("Incorrect Input: ")
                playagain = int(input("Type 1 to play again or Type 2 to end game: "))






def starting_balance(number_of_players):
    balance = []
    for i in range(number_of_players):
        for j in range(0, 1):
            balance.append([])
            balance[i].append(100)
    return balance

def dealhand(number_of_players, mydeck, players_hands, round, playerlist):
    for i in range(len(playerlist) + 1):
        if round == 1:
            players_hands.append([])
        for j in range(0, 1):
                players_hands[i].append(mydeck.draw())
    return players_hands, mydeck

def cards_by_value():
    deck = []
    for i in range(52):
        print(card.Card(i))

def find_hand_value(playernumber, players_hands, number_of_players):
    hand_value = 0
    for i in range(len(players_hands[playernumber])):
        if str(players_hands[playernumber][i]).split()[0] == "Ace":
            if hand_value <= 10:
                hand_value += 11
            else:
                hand_value += 1
        elif str(players_hands[playernumber][i]).split()[0] == "Two":
            hand_value += 2
        elif str(players_hands[playernumber][i]).split()[0] == "Three":
            hand_value += 3
        elif str(players_hands[playernumber][i]).split()[0] == "Four":
            hand_value += 4
        elif str(players_hands[playernumber][i]).split()[0] == "Five":
            hand_value += 5
        elif str(players_hands[playernumber][i]).split()[0] == "Six":
            hand_value += 6
        elif str(players_hands[playernumber][i]).split()[0] == "Seven":
            hand_value += 7
        elif str(players_hands[playernumber][i]).split()[0] == "Eight":
            hand_value += 8
        elif str(players_hands[playernumber][i]).split()[0] == "Nine":
            hand_value += 9
        elif str(players_hands[playernumber][i]).split()[0] == "Ten":
            hand_value += 10
        elif str(players_hands[playernumber][i]).split()[0] == "Jack":
            hand_value += 10
        elif str(players_hands[playernumber][i]).split()[0] == "Queen":
            hand_value += 10
        elif str(players_hands[playernumber][i]).split()[0] == "King":
            hand_value += 10
    return hand_value

def check_hand_value(player_number, player_hands, number_of_players):
    if find_hand_value(player_number, player_hands, number_of_players) > 21:
        return 'bust'
    elif player_number == number_of_players:
        if 17 < find_hand_value(player_number, player_hands, number_of_players) < 21:
            return 'dealerstop'

def take_bets(number_of_players, balance, playerlist):
    bets = []
    while len(bets) < len(playerlist):
        for i in range(len(playerlist)):

            while len(bets) <= i:

                print(("\nPlayer " + str(playerlist[i]) + " you have a balance of $" + str(balance[i][0])))
                bet = int(input("Player " + str(playerlist[i]) + ", How much will you bet?: "))

                if bet > int(balance[i][0]):
                    print("Insuficient Funds")
                elif bet < 5:
                    if int(balance[i][0]) < 5:
                        print("Your balance is less than $5 so your remaining money will be bet")
                        bets.append(balance[i][0])
                    else:
                        print("Bet must be at least $5")
                else:
                    bets.append(bet)
    return bets

def payouts(number_of_players, players_hands, bets, balance, playerlist):
    for i in range(len(playerlist)):
        if int(find_hand_value(number_of_players, players_hands, number_of_players)) > 21 and int(find_hand_value(i, players_hands, number_of_players)) <= 21:
            balance[i][0] = int(balance[i][0]) + int(bets[i])
        elif int(find_hand_value(i, players_hands, number_of_players)) > 21:
            balance[i][0] = int(balance[i][0]) - int(bets[i])
        elif int(find_hand_value(i, players_hands, number_of_players)) <= 21 and int(find_hand_value(i, players_hands, number_of_players) > int(find_hand_value(number_of_players, players_hands, number_of_players))):
            balance[i][0] = int(balance[i][0]) + int(bets[i])
        elif int(find_hand_value(i, players_hands, number_of_players)) <= 21 and int(find_hand_value(i, players_hands, number_of_players) == int(find_hand_value(number_of_players, players_hands, number_of_players))):
            balance[i][0] = int(balance[i][0])
        elif int(find_hand_value(i, players_hands, number_of_players)) <= 21 and int(find_hand_value(i, players_hands, number_of_players) < int(find_hand_value(number_of_players, players_hands, number_of_players))):
            balance[i][0] = int(balance[i][0]) - int(bets[i])
    for i in range(len(playerlist)):
        playernumber = i + 1
        print("New balance of player " + str(playernumber) + " is $" + str(balance[i][0]))

def playerout(number_of_players, balance, player_list):
    popnumber = 0
    for i in range(len(player_list)):

        if int(balance[popnumber][0]) == 0:
            print("\nPlayer " + str(i + 1) + " your out!")
            player_list.pop(popnumber)
            balance.pop(popnumber)
            number_of_players -= 1
        else:
            popnumber += 1
    return player_list, number_of_players




main()