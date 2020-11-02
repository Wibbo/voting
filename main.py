from election import election


choices = ['Salad', 'Burger', 'Pizza', 'Curry', 'Pasta', 'BLT']

campaign = election(300, choices)  


print('NEW ELECTION')
print(f'Number of voters is {campaign.voter_count}')
print(campaign.vote_counts)


