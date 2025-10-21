import earthaccess
from tqdm import tqdm
import os
import datetime

# --- Configuration for Successful Download ---

# NOTE: MERRA-2 data has a latency (1-2 months delay).
# For reliable model training, 10-15 years of continuous data is a good minimum.
# This range targets the last 20 years of available, processed data.
TEMPORAL_RANGE = ("2005-01-01", "2024-09-30")

# CHANGED SHORT NAME: Switched to a highly reliable Monthly Mean Surface Flux Diagnostics collection.
# This collection (M2TMNXFLX) includes variables like surface temperature, precipitation, and energy fluxes.
MERRA_SHORT_NAME = "M2TMNXFLX" 

# Geographic Bounding Box for Uttarakhand, India
UTTARAKHAND_BBOX = (77.5, 28.7, 81.0, 31.5)

# Local directory where data will be downloaded
MERRA_DOWNLOAD_DIR = "C:/BigData/ProjectStaging/data_MERRA2_Reanalysis"


# 1. Authentication (Will prompt for credentials if not already logged in)
print("Attempting Earthdata Login...")
try:
    auth = earthaccess.login()
    print("✅ Authentication successful.")
except Exception as e:
    print(f"❌ Authentication failed: {e}. Please ensure you have valid Earthdata credentials.")
    exit()

# 2. Search for Data
print(f"\nSearching for {MERRA_SHORT_NAME} data over Uttarakhand (Temporal Range: {TEMPORAL_RANGE[0]} to {TEMPORAL_RANGE[1]})...")
try:
    merra_results = earthaccess.search_data(
        short_name=MERRA_SHORT_NAME,
        bounding_box=UTTARAKHAND_BBOX,
        temporal=TEMPORAL_RANGE,
        cloud_hosted=True
    )
    
    num_results = len(merra_results)
    print(f"Found {num_results} MERRA-2 granules.")

    # 3. Download Data
    if merra_results:
        print(f"Starting download of MERRA-2 data to {MERRA_DOWNLOAD_DIR}...")
        os.makedirs(MERRA_DOWNLOAD_DIR, exist_ok=True)

        # Download granules using tqdm for progress tracking
        # We wrap the results iterator in tqdm, which will track each file (granule) being downloaded.
        # earthaccess handles the download process, and tqdm shows the file count progress.
        for result in tqdm(merra_results, desc="Downloading MERRA-2 Granules", unit="file"):
            earthaccess.download([result], MERRA_DOWNLOAD_DIR)


        print("\n✅ MERRA-2 Download complete!")
        print(f"Data saved in: {MERRA_DOWNLOAD_DIR}")
    else:
        print("\n❌ No MERRA-2 granules found matching the search criteria. Try expanding the temporal range.")

except Exception as e:
    print(f"\nAn error occurred during search or download: {e}")
