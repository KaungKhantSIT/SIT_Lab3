#Vars
total = 0
fails = 0

#Functions

#Input prompt, input validation, and return valid integer/"quit" signal
def get_valid_input():
    pass

#Calculates & returns running total 
def process_delivery(current_total, new_value):
    pass

#Takes delivery amt & returns tax
def calculate_tax(amount):
    pass

#Generate report of total units processed & failed entries
def generate_report(total_units, failed_attempts):
    pass

'''
while user.lower() != "quit":
    user = input("Enter stock quantity: ")
    try:
        if user.lower() == "quit":
            print("Total Units Processed:",stock)
            print("Number of Failed/Rejected Entries:",fails)
            break
        if int(user) >= 0:
            stock += int(user)
            print("Current Stock:",stock)
            if stock > 500:
                print("Alert: Total Inventory exceeds 500 units.")
                print("Total Units Processed:",stock)
                print("Number of Failed/Rejected Entries:",fails)
                break
        else:
            fails += 1
            print("Please enter a positive number.")
    except ValueError:
        fails += 1
        print("Please enter a number.")
'''