import pandas as pd
import numpy as np
import datetime
import os

def load_data():
    """Load data from CSV file, create empty DataFrame if file doesn't exist."""
    csv_file = 'Personal Finance & Budget Tracker.csv'
    try:
        if os.path.exists(csv_file):
            data = pd.read_csv(csv_file)
            # Ensure required columns exist
            required_columns = ['id', 'title', 'amount', 'date', 'category']
            for col in required_columns:
                if col not in data.columns:
                    data[col] = None
            return data
        else:
            # Create empty DataFrame with proper structure
            return pd.DataFrame(columns=['id', 'title', 'amount', 'date', 'category'])
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame(columns=['id', 'title', 'amount', 'date', 'category'])


def save_data(data):
    """Save data to CSV file with error handling."""
    try:
        data.to_csv('Personal Finance & Budget Tracker.csv', index=False)
        return True
    except Exception as e:
        print(f"Error saving data: {e}")
        return False


def add_transaction(data, title, amount, date, category):
    """Add a new transaction to the data."""
    try:
        # Generate new ID
        if data.empty or 'id' not in data.columns:
            new_id = 1
        else:
            # Handle case where id column might have non-numeric values
            existing_ids = []
            for id_val in data['id']:
                try:
                    existing_ids.append(int(id_val))
                except (ValueError, TypeError):
                    continue
            new_id = max(existing_ids) + 1 if existing_ids else 1

        # Validate and convert date
        try:
            parsed_date = pd.to_datetime(date)
        except:
            print("Invalid date format. Please use YYYY-MM-DD format.")
            return False

        # Create new transaction
        new_transaction = {
            'id': str(new_id),
            'title': str(title),
            'amount': float(amount),
            'date': parsed_date.strftime('%Y-%m-%d'),
            'category': str(category)
        }

        # Add to DataFrame
        new_row = pd.DataFrame([new_transaction])
        data = pd.concat([data, new_row], ignore_index=True)

        return save_data(data), data
    except Exception as e:
        print(f"Error adding transaction: {e}")
        return False, data


def view_monthly_summary(data):
    """Display monthly spending summary."""
    try:
        if data.empty:
            print("No data available.")
            return

        # Ensure date column is datetime
        data_copy = data.copy()
        data_copy['date'] = pd.to_datetime(data_copy['date'])
        data_copy['month'] = data_copy['date'].dt.strftime('%Y-%m')

        monthly_summary = data_copy.groupby('month')['amount'].sum().sort_index()
        print("\nMonthly Summary:")
        print("-" * 30)
        for month, total in monthly_summary.items():
            print(f"{month}: ${total:.2f}")
    except Exception as e:
        print(f"Error generating monthly summary: {e}")


def filter_by_specific_month(data, month):
    """Filter transactions by specific month number."""
    try:
        if data.empty:
            print("No data available.")
            return pd.DataFrame()

        data_copy = data.copy()
        data_copy['date'] = pd.to_datetime(data_copy['date'])
        filtered_data = data_copy[data_copy['date'].dt.month == month]
        return filtered_data
    except Exception as e:
        print(f"Error filtering by month: {e}")
        return pd.DataFrame()


def total_per_category(data):
    """Calculate total spending per category."""
    try:
        if data.empty:
            print("No data available.")
            return pd.Series()

        return data.groupby('category')['amount'].sum()
    except Exception as e:
        print(f"Error calculating category totals: {e}")
        return pd.Series()


def delete_transaction(data, id_to_delete):
    """Delete a transaction by ID."""
    try:
        if data.empty:
            print("No data available.")
            return data

        original_count = len(data)
        data_filtered = data[data['id'] != str(id_to_delete)]

        if len(data_filtered) == original_count:
            print(f"Transaction with ID {id_to_delete} not found.")

        return data_filtered
    except Exception as e:
        print(f"Error deleting transaction: {e}")
        return data


def get_mean(data):
    """Calculate mean of amounts."""
    try:
        if data.empty:
            return 0
        return data['amount'].mean()
    except Exception as e:
        print(f"Error calculating mean: {e}")
        return 0


def get_median(data):
    """Calculate median of amounts."""
    try:
        if data.empty:
            return 0
        return data['amount'].median()
    except Exception as e:
        print(f"Error calculating median: {e}")
        return 0


def get_std(data):
    """Calculate standard deviation of amounts."""
    try:
        if data.empty:
            return 0
        return data['amount'].std()
    except Exception as e:
        print(f"Error calculating standard deviation: {e}")
        return 0


def clean_data(data):
    """Clean data by removing null values and duplicates."""
    try:
        if data.empty:
            return data

        data_cleaned = data.copy()
        initial_count = len(data_cleaned)

        # Remove rows with null values in critical columns
        data_cleaned = data_cleaned.dropna(subset=['id', 'amount', 'date'])

        # Remove duplicates
        data_cleaned = data_cleaned.drop_duplicates()

        final_count = len(data_cleaned)
        print(f"Cleaned data: removed {initial_count - final_count} rows")

        return data_cleaned
    except Exception as e:
        print(f"Error cleaning data: {e}")
        return data


