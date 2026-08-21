print("PORTSYNC")
print("NORTHSTAR RETAIL")
print("=" * 38)
print("Inventory first trial")
print("=" * 39)

print("Container NO.   ALLOCATION      SIZE")
print("STJU1234567     SQ 32 F 1       40FT")
print("BSJU2345123     SL 41 C 3       20FT")
print("GSNU7823456     SR 24 A 1       45FT")

print("=" * 40)
print("         YARD AUDIT")
print("=" * 40)


# Yard inventory
yard_inventory = {
    "STJU1234567": "SQ 32 F 1",
    "BSJU2345123": "SL 41 C 3",
    "GSNU7823456": "SR 24 A 1"
}

#OPERATIONAL INVENTORY
operations_inventory = {
    "STJU1234567": "SQ 32 F 1",
    "BSJU2345123": "SQ 41 C 3",
    "GSNU7823456": "SR 24 A 1"
}

# Check and audit a container
def check_container():

    container_no = input("Enter Container No.: ")

    print()
    print("Container selected:", container_no)

    if container_no in yard_inventory:

        print("Container found in yard inventory.")

        allocation = yard_inventory[container_no]

        print("Expected Allocation:", allocation)

        actual_allocation = input("Enter Actual Allocation: ")

        print()
        print("Actual Allocation:", actual_allocation)

        if allocation == actual_allocation:
            print("Position match")
        else:
            print("Position mismatch")

    else:

        print("Container not found in yard inventory.")


# Run the container audit
check_container()

#inventories comparison
def compare_inventories():

    print()
    print("INVENTORY COMPARISON")
    print("=" * 40)

    discrepancies = []

    for container_no in yard_inventory:

        yard_position = yard_inventory[container_no]
        operations_position = operations_inventory[container_no]

        print()
        print("Container:", container_no)
        print("Yard Position:", yard_position)
        print("Operations Position:", operations_position)

        if yard_position == operations_position:

            print("Status: MATCH")

        else:

            print("Status: MISMATCH")
            discrepancies.append(container_no)

    print()
    print("=" * 40)
    print("DISCREPANCIES FOUND")
    print("=" * 40)

    if discrepancies:

        for container_no in discrepancies:
            print("Container requiring synchronization:", container_no)

    else:

        print("No discrepancies found.")

    return discrepancies

def synchronize_inventory():

    print()
    print("=" * 40)
    print("INVENTORY SYNCHRONIZATION")
    print("=" * 40)

    for container_no in yard_inventory:

        yard_position = yard_inventory[container_no]
        operations_position = operations_inventory[container_no]

        if yard_position != operations_position:

            print()
            print("Synchronizing:", container_no)
            print("Old Yard Position:", yard_position)
            print("Operations Position:", operations_position)

            yard_inventory[container_no] = operations_position

            print("New Yard Position:", yard_inventory[container_no])
            print("Synchronization complete.")


synchronize_inventory()