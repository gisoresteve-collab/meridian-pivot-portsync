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


# ========================================
# YARD INVENTORY
# ========================================

yard_inventory = {
    "STJU1234567": "SQ 32 F 1",
    "BSJU2345123": "SL 41 C 3",
    "GSNU7823456": "SR 24 A 1"
}


# ========================================
# OPERATIONS INVENTORY
# ========================================

operations_inventory = {
    "STJU1234567": "SQ 32 F 1",
    "BSJU2345123": "SQ 41 C 3",
    "GSNU7823456": "SR 24 A 1"
}


# ========================================
# 1. CONTAINER AUDIT
# ========================================

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


# ========================================
# 2. COMPARE INVENTORIES
# ========================================

def compare_inventories():

    print()
    print("=" * 40)
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

            print(
                "Container requiring synchronization:",
                container_no
            )

    else:

        print("No discrepancies found.")

    return discrepancies


# ========================================
# 3. SYNCHRONIZE INVENTORIES
# ========================================

def synchronize_inventory(discrepancies):

    print()
    print("=" * 40)
    print("INVENTORY SYNCHRONIZATION")
    print("=" * 40)

    synchronized_containers = []

    for container_no in discrepancies:

        old_position = yard_inventory[container_no]

        new_position = operations_inventory[container_no]

        print()
        print("Synchronizing:", container_no)

        print("Old Yard Position:", old_position)

        print("Operations Position:", new_position)

        # Update yard inventory
        yard_inventory[container_no] = new_position

        synchronized_containers.append({
            "container": container_no,
            "old_position": old_position,
            "new_position": new_position
        })

        print(
            "New Yard Position:",
            yard_inventory[container_no]
        )

        print("Synchronization complete.")

    return synchronized_containers


# ========================================
# 4. VERIFY SYNCHRONIZATION
# ========================================

def verify_synchronization():

    print()
    print("=" * 40)
    print("SYNC VERIFICATION")
    print("=" * 40)

    for container_no in yard_inventory:

        yard_position = yard_inventory[container_no]

        operations_position = operations_inventory[container_no]

        if yard_position == operations_position:

            print(container_no, ": MATCH")

        else:

            print(container_no, ": STILL MISMATCH")


# ========================================
# 5. GENERATE SYNC REPORT
# ========================================

def generate_sync_report(synchronized_containers):

    print()
    print("=" * 40)
    print("          PORTSYNC SYNC REPORT")
    print("=" * 40)

    total_containers = len(yard_inventory)

    synchronized = len(synchronized_containers)

    print()
    print("Containers Checked:", total_containers)

    print("Containers Synchronized:", synchronized)

    print()
    print("----------------------------------------")
    print("SYNCHRONIZED CONTAINERS")
    print("----------------------------------------")

    if synchronized_containers:

        for record in synchronized_containers:

            print()
            print("Container:", record["container"])

            print("Old Position:", record["old_position"])

            print("New Position:", record["new_position"])

    else:

        print("No containers required synchronization.")

    print()
    print("----------------------------------------")
    print("SYNC STATUS")
    print("----------------------------------------")

    print("SUCCESS - Synchronization completed.")


# ========================================
# PORTSYNC PROGRAM FLOW
# ========================================

# Step 1: Audit a container
check_container()

# Step 2: Compare the two inventories
discrepancies = compare_inventories()

# Step 3: Synchronize discrepancies
synchronized_containers = synchronize_inventory(discrepancies)

# Step 4: Verify synchronization
verify_synchronization()

# Step 5: Generate final report
generate_sync_report(synchronized_containers)
