try:
    filename = input("Enter filename: ")
    with open(filename, "r") as f:
        numbers = [int(line.strip()) for line in f.readlines()]
    
    index = int(input("Enter index to access: "))
    print("Number at index", index, "is", numbers[index])

except FileNotFoundError as e:
    print("Error: File not found.", e)
except PermissionError as e:
    print("Error: Permission denied.", e)
except ValueError as e:
    print("Error: Invalid number in file.", e)
except IndexError as e:
    print("Error: Index out of range.", e)
except Exception as e:
    print("An unexpected error occurred:", e)