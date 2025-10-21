import earthaccess
from tqdm import tqdm
import os

# Authenticate with Earthdata. This is necessary to download data.
# The user will be prompted to log in through the browser if not already authenticated.
#auth = earthaccess.login()

# MERRA-2 Short Name (Using GPM_3IMERGHH as it was in the original script)
# GPM_3IMERGHH is the Half-hourly GPM IMERG data.
short_name = "GPM_3IMERGHL"

# Bounding box for Uttarakhand, India
# (Min Longitude, Min Latitude, Max Longitude, Max Latitude)
uttarakhand_bbox = (77.5, 28.7, 81.0, 31.5)

# *** UPDATED TEMPORAL RANGE ***
# Set the temporal range for the entire months of August and September 2025.
# (Start Date YYYY-MM-DD, End Date YYYY-MM-DD)
temporal_range = ("2025-08-01", "2025-09-30")

# Define the local directory where data will be saved
download_dir = "C:/BigData/ProjectStaging/uttarakhand_gpm_data_aug_sep"

print(f"Searching for {short_name} data over Uttarakhand from {temporal_range[0]} to {temporal_range[1]}...")

# Search for data granules matching the criteria
results = earthaccess.search_data(
    short_name=short_name,
    bounding_box=uttarakhand_bbox,
    temporal=temporal_range,
    cloud_hosted=True
)

print(f"Found {len(results)} granules.")

if results:
    print(f"Starting download of GPM IMERG data to {download_dir}...")
    
    # Create the download directory if it doesn't exist
    os.makedirs(download_dir, exist_ok=True)

    # Download the files using tqdm for a progress bar
    for granule in tqdm(results, desc="Downloading GPM IMERG Files", unit="file"):
        earthaccess.download([granule], download_dir)

    print("✅ Download complete! The data is saved in the specified directory.")
else:
    print("❌ No granules found matching the search criteria for the given period.")
