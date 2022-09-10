"""
Write a program that creates a dictionary containing 
the U.S. states as keys and their capitals as values. 
(Use the Internet to get a list of the states and their capitals.)
The program should then randomly quiz the user by displaying 
the name of a state and asking the user to enter that state’s 
capital. The program should keep a count of the number of 
correct and incorrect responses.
"""
import random


def main():
    stateCapitals = usStates()  # dict object
    correctAnswer = 0

    print("U.S Capital Quiz")

    while True:
        # getting random state with it's capital
        state = random.choice(tuple(stateCapitals.keys()))
        capital = stateCapitals[state]
        print(capital)

        # remove randomly selected state from dictionery object
        del stateCapitals[state]
        # answer from user
        print()
        answer = input("What is the capital of " + state + "?")

        if capital.lower() == answer.lower():
            print("Correct")
            correctAnswer += 1
        else:
            print("Incorrect")
            print("\n Thank you for taking part. !!! You got",
                  correctAnswer, "right")
            break


def usStates():
    stateCapitals = {'Alabama': 'Montgomery',
                     'Alaska': 'Juneau',
                     'Arizona': 'Phoenix',
                     'Arkansas': 'Little Rock',
                     'California': 'Sacramento',
                     'Colorado': 'Denver',
                     'Connecticut': 'Hartford',
                     'Delaware': 'Dover',
                     'Florida': 'Tallahassee',
                     'Georgia': 'Atlanta',
                     'Hawaii': 'Honolulu',
                     'Idaho': 'Boise',
                     'Illinois': 'Springfield',
                     'Indiana': 'Indianapolis',
                     'Iowa': 'Des Moines',
                     'Kansas': 'Topeka',
                     'Kentucky': 'Frankfort',
                     'Louisiana': 'Baton Rouge',
                     'Maine': 'Augusta',
                     'Maryland': 'Annapolis',
                     'Massachusetts': 'Boston',
                     'Michigan': 'Lansing',
                     'Minnesota': 'Saint Paul',
                     'Mississippi': 'Jackson',
                     'Missouri': 'Jefferson City',
                     'Montana': 'Helena',
                     'Nebraska': 'Lincoln',
                     'Nevada': 'Carson City',
                     'New Hampshire': 'Concord',
                     'New Jersey': 'Trenton',
                     'New Mexico': 'Santa Fe',
                     'New York': 'Albany',
                     'North Carolina': 'Raleigh',
                     'North Dakota': 'Bismarck',
                     'Ohio': 'Columbus',
                     'Oklahoma': 'Oklahoma City',
                     'Oregon': 'Salem',
                     'Pennsylvania': 'Harrisburg',
                     'Rhode Island': 'Providence',
                     'South Carolina': 'Columbia',
                     'South Dakota': 'Pierre',
                     'Tennessee': 'Nashville',
                     'Texas': 'Austin',
                     'Utah': 'Salt Lake City',
                     'Vermont': 'Montpelier',
                     'Virginia': 'Richmond',
                     'Washington': 'Olympia',
                     'West Virginia': 'Charleston',
                     'Wisconsin': 'Madison',
                     'Wyoming': 'Cheyenne'}

    return stateCapitals


# call a method
main()
