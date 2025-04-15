"""
work2 -- requisitions_total
Author: Shantanu Thakur
"""
from work_1 import staff_info
def requisitions_total():
    total_price = 0.0

    while True:
        item_name = input("Enter the required item name (or type 'stop' when its done): ")
        if item_name.lower() == 'stop':  # Using this if staff member wants to stop the item list
            break

        else:
            item_price = float(input(f"Enter the price of {item_name}: $"))
            total_price += item_price  

    else: 
        print("Invalid input. Please enter a valid price.")

    print(f"\nTotal Requisition Cost: ${total_price:.2f}")
    
    return total_price  # Returning the total value data to here only

