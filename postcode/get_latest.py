import io
import re
import urllib.request
import zipfile

# Find the latest version of this from here
# https://geoportal.statistics.gov.uk/search?collection=Dataset&sort=-created&tags=all(PRD_ONSPD)
ONSPD_LATEST_ZIP = "https://www.arcgis.com/sharing/rest/content/items/94ccfba68a634adfb69371b458d71d12/data"

if __name__ == '__main__':
    with urllib.request.urlopen(ONSPD_LATEST_ZIP) as f:
        zip_content = io.BytesIO(f.read())

    onspd_zip = zipfile.ZipFile(zip_content)
    csv = [entry for entry in onspd_zip.namelist(
    ) if re.match(r'Data/[^/]*csv$', entry)].pop()

    with onspd_zip.open(csv) as z:
        data = z.read().decode('utf-8')

    with open('input/onspd.csv', 'w') as o:
        o.write(data)
