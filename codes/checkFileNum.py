import numpy as np

# Load the NumPy array from the saved file with allow_pickle=True
numpy_array = np.load(r"C:\Users\Hussein.Bassal\Desktop\trial 1\Hardness_Voltage_Seq1_Sp150_Cube3_t3_window_100_feature.npy", allow_pickle=True)

# Print the content of the NumPy array
print("NumPy Array Content:")
print(numpy_array)

# Print the shape of the NumPy array
print("\nNumPy Array Shape:")
print(numpy_array.shape)