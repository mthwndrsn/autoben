# Inputs for the calculations based on the example values provided

# Old and new values
old_time_per_task = 2  # hours
new_time_per_task = 0.5  # hours
number_of_tasks_per_week = 50  # tasks per week
labor_cost_per_hour = 40  # dollars per hour
material_cost_savings = 0  # assuming no material savings for now
investment_cost = 0  # automation investment cost, assuming zero for now

old_output_per_hour = 10  # units per hour
new_output_per_hour = 15  # units per hour

old_error_rate = 0.05  # 5%
new_error_rate = 0.01  # 1%

# Calculating Time Saved per Week (hours)
time_saved_per_week = (old_time_per_task - new_time_per_task) * number_of_tasks_per_week

# Calculating Cost Savings per Week ($)
cost_savings_per_week = time_saved_per_week * labor_cost_per_hour + material_cost_savings

# Calculating ROI (%) (assuming zero investment cost for this example)
roi = (cost_savings_per_week - investment_cost) / (investment_cost if investment_cost > 0 else 1) * 100  # Avoiding division by zero

# Calculating Productivity Increase (%)
productivity_increase = (new_output_per_hour - old_output_per_hour) / old_output_per_hour * 100

# Calculating Error Reduction (%)
error_reduction = (old_error_rate - new_error_rate) / old_error_rate * 100

# Output the results
time_saved_per_week, cost_savings_per_week, roi, productivity_increase, error_reduction
