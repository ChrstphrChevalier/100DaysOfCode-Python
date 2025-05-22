from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

def extract_dominant_colors(image_path, max_size=500, n_colors=5):
    image = Image.open(image_path)
    image = image.convert("RGB")

    if max(image.size) > max_size:
        image.thumbnail((max_size, max_size))

    pixels = np.array(image).reshape(-1, 3)

    kmeans = KMeans(n_clusters=n_colors, n_init=10)
    kmeans.fit(pixels)
    centers = kmeans.cluster_centers_.astype(int)

    colors = []
    for center in centers:
        r, g, b = (int(c) for c in center)
        hex_code = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        colors.append({
            'hex': hex_code,
            'rgb': (r, g, b)
        })

    return colors