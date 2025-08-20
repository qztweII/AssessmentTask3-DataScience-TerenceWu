import dataModule as dm
import pandas as pd

df = pd.read_csv("bigMacData.csv")

def show_menu():
    print("\n=== Main Menu ===")
    print("[M]ake a graph")
    print("[S]ettings for graph")
    print("[E]xit")

columnHeads = [list(df.columns.values)]
columnHeads = columnHeads[0] #The function before returns a list in a list. 
columnSettings = {}
for i in columnHeads:
    columnSettings[i] = True

def settings():
    print("\n=== Show/hide columns ===")
    notChosen = True
    while notChosen:
        for i in columnSettings:
            print(i, end='')
            for j in range(30-len(i)):
                print(".", end='')
            print(columnSettings[i])
        choice =input("What do you want to toggle?")
        try:
            if columnSettings[choice] and choice != "name":
                columnSettings[choice] = False
            else:
                columnSettings[choice] = True   
            if choice == "name":
                print("Country cannot be displayed on the y axis")
        except:
            if choice == "exit":
                notChosen = False
            else:
                print("Please choose from the menu!")
        else:
            notChosen = False
            print(f"{choice} {'will be' if columnSettings[choice] else 'will not be'} displayed in the graph. ")


def handle_choice(choice):
    global df
    if choice == 'M':
        dm.clean(df, False)
        df = dm.sort(df, "GDP_local", True)
        dm.graph(df, columnSettings)
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
