"""
work4 -- display_requisition
Author: Shantanu Thakur
"""

from work_3 import requisition_approval
from work_1 import staff_info

def display_requisition(date, staff_name, staff_id, requisition_id, total_price, status, approval_reference_number):
#    info=staff_info()

    print("\n---Printing Requisition Details:---")
    print(f"Date: {date}")
    print(f"Requisition ID: {requisition_id}")
    print(f"Staff ID: {staff_id}")
    print(f"Staff Name: {staff_name}")
    print(f"Total: ${total_price:.2f}")
    print(f"Status: {status}")
    print(f"Approval Reference Number: {approval_reference_number}")
    print("-" * 30)

def main():
    # Personal staff information is to be collected at the start
    date, staff_id, staff_name, requisition_id = staff_info()

    # requisition approval details needs to show approve 
    total_price, status, approval_reference_number = requisition_approval(staff_id, requisition_id)

    # Needs to display final requisistion details
    display_requisition(date, staff_name, staff_id, requisition_id, total_price, status, approval_reference_number)

if __name__ == "__main__":
    main()
