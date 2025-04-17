"""
Task1 -- requisitionsystem(class)
Author: Shantanu Thakur

"""


#Creating requistionsystem class 

class requisition_system:

    #Class level counters - DRY principle applied and utilized throughout the class system
    count = 10000
    total_submitted = 0
    total_approved = 0
    total_pending = 0
    total_not_approved = 0

    def __init__(self):   # self
        # KISS - Beginning is readable and simple to understand
        self.date = ""
        self.staff_id = ""
        self.staff_name = ""
        self.requisition_id = None
        self.total_price = 0.0
        self.status = "Pending"
        self.approval_reference_number = "No"

    def staff_info(self):   # Main Information
        # Collects staff info mostly - Single Responsibility
        #Able to handles both input & output, violates the delineation of priorities - Can be improved
        print("\n--- Staff Information ---")


        while True:   # while loop
            self.date = input("Enter Date (DD-MM-YYYY): ")
            self.staff_id = input("Enter Staff ID: ")
            self.staff_name = input("Enter Staff Name: ")
            
            
            requisition_system.count += 1
            self.requisition_id = requisition_system.count

            requisition_system.total_submitted += 1
            requisition_system.total_pending += 1

            more_entries = input("Do you want to add more entries? (yes/no): ")
            if more_entries.lower() != 'yes':  #this one shows entries on function according to lower
                break
            else:
                #KISS - the output is straightforward and clear

                print(f"\nPrinting Staff Information:")
                print(f"Date: {self.date}")
                print(f"Staff ID: {self.staff_id}")
                print(f"Staff Name: {self.staff_name}")
                print(f"Requisition ID: {self.requisition_id}\n")

        


    def requisitions_total(self):
        self.total_price = 0.0
        while True:   # while loop
            item_name = input("Enter the required item name (or type 'stop' when its done): ")
            if item_name.lower() == 'stop':  # Using this if staff member wants to stop the item list
                break
            else:
                item_price = float(input(f"Enter the price of {item_name}: $"))
                self.total_price += item_price
        else:
            print("Invalid input. Please enter a valid price.")
        # KISS - Keeps the cost calculation logically simple
        print(f"Total Requisition Cost: ${self.total_price:.2f}")

    def requisition_approval(self):
        # Open/ Closed - the logic cannot be stretched without modification
        if self.total_price < 500:
            self.status = "Approved"
            self.approval_reference_number = f"{self.staff_id}{str(self.requisition_id)[-3:]}"
            requisition_system.total_approved += 1
            requisition_system.total_pending -= 1
        else:
            self.status = "Pending"
            self.approval_reference_number = "No"


        print("\nRequisition Approval Details:")
        print("-" * 30)
        print(f"Total: ${self.total_price:.2f}")
        print(f"Status: {self.status}")
        print(f"Approval Reference Number: {self.approval_reference_number}")
        print(f"Staff Reference: {self.requisition_id}\n")    

    def respond_requisition(self):
        # YAGNI - it may be unneeded if approvals are handled
        if self.status == "Pending":
            print(f"\nResponding to Requisition ID {self.requisition_id}")
            decision = input("Enter your decision here (Approve / Pending / Not Approve ): ").strip().lower()

            if decision == "approve":
                self.status = "Approved"
                self.approval_reference_number = f"{self.staff_id}{str(self.requisition_id)[-3:]}"

                requisition_system.total_approved += 1
                requisition_system.total_pending -= 1

            elif decision == "not approve":
                self.status = "Not Approved"
                self.approval_reference_number = "No"
                
                requisition_system.total_not_approved += 1
                requisition_system.total_pending -= 1
            else:
                print("No changes are made in here.")
        # Single Responsibility - update + logic + decision in one

    def display_requisition(self):
        # KISS - formatting for output is simple
        print("\n---Printing Requisition Details:---")
        print(f"Date: {self.date}")
        print(f"Requisition ID: {self.requisition_id}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Staff Name: {self.staff_name}")
        print(f"Total: ${self.total_price:.2f}")
        print(f"Status: {self.status}")
        print(f"Approval Reference Number: {self.approval_reference_number}")
        print("-" * 30)

    def display_statistics(self):
        print("\n=== Displaying the Requisition Statistics: ===")
        print(f"Total Requisitions Submitted: {self.total_submitted}")
        print(f"Total Approved Requisitions: {self.total_approved}")
        print(f"Total Pending Requisitions: {self.total_pending}")
        print(f"Total Not Approved Requisitions: {self.total_not_approved}")
        print("=" * 30)


# === Main Statistics Program ===

requisition_id = []  #Changing this value in both class and work_1 from {} to [] for clear values on Statistics
# DRY - For storing multiple requisitions list is reused
while True:  # while loop
    reply = input("\nDo you want to create a new requisition? (yes/exit): ").strip().lower()
    if reply == "exit":
        break
    elif reply == "yes":
        requ = requisition_system()
        requ.staff_info()
        requ.requisitions_total()
        requ.requisition_approval() 
        requ.respond_requisition()
        requ.display_requisition()
        requisition_id.append(requ)
    else:
        print("Invalid input. Please enter 'yes' to continue forward or enter 'exit' to end.")

# Show the Statistics Output at the end
if requisition_id:
    requisition_id[0].display_statistics()
else:
    print("\nNo requisitions were submitted in here.")

# Finished
