# Player Rating Generator

## Overview
This project is designed to generate radar charts representing player ratings based on statistical data from a CSV or XLSX file. The radar chart visually displays a player's strengths and weaknesses across various categories like Passing, Shooting, Dribbling, and Defensive skills.

## Features
- **Supports both CSV and XLSX files** for input data.
- **Generates radar charts** with customizable labels and overall ratings.
- **Simple and easy-to-use** Python script.

## Prerequisites
Ensure you have Python installed on your machine. You will need to install the following libraries:

- `matplotlib`: For generating radar charts.
- `pandas`: For reading and manipulating CSV/XLSX data.
- `numpy`: For mathematical operations and averaging ratings.

## Usage
Clone the repository to your local machine:
git clone https://github.com/your-username/player-rating-generator.git

Navigate to the project directory:
cd player-rating-generator

Adjust the file path:
Open player-rating-generator.py.

Modify the file_path variable on line 15 to point to the player file you want to analyze. This should be a path to a CSV or XLSX file containing the player's statistical data.
Example:
file_path = 'player-stats/player-stats-W-Harris.xlsx'

Run the script to generate the radar chart:
python3 player-rating-generator.py

Files Description
player-rating-generator.py: The main script that reads player data from a specified file, processes it, and generates a radar chart.
player-stats/: A directory that contains example CSV and XLSX files with player data.

Contributing
Feel free to contribute to this project by submitting pull requests or opening issues. Contributions are welcome and appreciated!
