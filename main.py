import random
from game_data import data
from art import logo, vs

# generate player info from a dictionary
def get_details(dict):
    for info in dict:
        name = dict['name']
        # followers = dict['follower_countA']
        description = dict['description']
        country = dict['country']
    return (f"{name.title()}, a {description.title()}, from {country.title()}")
    
#Use generated data to get followers info
def followers(data):
    for key in data:
        followers = data['follower_count']
    return followers



def play_game():
    print(logo)    
    player_1 = random.choice(data)
    
    score = 0
    end_loop = False
    while end_loop == False:
        #Generating players

        player_2 = random.choice(data)
        if player_1 == player_2:
            player_2 = random.choice(data)

        #Player_1 details and followers
        player_1_details = get_details(player_1)
        player_1_followers = followers(player_1)
        #player_2 details and followers
        player_2_details = get_details(player_2)
        player_2_followers = followers(player_2)
        print(f"Compare A: {player_1_details}.")
        print(vs)
        print(f"Against B: {player_2_details}.")
        
        #A list for comparing values        
        compare = []
        compare.append(player_1_followers)
        compare.append(player_2_followers)
        
        #Variable for storing number of highest followers
        highest = 0
        for digit in compare:
            if digit > highest:
                highest = digit
  
        prompt = input("Who has more followers? Type 'A' or 'B: ")
            
        if prompt == 'A' and (player_1_followers == highest):
            score += 1
            print(f"You're right! Current score: {score}")
            player_1 = player_2
            
        elif prompt == 'A' and (player_1_followers != highest):
            end_loop = True
            print(f"Sorry, that's wrong. Final score: {score}")
            
        elif prompt == 'B' and (player_2_followers == highest):
            score += 1
            print(f"You're right! Current score: {score}")
            player_1 = player_2
            
        elif prompt == 'B' and (player_2_followers != highest):
            end_loop = True
            print(f"Sorry, that's wrong. Final score: {score}")
        
        else:
            end_loop = True
            print(f"Sorry, that's a wrong input. Final score: {score}")
          
play_game()