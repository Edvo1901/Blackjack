#
# File: part2_voyvy005.py
# Author: Dong (Edward) Vo
# Email Id: voyvy005@myemail.unisa.sa.edu
# Description: Assignment 2 (part 2) – You are required to write a Python program that will manage player information. The program will allow players to
# play blackjack (dice version) against the computer and will maintain information on players. Player information will be
# stored in a text file that will be read in when the program commences. Once the initial player information has been
# read in from the file, the program should allow the user to interactively query and manipulate the player information as
# well as play blackjack against the computer. Please ensure that you read sections titled 'Part II specification' below for
# further details.
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

import random
import blackjack


def display_details():
    print('File : part2_voyvy005.py'
          '\nAuthor : Dong Vo'
          '\nStud ID : 110322027'
          '\nEmail ID : voyvy005'
          '\nThis is my own work as defined by the University\'s Academic Misconduct Policy.')


def read_file(filename, player_list, score_list):
 
    # Open file for reading.
    infile = open(filename, "r")

    # Read first line of file.
    line = infile.readline()

    # While not end of file reached i.e. empty string not returned from readline method.
    while line != '':

        # Get name - remove new line character        
        name = line.strip('\n')
        
        # Read in next line
        line = infile.readline()
        
        # Get score - remove new line character and convert to integer
        score = int(line.strip('\n'))

        # Add name to player_list
        player_list.append(name)

        # Add score to score_list
        score_list.append(score)
        
        # Read next line of file.
        line = infile.readline()

    infile.close()
    return {'player_list':player_list,'score_list':score_list}

# Make a function display_players() to display player information
def display_players(player_list, score_list):

    # This line will eventually be removed - used for development purposes only.
    print("In function display_players()")

    # Place your code here
    print('====================================')
    print('         - Player Summary -          ')
    print('====================================')
    print('- Name                       Score -')
    print('------------------------------------')

    # Display data using loop
    for i,j in zip(player_list,score_list):
        print('{}   \t\t\t   {}'.format(i,j))


# Make a function write_to_file() to show score
def write_to_file(filename, player_list, score_list):

    # opeing file
    file_obj = open(filename,'w')
    for i,j in zip(player_list,score_list):

        # appending  player name
        file_obj.write(i+'\n')

        # appending score
        file_obj.write(str(j)+'\n')

    return True


def search(Mylist,search_Name):

    # check if search name is in playerlist
    for i,j in zip(Mylist['player_list'],Mylist['score_list']):
        if search_Name == i:
            return i,j
    return -1

def reset(playerlist,scorelist,searchname):

    # check if search name is in playerlist
    for i in range(len(playerlist)):
        if playerlist[i] == searchname:

            # convert to zero
            scorelist[i] = 0

    return {'player_list':playerlist,'score_list':scorelist}

def add_data(playerlist,scorelist,searchname):

    # search element exist then return -1
    if searchname in playerlist:
        return -1

    #  search element appending to playerist
    playerlist.append(searchname)

    #  zero appending to scorelist
    scorelist.append(0)

    return {'player_list':playerlist,'score_list':scorelist}

def remove_data(playerlist,scorelist,searchname):

    # search name checking in player list
    if searchname not in playerlist:

        # not exist then return true
        return -1

    player_list = []
    score_list = []

    # remove element by loop
    for i in range(len(playerlist)):

        if playerlist[i] == searchname:
            pass

        else:
            # append data other than search element
            player_list.append(playerlist[i])
            score_list.append(scorelist[i])

    return {'player_list':player_list,'score_list':score_list}

# Make a function play_blackjack_games() to operate the game
def play_blackjack_games(player_list, score_list, playename,player_pos):

    # print("In function play_blackjack_games()")
    for i in range(len(player_list)):
        if player_list[i] == playename:
            score_list[i] = player_pos

    return {'player_list':player_list,'score_list':score_list}

display_details()

n=0

# loop till quiting enter in choice
while n == 0:

    ### Define player list to store player information
    player_list = []

    ### Define score list to store score information
    score_list = []


    print('\nPlease enter choice ')
    Choice_list = ['list', 'search', 'reset', 'add', 'remove', 'play', 'quit']

    # enter choice
    choice = input('[list, search, reset, add, remove, play, quit] : ')

    # invalid choice then print message
    if choice not in Choice_list:
        print('Not a valid command - please try again.')

    # list entered choice
    elif 'list' == choice:

        # read data from players.txt file
        read_obj = read_file('players.txt',player_list,score_list)
        display_players(read_obj['player_list'],read_obj['score_list'])

    elif 'search' == choice:
        # enter search name
        search_name = input('Please enter name:')

        # read data from players.txt file
        read_obj = read_file('players.txt',player_list,score_list)

        # checking data from search function
        res = search(read_obj,search_name)
        if res == -1:
            print('{} is not found in player list.'.format(search_name))

        else:
            print('{} current score: {}'.format(res[0],res[1]))

    elif 'reset' == choice:
        # enter reset name
        search_name = input('Please enter name:')

        # read data from players.txt file
        read_obj = read_file('players.txt',player_list,score_list)

        # zero for entered name
        reset_obj = reset(read_obj['player_list'],read_obj['score_list'],search_name)

        if reset_obj == -1:
            print('{}  is not found in player list.'.format(search_name))

        else:
            write_to_file('players.txt',reset_obj['player_list'],reset_obj['score_list'])
            print('Successfully reset {}'.format(search_name),' score to 0')

    elif 'add' == choice:
        # name to add to list
        add_element = input('Please enter name : ')

        # read data from players.txt file
        read_obj = read_file('players.txt',player_list,score_list)

        # add_data to the list
        add_obj = add_data(read_obj['player_list'],read_obj['score_list'],add_element)

        if add_obj == -1:
            print('{} already exists in player list.'.format(add_element))

        else:
            # append data to file
            write_to_file('players.txt',add_obj['player_list'],add_obj['score_list'])
            print('Successfully added {}'.format(add_element))

    # Enter remove name
    elif 'remove' == choice:
        remove_name = input('Please enter name:')

        # read data from players.txt file
        read_obj = read_file('players.txt',player_list,score_list)

        # remove data from the list
        remove_obj = remove_data(read_obj['player_list'],read_obj['score_list'],remove_name)

        if remove_obj == -1:
            print('{}  is not found in player list.'.format(remove_name))

        # append new data to file
        else:
            write_to_file('players.txt',remove_obj['player_list'],remove_obj['score_list'])
            print('Successfully removed {}'.format(remove_name))

    elif 'play' == choice:
        player_name = input("Please enter player's name: ")

        # read data from players.txt file
        play_obj = read_file('players.txt',player_list,score_list)

        # player not exist then display error
        if player_name not in play_obj['player_list']:
            print('Please try again ')

        else:
            m = 'y'

            # continue loop till enter N,n
            while m == 'y':
                score = blackjack.play_one_game()

                # append new score to file
                game_obj = play_blackjack_games(play_obj['player_list'],play_obj['score_list'], player_name,score)

                # new data adding to players.txt file
                write_to_file('players.txt',game_obj['player_list'],game_obj['score_list'])

                while True:
                    input_data = input('Play again [y|n]? ')

                    # input y or Y then continue loop
                    if input_data == 'y' or input_data == 'Y':
                        m = 'y'
                        break

                    # input n or N to exit the game
                    elif input_data == 'n' or input_data == 'N':
                        m = 'n'
                        break

                    else:
                        print('please enter Y or N')

    elif 'quit' == choice:

        # exiting from the loop
        print("\n\n-- Program terminating --\n")
        n=1




