# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
#This assignment is about the European football final in 1988
from types import ClassMethodDescriptorType


scorer_one='Ruud Gullit'
scorer_two='Marco van Basten'
goal_0 = 32
goal_1 = 54
#print the names from the footballer that scored in the final and in which minute of the match they scored
scorers=scorer_one+ " " +str(goal_0)+ ", " +scorer_two + " "+str(goal_1)
print(scorers)
report=f'{scorer_one} scored in the {goal_0}nd minute\n{scorer_two} scored in the {goal_1}th minute'
print(report)
#Choose a player that played in the final
player="Rene van der Gijp"
#print his first name
first_name = player [:player.find(" ")]
print(first_name)
#How many characters contains the last name of this player
last_name = player [player.find(" ")+1:]
last_name_len=len(last_name)
print(last_name_len)
#Print the initials and last name of the player
name_short= f'{player[:1]}.{player[player.find(" "):]}'
print(name_short)
first_name_len=len(first_name)
print(first_name_len)
#Print the first name of the player followed by a "!" as many times as his first name contains letters
chant_one_time=first_name + "!"
chant_how_many_times=len(first_name)
print(chant_one_time)
print(chant_how_many_times)
chant_met_spatie =(chant_one_time + " ")*chant_how_many_times
print(chant_met_spatie)
chant = (chant_met_spatie[ :chant_met_spatie.find("[-1] ")])
print(chant)
good_chant = chant[-1] != " "
print(good_chant)