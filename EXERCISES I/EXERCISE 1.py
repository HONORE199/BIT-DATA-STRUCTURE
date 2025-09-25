# ------------------------------
# Blood Donation Camp Mini Project
# ------------------------------

import array

# === INTEGERS ===
# Number of donors in different sessions
donors = [45, 60, 38, 52, 70]

total_donors = sum(donors)
average_donors = total_donors / len(donors)
min_donors = min(donors)
max_donors = max(donors)

print("=== Integers ===")
print("Donors data:", donors)
print(f"Total Donors: {total_donors}")
print(f"Average Donors: {average_donors:.2f}")
print(f"Minimum Donors in a session: {min_donors}")
print(f"Maximum Donors in a session: {max_donors}")
print()

# === STRINGS (Formatted Report) ===
print("=== Strings ===")
report = (
    f"Blood Donation Camp Report:\n"
    f"- Total donors: {total_donors}\n"
    f"- Average donors per session: {average_donors:.2f}\n"
    f"- Range: {min_donors} to {max_donors}\n"
)
print(report)

# === BOOLEANS (Threshold Condition) ===
print("=== Booleans ===")
threshold = 50
if average_donors > threshold and max_donors > 65:
    print("Status: Above Standard ✅")
else:
    print("Status: Below Standard ❌")
print()

# === LISTS ===
print("=== Lists ===")
camp_items = ["Bags", "Needles", "Gloves", "Forms", "Snacks"]
print("Before modifications:", camp_items)

# Add new item
camp_items.append("Water Bottles")
# Remove one item based on a condition (remove 'Forms' if present)
if "Forms" in camp_items:
    camp_items.remove("Forms")
# Sort list
camp_items.sort()

print("After modifications:", camp_items)
print()

# === ARRAYS ===
print("=== Arrays ===")
donor_array = array.array('i', [45, 60, 38, 52, 70])
array_sum = sum(donor_array)
list_sum = sum(donors)

print("Array:", donor_array.tolist())
print("Sum using array:", array_sum)
print("Sum using list:", list_sum)
print("Comparison:", "Equal" if array_sum == list_sum else "Not Equal")
print()

# === DICTIONARIES ===
print("=== Dictionaries ===")
records = [
    {"id": 1, "name": "John", "value": 2},  # 2 pints donated
    {"id": 2, "name": "Mary", "value": 1},
    {"id": 3, "name": "Ali", "value": 3},
    {"id": 4, "name": "Grace", "value": 2},
]

# Update Ali’s record
for rec in records:
    if rec["id"] == 3:
        rec["value"] = 4  # updated donation

# Delete Mary’s record
records = [rec for rec in records if rec["id"] != 2]

# Compute total donations
total_value = sum(rec["value"] for rec in records)

print("Updated Records:", records)
print("Total Pints of Blood Collected:", total_value)

