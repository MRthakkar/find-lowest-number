# The script will find the lowest number in a file and write it to another file.
#
# Run as: python3 find_lowest_number.py <input_file> <output_file>
#
# Example: python3 find_lowest_number.py numbers.txt lowest_number.txt
#
# If python is setup to run as "python" instead of "python3" on the machine, 
# then we should use "python" instead of "python3" in the above.
#
# The input file should contain one number per line. The output file will 
# contain the lowest number.
#
# If the input file is blank, the output file will contain the text: "No 
# numbers found in file".

import sys

# Check if the correct number of arguments is provided
if len(sys.argv) != 3:
    print("Usage: python3 find_lowest_number.py <input_file> <output_file>")
    sys.exit(1)

input_filename = sys.argv[1]
output_filename = sys.argv[2]

try:
    # Read all numbers from the input file
    with open(input_filename, 'r') as input_file:
        numbers = [float(line.strip()) for line in input_file if line.strip()]

    # Write the result to the output file
    with open(output_filename, 'w') as output_file:
        if numbers:
            lowest_number = min(numbers)
            output_file.write(f"{lowest_number}\n")
        else:
            output_file.write("No numbers found in file\n")

except FileNotFoundError:
    print(f"Error: The file '{input_filename}' does not exist.")
    sys.exit(1)
except ValueError:
    print("Error: The input file contains invalid data.")
    sys.exit(1)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)
