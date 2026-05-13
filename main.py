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

dcef menu():
    while True:
        print(" MENU ")
        print("1. Hypothesis")
        print("2. Show Data Table")
        print("3. Open Line Graph")
        print("4. Mean/Average for Numeracy")
        print("7. School ranking by Year 9 Naplan Scores")
        print("8. School ranking by HSC Scores")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            hypothesis()
        elif choice == "2":
            show_data_table()
        elif choice == "3":
             show_line_graph()
        elif choice =="4":
            average_mean()
        
        elif choice =="7":
            print(" \n Naplan Score Rankings \n 1. James Ruse Agriculture  \n 2. North Sydney Boys \n 3. North Sydney Girls \n 4. Noramnhurst Boys \n 5. Sydney Grammar \n")
        elif choice == "8":
            print(" \n HSC Score Rankings \n 1. North Sydney Boys \n 2. James Ruse Agriculture \n 3. Sydney Grammar \n 4. North Sydney Girls \n 5. Normanhurst Boys\n" )
        elif choice == "9":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")

menu()
