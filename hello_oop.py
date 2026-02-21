class Player:
    """
    Represents a player in the Rock, Paper, Scissors game.
    
    Attributes:
        name: The name of the player
        score: The current score of the player
    """
    
    def __init__(self, name):
        """
        Initialize a new player with a name and zero score.
        
        Args:
            name: The name of the player
        """
        self.name = name
        self.score = 0
    
    def get_choice(self):
        """
        Prompt the player to input their choice.
        
        Returns:
            The player's choice ('rock', 'paper', 'scissors', or 'quit')
        """
        while True:
            try:
                choice = input(f"{self.name} - Choose (rock/paper/scissors) or 'quit' to exit: ").lower()
                if choice in ['rock', 'paper', 'scissors', 'quit']:
                    return choice
                print("Invalid choice! Try again.")
            except KeyboardInterrupt:
                return 'quit'
    
    def add_score(self):
        """
        Increment the player's score by 1.
        """
        self.score += 1
    
    def display_score(self):
        """
        Get the player's score as a formatted string.
        
        Returns:
            A string showing the player's name and score
        """
        return f"{self.name}: {self.score}"


class Game:
    """
    Manages the Rock, Paper, Scissors game logic and flow.
    
    Attributes:
        player1: The first player
        player2: The second player
        valid_choices: List of valid game choices
        winning_conditions: Dictionary mapping winning combinations
    """
    
    def __init__(self, player1, player2):
        """
        Initialize a new game with two players.
        
        Args:
            player1: The first player object
            player2: The second player object
        """
        self.player1 = player1
        self.player2 = player2
        self.valid_choices = ['rock', 'paper', 'scissors']
        self.winning_conditions = {
            ('rock', 'scissors'): 'rock',
            ('paper', 'rock'): 'paper',
            ('scissors', 'paper'): 'scissors'
        }
    
    def determine_winner(self, choice1, choice2):
        """
        Determine the winner based on the players' choices.
        
        Args:
            choice1: The first player's choice
            choice2: The second player's choice
        
        Returns:
            The result of the round ('tie', 'player1', or 'player2')
        """
        if choice1 == choice2:
            return 'tie'
        
        if (choice1, choice2) in self.winning_conditions:
            return 'player1'
        else:
            return 'player2'
    
    def play_round(self):
        """
        Play a single round of the game.
        
        Returns:
            True to continue the game, False to exit
        """
        p1_choice = self.player1.get_choice()
        
        if p1_choice == 'quit':
            return False  # Exit game
        
        p2_choice = self.player2.get_choice()
        
        if p2_choice == 'quit':
            return False  # Exit game
        
        print(f"\n{self.player1.name} chose: {p1_choice}")
        print(f"{self.player2.name} chose: {p2_choice}")
        
        result = self.determine_winner(p1_choice, p2_choice)
        
        if result == 'tie':
            print("It's a tie!")
        elif result == 'player1':
            print(f"{self.player1.name} wins!")
            self.player1.add_score()
        else:
            print(f"{self.player2.name} wins!")
            self.player2.add_score()
        
        print(f"\nScore - {self.player1.display_score()} | {self.player2.display_score()}")
        return True  # Continue game
    
    def play(self):
        """
        Start and manage the game loop.
        """
        print("=" * 40)
        print("Welcome to Rock, Paper, Scissors!")
        print("=" * 40)
        
        try:
            while self.play_round():
                pass
        except KeyboardInterrupt:
            print("\n\nGame interrupted! Thanks for playing!")
        
        self.display_final_results()
    
    def display_final_results(self):
        """
        Display the final results and winner of the game.
        """
        print("\n" + "=" * 40)
        print(f"Final Score - {self.player1.display_score()} | {self.player2.display_score()}")
        
        if self.player1.score > self.player2.score:
            print(f"{self.player1.name} wins the game! 🎉")
        elif self.player2.score > self.player1.score:
            print(f"{self.player2.name} wins the game! 🎉")
        else:
            print("It's a draw! 🤝")
        print("=" * 40)


if __name__ == "__main__":
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    game = Game(player1, player2)
    game.play()
