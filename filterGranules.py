import os
import glob
import shutil
import re
from pyhdf.SD import SD, SDC # Essential for MODIS HDF-EOS files

# --- 1. CONFIGURATION ---

# Define the source and target folders on your HOST OS / local VM filesystem
# IMPORTANT: Replace '/path/to/your/LST/data/' with the actual path where your .hdf files are stored.
SOURCE_DIR = 'C:/BigData/ProjectStaging/data_MODIS_LST' 
TARGET_BASE_DIR = os.path.join(SOURCE_DIR, 'Filtered_Granules')

# Define the Target Bounding Boxes (Lon_min, Lat_min, Lon_max, Lat_max)
BOUNDARIES = {
    'uttarakhand': (77.5, 28.7, 81.0, 31.5),
    'gujarat': (68.0, 20.0, 74.5, 24.5)
}
# Define the file extension pattern
FILE_PATTERN = os.path.join(SOURCE_DIR, 'MOD11A2.*.hdf')

# --- 2. FILE SYSTEM SETUP ---

# Create the target folders
os.makedirs(os.path.join(TARGET_BASE_DIR, 'uttarakhand'), exist_ok=True)
os.makedirs(os.path.join(TARGET_BASE_DIR, 'gujarat'), exist_ok=True)
os.makedirs(os.path.join(TARGET_BASE_DIR, 'other_regions'), exist_ok=True)

# --- 3. GEOSPATIAL EXTRACTION LOGIC ---

def intersects(granule_bbox, region_bbox):
    """Checks if Granule A and Region B bounding boxes intersect."""
    G_minLon, G_minLat, G_maxLon, G_maxLat = granule_bbox
    R_minLon, R_minLat, R_maxLon, R_maxLat = region_bbox
    
    return (G_maxLon > R_minLon and 
            G_minLon < R_maxLon and 
            G_maxLat > R_minLat and 
            G_minLat < R_maxLat)

def get_granule_bbox_from_hdf(filepath):
    """
    Extracts the bounding box from MODIS HDF-EOS metadata (Global Attributes).
    """
    try:
        hdf = SD(filepath, SDC.READ)
        
        # MODIS metadata is often embedded in a string attribute called 'StructMetadata.0' 
        # as Parameter Value Language (PVL).
        metadata_pvl = hdf.attributes()['StructMetadata.0'].split('\n')
        hdf.end() # Close the HDF file handle
        
        # Use regex to find the coordinate values from the PVL string
        # These are standard attribute names in MODIS HDF-EOS files
        min_lon = float(re.search(r'WESTBOUNDINGCOORDINATE\s*=\s*(-?\d+\.?\d*)', ' '.join(metadata_pvl)).group(1))
        max_lon = float(re.search(r'EASTBOUNDINGCOORDINATE\s*=\s*(-?\d+\.?\d*)', ' '.join(metadata_pvl)).group(1))
        min_lat = float(re.search(r'SOUTHBOUNDINGCOORDINATE\s*=\s*(-?\d+\.?\d*)', ' '.join(metadata_pvl)).group(1))
        max_lat = float(re.search(r'NORTHBOUNDINGCOORDINATE\s*=\s*(-?\d+\.?\d*)', ' '.join(metadata_pvl)).group(1))
        
        return (min_lon, min_lat, max_lon, max_lat)

    except Exception as e:
        # If parsing fails, log the error and return a global box to push it to 'other_regions'
        print(f"ERROR: Could not read Bounding Box from {os.path.basename(filepath)}. Error: {e}")
        return (-180.0, -90.0, 180.0, 90.0)


# --- 4. MAIN EXECUTION ---

print(f"Starting granule filtering from: {SOURCE_DIR}")
file_list = glob.glob(FILE_PATTERN)
print(f"Found {len(file_list)} HDF files to process.")

for i, filepath in enumerate(file_list):
    filename = os.path.basename(filepath)
    granule_bbox = get_granule_bbox_from_hdf(filepath)
    target_folder = 'other_regions'

    # 1. Check Uttarakhand (Priority 1)
    if intersects(granule_bbox, BOUNDARIES['uttarakhand']):
        target_folder = 'uttarakhand'
    
    # 2. Check Gujarat (Priority 2)
    elif intersects(granule_bbox, BOUNDARIES['gujarat']):
        target_folder = 'gujarat'
        
    # 3. Otherwise, it defaults to 'other_regions'

    # Move the file
    target_path = os.path.join(TARGET_BASE_DIR, target_folder, filename)
    shutil.move(filepath, target_path)
    
    if i % 50 == 0:
        print(f"Processed {i} files. Moving {filename} to {target_folder}/")

print("\n--- Filtering complete ---")
print(f"Uttarakhand LST data is isolated in: {os.path.join(TARGET_BASE_DIR, 'uttarakhand')}/")