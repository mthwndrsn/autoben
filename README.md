# Automation Benefit Calculator

Welcome to the Automation Benefit Calculator! This simple web app helps you calculate the potential time and cost savings from automating a manual and repetitive process. Hosted on GitHub Pages, this tool can be easily accessed and used directly from your browser.

## Features

- **Time Savings Calculation**: Input the time spent on manual and automated processes to see how much time you can save.
- **Cost Savings Estimation**: Calculate potential cost savings based on the time saved and your hourly cost rate.
- **Simple and Intuitive Interface**: Easy-to-use form allows for quick input and results.

## How It Works

1. **Enter Details**: Provide the following inputs in the form:
   - Time spent on the manual process (hours per instance).
   - Frequency of the process (times per month).
   - Time spent on the automated process (hours per instance).
   - Hourly cost rate ($).

2. **Calculate**: Click the "Calculate" button to compute the time saved and potential cost savings.

3. **Results**: View the results, including total manual time, total automated time, time saved, and potential cost savings per month.

## Usage

To use the calculator, simply visit the hosted page on GitHub Pages. No installation or setup is required, and the app runs entirely in your browser.

## Development

This project is built using HTML, CSS, and JavaScript, making it a lightweight and static web application. Feel free to clone the repository and modify the code to fit your specific needs.

## Contributing

Contributions are welcome! If you have any ideas for improvements or want to report a bug, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



## Acknowledgments

Thanks to the open-source community for providing the tools and resources that made this project possible.


Additional Pythong Content to be added 

```
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
```
