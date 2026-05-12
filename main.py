import pandas as pd
import matplotlib.pyplot as plt

# Hypothesis #
df = pd.read_csv("naplan_school_data.csv")
def hypothesis():
    print("Hypothesis:")
    print("Students that go to higher ranked NSW high schools achieve higher NAPLAN Numeracy scores than Reading and Writing scores,") 
    print("suggesting that these schools demonstrate stronger performance in mathematics compared to literacy subjects.")


# Data table#
def show_data_table():
    print("\n    DATA TABLE    ")
    print(df.to_string(index=False))
    print()



# Line graph #
def show_line_graph():
    print("Opening graph...")
    plt.figure(figsize=(12,6))
    plt.plot(df["School"], df["Numeracy"], marker="o", label="Numeracy")
    plt.plot(df["School"], df["Reading"], marker="o", label="Reading")
    plt.plot(df["School"], df["Writing"], marker="o", label="Writing")

    plt.title("Year 9 NAPLAN Scores Across Selected NSW Schools")
    plt.ylabel("NAPLAN Score")
    
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.show()



    # Average/Mean score #
def average_mean():
    print("\n  Average Scores ")
    avg_numeracy = df["Numeracy"].mean()
    avg_reading = df["Reading"].mean()
    avg_writing = df["Writing"].mean()

    print(f"Average Numeracy: {avg_numeracy:.2f}")
    print(f"Average Reading:  {avg_reading:.2f}")
    print(f"Average Writing:  {avg_writing:.2f}")
    print()
 

 # Final #

def menu():
    while True:
        print(" MENU ")
        print("1. Hypothesis")
        print("2. Show Data Table")
        print("3. Open Line Graph")
        print("4. Mean/Average for Numeracy")
        print("5. School ranking by Year 9 Naplan Scores")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            hypothesis()
        elif choice == "2":
            show_data_table()
        elif choice == "3":
             show_line_graph()
        elif choice =="4":
            average_mean()
        elif choice =="5":
            print(" 1. James Ruse Agriculture High School ")
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")

menu()
