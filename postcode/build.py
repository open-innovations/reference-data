import pandas as pd
import geopandas as gpd
import logging
from config import PARQUET_FILE, CENTROIDS_JSON, CENTROIDS_CSV

logger = logging.getLogger(__name__)

properties = ['pcds', 'oslaua', 'osward', 'lsoa11', 'msoa11']


def save_as_geojson(data):
    data = gpd.GeoDataFrame(
        data[properties], geometry=gpd.points_from_xy(data.long, data.lat)
    )
    centroids.to_file(CENTROIDS_JSON, driver='GeoJSON')


if __name__ == '__main__':
    logger.info('Reading existing Parquet file')
    centroids = pd.read_parquet(PARQUET_FILE)

    centroids[properties].to_csv(
        CENTROIDS_CSV, index=False)
