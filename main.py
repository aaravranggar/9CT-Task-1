import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset
df = pd.read_csv("naplan_school_data.csv")
def hypothesis():
    print("Students that go to higher ranked NSW high schools achieve higher NAPLAN Numeracy scores than Reading and Writing scores, suggesting that these schools demonstrate stronger performance in mathematics compared to literacy subjects.")
def show_data_table():
    print("\n--- DATA TABLE ---")
    print(df.to_string(index=False))
    print()

def show_line_graph():
    print("Opening graph...")
    plt.figure(figsize=(12,6))
    plt.plot(df["School"], df["Numeracy"], marker="o", label="Numeracy")
    plt.plot(df["School"], df["Reading"], marker="o", label="Reading")
    plt.plot(df["School"], df["Writing"], marker="o", label="Writing")

    plt.title("Year 9 NAPLAN Scores Across Selected NSW Schools")
    plt.ylabel("NAPLAN Score")
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.show()

def menu():
    while True:
        print(" MENU ")
        print("1. Hypothesis")
        print("2. Show Data Table")
        print("3. Open Line Graph")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "2":
            show_data_table()
        elif choice == "3":
            show_line_graph()
        elif choice == "1":
            hypothesis()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")

menu()
