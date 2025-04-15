"""
work3 -- requisition_approval
Author: Shantanu Thakur
"""

from work_2 import requisitions_total

staff_id = "FN19" #As a reference
requisition_id = 10001  #As a reference

def requisition_approval(staff_id, requisition_id):
    
    # total price is obtained from requisitions_total() value
    total_price = requisitions_total()

    # If total value is showing more than 500, it is approvable
    if total_price < 500:
        status = "Approved"
        approval_reference_number = (f"{staff_id}{str(requisition_id)[-3:]}")

    else:
        status = "Pending"
        approval_reference_number = "No"  

    print("\nRequisition Approval Details:")
    print("-" * 30)
    print(f"Total: ${total_price:.2f}")
    print(f"Status: {status}")
    print(f"Approval Reference Number: {approval_reference_number}")
    print(f"Staff Reference: {requisition_id}\n")

    return total_price, status, approval_reference_number  #Returning the obtained data to here of requisition total