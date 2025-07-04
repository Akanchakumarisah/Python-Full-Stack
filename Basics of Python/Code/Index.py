#Ask the user to input an index
#Access that index from a predefined list
#Handle IndexError and ValueError using nested try blocks
#Print “End of program” using finally
def access_index():
    predefined_list = [10, 20, 30, 40, 50]  # Example predefined list
    try:
        index = int(input("Enter an index to access (0-4): "))
        try:
            value = predefined_list[index]
            print(f"Value at index {index}: {value}")
        except IndexError:
            print("Error: Index out of range. Please enter a valid index.")
    except ValueError:
        print("Error: Invalid input. Please enter a numeric index.")
    finally:
        print("End of program")
        # Call the function to execute the index access
access_index()
