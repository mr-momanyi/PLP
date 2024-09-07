try:
    # Open the file in write mode and write initial lines
    with open("my_file.txt", 'w') as file:
        file.write("Hello, this is me in 2030.\n")
        file.write("The school is good.\n")
        file.write("Today's activity is coding.\n")

    # Open the file in append mode and add more lines
    with open("my_file.txt", 'a') as file:
        file.write("I will be an expert programmer.\n")
        file.write("Code best programs.\n")
        file.write("Create a digital hub.\n")

    # Open the file in read mode and display its contents
    with open("my_file.txt", 'r') as file:
        contents = file.read()

    # Display the contents
    print("Contents of 'my_file.txt':")
    print(contents)

except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: You do not have permission to access the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("File operation completed.")
