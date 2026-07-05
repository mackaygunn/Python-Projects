import json
import os
import numpy as np
import matplotlib.pyplot as plt

# --- PATH CONFIGURATION ---
scores_file = r"C:\Users\Ramiru\Documents\Programming\Python language\Python projects\ASD Speech recognition AI model\speechocean762\resource\scores.json"
balanced_file = r"C:\Users\Ramiru\Documents\Programming\Python language\Python projects\ASD Speech recognition AI model\analysing program\balanced_dataset.json"
output_dir = r"C:\Users\Ramiru\Documents\Programming\Python language\Python projects\ASD Speech recognition AI model\Feature comparison"

# Create the new folder if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# 1. Load the Data
try:
    with open(scores_file, 'r') as f:
        raw_scores = json.load(f)
    with open(balanced_file, 'r') as f:
        balanced_data = json.load(f)
except FileNotFoundError as e:
    print(f"ERROR: {e}")
    exit()

features = ['accuracy', 'completeness', 'fluency', 'prosodic']
typical_data = {f: [] for f in features}
atypical_data = {f: [] for f in features}

# 2. Extract Data and Save to Text File
output_txt = os.path.join(output_dir, 'extracted_feature_scores.txt')

with open(output_txt, 'w') as out_f:
    # Write the column headers for the text file
    out_f.write("Utterance_ID\tCategory\tGender\tAccuracy\tCompleteness\tFluency\tProsodic\n")
    
    for category in ["typical", "atypical"]:
        for gender in ["male", "female"]:
            for utt_id in balanced_data[category][gender].keys():
                metrics = raw_scores.get(utt_id, {})
                
                acc = metrics.get('accuracy', 0)
                comp = metrics.get('completeness', 0)
                flu = metrics.get('fluency', 0)
                pros = metrics.get('prosodic', 0)
                
                # Write the row to the text file
                out_f.write(f"{utt_id}\t{category}\t{gender}\t{acc}\t{comp}\t{flu}\t{pros}\n")
                
                # Store data in arrays for our mathematical analysis
                if category == "typical":
                    typical_data['accuracy'].append(acc)
                    typical_data['completeness'].append(comp)
                    typical_data['fluency'].append(flu)
                    typical_data['prosodic'].append(pros)
                else:
                    atypical_data['accuracy'].append(acc)
                    atypical_data['completeness'].append(comp)
                    atypical_data['fluency'].append(flu)
                    atypical_data['prosodic'].append(pros)

print(f"\n✅ SUCCESS: Extracted scores saved to: {output_txt}")

# 3. Calculate Means, StDevs, and Find the BEST Feature
print("\n--- STATISTICAL ANALYSIS ---")
best_feature = None
max_gap = -1

typ_means, typ_stds = [], []
atyp_means, atyp_stds = [], []

for f in features:
    t_mean = np.mean(typical_data[f])
    t_std = np.std(typical_data[f])
    a_mean = np.mean(atypical_data[f])
    a_std = np.std(atypical_data[f])
    
    # The "Gap" is the mathematical difference between Typical and Atypical scores
    gap = abs(t_mean - a_mean)
    
    typ_means.append(t_mean)
    typ_stds.append(t_std)
    atyp_means.append(a_mean)
    atyp_stds.append(a_std)
    
    print(f"{f.capitalize()}: Typical Mean = {t_mean:.2f}, Atypical Mean = {a_mean:.2f} | GAP = {gap:.2f}")
    
    if gap > max_gap:
        max_gap = gap
        best_feature = f

print("-" * 30)
print(f"🏆 THE MATHEMATICALLY BEST FEATURE IS: {best_feature.upper()} (Gap: {max_gap:.2f})")
print("-" * 30)

# 4. Plot the Bar Chart with Error Bars
x = np.arange(len(features))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width/2, typ_means, width, yerr=typ_stds, label='Typical (>=7)', color='#2196F3', edgecolor='black', capsize=5)
rects2 = ax.bar(x + width/2, atyp_means, width, yerr=atyp_stds, label='Atypical (<7)', color='#F44336', edgecolor='black', capsize=5)

ax.set_ylabel('Average Assigned Score (0-10)', fontweight='bold')
ax.set_title('Feature Means and Variance: Identifying the Best Predictor', fontweight='bold', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels([f.capitalize() for f in features], fontweight='bold')
ax.legend()
ax.set_ylim(0, 11)

plt.tight_layout()
output_image = os.path.join(output_dir, 'feature_comparison_bars.png')
plt.savefig(output_image, dpi=300)
print(f"✅ Bar graph saved to: {output_image}\n")
plt.show()