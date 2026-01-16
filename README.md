# Project 02: Image Intelligence Scraper (AICV) 📸 🔍

A Python-based data extraction tool designed to parse hidden EXIF (Exchangeable Image File Format) metadata from images. This project serves as the "Data Ingestion" layer for AI Computer Vision pipelines.

## 🚀 The Mission
Raw images contain "Digital Fingerprints." This tool extracts sensor data, GPS coordinates, and camera settings to create a structured JSON dataset for AI training or geospatial analysis.

### Key Features:
- **Metadata Sanitization:** Maps raw EXIF Tag IDs (e.g., `271`) to human-readable labels (`Make`).
- **Binary Filtering:** Automatically identifies and removes unreadable binary blobs (MakerNotes) to keep datasets clean.
- **GPS Extraction:** Parses geospatial data for location-based intelligence.
- **Structured Output:** Generates `image_metadata.json` for seamless integration with Data Science tools.

---

## 🛠️ Tech Stack
- **Language:** Python 3.9+
- **Core Library:** `Pillow`
- **Environment:** Docker

---

## 📦 Installation & Docker Execution

### 1. Build the Image
Ensure you are in the project root folder:
```bash
docker build -t image-scraper .