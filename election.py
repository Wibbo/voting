from voter import voter

class election:

    def __init__(self, voter_count, options):
        self.voter_count = voter_count
        self.options = options
        self.rule = None
        self.voters = []

        id = 0 
        self.vote_counts = {}
        
        for v in range(self.voter_count):
            self.voters.append(voter(id, self.options))

            choice = self.voters[v].options[0]
            
            # Does the current vote exist in the dictionary?
            if choice in self.vote_counts:
                self.vote_counts[choice] += 1   
            else:
                self.vote_counts[choice] = 1
            
            id += 1

        highest_vote = 0
        self.winning_choice = ''
        self.winning_count = 0

        for key, value in self.vote_counts.items():
            if value >= highest_vote:
                highest_vote = value
                self.winning_choice = key
                self.winning_count = value

    