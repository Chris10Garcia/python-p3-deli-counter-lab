def line(line_list):
    if not len(line_list):
        print("The line is currently empty.")
        # return "The line is currently empty.\n"
    else:
        print("The line is currently: " + " ".join(["{}. {}".format(index + 1, name) for index, name in enumerate(line_list)]))

KATZ_DELI = []
OTHER_DELI = ["Logan", "Avi", "Spencer"]
ANOTHER_DELI = ["Amanda", "Annette", "Ruchi", "Jason", "Logan", "Spencer", "Avi", "Joe", "Rachel", "Lindsey"]



def take_a_number(people_list, name):
    print (f"Welcome, {name}. You are number {len(people_list) + 1} in line.")
    people_list.append(name)
    return people_list

take_a_number(KATZ_DELI, "Ada")

def now_serving(people_list):
    if len(people_list) == 0:
        print("There is nobody waiting to be served!")
    else:
        print("Currently serving {}.".format(people_list.pop(0)))