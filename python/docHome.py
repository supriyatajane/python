#define  a function to print the player name and scores and
#then prints the highest score in next line  
#use **kwargs as parameter in the function
#use below data as input while calling the function:

dict_data = {
    'player1': [12,28,32,84,53],
    'player2': [12,28,3,94,35],
    'player3': [13,22,83,42,100],
    'player4': [12,22,33,4,85]
}


def players(**kwargs):
    for key,value in kwargs.items():
        print('The scores of',key,'are', value)
        print('Highest score by',key,'is:',max(value))

players(**dict_data)


