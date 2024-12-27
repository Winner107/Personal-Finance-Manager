import pandas as pd
import matplotlib.pyplot as plt

# Create an empty DataFrame to store finance data
columns = ['Date', 'Category', 'Amount', 'Type']  # Type: 'Income' or 'Expense'
df = pd.DataFrame(columns=columns)


# Function to add a transaction
def add_transaction(date, category, amount, type):
    global df
    new_data = pd.DataFrame([[date, category, amount, type]], columns=columns)

    # Ensure the data being added is valid and not empty
    if new_data.dropna().empty:
        print("Error: Transaction data is invalid.")
        return

    # Modern solution to avoid warning: using pd.concat with a check for non-empty data
    if not new_data.isnull().all(axis=1).any():  # Check if new data contains only valid entries
        df = pd.concat([df, new_data], ignore_index=True)
    else:
        print("Invalid data, not adding to DataFrame.")


# Function to display a summary of the user's finance
def display_summary():
    print("\n--- Financial Summary ---")
    print(f'Total Income: ${df[df["Type"] == "Income"]["Amount"].sum():.2f}')
    print(f'Total Expenses: ${df[df["Type"] == "Expense"]["Amount"].sum():.2f}')
    print(
        f'Net Balance: ${df[df["Type"] == "Income"]["Amount"].sum() - df[df["Type"] == "Expense"]["Amount"].sum():.2f}')


# Function to visualize data with a pie chart of categories
def visualize_data():
    print("\n--- Data Visualization ---")
    category_expenses = df[df["Type"] == "Expense"].groupby("Category")["Amount"].sum()
    category_expenses.plot(kind='pie', autopct='%1.1f%%', figsize=(7, 7), title='Expense Distribution by Category')
    plt.ylabel('')
    plt.show()


# Function to handle user input for adding transactions
def get_transaction_input():
    date = input("Enter the transaction date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Groceries, Rent, Entertainment): ")
    amount = float(input("Enter the amount: "))
    type_of_transaction = input("Is this an 'Income' or 'Expense'? ").capitalize()

    # Add the transaction to the DataFrame
    add_transaction(date, category, amount, type_of_transaction)


# Main function to run the program
def run_finance_manager():
    while True:
        print("\n--- Personal Finance Manager ---")
        print("1. Add Transaction")
        print("2. Show Financial Summary")
        print("3. Show Data Visualization")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            get_transaction_input()
        elif choice == "2":
            display_summary()
        elif choice == "3":
            visualize_data()
        elif choice == "4":
            print("Exiting the program. Have a great day!")
            break
        else:
            print("Invalid choice, please select again.")


# Run the finance manager program
run_finance_manager()
