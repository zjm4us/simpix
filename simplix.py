import numpy as np
from PIL import Image
import math
from numba import njit
import time

# Define the simulated annealing function
@njit
def anneal(flat_a, flat_b, perm, T, alpha, iterations):
    num_pixels = len(flat_a)
    for _ in range(iterations):
        i1 = np.random.randint(0, num_pixels)
        i2 = np.random.randint(0, num_pixels)

        # Compute old cost for the two pixels
        da = flat_a[perm[i1]] - flat_b[i1]
        db = flat_a[perm[i2]] - flat_b[i2]
        old_cost = da[0]**2 + da[1]**2 + da[2]**2 + db[0]**2 + db[1]**2 + db[2]**2

        # Swap pixels
        perm[i1], perm[i2] = perm[i2], perm[i1]

        # Compute new cost after swap
        da = flat_a[perm[i1]] - flat_b[i1]
        db = flat_a[perm[i2]] - flat_b[i2]
        new_cost = da[0]**2 + da[1]**2 + da[2]**2 + db[0]**2 + db[1]**2 + db[2]**2

        delta = new_cost - old_cost
        arg = -delta / T

        # Accept swap if it improves cost or probabilistically
        if delta < 0 or (arg > -700 and np.random.random() < math.exp(arg)):
            pass
        else:
            perm[i1], perm[i2] = perm[i2], perm[i1]

        # Decrease temperature
        T *= alpha

    return perm

# -------------------------
# First pair: imageA -> imageB
print("Starting annealing for imageA -> imageB")
start_time = time.perf_counter()

image_a1 = Image.open("imageA.jpg").convert("RGB")
image_b1 = Image.open("imageB.jpg").convert("RGB")
image_a1 = image_a1.resize(image_b1.size)
flat_a1 = np.array(image_a1).reshape(-1, 3).astype(np.float32)
flat_b1 = np.array(image_b1).reshape(-1, 3).astype(np.float32)

perm1 = np.arange(len(flat_a1))
np.random.shuffle(perm1)
perm1 = anneal(flat_a1, flat_b1, perm1, T=2000.0, alpha=0.999, iterations=2_000_000)

mapped_pixels1 = flat_a1[perm1].reshape(np.array(image_a1).shape)
Image.fromarray(mapped_pixels1.astype('uint8'), 'RGB').save("imageA_to_imageB.jpg")

end_time = time.perf_counter()
print(f"Elapsed time for imageA -> imageB: {end_time - start_time:.4f} seconds")

# -------------------------
# Second pair: frisbe_scott_stadium -> rotunda_north_facade
print("Starting annealing for frisbe_scott_stadium -> rotunda_north_facade")
start_time = time.perf_counter()

image_a2 = Image.open("frisbe_scott_stadium.png").convert("RGB")
image_b2 = Image.open("rotunda_north_facade.png").convert("RGB")
image_a2 = image_a2.resize(image_b2.size)
flat_a2 = np.array(image_a2).reshape(-1, 3).astype(np.float32)
flat_b2 = np.array(image_b2).reshape(-1, 3).astype(np.float32)

perm2 = np.arange(len(flat_a2))
np.random.shuffle(perm2)
perm2 = anneal(flat_a2, flat_b2, perm2, T=2000.0, alpha=0.999, iterations=2_000_000)

mapped_pixels2 = flat_a2[perm2].reshape(np.array(image_a2).shape)
Image.fromarray(mapped_pixels2.astype('uint8'), 'RGB').save("frisbee_to_rotunda.jpg")

end_time = time.perf_counter()
print(f"Elapsed time for frisbe_scott_stadium -> rotunda_north_facade: {end_time - start_time:.4f} seconds")

