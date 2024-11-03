
try:

    with open("my_file.txt", 'w') as file:
        # Writing three lines of text, mixing strings and numbers
        file.write("Hello, this is the first line.\n")
        file.write("Here is the second line with a number: 123.\n")
        file.write("The third line includes text and the number 456.\n")
    print("Initial content written to 'my_file.txt'.")
except (FileNotFoundError, PermissionError) as e:
    print(f"Error while creating/writing to the file: {e}")

# Step 2: Read and display contents of the file
try:
    # Open "my_file.txt" in read mode
    with open("my_file.txt", 'r') as file:
        print("\nContents of 'my_file.txt':")
        # Read and print each line
        for line in file:
            print(line, end='')
except (FileNotFoundError, PermissionError) as e:
    print(f"Error while reading the file: {e}")

# Step 3: Append additional content to the file
try:
    # Open "my_file.txt" in append mode
    with open("my_file.txt", 'a') as file:
        # Writing three additional lines of text
        file.write("\nAdding a fourth line with text and the number 789.\n")
        file.write("Fifth line contains some text.\n")
        file.write("And finally, the sixth line with number: 101112.\n")
    print("\nAdditional content appended to 'my_file.txt'.")
except (FileNotFoundError, PermissionError) as e:
    print(f"Error while appending to the file: {e}")

# Step 4: Final reading to confirm changes and close file in 'finally' block
try:
    # Reopen "my_file.txt" to display the final content
    with open("my_file.txt", 'r') as file:
        print("\nFinal contents of 'my_file.txt':")
        for line in file:
            print(line, end='')
except (FileNotFoundError, PermissionError) as e:
    print(f"Error while final reading the file: {e}")
finally:
    print("\n\nFile handling operations complete.")
