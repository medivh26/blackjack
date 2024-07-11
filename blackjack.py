import random

# Define global variables
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']  # List of card suits
values = range(1, 14)  # List of card values from 1 to 13 (Ace to King)
player1_name = "Player 1"  # Name of Player 1
player2_name = "Player 2"  # Name of Player 2

def create_deck():
    """ Create a deck of 52 cards """
    deck = [(suit, value) for suit in suits for value in values]  # Generate all 52 cards in a deck
    random.shuffle(deck)  # Shuffle the deck randomly
    return deck

def calculate_total(cards):
    """ Calculate the total value of cards in hand """
    total = sum(card[1] for card in cards)  # Sum up all card values in the hand
    num_aces = sum(1 for card in cards if card[1] == 1)  # Count how many Aces (value 1) are in the hand
    
    # Adjust total if there are Aces in hand (Ace can be 1 or 11)
    while total <= 11 and num_aces > 0:
        total += 10
        num_aces -= 1
    
    return total

def display_cards(player_name, cards):
    """ Display cards for a player or dealer """
    card_names = [f"{card[1]} of {card[0]}" for card in cards]  # Format card names for display
    print(f"{player_name} cards: {', '.join(card_names)}")  # Print player's cards

def play_blackjack():
    """ Main function to play the blackjack game """
    deck = create_deck()  # Create a shuffled deck of cards
    rounds_played = 0  # Counter for rounds played
    player1_score = 0  # Initialize Player 1's score
    player2_score = 0  # Initialize Player 2's score
    
    while True:  # Loop to play multiple rounds until players decide to stop
        print(f"\n===== Round {rounds_played + 1} =====")  # Print round number
        rounds_played += 1  # Increment round counter
        
        # Deal initial cards to players and dealer
        player1_cards = [deck.pop(), deck.pop()]  # Deal two cards to Player 1
        player2_cards = [deck.pop(), deck.pop()]  # Deal two cards to Player 2
        dealer_cards = [deck.pop(), deck.pop()]  # Deal two cards to the Dealer
        
        # Display initial cards
        display_cards(player1_name, player1_cards)  # Display Player 1's cards
        display_cards(player2_name, player2_cards)  # Display Player 2's cards
        print(f"Dealer's cards: {dealer_cards[0][1]} of {dealer_cards[0][0]}")  # Display Dealer's visible card
        
        # Player 1's turn to hit or stand
        while True:
            choice = input(f"{player1_name}, do you want to hit or stand? (h/s): ").lower()  # Prompt Player 1 for choice
            if choice == 'h':  # If Player 1 chooses to hit
                player1_cards.append(deck.pop())  # Deal another card to Player 1
                display_cards(player1_name, player1_cards)  # Display Player 1's updated hand
                if calculate_total(player1_cards) > 21:  # Check if Player 1 busts
                    print(f"{player1_name} busts!")  # Print bust message
                    break  # Break out of Player 1's turn loop
            elif choice == 's':  # If Player 1 chooses to stand
                break  # Break out of Player 1's turn loop
        
        # Player 2's turn to hit or stand (similar logic as Player 1)
        while True:
            choice = input(f"{player2_name}, do you want to hit or stand? (h/s): ").lower()
            if choice == 'h':
                player2_cards.append(deck.pop())
                display_cards(player2_name, player2_cards)
                if calculate_total(player2_cards) > 21:
                    print(f"{player2_name} busts!")
                    break
            elif choice == 's':
                break
        
        # Dealer's turn logic
        while calculate_total(dealer_cards) < 17:  # Dealer must hit until reaching 17 or higher
            dealer_cards.append(deck.pop())  # Deal another card to the Dealer
        display_cards("Dealer", dealer_cards)  # Display Dealer's final hand
        
        # Determine winners and update scores
        player1_total = calculate_total(player1_cards)  # Calculate Player 1's total
        player2_total = calculate_total(player2_cards)  # Calculate Player 2's total
        dealer_total = calculate_total(dealer_cards)  # Calculate Dealer's total
        
        print(f"\nFinal results:")  # Print final results
        print(f"{player1_name}: {player1_total}")  # Print Player 1's total
        print(f"{player2_name}: {player2_total}")  # Print Player 2's total
        print(f"Dealer: {dealer_total}")  # Print Dealer's total
        
        # Determine winners and update scores based on game rules
        if (player1_total > 21 and player2_total > 21) or (dealer_total <= 21 and dealer_total >= max(player1_total, player2_total)):
            print(f"Dealer wins this round!")  # Dealer wins
            player1_score -= 1  # Decrease Player 1's score
            player2_score -= 1  # Decrease Player 2's score
        else:
            if player1_total <= 21:
                print(f"{player1_name} wins this round!")  # Player 1 wins
                player1_score += 1  # Increase Player 1's score
            if player2_total <= 21:
                print(f"{player2_name} wins this round!")  # Player 2 wins
                player2_score += 1  # Increase Player 2's score
        
        print(f"\nCurrent score:")  # Print current score
        print(f"{player1_name}: {player1_score}")  # Print Player 1's current score
        print(f"{player2_name}: {player2_score}")  # Print Player 2's current score
        
        # Check if players want to continue playing another round
        if input("Do you want to play another round? (y/n): ").lower() != 'y':
            break  # Exit loop if players do not want to play another round
    
    # Game over, display final score table
    print("\n===== Game Over =====")
    print("Final score table:")
    scores = {player1_name: player1_score, player2_name: player2_score, "Dealer": 0}  # Final scores including Dealer
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)  # Sort scores descending
    for player, score in sorted_scores:
        print(f"{player}: {score}")  # Print each player's final score

# Start the game by calling the main function
play_blackjack()