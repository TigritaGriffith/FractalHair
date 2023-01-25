import fractal
import random
import numpy as np
import matplotlib.pyplot as plt

def generate_fractal_hair():
    # Create a fractal object with random parameters
    f = fractal.Fractal(random.randint(3, 6), random.uniform(0.1, 0.9), random.uniform(0.1, 0.9))
    # Generate the fractal shape
    hair = f.generate()
    # Add noise to the fractal shape to make it look more like hair
    noise = np.random.normal(0, 0.05, hair.shape)
    hair = hair + noise
    hair = np.clip(hair, 0, 1)
    # Apply a hair-like color map to the fractal shape
    hair = plt.cm.Blues(hair)
    # Return the fractal hair
    return hair

# Generate 10 fractal hair images
for i in range(10):
    hair = generate_fractal_hair()
    plt.imsave("fractal_hair_{}.png".format(
