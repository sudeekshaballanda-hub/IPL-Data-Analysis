import os
import streamlit as st
import pandas as pd
import plotly.express as px

# 1. PAGE ARCHITECTURE CONFIGURATION
st.set_page_config(
    layout="wide", 
    page_title="IPL Elite Performance Engine",
    page_icon="🏏"
)

# Custom Theme Injection via Markdown
st.markdown("""
    <style>
    .main-title { font-size:38px !important; font-weight: bold; color: #1e3d59; text-align: center; margin-bottom: 5px; }
    .sub-title { font-size:18px !important; color: #17b978; text-align: center; margin-bottom: 30px; font-style: italic; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="main-title">🏏 IPL Advanced Performance & Analytics Engine</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Senior Data Scientist Portfolio Presentation Layer</p>', unsafe_allow_html=True)
st.markdown("---")


# 2. AUTO-DIAGNOSTIC DATA LOADER ENGINE
@st.cache_data
def load_dashboard_data():
    # Handle possible nested directory variations dynamically
    possible_paths = [
        r"C:\Users\Admin\IPL-DataAnalysis\IPL-Data-Analysis",
        r"C:\Users\Admin\IPL-DataAnalysis"
    ]
    
    base_dir = None
    player_stats_path = None
    matches_path = None
    
    # Locate valid files on disk
    for path in possible_paths:
        test_stats = os.path.join(path, "outputs", "aggregations", "player_stats.csv")
        if os.path.exists(test_stats) and os.path.getsize(test_stats) > 0:
            base_dir = path
            player_stats_path = test_stats
            matches_path = os.path.join(path, "outputs", "cleaned_data", "cleaned_matches.csv")
            break

    # SELF-HEALING BLOCK: If files are missing/empty, calculate right here
    if not player_stats_path:
        for path in possible_paths:
            if os.path.exists(os.path.join(path, "outputs", "cleaned_data", "cleaned_matches.csv")):
                base_dir = path
                break
                
        if not base_dir:
            st.error("🚨 System Error: Unable to locate 'outputs/cleaned_data' folder directory path structure.")
            st.stop()
            
        matches_path = os.path.join(base_dir, "outputs", "cleaned_data", "cleaned_matches.csv")
        del_path = os.path.join(base_dir, "data", "deliveries.csv")
        if not os.path.exists(del_path):
            del_path = os.path.join(base_dir, "outputs", "cleaned_data", "cleaned_deliveries.csv")
            
        # Run real-time background fallback calculations 
        m_df = pd.read_csv(matches_path)
        d_df = pd.read_csv(del_path)
        
        batting_df = pd.merge(d_df, m_df[['id', 'season']], left_on='match_id', right_on='id')
        player_run_summary = batting_df.groupby(['season', 'batter'])['batsman_runs'].sum().reset_index()
        player_run_summary.columns = ['season', 'batsman', 'batsman_runs']
        
        agg_dir = os.path.join(base_dir, "outputs", "aggregations")
        os.makedirs(agg_dir, exist_ok=True)
        player_stats_path = os.path.join(agg_dir, "player_stats.csv")
        player_run_summary.to_csv(player_stats_path, index=False)
        
    # Read finalized data streams cleanly
    matches = pd.read_csv(matches_path)
    player_stats = pd.read_csv(player_stats_path)
    
    return matches, player_stats


# Execute Data Load
matches, player_stats = load_dashboard_data()


# 3. GLOBAL INTERACTIVE FILTER CONTROLS (SIDEBAR)
st.sidebar.header("🕹️ Dashboard Navigation")
seasons = sorted(matches['season'].unique(), reverse=True)
selected_season = st.sidebar.selectbox("Select Tournament Year / Season", seasons)

# Dynamic Slice Engine based on Filter Selections
season_matches = matches[matches['season'] == selected_season]


# 4. HIGH-LEVEL KPI METRIC BLOCKS
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total Contested Fixtures", value=len(season_matches))
with col2:
    dominant_team = season_matches['winner'].mode()[0] if not season_matches.empty else "N/A"
    st.metric(label="Season Champion / Dominant Franchise", value=dominant_team)
with col3:
    top_mvp = season_matches['player_of_match'].mode()[0] if not season_matches.empty else "N/A"
    st.metric(label="Season Match-Winner (Most Player of Matches)", value=top_mvp)

st.markdown("---")


# 5. ADVANCED DATA VISUALIZATION GRID LAYER
left_chart, right_chart = st.columns(2)

with left_chart:
    st.subheader("📊 Franchise Win Dominance Share")
    win_counts = season_matches['winner'].value_counts().reset_index()
    win_counts.columns = ['Franchise', 'Wins']
    
    fig_wins = px.bar(
        win_counts,
        x='Wins',
        y='Franchise',
        orientation='h',
        color='Wins',
        color_continuous_scale='plasma',
        labels={'Wins': 'Matches Won', 'Franchise': 'IPL Franchise Team'}
    )
    fig_wins.update_layout(yaxis={'categoryorder':'total ascending'}, showlegend=False)
    st.plotly_chart(fig_wins, use_container_width=True)

with right_chart:
    st.subheader("🔥 Top 10 Elite Batsmen (Orange Cap Contenders)")
    season_players = player_stats[player_stats['season'] == selected_season].sort_values(by='batsman_runs', ascending=False).head(10)
    
    fig_players = px.bar(
        season_players, 
        x='batsman_runs', 
        y='batsman', 
        orientation='h',
        labels={'batsman_runs': 'Total Season Runs Scored', 'batsman': 'Player Handle'}, 
        color='batsman_runs',
        color_continuous_scale='viridis'
    )
    fig_players.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig_players, use_container_width=True)