def sort_data(data):
    """Sort data by amount in descending order."""
    try:
        if data.empty:
            return data
        return data.sort_values(by='amount', ascending=False)
    except Exception as e:
        print(f"Error sorting data: {e}")
        return data


def filter_by_date_range(data, start_date, end_date):
    """Filter data by date range."""
    try:
        if data.empty:
            return data

        data_copy = data.copy()
        data_copy['date'] = pd.to_datetime(data_copy['date'])

        start_dt = pd.to_datetime(start_date)
        end_dt = pd.to_datetime(end_date)

        mask = (data_copy['date'] >= start_dt) & (data_copy['date'] <= end_dt)
        return data_copy[mask]
    except Exception as e:
        print(f"Error filtering by date range: {e}")
        return data


def cumulative_spending(data):
    """Calculate cumulative spending over time."""
    try:
        if data.empty:
            return pd.DataFrame(columns=['date', 'amount', 'cumulative'])

        data_copy = data.copy()
        data_copy['date'] = pd.to_datetime(data_copy['date'])
        data_sorted = data_copy.sort_values('date')
        data_sorted['cumulative'] = data_sorted['amount'].cumsum()

        return data_sorted[['date', 'amount', 'cumulative']]
    except Exception as e:
        print(f"Error calculating cumulative spending: {e}")
        return pd.DataFrame(columns=['date', 'amount', 'cumulative'])


def check_budget(data, category_limits):
    """Check if spending exceeds budget limits for each category."""
    try:
        if data.empty:
            return {}

        result = {}
        for category, limit in category_limits.items():
            spent = data[data['category'] == category]['amount'].sum()
            over_budget = spent > limit
            result[category] = {
                'spent': spent,
                'limit': limit,
                'status': 'Over Budget' if over_budget else 'Within Budget',
                'difference': spent - limit
            }
        return result
    except Exception as e:
        print(f"Error checking budget: {e}")
        return {}


def moving_average_with_dates(data, window=7):
    """Calculate moving average of spending with dates."""
    try:
        if data.empty or len(data) < window:
            print(f"Not enough data for {window}-day moving average.")
            return pd.DataFrame(columns=['date', 'moving_average'])

        data_copy = data.copy()
        data_copy['date'] = pd.to_datetime(data_copy['date'])
        sorted_data = data_copy.sort_values('date')
        amounts = sorted_data['amount'].values

        # Calculate moving average
        ma = np.convolve(amounts, np.ones(window) / window, mode='valid')
        dates = sorted_data['date'].values[window - 1:]

        return pd.DataFrame({'date': dates, 'moving_average': ma})
    except Exception as e:
        print(f"Error calculating moving average: {e}")
        return pd.DataFrame(columns=['date', 'moving_average'])


def category_percentage_labeled(data):
    """Calculate percentage breakdown by category."""
    try:
        if data.empty:
            return {}

        total = data['amount'].sum()
        if total == 0:
            return {}

        grouped = data.groupby('category')['amount'].sum()
        percentages = (grouped / total * 100).round(2)

        return dict(zip(grouped.index, percentages))
    except Exception as e:
        print(f"Error calculating category percentages: {e}")
        return {}


def validate_date_input(date_str):
    """Validate date input format."""
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def validate_amount_input(amount_str):
    """Validate amount input."""
    try:
        amount = float(amount_str)
        return True, amount
    except ValueError:
        return False, 0


