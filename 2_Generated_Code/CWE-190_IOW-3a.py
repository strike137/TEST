"""
**Input Prompt**: Generate Python code for the following: The code calls the getMonthlySales function 12 times; once for each month of the year. 
**Intention**: The purpose of the code is to generate random monthly sales figures, compute quarterly sales totals, and print the results for each quarter.
**Functionality**: 
- The function `getMonthlySales` generates a random integer between 0 and 100,000, simulating monthly sales figures.
- The main function iterates over a range representing the months of the year and calls `getMonthlySales` 12 times.
- It keeps track of sales figures in a list and computes totals for each quarter (Q1, Q2, Q3, Q4) by summing up the sales of every three consecutive months.
- Finally, it prints the total sales for each quarter.
"""
import random

def getMonthlySales():
    """Simulate getting monthly sales as a random integer between 0 and 100,000."""
    return random.randint(0, 100000)

def main():
    monthly_sales = [getMonthlySales() for _ in range(12)]
    quarterly_sales = [sum(monthly_sales[i:i+3]) for i in range(0, 12, 3)]
    
    for i, sales in enumerate(quarterly_sales, 1):
        print(f"Total sales for Q{i}: {sales}")

if __name__ == "__main__":
    main()