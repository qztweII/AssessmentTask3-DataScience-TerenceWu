import dataModule as dm
from pandas import *

df = dm.read("dummyData.csv")

def show_menu():
    print("\n=== Main Menu ===")
    print("[M]ake a graph")
    print("[S]ettings for graph")
    print("[E]xit")

def handle_choice(choice):
    if choice == 'M':
        print("Hello, Terence!")
    elif choice == 'S':
        result = 5 + 7
        print(f"5 + 7 = {result}")
    elif choice == 'E':
        print("Goodbye!")
        return False
    else:
        print("Invalid choice. Try again.")
    return True

columnHeads = [list(df.columns.values)]
columnSettings = {}
for i in columnHeads:
    columnSettings[i] = True

def settings(choice):
    print("\nWhat do you want to change?")
    for i in columnSettings:
        print(f"{i}, {columnSettings[i]}")
    #Selects the columns

def main():
    running = True
    while running:
        show_menu()
        user_choice = input("Enter your choice: ")
        running = handle_choice(user_choice)

if __name__ == "__main__":
    main()


print(df.describe())