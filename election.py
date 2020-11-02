from voter import voter
from collections import defaultdict

class election:

    def __init__(self, voter_count, options):
        self.voter_count = voter_count  
        self.options = options  # The options to choose from.
        self.rule = None
        self.voters = []  # Each voter os stored here. 

        id = 0 
        self.vote_counts = []  # Dictionary stores the total votes for each choice. 
        
        # Process all voters.
        for v in range(self.voter_count):
            # Create a new voter and add to the voters list.
            new_voter = voter(id, self.options)
            self.voters.append(new_voter)






            # The voters choices are in order of preference.
            # Add up all the first choice votes.
            choice = self.voters[v].options[0]
            if choice in self.vote_counts:
                self.vote_counts[choice] += 1   
            else:
                self.vote_counts[choice] = 1
            
            id += 1

        highest_vote = 0
        self.winning_choice = ''
        self.winning_count = 0


        for choice in sorted(self.vote_counts, key=self.vote_counts.get, reverse=True): 
            self.winning_choice = 
            print(choice, self.vote_counts[choice])


    