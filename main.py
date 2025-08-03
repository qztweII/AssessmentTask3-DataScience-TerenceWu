import dataModule as dm
from pandas import *

df = dm.read("dummyData.csv")

def show_menu():
    print("\n=== Main Menu ===")
    print("[M]ake a graph")
    print("[S]ettings for graph")
    print("[E]xit")

columnHeads = [list(df.columns.values)]
columnSettings = {}
for i in len(columnHeads):
    columnSettings[i] = True

def settings():
    print("\nWhat do you want to change?")
    for i in columnSettings:
        print(f"{i}, {columnSettings[i]}")
    notChosen = True
    while notChosen:
        try:
            choice = int(input("What do you want to toggle?"))
        except:
            print("Choose from the menu!")
        else:
            if columnSettings[choice]:
                columnSettings[choice] = False
            else:
                columnSettings[choice] = True

def handle_choice(choice):
    if choice == 'M':
        print("Hello, Terence!")
    elif choice == 'S':
        settings()
    elif choice == 'E':
        print("Goodbye!")
        return False
    else:
        print("Invalid choice. Try again.")
    return True



def main():
    running = True
    while running:
        show_menu()
        user_choice = input("Enter your choice: ")
        running = handle_choice(user_choice)

if __name__ == "__main__":
    main()


print(df.describe())