def main():
    """Main function to run the personal finance tracker."""
    print('Welcome to the Personal Finance & Budget Tracker')

    # Load and prepare data
    data = load_data()

    if not data.empty:
        try:
            data['date'] = pd.to_datetime(data['date'])
            data['amount'] = pd.to_numeric(data['amount'], errors='coerce')
            # Remove rows where amount conversion failed
            data = data.dropna(subset=['amount'])
        except Exception as e:
            print(f"Error processing existing data: {e}")

    while True:
        print('\n' + '=' * 50)
        print('PERSONAL FINANCE TRACKER MENU')
        print('=' * 50)
        print('1.  Add transaction')
        print('2.  View monthly summary')
        print('3.  Filter by specific month')
        print('4.  Get total per category')
        print('5.  Delete transaction')
        print('6.  Get mean amount')
        print('7.  Get median amount')
        print('8.  Get standard deviation')
        print('9.  Get sorted data')
        print('10. Filter by date range')
        print('11. Get cumulative spending')
        print('12. Check budget')
        print('13. Get moving average by date')
        print('14. Get category percentage breakdown')
        print('15. Clean data')
        print('16. View all transactions')
        print('17. Exit')
        print('=' * 50)

        choice = input('Choose an option (1-17): ').strip()

        if choice == '1':
            print('\n--- Add Transaction ---')
            title = input('Enter title: ').strip()
            if not title:
                print("Title cannot be empty.")
                continue

            category = input('Enter category (expense/income): ').strip().lower()
            if category not in ['expense', 'income']:
                print("Category must be 'expense' or 'income'.")
                continue

            amount_str = input('Enter amount: ').strip()
            valid_amount, amount = validate_amount_input(amount_str)
            if not valid_amount:
                print("Invalid amount. Please enter a number.")
                continue

            # Make expenses negative
            if category == 'expense':
                amount = -abs(amount)
            elif category == 'income':
                amount = abs(amount)

            date_str = input('Enter date (YYYY-MM-DD): ').strip()
            if not validate_date_input(date_str):
                print("Invalid date format. Please use YYYY-MM-DD.")
                continue

            success, data = add_transaction(data, title, amount, date_str, category)
            if success:
                print('Transaction added successfully.')
            else:
                print('Failed to add transaction.')

        elif choice == '2':
            view_monthly_summary(data)

        elif choice == '3':
            try:
                month = int(input('Enter month number (1-12): '))
                if 1 <= month <= 12:
                    result = filter_by_specific_month(data, month)
                    if not result.empty:
                        print(f"\nTransactions for month {month}:")
                        print(result.to_string(index=False))
                    else:
                        print(f"No transactions found for month {month}.")
                else:
                    print("Month must be between 1 and 12.")
            except ValueError:
                print("Please enter a valid month number.")

        elif choice == '4':
            totals = total_per_category(data)
            if not totals.empty:
                print("\nTotal per category:")
                for category, total in totals.items():
                    print(f"{category}: ${total:.2f}")

        elif choice == '5':
            if data.empty:
                print("No transactions to delete.")
                continue

            print("\nCurrent transactions:")
            print(data[['id', 'title', 'amount', 'date']].to_string(index=False))

            id_to_delete = input('Enter transaction ID to delete: ').strip()
            data = delete_transaction(data, id_to_delete)
            if save_data(data):
                print('Transaction deleted successfully.')
            else:
                print('Failed to save changes.')

        elif choice == '6':
            mean_val = get_mean(data)
            print(f'Mean amount: ${mean_val:.2f}')

        elif choice == '7':
            median_val = get_median(data)
            print(f'Median amount: ${median_val:.2f}')

        elif choice == '8':
            std_val = get_std(data)
            print(f'Standard deviation: ${std_val:.2f}')

        elif choice == '9':
            sorted_df = sort_data(data)
            if not sorted_df.empty:
                print("\nData sorted by amount (highest to lowest):")
                print(sorted_df.to_string(index=False))

        elif choice == '10':
            start = input('Enter start date (YYYY-MM-DD): ').strip()
            end = input('Enter end date (YYYY-MM-DD): ').strip()

            if validate_date_input(start) and validate_date_input(end):
                filtered = filter_by_date_range(data, start, end)
                if not filtered.empty:
                    print(f"\nTransactions from {start} to {end}:")
                    print(filtered.to_string(index=False))
                else:
                    print("No transactions found in the specified date range.")
            else:
                print("Invalid date format. Please use YYYY-MM-DD.")

        elif choice == '11':
            cum_data = cumulative_spending(data)
            if not cum_data.empty:
                print("\nCumulative spending:")
                print(cum_data.to_string(index=False))

        elif choice == '12':
            limits = {}
            print('Enter category limits (press Enter with empty category name to stop):')
            while True:
                cat = input('Category name: ').strip()
                if not cat:
                    break
                try:
                    limit = float(input(f'Limit for {cat}: $'))
                    limits[cat] = limit
                except ValueError:
                    print("Invalid limit amount.")

            if limits:
                result = check_budget(data, limits)
                print("\nBudget check results:")
                for category, info in result.items():
                    print(f"{category}:")
                    print(f"  Spent: ${info['spent']:.2f}")
                    print(f"  Limit: ${info['limit']:.2f}")
                    print(f"  Status: {info['status']}")
                    print(f"  Difference: ${info['difference']:.2f}")

        elif choice == '13':
            try:
                window = int(input('Enter moving average window (e.g., 7): '))
                if window > 0:
                    result = moving_average_with_dates(data, window)
                    if not result.empty:
                        print(f"\n{window}-day moving average:")
                        print(result.to_string(index=False))
                else:
                    print("Window size must be positive.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '14':
            percentages = category_percentage_labeled(data)
            if percentages:
                print("\nCategory percentage breakdown:")
                for category, percentage in percentages.items():
                    print(f"{category}: {percentage}%")

        elif choice == '15':
            data = clean_data(data)
            if save_data(data):
                print("Data cleaned and saved successfully.")

        elif choice == '16':
            if not data.empty:
                print("\nAll transactions:")
                print(data.to_string(index=False))
            else:
                print("No transactions available.")

        elif choice == '17':
            print('Thank you for using Personal Finance & Budget Tracker!')
            break

        else:
            print('Invalid option. Please choose from 1 to 17.')


if __name__ == '__main__':
    main()
