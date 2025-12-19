import numpy as np
from PIL import Image
import math
from numba import njit
import time

# Simulated annealing function
@njit
def anneal(flat_a, flat_b, perm, T, alpha, iterations):
    num_pixels = len(flat_a)
    for _ in range(iterations):
        i1 = np.random.randint(0, num_pixels)
        i2 = np.random.randint(0, num_pixels)

        da = flat_a[perm[i1]] - flat_b[i1]
        db = flat_a[perm[i2]] - flat_b[i2]
        old_cost = da[0]**2 + da[1]**2 + da[2]**2 + db[0]**2 + db[1]**2 + db[2]**2

        perm[i1], perm[i2] = perm[i2], perm[i1]

        da = flat_a[perm[i1]] - flat_b[i1]
        db = flat_a[perm[i2]] - flat_b[i2]
        new_cost = da[0]**2 + da[1]**2 + da[2]**2 + db[0]**2 + db[1]**2 + db[2]**2

        delta = new_cost - old_cost
        arg = -delta / T

        if delta < 0 or (arg > -700 and np.random.random() < math.exp(arg)):
            pass
        else:
            perm[i1], perm[i2] = perm[i2], perm[i1]

        T *= alpha
    return perm

# -------------------------
# First pair: large_imageA -> large_imageB
print("Starting annealing for large_imageA -> large_imageB")
start_time = time.perf_counter()

image_a = Image.open("large_imageA.jpg").convert("RGB")
image_b = Image.open("large_imageB.jpg").convert("RGB")
image_a = image_a.resize(image_b.size)
flat_a = np.array(image_a).reshape(-1, 3).astype(np.float32)
flat_b = np.array(image_b).reshape(-1, 3).astype(np.float32)

perm = np.arange(len(flat_a))
np.random.shuffle(perm)
perm = anneal(flat_a, flat_b, perm, T=4000.0, alpha=0.999, iterations=200_000_000)

mapped_pixels = flat_a[perm].reshape(np.array(image_a).shape)
Image.fromarray(mapped_pixels.astype('uint8'), 'RGB').save("A_to_B.jpg")

end_time = time.perf_counter()
print(f"Elapsed time for large_imageA -> large_imageB: {end_time - start_time:.2f} seconds")

# -------------------------
# Reverse: large_imageB -> large_imageA
print("Starting annealing for large_imageB -> large_imageA")
start_time = time.perf_counter()

image_a = Image.open("large_imageB.jpg").convert("RGB")
image_b = Image.open("large_imageA.jpg").convert("RGB")
image_a = image_a.resize(image_b.size)
flat_a = np.array(image_a).reshape(-1, 3).astype(np.float32)
flat_b = np.array(image_b).reshape(-1, 3).astype(np.float32)

perm = np.arange(len(flat_a))
np.random.shuffle(perm)
perm = anneal(flat_a, flat_b, perm, T=4000.0, alpha=0.999, iterations=200_000_000)

mapped_pixels = flat_a[perm].reshape(np.array(image_a).shape)
Image.fromarray(mapped_pixels.astype('uint8'), 'RGB').save("B_to_A.jpg")

end_time = time.perf_counter()
print(f"Elapsed time for large_imageB -> large_imageA: {end_time - start_time:.2f} seconds")

# -------------------------
# Second pair: large_imageC -> large_imageD
print("Starting annealing for large_imageC -> large_imageD")
start_time = time.perf_counter()

image_a = Image.open("large_imageC.jpg").convert("RGB")
image_b = Image.open("large_imageD.jpg").convert("RGB")
image_a = image_a.resize(image_b.size)
flat_a = np.array(image_a).reshape(-1, 3).astype(np.float32)
flat_b = np.array(image_b).reshape(-1, 3).astype(np.float32)

perm = np.arange(len(flat_a))
np.random.shuffle(perm)
perm = anneal(flat_a, flat_b, perm, T=4000.0, alpha=0.999, iterations=200_000_000)

mapped_pixels = flat_a[perm].reshape(np.array(image_a).shape)
Image.fromarray(mapped_pixels.astype('uint8'), 'RGB').save("C_to_D.jpg")

end_time = time.perf_counter()
print(f"Elapsed time for large_imageC -> large_imageD: {end_time - start_time:.2f} seconds")

# -------------------------
# Reverse: large_imageD -> large_imageC
print("Starting annealing for large_imageD -> large_imageC")
start_time = time.perf_counter()

image_a = Image.open("large_imageD.jpg").convert("RGB")
image_b = Image.open("large_imageC.jpg").convert("RGB")
image_a = image_a.resize(image_b.size)
flat_a = np.array(image_a).reshape(-1, 3).astype(np.float32)
flat_b = np.array(image_b).reshape(-1, 3).astype(np.float32)

perm = np.arange(len(flat_a))
np.random.shuffle(perm)
perm = anneal(flat_a, flat_b, perm, T=4000.0, alpha=0.999, iterations=200_000_000)

mapped_pixels = flat_a[perm].reshape(np.array(image_a).shape)
Image.fromarray(mapped_pixels.astype('uint8'), 'RGB').save("D_to_C.jpg")

end_time = time.perf_counter()
print(f"Elapsed time for large_imageD -> large_imageC: {end_time - start_time:.2f} seconds")

