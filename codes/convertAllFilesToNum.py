import os
import numpy as np

# Input and output folders
input_folder = r"C:\Users\Hussein.Bassal\Desktop\Hardness with windowing\Hardness window 1000\Cube 7"
output_folder = r"C:\Users\Hussein.Bassal\Desktop\Hardness with windowing\Hardness window 1000 Num\Cube 7"


# Ensure output folder exists, create if not
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate over each file in the input folder
for filename in os.listdir(input_folder):
    # Check if the file is an LVM file
    if filename.endswith(".lvm"):
        # Construct full paths for input and output files
        input_filepath = os.path.join(input_folder, filename)
        output_filepath = os.path.join(output_folder, filename.replace(".lvm", ".npy"))

        # Read each column from the LVM file
        column_data = []
        with open(input_filepath, "r") as f:
            for line in f:
                # Skip lines that start with "Ch" (assuming these are headers)
                if line.startswith("Ch"):
                    continue
                # Assuming columns are separated by whitespace
                columns = line.split()
                # Convert each column to float and store them
                column_data.append([float(col) for col in columns])

        # Convert list of lists to NumPy array
        numpy_array = np.array(column_data)

        # Save the NumPy array as a .npy file
        np.save(output_filepath, numpy_array)
