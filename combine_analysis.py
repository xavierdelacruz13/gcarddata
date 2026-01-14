#!/usr/bin/env python3
"""
Combines batch analysis JSON files into a single card_analysis.json
Run this after all batch analysis agents complete.
"""
import json
import os
from pathlib import Path

BASE_DIR = Path("/Users/xavierdelacruz/Documents/G-Test")

def combine_batch_files():
    """Combine all analysis_batch*.json files into card_analysis.json"""
    all_cards = []

    batch_files = [
        BASE_DIR / "analysis_batch1.json",
        BASE_DIR / "analysis_batch2a.json",
        BASE_DIR / "analysis_batch2b.json",
        BASE_DIR / "analysis_batch2c.json",
        BASE_DIR / "analysis_batch3.json",
        BASE_DIR / "analysis_batch4.json",
    ]

    for batch_file in batch_files:
        if batch_file.exists():
            print(f"Loading {batch_file.name}...")
            with open(batch_file, 'r') as f:
                batch_data = json.load(f)
                # Handle both array format and object with "cards" property
                if isinstance(batch_data, list):
                    cards = batch_data
                elif isinstance(batch_data, dict) and 'cards' in batch_data:
                    cards = batch_data['cards']
                else:
                    print(f"  Warning: Unknown format in {batch_file.name}")
                    continue
                all_cards.extend(cards)
                print(f"  Added {len(cards)} cards")
        else:
            print(f"Warning: {batch_file.name} not found")

    # Sort by rank
    all_cards.sort(key=lambda x: x.get('rank', 999))

    # Write combined file
    output_file = BASE_DIR / "card_analysis.json"
    with open(output_file, 'w') as f:
        json.dump(all_cards, f, indent=2)

    print(f"\nCombined {len(all_cards)} cards into {output_file}")

    # Print summary stats
    if all_cards:
        occasions = {}
        styles = {}
        for card in all_cards:
            occ = card.get('occasion', 'unknown')
            style = card.get('design_style', 'unknown')
            occasions[occ] = occasions.get(occ, 0) + 1
            styles[style] = styles.get(style, 0) + 1

        print("\n--- Occasion Distribution ---")
        for occ, count in sorted(occasions.items(), key=lambda x: -x[1]):
            print(f"  {occ}: {count}")

        print("\n--- Design Style Distribution ---")
        for style, count in sorted(styles.items(), key=lambda x: -x[1]):
            print(f"  {style}: {count}")

if __name__ == "__main__":
    combine_batch_files()
