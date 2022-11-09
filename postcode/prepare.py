import os
import sys
import pandas as pd
import logging

logger = logging.getLogger(__name__)

from config import PARQUET_FILE

if __name__ == '__main__':
    '''
    Get the latest ONS Postcode Database from the ONS.

    https://www.ons.gov.uk/methodology/geography/geographicalproducts/postcodeproducts
    '''
    onspd_csv = sys.argv[1]

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
    centroids = centroids.round({'lat': 5, 'long': 5})
    centroids.to_parquet(PARQUET_FILE)

