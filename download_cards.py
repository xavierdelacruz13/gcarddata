#!/usr/bin/env python3
"""
Download card images from Givingli API based on CSV data.
Uses curl for reliable SSL handling on macOS.
"""

import csv
import os
import re
import json
import subprocess
from pathlib import Path

def extract_card_ids(csv_path):
    """Extract card IDs from Column B of the CSV file."""
    card_ids = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header row
        for row in reader:
            if len(row) >= 2:
                # Column B contains format like "1809_Have the Best Birthday Ever Paper&Stuff"
                card_name = row[1]
                # Extract the number before the underscore
                match = re.match(r'^(\d+)_', card_name)
                if match:
                    card_id = match.group(1)
                    card_ids.append((card_id, card_name))
    return card_ids

def fetch_card_data(card_id):
    """Fetch card data from the Givingli API using curl."""
    url = f"https://app.givingli.com/api/v3/cards/{card_id}"
    try:
        result = subprocess.run(
            ['curl', '-s', url],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            data = json.loads(result.stdout)
            # API returns nested result object
            return data.get('result', data)
        else:
            print(f"Error fetching card {card_id}: curl returned {result.returncode}")
            return None
    except Exception as e:
        print(f"Error fetching card {card_id}: {e}")
        return None

def download_image(url, output_path):
    """Download image from URL using curl and save to output path."""
    try:
        result = subprocess.run(
            ['curl', '-s', '-o', str(output_path), url],
            capture_output=True,
            timeout=60
        )
        if result.returncode == 0 and output_path.exists() and output_path.stat().st_size > 0:
            return True
        else:
            print(f"Error downloading image: curl returned {result.returncode}")
            return False
    except Exception as e:
        print(f"Error downloading image: {e}")
        return False

def get_image_url(card_data, size='large'):
    """Extract image URL from card data."""
    if not card_data:
        return None

    # Check for pictures nested object
    pictures = card_data.get('pictures', {})
    if pictures and size in pictures:
        return pictures[size]

    # Fallback to other sizes
    for fallback_size in ['large', 'medium', 'small']:
        if fallback_size in pictures:
            return pictures[fallback_size]

    return None

def sanitize_filename(name):
    """Sanitize filename by removing/replacing invalid characters."""
    # Remove the ID prefix since we'll add it back
    name = re.sub(r'^\d+_', '', name)
    # Replace invalid filename characters
    name = re.sub(r'[<>:"/\\|?*]', '_', name)
    # Limit length
    return name[:100]

def main():
    csv_path = "/Users/xavierdelacruz/Documents/G-Test/Top 300 Cards - 2025.csv"
    output_dir = Path("/Users/xavierdelacruz/Documents/G-Test/card_images")

    # Create output directory
    output_dir.mkdir(exist_ok=True)

    # Extract card IDs
    print("Extracting card IDs from CSV...")
    cards = extract_card_ids(csv_path)
    print(f"Found {len(cards)} cards")

    # Track progress
    success_count = 0
    failed_cards = []

    for i, (card_id, card_name) in enumerate(cards, 1):
        print(f"[{i}/{len(cards)}] Processing card {card_id}...", flush=True)

        # Fetch card data
        card_data = fetch_card_data(card_id)
        if not card_data:
            print(f"  Failed to fetch card data for {card_id}")
            failed_cards.append((card_id, card_name, "API fetch failed"))
            continue

        # Get image URL
        image_url = get_image_url(card_data)
        if not image_url:
            print(f"  No image URL found for card {card_id}")
            failed_cards.append((card_id, card_name, "No image URL"))
            continue

        # Determine file extension from URL
        ext = '.jpg'  # Default
        if '.png' in image_url.lower():
            ext = '.png'
        elif '.gif' in image_url.lower():
            ext = '.gif'

        # Create filename
        safe_name = sanitize_filename(card_name)
        filename = f"{card_id}_{safe_name}{ext}"
        output_path = output_dir / filename

        # Download image
        if download_image(image_url, output_path):
            print(f"  Downloaded: {filename}")
            success_count += 1
        else:
            print(f"  Failed to download image for card {card_id}")
            failed_cards.append((card_id, card_name, "Download failed"))

    # Summary
    print("\n" + "="*50)
    print(f"Download complete!")
    print(f"Successful: {success_count}/{len(cards)}")
    print(f"Failed: {len(failed_cards)}")

    if failed_cards:
        print("\nFailed cards:")
        for card_id, card_name, reason in failed_cards:
            print(f"  {card_id}: {reason}")

    # Save failed cards to file
    if failed_cards:
        failed_path = output_dir / "failed_downloads.txt"
        with open(failed_path, 'w') as f:
            for card_id, card_name, reason in failed_cards:
                f.write(f"{card_id},{card_name},{reason}\n")
        print(f"\nFailed cards list saved to: {failed_path}")

if __name__ == "__main__":
    main()
