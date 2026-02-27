# Study Spot Data Generation
# This notebook generates a synthetic dataset representing cafes and libraries used as study spots for the Spot2Go ranking model.

import pandas as pd
import numpy as np

np.random.seed(42)

NUM_SPOTS = 200 # Synthetic dataset size which is reasonable

# Attribute 1:
spot_ids = [f"spot{i}" for i in range(1, NUM_SPOTS+1)]

# Attribute 2
spot_types = np.random.choice(
    ["cafe", "library"],
    size = NUM_SPOTS,
    p = [0.7, 0.3]
)