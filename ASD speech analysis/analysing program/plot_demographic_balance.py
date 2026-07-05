import json
import os
import matplotlib.pyplot as plt
import numpy as np

# --- VERIFIED PATH CONFIGURATION ---
scores_file = r"C:\Users\Ramiru\Documents\Programming\Python language\Python projects\ASD Speech recognition AI model\speechocean762\resource\scores.json"
gender_file = r"C:\Users\Ramiru\Documents\Programming\Python language\Python projects\ASD Speech recognition AI model\speechocean762\train\spk2gender"
output_dir = r"C:\Users\Ramiru\Documents\Programming\Python language\Python projects\ASD Speech recognition AI model\analysing program"

# 1. Load the Gender Mapping (WITH ROBUST PARSING)
speaker_to_gender = {}
try:
    with open(gender_file, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 2:
                raw_spk_id = parts[0]
                # Strip all letters, keep only numbers, and pad to 5 digits
                numeric_id = ''.join(filter(str.isdigit, raw_spk_id))
                if numeric_id: 
                    clean_id = numeric_id.zfill(5) 
                    speaker_to_gender[clean_id] = "Male" if parts[1].upper() == 'M' else "Female"
except FileNotFoundError:
    print(f"ERROR: Cannot find spk2gender at {gender_file}")
    exit()

# 2. Load the Scores and Calculate Raw Counts
try:
    with open(scores_file, 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    print(f"ERROR: Cannot find scores.json at {scores_file}")
    exit()

raw_counts = {"Typical": {"Male": 0, "Female": 0}, "Atypical": {"Male": 0, "Female": 0}}

for utt_id, metrics in data.items():
    score = metrics.get('total', 0)
    spk_id = utt_id[:5]
    gender = speaker_to_gender.get(spk_id)
    
    if gender:
        cat = "Typical" if score >= 7 else "Atypical"
        raw_counts[cat][gender] += 1

# 3. Calculate Balanced Counts (Based on the limiting factor)
min_count = min(
    raw_counts["Typical"]["Male"], raw_counts["Typical"]["Female"],
    raw_counts["Atypical"]["Male"], raw_counts["Atypical"]["Female"]
)

balanced_counts = {"Typical": {"Male": min_count, "Female": min_count}, 
                   "Atypical": {"Male": min_count, "Female": min_count}}

# --- PLOTTING ---
labels = ['Typical (>=7)', 'Atypical (<7)']
x = np.arange(len(labels))
width = 0.35  # width of the bars

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Demographic Distribution: Mitigating Gender Bias in Training Data', fontsize=16, fontweight='bold')

# Helper function to add value labels
def add_labels(ax, rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontweight='bold')

# --- PLOT 1: BEFORE (RAW DATA) ---
raw_males = [raw_counts['Typical']['Male'], raw_counts['Atypical']['Male']]
raw_females = [raw_counts['Typical']['Female'], raw_counts['Atypical']['Female']]

rects1 = ax1.bar(x - width/2, raw_males, width, label='Male', color='#1976D2')
rects2 = ax1.bar(x + width/2, raw_females, width, label='Female', color='#E91E63')

ax1.set_ylabel('Number of Utterances', fontweight='bold')
ax1.set_title('BEFORE: Raw Demographic Imbalance', color='red', fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(labels, fontweight='bold')
ax1.legend()
ax1.set_ylim(0, max(max(raw_males), max(raw_females)) * 1.15)
add_labels(ax1, rects1)
add_labels(ax1, rects2)

# --- PLOT 2: AFTER (BALANCED DATA) ---
bal_males = [balanced_counts['Typical']['Male'], balanced_counts['Atypical']['Male']]
bal_females = [balanced_counts['Typical']['Female'], balanced_counts['Atypical']['Female']]

rects3 = ax2.bar(x - width/2, bal_males, width, label='Male', color='#1976D2')
rects4 = ax2.bar(x + width/2, bal_females, width, label='Female', color='#E91E63')

ax2.set_title('AFTER: 4-Way Balanced Baseline', color='green', fontweight='bold')
ax2.set_xticks(x)
ax2.set_xticklabels(labels, fontweight='bold')
ax2.legend()
ax2.set_ylim(0, max(max(bal_males), max(bal_females)) * 1.3) # Give some headroom
add_labels(ax2, rects3)
add_labels(ax2, rects4)

# Save and Show
plt.tight_layout()
output_image = os.path.join(output_dir, 'demographic_balance_comparison.png')
plt.savefig(output_image, dpi=300)
print(f"\nGraph saved successfully to: {output_image}")
plt.show()