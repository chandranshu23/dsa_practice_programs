import earthaccess
from tqdm import tqdm
import os

auth = earthaccess.login()

LST_SHORT_NAME = "MOD11A2"
UTTARAKHAND_BBOX = (77.5, 28.7, 81.0, 31.5)
TEMPORAL_RANGE = ("2002-01-01", "2020-12-31")
LST_DOWNLOAD_DIR = "C:/BigData/ProjectStaging/data_MODIS_LST"

print(f"Searching for {LST_SHORT_NAME} data over Uttarakhand ({TEMPORAL_RANGE[0]} to {TEMPORAL_RANGE[1]})...")
lst_results = earthaccess.search_data(
    short_name=LST_SHORT_NAME,
    bounding_box=UTTARAKHAND_BBOX,
    temporal=TEMPORAL_RANGE,
    cloud_hosted=True
)
print(f"Found {len(lst_results)} LST granules.")

if lst_results:
    print(f"Starting download of LST data to {LST_DOWNLOAD_DIR}...")
    os.makedirs(LST_DOWNLOAD_DIR, exist_ok=True)

    for granule in tqdm(lst_results, desc="Downloading MODIS LST Files", unit="file"):
        earthaccess.download([granule], LST_DOWNLOAD_DIR)

    print("✅ MODIS LST Download complete!")
else:
    print("❌ No LST granules found matching the search criteria.")
