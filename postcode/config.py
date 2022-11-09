import os

WORKING_DIR = 'working'
OUTPUT_DIR = 'output'

os.makedirs(WORKING_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

PARQUET_FILE = os.path.join(WORKING_DIR, 'postcodes.parquet')
CENTROIDS_CSV = os.path.join(OUTPUT_DIR, 'postcodes.csv')
CENTROIDS_JSON = os.path.join(OUTPUT_DIR, 'postcodes.geojson')
