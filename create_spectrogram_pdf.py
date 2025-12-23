#!/usr/bin/env python3
"""
Generate a PDF containing all spectrograms, one per page in landscape format.
Includes individual spectrograms plus analysis charts.
"""

import json
from pathlib import Path
from PIL import Image
from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

# Paths
SPECTROGRAMS_DIR = Path("spectrograms")
OUTPUT_PDF = SPECTROGRAMS_DIR / "spectrograms_collection.pdf"
METADATA_FILE = Path("metadata.json")

# Load metadata for titles
with open(METADATA_FILE) as f:
    metadata = json.load(f)

# Create lookup by sample ID with short labels
sample_info = {}
for sample in metadata["samples"]:
    sample_id = sample["id"]
    mic = sample["microphone"]
    name = f"{mic['manufacturer']} {mic['model']}"

    # Create short variant descriptor
    variant = ""
    if sample.get("distance_cm"):
        variant = f"{sample['distance_cm']}cm"
    if sample_id == 5:
        variant = "Voicenotes (MP3)"
    elif sample_id == 4:
        variant = "ASR HQ"
    elif sample_id == 7:
        variant = "80cm (long throw)"
    elif sample_id == 11:
        variant = "BT51 dongle"
    elif sample_id == 12:
        variant = "TP-Link BT"
    elif sample_id == 14:
        variant = "Noisy (Mahane Yehuda)"
    elif sample_id == 15:
        variant = "Quiet (home office)"

    sample_info[sample_id] = f"{name}" + (f" / {variant}" if variant else "")

# Get all individual spectrograms in order
individual_spectrograms = sorted(
    SPECTROGRAMS_DIR.glob("spectrogram_[0-9][0-9]_*.png"),
    key=lambda x: int(x.name.split("_")[1])
)

# Analysis charts to include at the end
analysis_charts = [
    SPECTROGRAMS_DIR / "spectrograms_ranked_by_wer.png",
    SPECTROGRAMS_DIR / "correlation_analysis.png",
    SPECTROGRAMS_DIR / "price_vs_wer_analysis.png",
]

# Filter to only existing files
analysis_charts = [f for f in analysis_charts if f.exists()]

print(f"Found {len(individual_spectrograms)} individual spectrograms")
print(f"Found {len(analysis_charts)} analysis charts")

# Create PDF
page_width, page_height = landscape(A4)
c = canvas.Canvas(str(OUTPUT_PDF), pagesize=landscape(A4))

def add_image_page(image_path, title=None):
    """Add an image as a full page, centered with margins."""
    img = Image.open(image_path)
    img_width, img_height = img.size

    # Calculate scaling to fit within margins (0.5 inch on each side)
    margin = 0.5 * inch
    available_width = page_width - 2 * margin
    available_height = page_height - 2 * margin - (0.4 * inch if title else 0)

    # Scale to fit
    scale_w = available_width / img_width
    scale_h = available_height / img_height
    scale = min(scale_w, scale_h)

    final_width = img_width * scale
    final_height = img_height * scale

    # Center on page
    x = (page_width - final_width) / 2
    y = (page_height - final_height) / 2

    # Adjust y if there's a title
    if title:
        y -= 0.2 * inch

    # Draw image
    c.drawImage(str(image_path), x, y, final_width, final_height)

    # Add title if provided
    if title:
        c.setFont("Helvetica-Bold", 14)
        c.drawCentredString(page_width / 2, page_height - 0.4 * inch, title)

    c.showPage()

# Add individual spectrograms
for spec_path in individual_spectrograms:
    # Extract sample ID from filename
    sample_id = int(spec_path.name.split("_")[1])
    title = f"Sample {sample_id}: {sample_info.get(sample_id, 'Unknown')}"
    add_image_page(spec_path, title)
    print(f"  Added: {spec_path.name}")

# Add analysis charts
chart_titles = {
    "spectrograms_ranked_by_wer.png": "All Spectrograms Ranked by Word Error Rate",
    "correlation_analysis.png": "Audio Feature Correlations with WER",
    "price_vs_wer_analysis.png": "Price vs Word Error Rate Analysis",
}

for chart_path in analysis_charts:
    title = chart_titles.get(chart_path.name, chart_path.stem)
    add_image_page(chart_path, title)
    print(f"  Added: {chart_path.name}")

# Save
c.save()
print(f"\nPDF created: {OUTPUT_PDF}")
print(f"Total pages: {len(individual_spectrograms) + len(analysis_charts)}")
