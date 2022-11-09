import sys
import pandas as pd
import geopandas as gpd
import logging
from config import PARQUET_FILE, CENTROIDS_JSON

logger = logging.getLogger(__name__)

properties = ['pcds', 'oslaua', 'osward', 'lsoa11', 'msoa11']


def save_as_geojson(data):
    data = gpd.GeoDataFrame(
        data[properties], geometry=gpd.points_from_xy(data.long, data.lat)
    )
    centroids.to_file(CENTROIDS_JSON, driver='GeoJSON')


if __name__ == '__main__':
    onspd_extract_csv = sys.argv[1]
    logger.info('Reading existing Parquet file')
    centroids = pd.read_parquet(PARQUET_FILE)

    centroids[properties].to_csv(
        onspd_extract_csv, index=False)
