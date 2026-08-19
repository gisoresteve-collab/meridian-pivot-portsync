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

# Ask the auditor for the container number
container_no = input("Enter Container No.: ")

print()
print("Container selected:", container_no)

# Yard inventory
inventory = {
    "STJU1234567": "SQ 32 F 1",
    "BSJU2345123": "SL 41 C 3",
    "GSNU7823456": "SR 24 A 1"
}

# Check whether container exists
if container_no in inventory:

    print("Container found in yard inventory.")

    # Get expected allocation
    allocation = inventory[container_no]
    print("Expected Allocation:", allocation)

    # Ask auditor for actual allocation
    actual_allocation = input("Enter Actual Allocation: ")

    print()
    print("Actual Allocation:", actual_allocation)

    # Compare expected and actual allocation
    if allocation == actual_allocation:
        print("Position match")
    else:
        print("Position mismatch")

else:

    print("Container not found in yard inventory.")