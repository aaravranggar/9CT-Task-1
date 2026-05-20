import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("naplan_school_data.csv")

def hypothesis():
    print("Hypothesis:")
    print("Students that go to higher ranked NSW high schools achieve higher NAPLAN Numeracy scores than Reading and Writing scores,")
    print("suggesting that these schools demonstrate stronger performance in mathematics compared to literacy subjects.")

def show_datatable():
    print("\n    DATA TABLE    ")
    print(df.to_string(index=False))
    print()

def show_linegraph():
    print("Opening graph...")
    plt.figure(figsize=(12, 6))

    plt.plot(df["School"], df["Numeracy"], marker="o", label="Numeracy")
    plt.plot(df["School"], df["Reading"], marker="o", label="Reading")
    plt.plot(df["School"], df["Writing"], marker="o", label="Writing")

    plt.title("Year 9 NAPLAN Scores Across Selected NSW Schools")
    plt.ylabel("NAPLAN Score")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.show()

def average_mean():
    print("\nAverage Scores")

    numeracy_average = df["Numeracy"].mean()
    print("Numeracy Average:", round(numeracy_average, 2))

    reading_average = df["Reading"].mean()
    print("Reading Average:", round(reading_average, 2))

    writing_average = df["Writing"].mean()
    print("Writing Average:", round(writing_average, 2))

    print()

def naplan_rankings():
    print("\nNaplan Score Rankings")
    print("1. James Ruse Agriculture")
    print("2. North Sydney Boys")
    print("3. North Sydney Girls")
    print("4. Normanhurst Boys")
    print("5. Sydney Grammar\n")

def hsc_rankings():
    print("\nHSC Score Rankings")
    print("1. North Sydney Boys")
    print("2. James Ruse Agriculture")
    print("3. Sydney Grammar")
    print("4. North Sydney Girls")
    print("5. Normanhurst Boys\n")
