# Project 02: Image Intelligence Scraper (AICV) 📸 🔍

A Python-based data extraction tool designed to parse hidden EXIF (Exchangeable Image File Format) metadata from images. This project serves as the "Data Ingestion" layer for AI Computer Vision pipelines, turning raw pixels into structured, actionable intelligence.

## 🚀 The Mission
Raw images are more than just pixels; they contain "Digital Fingerprints." This tool extracts sensor data, GPS coordinates, and camera settings to create a structured JSON dataset that can be used for training AI models or performing geospatial analysis.

### Key Features:
- **Metadata Sanitization:** Automatically converts raw EXIF Tag IDs into human-readable labels.
- **Binary Filtering:** Detects and removes unreadable binary blobs (MakerNotes) to keep datasets lightweight.
- **GPS Extraction:** Identifies geospatial "GPSInfo" tags for location-based data science.
- **Structured Output:** Exports all findings into a `image_metadata.json` file for easy integration with Pandas or NoSQL databases.

---

## 🛠️ Tech Stack
- **Language:** Python 3.9+
- **Core Library:** `Pillow` (PIL)
- **Data Format:** JSON / EXIF

---

## 📦 Installation & Usage

### 1. Install Dependencies
```bash
pip install Pillow