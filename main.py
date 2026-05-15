import pandas as panda
import matplotlib.pyplot as graph
import os

data  = panda.read_csv("naplan_school_data.csv")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
# My hypothesis #
def hypothesis():
    print("Hypothesis:")
    print("Students that go to higher ranked NSW high schools achieve higher NAPLAN Numeracy scores than Reading and Writing scores,") 
    print("suggesting that these schools demonstrate stronger performance in mathematics compared to literacy subjects.")


# Data table#
def show_datatable():
    print("\n    DATA TABLE    ")
    print(data.to_string(index=False))
    print()



# Line graph matplotlib visual representation #
def show_linegraph():
    print("Opening graph   ..  ")
    graph.figure(figsize=(12,6))


    graph.plot(data["School"], data["Numeracy"], marker="o", label="Numeracy")
    graph.plot(data["School"], data["Reading"], marker="o", label="Reading")
    graph.plot(data["School"], data["Writing"], marker="o", label="Writing")
   

    graph.title("Year 9 NAPLAN Scores Across Selected NSW Schools")
   
    graph.ylabel("NAPLAN Score")
    

    graph.grid(True, linestyle='--', alpha=0.6)
    graph.legend()
    graph.tight_layout()
    graph.show()



# the average
def average_mean():
    print("\nAverage Scores")






# Numeracy average
    numeracy_average = data["Numeracy"].mean()
    print("Numeracy Average:", round(numeracy_average, 2))



# Reading average
    reading_average = data["Reading"].mean()
    print("Reading Average:", round(reading_average, 2))



# Writing average for each school combined
    writing_average = data["Writing"].mean()
    print("Writing Average:", round(writing_average, 2))











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
            clear_screen()
            hypothesis()

        elif choice == "2":
            clear_screen()
            show_datatable()

        elif choice == "3":
            clear_screen()
            show_linegraph()

        elif choice == "4":
            clear_screen()
            average_mean()

        elif choice == "5":
            clear_screen()
            print("\n Naplan Score Rankings")
            print(" 1. James Ruse Agriculture")
            print(" 2. North Sydney Boys")
            print(" 3. North Sydney Girls")
            print(" 4. Normanhurst Boys")
            print(" 5. Sydney Grammar\n")

        elif choice == "6":
            clear_screen()
            print("\n HSC Score Rankings")
            print(" 1. North Sydney Boys")
            print(" 2. James Ruse Agriculture")
            print(" 3. Sydney Grammar")
            print(" 4. North Sydney Girls")
            print(" 5. Normanhurst Boys\n")

        elif choice == "7":
            clear_screen()
            print("Exiting program\nYou have successfully exited the program.")
            break

        else:
            clear_screen()
            print("Invalid choice. Try again.\n")

menu()