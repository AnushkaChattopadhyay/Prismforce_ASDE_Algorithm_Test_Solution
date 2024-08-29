# Function to check if Abhimanyu can cross the Chakravyuha and reach the Pandavas or not
def can_reach_pandavas(enemy_powers, enemy, cur_power, behind, skips, recharge, initial_power):

    # All the 11 enemies are defeated
    if enemy==last_circle:
        return True

    flag = False

    # Perform recharge if still permitted and helps to defeat the enemy
    if recharge > 0 and cur_power < initial_power:
        flag |= can_reach_pandavas(enemy_powers, enemy, initial_power, behind, skips, recharge - 1, initial_power)

    # Check if Abhimanyu can defeat the enemy attacking from behind and decrement the power in accordance
    if cur_power >= behind:
        cur_power -= behind
        behind = 0
    else:
        return False

    # Perform skipping this enemy if skips are permitted
    if skips > 0:
        flag |= can_reach_pandavas(enemy_powers, enemy + 1, cur_power, behind, skips - 1, recharge, initial_power)

    # Fight the current enemy and decrement the power in accordance
    if cur_power >= enemy_powers[enemy]:
        if enemy == 2 or enemy == 6:
            behind = enemy_powers[enemy] // 2

        flag |= can_reach_pandavas(enemy_powers, enemy + 1, cur_power - enemy_powers[enemy], behind, skips, recharge, initial_power)

    return flag

# Total number of circles in the Chakravyuha to cross
last_circle = 11  
'''
#Parameters taken from user
enemy_powers = list(map(int, input().split()))
power = int(input())
a = int(input())  # Number of skips permitted
b = int(input())  # Number of recharges permitted
a = min(a,last_circle)  # Restrict the maximum skips to the total number of enemies (11)
b = min(b,last_circle)  # Restrict the maximum recharges to the total number of enemies (11)

behind = 0  # Power of regenerated enemy to attack from behind.
'''


enemy_powers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
power = 300
a = 2 
b = 1
a = min(a,last_circle)  # Restrict the maximum skips to the total number of enemies (11)
b = min(b,last_circle)  # Restrict the maximum recharges to the total number of enemies (11)

behind = 0

# Result Generation
if can_reach_pandavas(enemy_powers, 0, power, behind, a, b, power):
    print("Abhimanyu can cross the Chakrvyuha")
else:
    print("Abhimanyu cannot cross the Chakrvyuha")



'''
Test case: 1 

enemy_powers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
power = 300
a = 2 
b = 1
Result: Abhimanyu can cross the Chakrvyuha

Test case: 2

enemy_powers =[10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
power = 250
a = 2
b = 1
Answer: Abhimanyu cannot cross the Chakrvyuha

'''


