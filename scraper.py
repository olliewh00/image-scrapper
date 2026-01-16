import os
import json
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS # Added GPSTAGS

def clean_exif_data(exif_data):
    """Converts Tag IDs to names and removes unreadable binary data."""
    clean_data = {}
    if not exif_data:
        return clean_data

    for tag, value in exif_data.items():
        tag_name = TAGS.get(tag, tag)
        
        # Handle GPS specifically
        if tag_name == "GPSInfo":
            gps_data = {}
            for t in value:
                sub_tag = GPSTAGS.get(t, t)
                gps_data[sub_tag] = str(value[t])
            clean_data[tag_name] = gps_data
            
        # Filter out binary blobs
        elif isinstance(value, bytes):
            clean_data[tag_name] = "<Binary Data Removed>"
        else:
            clean_data[tag_name] = str(value)
            
    return clean_data

def run_scraper():
    results = []
    image_folder = "images"

    if not os.path.exists(image_folder):
        os.makedirs(image_folder)
        print(f"📁 Created '{image_folder}' folder. Add JPGs and restart.")
        return

    files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    
    if not files:
        print("Empty folder. No images to process.")
        return

    for filename in files:
        image_path = os.path.join(image_folder, filename)
        try:
            img = Image.open(image_path)
            raw_exif = img._getexif()
            
            if raw_exif:
                cleaned = clean_exif_data(raw_exif)
                cleaned['filename'] = filename
                results.append(cleaned)
                
                # Print clean summary to terminal
                print(f"\n📸 File: {filename}")
                print(f"   Make: {cleaned.get('Make', 'Unknown')}")
                print(f"   Model: {cleaned.get('Model', 'Unknown')}")
                print(f"   Date: {cleaned.get('DateTime', 'Unknown')}")
            else:
                print(f"⚠️  {filename}: No EXIF data found.")
                
        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")

    # Save to JSON
    with open('image_metadata.json', 'w') as f:
        json.dump(results, f, indent=4)
    print(f"\n📂 Success! Data for {len(results)} images saved to image_metadata.json")

if __name__ == "__main__":
   run_scraper()