import os
import pandas as pd
import logging

logger = logging.getLogger(__name__)

os.makedirs('working', exist_ok=True)
os.makedirs('data', exist_ok=True)

PARQUET_FILE = os.path.join('working', 'postcodes.parquet')
CENTROIDS_CSV = os.path.join('data', 'reference', 'postcodes.csv')


def create_centroid_file(onspd_csv):
    '''
    Get the latest ONS Postcode Database from the ONS.

    https://www.ons.gov.uk/methodology/geography/geographicalproducts/postcodeproducts
    '''
    if not os.path.exists(onspd_csv):
        logger.error('Cannot find source CSV')
        raise "Can't find source CSV {0}. Have you downloaded it?".format(
            onspd_csv)

    """
      pcds       Postcode (variable length with spaces)
      lat, long  Centroid of postcode - lat/long
      pcon       Westminster parliamentary constituency
      oslaua     Local authority district (LAD)/unitary authority (UA)/ metropolitan district (MD)/ London borough (LB)/ council area (CA)/district council area (DCA)
      osward     (Electoral) ward/division
      lsoa11     2011 Census Lower Layer Super Output Area (LSOA)/ Data Zone (DZ)/ SOA
      msoa11     2011 Census Middle Layer Super Output Area (MSOA)/ Intermediate Zone (IZ)
    """
    columns = 'pcds lat long pcon oslaua osward lsoa11 msoa11'.split()
    logger.info('Processing CSV to Parquet')
    centroids = pd.read_csv(onspd_csv, usecols=columns)
    centroids.to_parquet(PARQUET_FILE)


def get_centroids():
    logger.info('Reading existing Parquet file')
    centroids = pd.read_parquet(PARQUET_FILE)

    return centroids


def create_geographic_files():
    # Round numeric values to 5 decimal places
    centroids = centroids.round({'lat': 5, 'long': 5})
    centroids = gpd.GeoDataFrame(
        centroids, geometry=gpd.points_from_xy(
            centroids.long, centroids.lat)
    )


def save_ref_csv(centroids):
    centroids[['pcds', 'oslaua', 'osward']].to_csv(
        CENTROIDS_CSV, index=False)

