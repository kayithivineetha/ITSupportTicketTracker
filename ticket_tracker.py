
# IT Support Ticket Tracker

print("===================================")
print("       IT SUPPORT TICKET SYSTEM")
print("===================================")

tickets = [
    {
        "id": 101,
        "issue": "Laptop not connecting to Wi-Fi",
        "priority": "High",
        "status": "Open"
    },
    {
        "id": 102,
        "issue": "Outlook is not opening",
        "priority": "Medium",
        "status": "In Progress"
    },
    {
        "id": 103,
        "issue": "Password reset request",
        "priority": "Low",
        "status": "Resolved"
    }
]

for ticket in tickets:
    print("\nTicket ID:", ticket["id"])
    print("Issue:", ticket["issue"])
    print("Priority:", ticket["priority"])
    print("Status:", ticket["status"])
    print("-----------------------------------")

print("Total tickets:", len(tickets))
print("===================================")
