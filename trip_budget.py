# Simple Travel Budget Calculator

def travel_budget(days, cost_per_day, flight_cost):
    return (days * cost_per_day) + flight_cost

# Example: 5 days in Turkey, $120 per day, $600 flight
print("Turkey Trip Cost:", travel_budget(5, 120, 600))
