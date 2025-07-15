# Task_04_Descriptive_Stats

This repository contains scripts for descriptive statistical analysis of the `SocialMediaTop100.csv` dataset using pure Python, pandas, and polars. Bonus: visualization script included.

## Files
- `pure_python_stats.py`: Analysis using only the Python standard library.
- `pandas_stats.py`: Analysis using pandas.
- `polars_stats.py`: Analysis using polars.
- `visualizations.py`: Generates histograms, bar charts, and boxplots (bonus).
- `requirements.txt`: Python dependencies for pandas, polars, matplotlib, seaborn.
- `SocialMediaTop100.csv`: The dataset (add this file to the repo, not included here).

## Instructions
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Place `SocialMediaTop100.csv` in the repository directory.
3. Run the scripts:
   - Pure Python: `python3 pure_python_stats.py`
   - Pandas: `python3 pandas_stats.py`
   - Polars: `python3 polars_stats.py`
   - Visualizations: `python3 visualizations.py` (outputs PNG files)

## Summary of Findings
- The dataset covers the top 100 social media profiles across platforms (Instagram, Twitter, TikTok, YouTube, Twitch).
- **Instagram** and **YouTube** dominate the top spots by follower count.
- Some profiles (e.g., Cristiano Ronaldo, MrBeast, Selena Gomez) appear across multiple platforms, showing cross-platform influence.
- Follower counts are highly skewed, with a few accounts having hundreds of millions of followers.
- The number of posts varies widely, with some accounts posting tens of thousands of times.
- The most frequent platform in the dataset is Instagram, and the most frequent profile is Kevin Hart.
- Visualizations reveal the heavy-tailed distribution of followers and posts, and the diversity of content creators.

## Bonus
- Run `visualizations.py` to generate histograms, bar charts, and boxplots for numeric and categorical columns. Output images are saved as PNG files in the repo directory.

---

**Note:** Please add the dataset file (`SocialMediaTop100.csv`) to the repository before running the scripts. 