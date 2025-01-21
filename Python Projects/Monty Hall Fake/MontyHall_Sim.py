import random

#   Function Name: remove_until_n_elements_but_not
#   Description: Remove n random elements from a list but preventing specified elements from being removed
#   Arguments:
#       list - the list to be removed from
#       n - the amount of numbers to be removed
#       safe - the list of values that should be saved / should be prevented from being removed
#   
#   Example:
#   Remove 5 random elements from [1,2,3,4,5,6,7,8], but keep [3,7] safe
#   -> [1,3,7]
def remove_until_n_elements_but_not(list=[1,2,3], safe=[1,2], n=2):
    while len(list) >n:
        to_remove = random.choice(list)
        if to_remove in safe:
            continue
        list.remove(to_remove)
    
    return list

def conduct_monty_hall(sample_size, no_of_doors):

    # Do not change unless u know what u doing
    no_of_success = 0   # Counts number of correct guesses after swapping
    no_of_fail = 0      # Counts number of wrong guesses after swapping
    list_choice = []    # Stores all the first choices (before the reveal)
    list_actual = []    # Stores all the cars

    for i in range(sample_size):

        doors = [i for i in range(1, no_of_doors+1)]

        # generate the first choice
        curr_choice = random.choice(doors)
        list_choice.append(curr_choice)

        # generate the car
        curr_actual = random.choice(doors)
        list_actual.append(curr_actual)

        # reveal goats (remove doors until only 2 choices, ensuring that the car and the original choice were both selected)
        remaining_doors = remove_until_n_elements_but_not(list=doors, safe=[curr_choice, curr_actual], n=2)

        # swap the choice
        if curr_choice == remaining_doors[0]:
            final_choice = remaining_doors[1]
        else:
            final_choice = remaining_doors[0]

        # update success/fail count  
        if final_choice == curr_actual:
            no_of_success+=1
        else:
            no_of_fail+=1

    # calculate win rate
    win_rate = no_of_success/sample_size

    return {"sample_size":sample_size, "no_of_doors":no_of_doors, "success":no_of_success, "fail":no_of_fail, "choices":list_choice, "actual":list_actual, "win_rate":win_rate}


def display(stat, bool_print_choices=False, bool_print_actual=False):
    print("Results of the Monty Hall Simulation")
    print(f"Sample size: {stat['sample_size']}")
    print(f"No. of Doors: {stat['no_of_doors']}")
    print(f"Successes: {stat['success']}")
    print(f"Fails: {stat['fail']}")
    print(f"Win Rate: {stat['win_rate']}")

    if bool_print_choices:
        print(f"List of first choices: {stat.choices}")
    if bool_print_actual:
        print(f"List of correct door (car door): {stat.list_actual}")



if __name__ == "__main__":
    # Change if you want
    sample_size = 100000
    no_of_doors = 5       
    print_first_choices =   False   # Can set to True
    print_correct_choices = False   # Can set to True

    # Do not change
    statistics = conduct_monty_hall(sample_size=sample_size, no_of_doors=no_of_doors)

    display(statistics, print_first_choices, print_correct_choices)
    