# --- Exercise A: Conditional Logic ---
record_count = 850

# Notice the colon (:) at the end of conditions and the mandatory 4-space indentation
if record_count >= 1000:
    status = "High Volume Pipeline"
elif record_count >= 500 and record_count < 1000:
    status = "Standard Volume Pipeline"
else:
    status = "Low Volume Pipeline"

print(f"Status for {record_count} records: {status}")

# --- Exercise B: Processing Data Records ---
sales_regions = ["North America", "EMEA", "APAC", "LATAM"]

print("\n--- Processing Regional Pipelines ---")
for region in sales_regions:
    # Filter out or flag specific regions cleanly
    if region == "APAC":
        print(f"-> {region}: Special Priority Region")
    else:
        print(f"-> {region}: Standard Audit")