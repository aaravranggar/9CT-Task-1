from data_module import (
    hypothesis,
    show_datatable,
    show_linegraph,
    average_mean,
    naplan_rankings,
    hsc_rankings
)

def menu():
    while True:
        print(" Menu ")
        print("1. Hypothesis")
        print("2. Data Table")
        print("3. The Line Graph Visual representation")
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
        elif choice == "4":
            average_mean()
        elif choice == "5":
            naplan_rankings()
        elif choice == "6":
            hsc_rankings()
        elif choice == "7":
            print("Exiting program\nYou have successfully exited the program.")
            break
        else:
            print("Invalid choice. Try again.\n")

menu()
