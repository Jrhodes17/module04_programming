# week_lab.py
# Author: James Rhodes
# Business domain: Tech bro buy new tech yo

product_name = "Laptop"
status = "Pending"
quanitity = 3
unit_price = 450.00
is_over_limit = unit_price * quanitity > 1000

print(
    type(product_name),
    type(status),
    type(unit_price),
    type(quanitity),
    type(is_over_limit),
)

# Step 4

subtotal = unit_price * quanitity
tax = subtotal * 0.07
total = subtotal + tax
requires_approval = total > 1000

# Step 5
print(" === Purchase Request Summary === ")
print(f"Product: {product_name}")
print(f"Qty: {quanitity}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
print(f"Requires Approval: {requires_approval}")

# Step 6

user_qty = int(input("Enter a new quantity: "))  # convert str to int
new_total = unit_price * user_qty * 1.07
print(f"New total for {user_qty} units: ${new_total:.2f}")
print(f"Requires Approval: {new_total > 1000}")
