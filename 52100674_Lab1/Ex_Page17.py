import numpy as np

def calculate_average_intensity(binary_image):
    M, N = binary_image.shape
    avg_intensity = 0
    
    for r in range(M):
        for c in range(N):
            avg_intensity += binary_image[r, c]
    
    avg_intensity /= (M * N)
    
    return avg_intensity

B = np.array([[0, 1, 0],
              [1, 0, 1],
              [0, 1, 0]])

avg_intensity = calculate_average_intensity(B)

print("Average Intensity:", avg_intensity)
