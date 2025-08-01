import csv

total_cost = 0
in_transit_shipments = []

with open('shipments.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['status'] == 'In Transit':
            in_transit_shipments.append(row)
            total_cost += int(row['cost'])

print(f"Total cost of In Transit shipments: ₹{total_cost}")

# Export to new CSV
with open('in_transit_shipments.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=in_transit_shipments[0].keys())
    writer.writeheader()
    writer.writerows(in_transit_shipments)

print("Exported in-transit shipments to 'in_transit_shipments.csv'")


