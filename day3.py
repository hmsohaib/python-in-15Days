# --- Day 3: Lists, Aggregations & Slicing ---

# 1. Defining a List of Revenue Figures ($ Thousands)
monthly_revenue = [120, 135, 150, 142, 160, 175, 190, 185, 210, 205, 230, 250]

# 2. Built-in List Aggregations
total_annual_rev = sum(monthly_revenue)
max_month = max(monthly_revenue)
min_month = min(monthly_revenue)

print(f"Total Annual Revenue: ${total_annual_rev}k")
print(f"Peak Month: ${max_month}k | Lowest Month: ${min_month}k")

# 3. Quarterly Slicing (Extracting 3-month blocks)
q1_rev = monthly_revenue[0:3]   # Indices 0, 1, 2
q2_rev = monthly_revenue[3:6]   # Indices 3, 4, 5
q3_rev = monthly_revenue[6:9]   # Indices 6, 7, 8
q4_rev = monthly_revenue[9:12]  # Indices 9, 10, 11

print(f"\nQ1 Total: ${sum(q1_rev)}k")
print(f"Q4 Total: ${sum(q4_rev)}k")

# 4. Extracting the Last 6 Months using Negative Slicing
h2_rev = monthly_revenue[-6:]
print(f"H2 (Last 6 Months) Total: ${sum(h2_rev)}k")

# 5. Modifying Lists (Appending and Updating)
monthly_revenue.append(265)  # Add Month 13 (Projection)
print(f"\nUpdated Revenue Stream (13 Months): {monthly_revenue}")