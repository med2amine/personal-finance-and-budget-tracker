💰 Personal Finance & Budget Tracker
A comprehensive command-line personal finance management tool built with Python, leveraging the power of Pandas and NumPy for data analysis and manipulation. This project marks my first deep dive into data science libraries and demonstrates practical applications of data analysis in personal finance.
🎯 Project Overview
This finance tracker allows users to manage their personal expenses and income through an intuitive command-line interface. Built as a learning project to explore Pandas and NumPy, it showcases various data manipulation techniques, statistical analysis, and file operations.
✨ Features
📊 Data Management

Add Transactions: Record income and expenses with automatic categorization
Delete Transactions: Remove unwanted entries by ID
Data Cleaning: Automatic removal of duplicates and null values
CSV Persistence: All data automatically saved to CSV format

📈 Analytics & Insights

Monthly Summaries: Track spending patterns month by month
Category Analysis: Breakdown spending by categories with percentages
Statistical Analysis: Calculate mean, median, and standard deviation
Moving Averages: Analyze spending trends over time
Cumulative Spending: Track total expenditure over time periods

🎛️ Filtering & Sorting

Date Range Filtering: View transactions within specific periods
Monthly Filtering: Focus on specific months
Amount Sorting: Sort transactions from highest to lowest
Custom Data Views: Multiple ways to slice and dice your data

💡 Budget Management

Budget Limits: Set spending limits for different categories
Budget Tracking: Monitor if you're over or under budget
Financial Health Check: Get insights into your spending habits

🛠️ Technologies Used

Python 3.x: Core programming language
Pandas: Data manipulation and analysis
NumPy: Numerical computations and array operations
Datetime: Date and time handling
CSV: Data persistence

📋 Prerequisites
Make sure you have Python installed on your system. You can check by running:
bashpython --version
🚀 Installation

Clone the repository
bashgit clone https://github.com/yourusername/personal-finance-tracker.git
cd personal-finance-tracker

Install required packages
bashpip install pandas numpy

Run the application
bashpython finance_tracker.py


📖 Usage
Starting the Application
Run the script and you'll be greeted with an interactive menu:
Welcome to the Personal Finance & Budget Tracker
==================================================
PERSONAL FINANCE TRACKER MENU
==================================================
1.  Add transaction
2.  View monthly summary
3.  Filter by specific month
...
17. Exit
==================================================
Adding Transactions

Choose option 1 from the menu
Enter transaction details:

Title: Description of the transaction
Category: expense or income
Amount: Numeric value (expenses automatically made negative)
Date: Format as YYYY-MM-DD



Example Workflow
Enter title: Grocery Shopping
Enter category (expense/income): expense
Enter amount: 85.50
Enter date (YYYY-MM-DD): 2024-01-15
Transaction added successfully.
📊 Data Analysis Features
📈 Statistical Analysis

Mean Calculation: Average transaction amount
Median Analysis: Middle value of all transactions
Standard Deviation: Measure of spending volatility

📅 Time-Based Analysis

Monthly Summaries: Total spending per month
Date Range Filtering: Custom period analysis
Moving Averages: Trend analysis over time windows

🏷️ Category Breakdown

Spending by Category: Total and percentage breakdown
Budget vs Actual: Compare planned vs actual spending

🗂️ File Structure
personal-finance-tracker/
│
├── finance_tracker.py              # Main application file
├── Personal Finance & Budget Tracker.csv  # Data storage (auto-created)
├── README.md                       # Project documentation
└── requirements.txt               # Dependencies (optional)
💾 Data Storage
The application uses a CSV file (Personal Finance & Budget Tracker.csv) to store all transaction data. The file structure includes:

id: Unique transaction identifier
title: Transaction description
amount: Transaction amount (negative for expenses)
date: Transaction date (YYYY-MM-DD format)
category: Transaction type (expense/income)

🧠 Learning Highlights
This project was instrumental in learning:
Pandas Mastery

DataFrame creation and manipulation
Data filtering with boolean indexing
GroupBy operations for aggregations
Date/time data handling
CSV file operations
Data cleaning techniques

NumPy Applications

Array operations for statistical calculations
Convolution for moving averages
Mathematical computations
Data type conversions

Python Best Practices

Error handling and validation
Function modularity
User input sanitization
File I/O operations

🚧 Future Enhancements

 GUI Interface: Tkinter or web-based interface
 Data Visualization: Charts and graphs with Matplotlib
 Export Options: PDF reports and Excel exports
 Multi-Currency Support: Handle different currencies
 Investment Tracking: Portfolio management features
 Automated Imports: Bank statement integration
 
 🤝 Contributing
This is a learning project, but contributions are welcome! If you have suggestions or improvements:

Fork the repository
Create a feature branch (git checkout -b feature/AmazingFeature)
Commit changes (git commit -m 'Add AmazingFeature')
Push to branch (git push origin feature/AmazingFeature)
Open a Pull Request

📝 License
This project is open source and available under the MIT License.
