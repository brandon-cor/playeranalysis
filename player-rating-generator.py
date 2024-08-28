import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import math

physical_ratings = {'Passing': [], 'Shooting': [], 'Dribbling': [], 'Defensive': []}

# Normalize a stat to a scale of 10
def normalize_stat(stat, max_value):
    return 10 * (stat / max_value)

# File path
file_path = 'player-stats/player-stats-M-Corcoran.xlsx'  # Change to your file path
label_name = os.path.basename(file_path).replace('player-stats-', '').replace('.csv', '').replace('.xlsx', '')

# Determine file type and read data
if file_path.endswith('.csv'):
    with open(file_path, encoding="utf-8") as f_in:
        csv_reader = csv.reader(f_in)
        header = next(csv_reader)  # Skip the header row if there is one

        for line in csv_reader:
            # Assuming max values for the stats are known
            max_stat = 100  # Example max value, adjust according to your data

            # Replace with the correct indices for passing, shooting, dribbling, and defensive stats
            passing = normalize_stat(float(line[24]), max_stat)
            shooting = normalize_stat(float(line[25]), max_stat)
            dribbling = normalize_stat(float(line[26]), max_stat)
            defensive = normalize_stat(float(line[27]), max_stat)

            physical_ratings['Passing'].append(passing)
            physical_ratings['Shooting'].append(shooting)
            physical_ratings['Dribbling'].append(dribbling)
            physical_ratings['Defensive'].append(defensive)

elif file_path.endswith('.xlsx'):
    df = pd.read_excel(file_path)
    
    # Assuming the columns for passing, shooting, dribbling, and defensive stats are 24, 25, 26, 27
    max_stat = 100  # Example max value, adjust according to your data
    
    physical_ratings['Passing'] = normalize_stat(df.iloc[:, 24], max_stat).tolist()
    physical_ratings['Shooting'] = normalize_stat(df.iloc[:, 25], max_stat).tolist()
    physical_ratings['Dribbling'] = normalize_stat(df.iloc[:, 26], max_stat).tolist()
    physical_ratings['Defensive'] = normalize_stat(df.iloc[:, 27], max_stat).tolist()

else:
    raise ValueError("Unsupported file format. Please use a CSV or XLSX file.")

# Calculate the average rating for each skill
average_ratings = {key: np.mean(values) for key, values in physical_ratings.items()}

# Print the individual average scores used in the radar chart
print("Average Passing Score:", average_ratings['Passing'])
print("Average Shooting Score:", average_ratings['Shooting'])
print("Average Dribbling Score:", average_ratings['Dribbling'])
print("Average Defensive Score:", average_ratings['Defensive'])

# Calculate the overall rating as the average of all the categories
overall_rating = math.floor(np.mean(list(average_ratings.values())) * 100)

# Print the overall rating
print(f"Overall Rating: {overall_rating}")

# Radar chart (circle graph) plot
categories = list(average_ratings.keys())
values = list(average_ratings.values())

# We need to complete the loop and set the values for the radar chart
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
values += values[:1]  # Ensure values completes the loop
angles += angles[:1]  # Ensure angles completes the loop

# Plotting
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, values, color='blue', alpha=0.25)
ax.plot(angles, values, color='blue', linewidth=2)

ax.set_xticks(angles[:-1])  # Set ticks based on the original angles length
ax.set_xticklabels(categories)

passing_rating = int(average_ratings['Passing'] * 100)
shooting_rating = int(average_ratings['Shooting'] * 100)
dribbling_rating = int(average_ratings['Dribbling'] * 100)
defensive_rating = int(average_ratings['Defensive'] * 100)

# Add the overall rating to the plot
plt.text(0.5, -0.1, f'Overall: {overall_rating}', ha='center', va='center', fontsize=16, color='blue', weight='bold', transform=ax.transAxes)
plt.text(1, 0, f"Passing: {passing_rating}", ha='center', va='center', fontsize=8, color='black', weight='light', transform=ax.transAxes)
plt.text(1, -0.03, f"Shooting: {shooting_rating}", ha='center', va='center', fontsize=8, color='black', weight='light', transform=ax.transAxes)
plt.text(1, -0.06, f"Dribbling: {dribbling_rating}", ha='center', va='center', fontsize=8, color='black', weight='light', transform=ax.transAxes)
plt.text(1, -0.09, f"Defensive: {defensive_rating}", ha='center', va='center', fontsize=8, color='black', weight='light', transform=ax.transAxes)

plt.title(f'{label_name} - Player Overall Ratings')
plt.show()
