# Unit-3 Assignment 8
# File Handling in Python
# Read file, count lines, extract first two lines,
# and write them into a new file.


def main():
    input_file = "input.txt"
    output_file = "output.txt"

    try:
        # Read data from input file
        with open(input_file, "r") as file:
            lines = file.readlines()

        # Count total number of lines
        total_lines = len(lines)

        # Extract first two lines
        first_two_lines = lines[:2]

        # Display results
        print("Total number of lines:", total_lines)
        print("\nFirst two lines:")

        for line in first_two_lines:
            print(line.strip())

        # Write first two lines into output file
        with open(output_file, "w") as file:
            file.writelines(first_two_lines)

        print("\nFirst two lines successfully written to", output_file)

    except FileNotFoundError:
        print("Error: input.txt file not found.")

    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()