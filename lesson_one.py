
def compare_two_numbers(numberOne, numberTwo):
    if numberOne > numberTwo:
        return numberOne
    else:
        return numberTwo

# print(compare_two_numbers(numberOne=7, numberTwo=5))

def check_year(year):
    if year % 100 == 0 and year % 400 != 0:
        return "No"
    if year % 4 == 0:
        return "Yes"
    return "No"

print(check_year(360))

# def check_year(year):
#     if not (year % 400):
#         return "Yes"
#     if not (year % 4):
#         return "Yes"
#     return "No"
# print(check_year(2001))

def rook_attack(rook_coordinates, target_coordinates):
    if (rook_coordinates[0] == target_coordinates[0]) or (rook_coordinates[1] == target_coordinates[1]):
        return "Yes"
    else:
        return "No"

# print(rook_attack("G5","B5"))

def icecream(number_of_balls):
    if number_of_balls == 3 or number_of_balls == 5:
        return "Yes"
    else:
        return "No"
#
# print(icecream(7))