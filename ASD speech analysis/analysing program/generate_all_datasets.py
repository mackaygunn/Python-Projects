import json
import random
import os

# --- VERIFIED PATH CONFIGURATION ---
scores_file = r"C:\Users\Ramiru\Documents\Programming\Python language\Python projects\ASD Speech recognition AI model\speechocean762\resource\scores.json"
gender_file = r"C:\Users\Ramiru\Documents\Programming\Python language\Python projects\ASD Speech recognition AI model\speechocean762\train\spk2gender"
output_dir = r"C:\Users\Ramiru\Documents\Programming\Python language\Python projects\ASD Speech recognition AI model\analysing program"

file_full = os.path.join(output_dir, 'full_unbalanced_dataset.json')
file_balanced = os.path.join(output_dir, 'balanced_dataset.json')
file_leftovers = os.path.join(output_dir, 'leftovers_testing_dataset.json')

os.makedirs(output_dir, exist_ok=True)

# 1. Load the Gender Mapping
speaker_to_gender = {}
try:
    with open(gender_file, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 2:
                numeric_id = ''.join(filter(str.isdigit, parts[0]))
                if numeric_id:
                    clean_id = numeric_id.zfill(5)
                    speaker_to_gender[clean_id] = "male" if parts[1].upper() == 'M' else "female"
except FileNotFoundError:
    print(f"ERROR: Cannot find spk2gender at {gender_file}")
    exit()

# 2. Load the Scores
try:
    with open(scores_file, 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    print(f"ERROR: Cannot find scores.json at {scores_file}")
    exit()

# 3. Create the sorting structures
full_data = {"typical": {"male": {}, "female": {}}, "atypical": {"male": {}, "female": {}}}
balanced_data = {"typical": {"male": {}, "female": {}}, "atypical": {"male": {}, "female": {}}}
leftovers_data = {"typical": {"male": {}, "female": {}}, "atypical": {"male": {}, "female": {}}}

# 4. Populate the Full Dataset
for utterance_id, metrics in data.items():
    score = metrics.get('total', 0)
    speaker_id = utterance_id[:5]
    gender = speaker_to_gender.get(speaker_id)
    
    if gender:
        category = "typical" if score >= 7 else "atypical"
        full_data[category][gender][utterance_id] = {
            "gender": gender,
            "score": score
        }

# 5. Determine the Limiting Factor for Balancing
min_count = min(
    len(full_data["typical"]["male"]), len(full_data["typical"]["female"]),
    len(full_data["atypical"]["male"]), len(full_data["atypical"]["female"])
)

# 6. Perform Balancing and Isolate Leftovers
random.seed(42) # Locked for reproducibility

for category in ["typical", "atypical"]:
    for gender in ["male", "female"]:
        all_keys = list(full_data[category][gender].keys())
        
        # Randomly select keys for the balanced dataset
        sampled_keys = set(random.sample(all_keys, min_count))
        
        for k in all_keys:
            entry = full_data[category][gender][k]
            if k in sampled_keys:
                balanced_data[category][gender][k] = entry
            else:
                leftovers_data[category][gender][k] = entry

# 7. Save all three files
with open(file_full, 'w') as f: json.dump(full_data, f, indent=4)
with open(file_balanced, 'w') as f: json.dump(balanced_data, f, indent=4)
with open(file_leftovers, 'w') as f: json.dump(leftovers_data, f, indent=4)

# Print Summary
print("--- DATA EXTRACTION COMPLETE ---")
print(f"1. Full Unbalanced Data: {sum(len(full_data[c][g]) for c in full_data for g in full_data[c])} utterances -> Saved to {file_full}")
print(f"2. Balanced Training Data: {sum(len(balanced_data[c][g]) for c in balanced_data for g in balanced_data[c])} utterances -> Saved to {file_balanced}")
print(f"3. Leftover Testing Data: {sum(len(leftovers_data[c][g]) for c in leftovers_data for g in leftovers_data[c])} utterances -> Saved to {file_leftovers}")