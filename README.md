# IPL-Data-Analysis
 IPL Data Analysis Using Python - Team Project

# 🏏 IPL Advanced Performance & Inference Engine

A professional data analytics pipeline and interactive dashboard that processes historic IPL data, isolates tactical situational splits, and applies scientific statistical testing to validate common cricket assumptions.

👉 **[Click Here to View the Live Interactive Dashboard]
https://ipl-data-analysis-cwm47nzbuprapjb7cywrox.streamlit.app/

---

## 📊 Executive Insights Discovered
* **The Toss Myth Debunked:** A Chi-Square ($\chi^2$) Test of Independence proved that winning the toss grants **no statistically significant advantage** ($p > 0.05$) to winning the match in the long term.
* **Venue DNA Profiles:** A Kruskal-Wallis test structurally confirmed ($p < 0.05$) that stadium boundary dimensions and pitch archetypes create permanent, distinct scoring baselines rather than random variance.
* **Situational Masters:** High-velocity filtering isolated custom tactical splits, ranking the top 10 historical players by powerplay strike-rates and death-overs finishing efficiency.

---

## 🛠️ Tech Stack & Architecture
* **Frontend Dashboard:** Streamlit, Plotly Express
* **Data Processing:** Python, Pandas (Optimized via Dictionary Key-Value Mapping)
* **Statistical Inference:** SciPy (Stats module)

### Pipeline Breakdown
1. `notebooks/01_data_cleaning.ipynb`: Schema standardization, handling corporate franchise name changes, and structural formatting.
2. `notebooks/02_descriptive_eda.ipynb`: Evaluates macro trends, stadium scoring distributions, and asymmetric head-to-head franchise rivalries.
3. `notebooks/03_situational_analysis.ipynb`: Isolates situational pressure phases (Powerplay vs Death Overs) using high-performance filtering.
4. `notebooks/04_statistical_testing.ipynb`: Mathematical verification layer running non-parametric ANOVA and independence tests.
5. `dashboard/app.py`: Production-ready presentation layer with automated relative path fallbacks for cloud deployment.