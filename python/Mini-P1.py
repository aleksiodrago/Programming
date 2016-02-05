# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    if(name=="Spock"):
        n=1
        return n
    elif(name=="rock"):
        n=0
        return n
    elif(name=="paper"):
        n=2
        return n
    elif(name=="lizard"):
        n=3
        return n
    elif(name=="scissors"):
        n=4
        return n





def number_to_name(number):
    if(number==0):
        n="rock"
        return n
    elif(number==1):
        n="Spock"
        return n
    elif(number==2):
        n="paper"
        return n
    elif(number==3):
        n= "lizard"
        return n
    elif(number==4):
        n="scissors"
        return n


def rpsls(player_choice):
    print "\n"
    print "The Player picked ", player_choice
    player_number = name_to_number(player_choice)
    comp_number= round(random.randrange(0,4))
    comp_choice=number_to_name(comp_number)
    print "The computer chose ", comp_choice
    result = (comp_number-player_number) %5
    if(result==1):
        print "Computer Wins!"
    elif(result==2):
        print "Player Wins!"
    elif(result==0):
        print "Its a TIE!"

    # ✓print a blank line to separate consecutive games

    # ✓print out the message for the player's choice

    # ✓convert the player's choice to player_number using the function name_to_number()

    # ✓compute random guess for comp_number using random.randrange()

    # ✓convert comp_number to comp_choice using the function number_to_name()

    # ✓print out the message for computer's choice

    # ✓compute difference of comp_number and player_number modulo five

    # use if/elif/else to determine winner, print winner message


# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

# print name_to_number("Spock")
# print name_to_number("rock")
# print name_to_number("paper")
# print name_to_number("lizard")
# print name_to_number("scissors")
# print number_to_name(0)
# print number_to_name(1)
# print number_to_name(2)
# print number_to_name(3)
# print number_to_name(4)
