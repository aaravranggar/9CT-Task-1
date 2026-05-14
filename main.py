import pandas as pd
import matplotlib.pyplot as plt

# My hypothesis #
df = pd.read_csv("naplan_school_data.csv")
def hypothesis():
    print("Hypothesis:")
    print("Students that go to higher ranked NSW high schools achieve higher NAPLAN Numeracy scores than Reading and Writing scores,") 
    print("suggesting that these schools demonstrate stronger performance in mathematics compared to literacy subjects.")


# Data table#
def show_datatable():
    print("\n    DATA TABLE    ")
    print(df.to_string(index=False))
    print()



# Line graph matplotlib visual representation #
def show_linegraph():
    print("Opening graph   ..  ")
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

# the average
def average_mean():
    print("\nAverage Scores")

# Numeracy average
    numeracy_average = df["Numeracy"].mean()
    print("Numeracy Average:", round(numeracy_average, 2))

# Reading average
    reading_average = df["Reading"].mean()
    print("Reading Average:", round(reading_average, 2))

# Writing average for each school combined
    writing_average = df["Writing"].mean()
    print("Writing Average:", round(writing_average, 2))



    print()


 # Final code for output 

def menu():
    while True:
        print(" Menu ")
        print("1. Hypothesis")
        print("2. Data Table")
        print("3. Line Graph Visual representation")
        print("4. Average for each subject")
        print("5. School ranking by Year 9 Naplan Scores")
        print("6. School ranking by HSC Scores")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            hypothesis()
        elif choice == "2":
            show_datatable()
        elif choice == "3":
             show_linegraph()
        elif choice =="4":
            average_mean()
        elif choice =="5":
            print(" \n Naplan Score Rankings \n 1. James Ruse Agriculture  \n 2. North Sydney Boys \n 3. North Sydney Girls \n 4. Noramnhurst Boys \n 5. Sydney Grammar \n")
        elif choice == "6":
            print(" \n HSC Score Rankings \n 1. North Sydney Boys \n 2. James Ruse Agriculture \n 3. Sydney Grammar \n 4. North Sydney Girls \n 5. Normanhurst Boys\n" )
        elif choice == "7":
            print("Exiting program\n You have succesfully exited the program.")

            break
        else:
            print("Invalid choice. Try again.\n")

menu()
