"""
Greeting Card Analytics Dashboard
An editorial-style dashboard showcasing greeting card performance with magazine aesthetics.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
import base64
import random
from pathlib import Path
from collections import defaultdict

# Page configuration
st.set_page_config(
    page_title="Card Analytics | Editorial",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =============================================================================
# CUSTOM CSS - EDITORIAL MAGAZINE AESTHETIC
# =============================================================================
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,500&family=Source+Sans+3:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap');

    /* ===========================================
       HIDE STREAMLIT DEFAULT ELEMENTS
    =========================================== */
    #MainMenu {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    header {visibility: hidden !important;}
    .stDeployButton {display: none !important;}
    [data-testid="stToolbar"] {display: none !important;}
    [data-testid="stDecoration"] {display: none !important;}
    [data-testid="stStatusWidget"] {display: none !important;}
    .viewerBadge_container__r5tak {display: none !important;}
    .styles_viewerBadge__CvC9N {display: none !important;}

    /* ===========================================
       BASE STYLES
    =========================================== */
    :root {
        --cream: #FDFBF7;
        --cream-dark: #F5F2EC;
        --terracotta: #C65D3B;
        --terracotta-light: #D4785C;
        --terracotta-dark: #A84D2E;
        --charcoal: #2D2A26;
        --charcoal-light: #4A4641;
        --gray: #8B8680;
        --gray-light: #B8B4AE;
        --white: #FFFFFF;
    }

    html, body, [data-testid="stAppViewContainer"] {
        background-color: var(--cream) !important;
        font-family: 'Source Sans 3', -apple-system, BlinkMacSystemFont, sans-serif;
        color: var(--charcoal);
    }

    [data-testid="stAppViewContainer"] > .main {
        background-color: var(--cream);
    }

    .main .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }

    /* ===========================================
       CUSTOM SCROLLBAR
    =========================================== */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }

    ::-webkit-scrollbar-track {
        background: var(--cream-dark);
    }

    ::-webkit-scrollbar-thumb {
        background: var(--gray-light);
        border-radius: 4px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: var(--gray);
    }

    /* ===========================================
       TYPOGRAPHY
    =========================================== */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Playfair Display', Georgia, serif !important;
        color: var(--charcoal);
        font-weight: 600 !important;
    }

    p, span, div, label {
        font-family: 'Source Sans 3', sans-serif;
    }

    /* ===========================================
       HERO SECTION
    =========================================== */
    .hero-section {
        background: linear-gradient(135deg, var(--cream) 0%, var(--cream-dark) 100%);
        padding: 4rem 5%;
        margin-bottom: 3rem;
        border-bottom: 1px solid rgba(45, 42, 38, 0.1);
        position: relative;
        overflow: hidden;
    }

    .hero-section::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -10%;
        width: 500px;
        height: 500px;
        background: radial-gradient(circle, rgba(198, 93, 59, 0.08) 0%, transparent 70%);
        border-radius: 50%;
    }

    .hero-section::after {
        content: '';
        position: absolute;
        bottom: -30%;
        left: -5%;
        width: 300px;
        height: 300px;
        background: radial-gradient(circle, rgba(198, 93, 59, 0.05) 0%, transparent 70%);
        border-radius: 50%;
    }

    .hero-masthead {
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 0.85rem;
        font-weight: 500;
        letter-spacing: 3px;
        text-transform: uppercase;
        color: var(--terracotta);
        margin-bottom: 1rem;
    }

    .hero-title {
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 3.5rem;
        font-weight: 700;
        color: var(--charcoal);
        margin: 0 0 1rem 0;
        line-height: 1.1;
        letter-spacing: -1px;
    }

    .hero-subtitle {
        font-family: 'Source Sans 3', sans-serif;
        font-size: 1.15rem;
        color: var(--gray);
        font-weight: 400;
        max-width: 500px;
        line-height: 1.6;
    }

    .hero-stats-container {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 2rem;
        margin-top: 3rem;
        position: relative;
        z-index: 1;
    }

    .hero-stat {
        position: relative;
        padding-left: 1.5rem;
    }

    .hero-stat::before {
        content: '';
        position: absolute;
        left: 0;
        top: 0;
        height: 100%;
        width: 2px;
        background: linear-gradient(180deg, var(--terracotta) 0%, var(--terracotta-light) 100%);
    }

    .hero-stat-value {
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 2.5rem;
        font-weight: 700;
        color: var(--charcoal);
        line-height: 1;
        margin-bottom: 0.5rem;
    }

    .hero-stat-label {
        font-family: 'Source Sans 3', sans-serif;
        font-size: 0.85rem;
        color: var(--gray);
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 500;
    }

    /* ===========================================
       SIDEBAR STYLES
    =========================================== */
    [data-testid="stSidebar"] {
        background-color: var(--white) !important;
        border-right: 1px solid rgba(45, 42, 38, 0.08);
        min-width: 300px !important;
        width: 300px !important;
        transform: none !important;
    }

    /* Hide sidebar completely */
    [data-testid="stSidebar"] {
        display: none !important;
    }

    [data-testid="stSidebarCollapsedControl"] {
        display: none !important;
    }

    .sidebar-subtitle {
        font-family: 'Source Sans 3', sans-serif;
        font-size: 0.85rem;
        color: var(--gray);
        margin-bottom: 2rem;
    }

    .sidebar-section-title {
        font-family: 'Source Sans 3', sans-serif;
        font-size: 0.7rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        color: var(--gray);
        margin: 1.5rem 0 0.75rem 0;
    }

    /* Custom select boxes */
    [data-testid="stSidebar"] .stSelectbox > div > div {
        background-color: var(--cream) !important;
        border: 1px solid rgba(45, 42, 38, 0.15) !important;
        border-radius: 8px !important;
        font-family: 'Source Sans 3', sans-serif !important;
        transition: all 0.2s ease !important;
    }

    [data-testid="stSidebar"] .stSelectbox > div > div:hover {
        border-color: var(--terracotta) !important;
    }

    [data-testid="stSidebar"] .stSelectbox > div > div:focus-within {
        border-color: var(--terracotta) !important;
        box-shadow: 0 0 0 2px rgba(198, 93, 59, 0.15) !important;
    }

    /* Custom text input */
    [data-testid="stSidebar"] .stTextInput > div > div > input {
        background-color: var(--cream) !important;
        border: 1px solid rgba(45, 42, 38, 0.15) !important;
        border-radius: 8px !important;
        font-family: 'Source Sans 3', sans-serif !important;
        padding: 0.6rem 1rem !important;
        transition: all 0.2s ease !important;
    }

    [data-testid="stSidebar"] .stTextInput > div > div > input:focus {
        border-color: var(--terracotta) !important;
        box-shadow: 0 0 0 2px rgba(198, 93, 59, 0.15) !important;
    }

    [data-testid="stSidebar"] .stTextInput > div > div > input::placeholder {
        color: var(--gray-light) !important;
    }

    /* Custom slider */
    [data-testid="stSidebar"] .stSlider > div > div > div > div {
        background-color: var(--terracotta) !important;
    }

    [data-testid="stSidebar"] .stSlider [data-baseweb="slider"] > div:first-child {
        background: linear-gradient(to right, var(--cream-dark), var(--cream-dark)) !important;
    }

    /* ===========================================
       SECTION STYLES
    =========================================== */
    .section-container {
        padding: 0 5% 4rem 5%;
    }

    .section-header {
        display: flex;
        align-items: baseline;
        margin-bottom: 2rem;
        gap: 1rem;
    }

    .section-title {
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 1.8rem;
        font-weight: 600;
        color: var(--charcoal);
        margin: 0;
    }

    .section-number {
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 0.9rem;
        color: var(--terracotta);
        font-weight: 500;
    }

    .section-line {
        flex-grow: 1;
        height: 1px;
        background: linear-gradient(90deg, rgba(45, 42, 38, 0.2) 0%, transparent 100%);
        margin-left: 1rem;
    }

    /* ===========================================
       CHART CONTAINER STYLES
    =========================================== */
    .chart-container {
        background: var(--white);
        border-radius: 12px;
        padding: 2rem;
        box-shadow: 0 4px 20px rgba(45, 42, 38, 0.06);
        border: 1px solid rgba(45, 42, 38, 0.06);
        transition: all 0.3s ease;
    }

    .chart-container:hover {
        box-shadow: 0 8px 30px rgba(45, 42, 38, 0.1);
    }

    .chart-title {
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 1.25rem;
        font-weight: 600;
        color: var(--charcoal);
        margin-bottom: 0.5rem;
    }

    .chart-subtitle {
        font-family: 'Source Sans 3', sans-serif;
        font-size: 0.85rem;
        color: var(--gray);
        margin-bottom: 1.5rem;
    }

    /* ===========================================
       CARD GALLERY STYLES
    =========================================== */
    .gallery-grid {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 1.5rem;
    }

    .card-item {
        background: var(--white);
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 20px rgba(45, 42, 38, 0.06);
        border: 1px solid rgba(45, 42, 38, 0.06);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        cursor: pointer;
        position: relative;
        display: flex;
        flex-direction: column;
        height: 100%;
    }

    .card-item:hover {
        transform: translateY(-6px);
        box-shadow: 0 16px 32px rgba(45, 42, 38, 0.12);
    }

    .card-image-container {
        position: relative;
        overflow: hidden;
        aspect-ratio: 4/5;
        background: var(--cream-dark);
        flex-shrink: 0;
    }

    .card-image-container img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .card-item:hover .card-image-container img {
        transform: scale(1.05);
    }

    .card-rank-badge {
        position: absolute;
        top: 0.6rem;
        left: 0.6rem;
        background: var(--white);
        color: var(--charcoal);
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 0.75rem;
        font-weight: 600;
        padding: 0.3rem 0.6rem;
        border-radius: 5px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        z-index: 2;
    }

    .card-occasion-tag {
        position: absolute;
        top: 0.6rem;
        right: 0.6rem;
        background: var(--terracotta);
        color: var(--white);
        font-family: 'Source Sans 3', sans-serif;
        font-size: 0.6rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        padding: 0.25rem 0.5rem;
        border-radius: 4px;
        z-index: 2;
    }

    .card-info {
        padding: 0.875rem 1rem 1rem;
        display: flex;
        flex-direction: column;
        flex-grow: 1;
    }

    .card-title {
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 0.85rem;
        font-weight: 600;
        color: var(--charcoal);
        margin-bottom: 0.5rem;
        line-height: 1.35;
        height: 2.3em;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }

    .card-sends {
        display: flex;
        align-items: center;
        gap: 0.4rem;
        margin-top: auto;
    }

    .card-sends-value {
        font-family: 'Source Sans 3', sans-serif;
        font-size: 0.95rem;
        font-weight: 600;
        color: var(--terracotta);
    }

    .card-sends-label {
        font-family: 'Source Sans 3', sans-serif;
        font-size: 0.7rem;
        color: var(--gray);
    }

    /* ===========================================
       PAGINATION
    =========================================== */
    .pagination-container {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 0.5rem;
        margin-top: 3rem;
    }

    .page-indicator {
        font-family: 'Source Sans 3', sans-serif;
        font-size: 0.9rem;
        color: var(--gray);
    }

    /* ===========================================
       BUTTON STYLES
    =========================================== */
    .stButton > button {
        background: var(--terracotta) !important;
        color: var(--white) !important;
        border: none !important;
        border-radius: 8px !important;
        font-family: 'Source Sans 3', sans-serif !important;
        font-weight: 500 !important;
        padding: 0.6rem 1.5rem !important;
        transition: all 0.3s ease !important;
    }

    .stButton > button:hover {
        background: var(--terracotta-dark) !important;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(198, 93, 59, 0.3) !important;
    }

    /* Secondary button style */
    [data-testid="stSidebar"] .stButton > button {
        background: transparent !important;
        color: var(--charcoal) !important;
        border: 1px solid rgba(45, 42, 38, 0.2) !important;
    }

    [data-testid="stSidebar"] .stButton > button:hover {
        background: var(--cream) !important;
        border-color: var(--terracotta) !important;
        color: var(--terracotta) !important;
        box-shadow: none !important;
    }

    /* ===========================================
       FILTER STATUS BAR
    =========================================== */
    .filter-status {
        background: var(--cream-dark);
        padding: 1rem 5%;
        margin-bottom: 2rem;
        border-top: 1px solid rgba(45, 42, 38, 0.06);
        border-bottom: 1px solid rgba(45, 42, 38, 0.06);
    }

    .filter-status-text {
        font-family: 'Source Sans 3', sans-serif;
        font-size: 0.9rem;
        color: var(--gray);
    }

    .filter-status-count {
        font-weight: 600;
        color: var(--terracotta);
    }

    /* ===========================================
       TABS STYLING
    =========================================== */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0;
        background: transparent;
        border-bottom: 1px solid rgba(45, 42, 38, 0.1);
    }

    .stTabs [data-baseweb="tab"] {
        font-family: 'Source Sans 3', sans-serif !important;
        font-weight: 500;
        color: var(--gray);
        padding: 1rem 2rem;
        background: transparent;
        border: none;
        transition: all 0.2s ease;
    }

    .stTabs [data-baseweb="tab"]:hover {
        color: var(--charcoal);
    }

    .stTabs [aria-selected="true"] {
        color: var(--terracotta) !important;
        border-bottom: 2px solid var(--terracotta) !important;
        background: transparent !important;
    }

    .stTabs [data-baseweb="tab-highlight"] {
        background-color: var(--terracotta) !important;
    }

    /* ===========================================
       DATA TABLE
    =========================================== */
    .stDataFrame {
        border-radius: 12px !important;
        overflow: hidden;
        box-shadow: 0 4px 20px rgba(45, 42, 38, 0.06);
    }

    .stDataFrame [data-testid="stDataFrameContainer"] {
        background: var(--white);
    }

    /* ===========================================
       EXPANDER STYLING
    =========================================== */
    .streamlit-expanderHeader {
        font-family: 'Source Sans 3', sans-serif !important;
        font-weight: 500 !important;
        color: var(--charcoal) !important;
        background: var(--cream) !important;
        border-radius: 8px !important;
    }

    /* ===========================================
       RESPONSIVE
    =========================================== */
    @media (max-width: 1400px) {
        .gallery-grid {
            grid-template-columns: repeat(4, 1fr);
        }
    }

    @media (max-width: 1200px) {
        .gallery-grid {
            grid-template-columns: repeat(3, 1fr);
        }

        .hero-stats-container {
            grid-template-columns: repeat(2, 1fr);
        }
    }

    @media (max-width: 900px) {
        .gallery-grid {
            grid-template-columns: repeat(2, 1fr);
        }
    }

    @media (max-width: 768px) {
        .gallery-grid {
            grid-template-columns: 1fr;
        }

        .hero-stats-container {
            grid-template-columns: 1fr;
        }

        .hero-title {
            font-size: 2.5rem;
        }
    }

    /* ===========================================
       NO IMAGE PLACEHOLDER
    =========================================== */
    .no-image-placeholder {
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        background: linear-gradient(135deg, var(--cream-dark) 0%, var(--cream) 100%);
        color: var(--gray-light);
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 1rem;
        font-style: italic;
    }

    /* ===========================================
       CARD COMPARISON TOOL STYLES
    =========================================== */
    .comparison-header {
        text-align: center;
        padding: 2rem 0;
        margin-bottom: 1.5rem;
    }

    .comparison-header h2 {
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 2rem;
        color: var(--charcoal);
        margin-bottom: 0.5rem;
    }

    .comparison-header p {
        font-family: 'Source Sans 3', sans-serif;
        color: var(--gray);
        font-size: 1rem;
    }

    .comparison-card {
        background: var(--white);
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 20px rgba(45, 42, 38, 0.08);
        border: 1px solid rgba(45, 42, 38, 0.06);
        height: 100%;
        transition: all 0.3s ease;
    }

    .comparison-card:hover {
        box-shadow: 0 8px 30px rgba(45, 42, 38, 0.12);
    }

    .comparison-card-image {
        width: 100%;
        aspect-ratio: 4/5;
        object-fit: cover;
        border-bottom: 1px solid rgba(45, 42, 38, 0.06);
    }

    .comparison-card-body {
        padding: 1.5rem;
    }

    .comparison-card-rank {
        display: inline-block;
        background: var(--terracotta);
        color: white;
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 0.9rem;
        font-weight: 600;
        padding: 0.3rem 0.8rem;
        border-radius: 4px;
        margin-bottom: 1rem;
    }

    .comparison-card-title {
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 1.1rem;
        font-weight: 600;
        color: var(--charcoal);
        margin-bottom: 1rem;
        line-height: 1.4;
    }

    .comparison-stat {
        display: flex;
        justify-content: space-between;
        padding: 0.6rem 0;
        border-bottom: 1px solid rgba(45, 42, 38, 0.06);
        font-family: 'Source Sans 3', sans-serif;
    }

    .comparison-stat:last-child {
        border-bottom: none;
    }

    .comparison-stat-label {
        color: var(--gray);
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .comparison-stat-value {
        color: var(--charcoal);
        font-weight: 600;
        font-size: 0.9rem;
    }

    .comparison-stat-value.positive {
        color: #4CAF50;
    }

    .comparison-stat-value.negative {
        color: #F44336;
    }

    .comparison-attribute {
        margin-bottom: 1rem;
    }

    .comparison-attribute-label {
        font-family: 'Source Sans 3', sans-serif;
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: var(--gray);
        margin-bottom: 0.4rem;
    }

    .comparison-attribute-value {
        font-family: 'Source Sans 3', sans-serif;
        font-size: 0.9rem;
        color: var(--charcoal);
        font-weight: 500;
    }

    .comparison-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 0.4rem;
    }

    .comparison-tag {
        background: var(--cream-dark);
        color: var(--charcoal);
        font-family: 'Source Sans 3', sans-serif;
        font-size: 0.75rem;
        padding: 0.25rem 0.6rem;
        border-radius: 4px;
    }

    .comparison-summary-box {
        background: linear-gradient(135deg, var(--cream) 0%, var(--cream-dark) 100%);
        border-radius: 12px;
        padding: 2rem;
        margin-top: 2rem;
        border: 1px solid rgba(198, 93, 59, 0.15);
    }

    .comparison-summary-title {
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 1.4rem;
        color: var(--charcoal);
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }

    .comparison-summary-title::before {
        content: '';
        display: inline-block;
        width: 4px;
        height: 24px;
        background: var(--terracotta);
        border-radius: 2px;
    }

    .comparison-summary-section {
        margin-bottom: 1.5rem;
    }

    .comparison-summary-section:last-child {
        margin-bottom: 0;
    }

    .comparison-summary-section h4 {
        font-family: 'Source Sans 3', sans-serif;
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        color: var(--terracotta);
        margin-bottom: 0.75rem;
        font-weight: 600;
    }

    .comparison-summary-section ul {
        margin: 0;
        padding-left: 1.25rem;
    }

    .comparison-summary-section li {
        font-family: 'Source Sans 3', sans-serif;
        font-size: 0.95rem;
        color: var(--charcoal);
        margin-bottom: 0.5rem;
        line-height: 1.5;
    }

    .comparison-insight-card {
        background: var(--white);
        border-radius: 8px;
        padding: 1.25rem;
        border-left: 3px solid var(--terracotta);
        margin-bottom: 1rem;
    }

    .comparison-insight-card h5 {
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 1rem;
        color: var(--charcoal);
        margin-bottom: 0.5rem;
        font-weight: 600;
    }

    .comparison-insight-card p {
        font-family: 'Source Sans 3', sans-serif;
        font-size: 0.9rem;
        color: var(--gray);
        line-height: 1.5;
        margin: 0;
    }

    .color-swatch {
        display: inline-block;
        width: 16px;
        height: 16px;
        border-radius: 50%;
        margin-right: 4px;
        vertical-align: middle;
        border: 1px solid rgba(0,0,0,0.1);
    }

    .empty-comparison-state {
        text-align: center;
        padding: 4rem 2rem;
        background: var(--cream-dark);
        border-radius: 12px;
        margin: 2rem 0;
    }

    .empty-comparison-state h3 {
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 1.5rem;
        color: var(--charcoal);
        margin-bottom: 1rem;
    }

    .empty-comparison-state p {
        font-family: 'Source Sans 3', sans-serif;
        color: var(--gray);
        font-size: 1rem;
        max-width: 400px;
        margin: 0 auto;
    }

    .comparison-no-image {
        width: 100%;
        aspect-ratio: 4/5;
        display: flex;
        align-items: center;
        justify-content: center;
        background: linear-gradient(135deg, var(--cream-dark) 0%, var(--cream) 100%);
        color: var(--gray-light);
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 0.9rem;
        font-style: italic;
        border-bottom: 1px solid rgba(45, 42, 38, 0.06);
    }

    .performance-winner {
        background: linear-gradient(135deg, #E8F5E9 0%, #C8E6C9 100%);
        border: 1px solid #4CAF50;
    }

    .performance-winner .comparison-card-rank {
        background: #4CAF50;
    }
</style>
""", unsafe_allow_html=True)

# =============================================================================
# CONSTANTS & CONFIGURATION
# =============================================================================
BASE_DIR = Path(__file__).parent
IMAGES_DIR = BASE_DIR / "card_images"
CSV_FILE = BASE_DIR / "Top 300 Cards - 2025.csv"
ANALYSIS_FILE = BASE_DIR / "card_analysis.json"
TREND_DATA_FILE = BASE_DIR / "trend_data_2026.json"
VALENTINE_CSV = BASE_DIR / "valentine_cards.csv"
BIRTHDAY_CSV = BASE_DIR / "birthday_cards.csv"
THANKYOU_CSV = BASE_DIR / "thankyou_cards.csv"
CARDS_PER_PAGE = 15

# Warm color palette for charts
CHART_COLORS = [
    "#C65D3B",  # Terracotta
    "#D4785C",  # Light Terracotta
    "#E8A87C",  # Peach
    "#DEB887",  # Burlywood
    "#B8860B",  # Dark Goldenrod
    "#CD853F",  # Peru
    "#8B7355",  # Burly Wood Dark
    "#A0522D",  # Sienna
    "#BC8F8F",  # Rosy Brown
    "#C4A484",  # Tan
]

# =============================================================================
# DATA LOADING FUNCTIONS
# =============================================================================
@st.cache_data(ttl=3600)
def load_csv_data() -> pd.DataFrame:
    """Load and process the CSV data."""
    if not CSV_FILE.exists():
        return pd.DataFrame()

    try:
        df = pd.read_csv(CSV_FILE)
        df.columns = ["Metric", "Card Name", "Previous Period", "Current Period"]
        df = df[df["Metric"] == "Total Events of Sent"].copy()
        df["Previous Period"] = pd.to_numeric(df["Previous Period"], errors="coerce")
        df["Current Period"] = pd.to_numeric(df["Current Period"], errors="coerce")
        df["Change"] = df["Current Period"] - df["Previous Period"]
        df["Change %"] = ((df["Current Period"] - df["Previous Period"]) / df["Previous Period"] * 100).round(1)
        df = df.sort_values("Current Period", ascending=False).reset_index(drop=True)
        df["Rank"] = df.index + 1

        # Extract card ID from name
        df["Card ID"] = df["Card Name"].apply(lambda x: x.split("_")[0] if "_" in x else "")
        df["Display Name"] = df["Card Name"].apply(lambda x: "_".join(x.split("_")[1:]) if "_" in x else x)

        return df

    except Exception as e:
        st.error(f"Error loading CSV data: {str(e)}")
        return pd.DataFrame()


@st.cache_data(ttl=3600)
def load_analysis_data() -> list:
    """Load the analysis JSON data."""
    if not ANALYSIS_FILE.exists():
        return []

    try:
        with open(ANALYSIS_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return []


@st.cache_data(ttl=3600)
def load_trend_data() -> dict:
    """Load 2026 trend data from JSON file."""
    if not TREND_DATA_FILE.exists():
        return get_default_trend_data()

    try:
        with open(TREND_DATA_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return get_default_trend_data()


def get_default_trend_data() -> dict:
    """Return minimal default trend structure when file is unavailable."""
    return {
        "last_updated": "N/A",
        "version": "default",
        "sources": [],
        "color_trends": {
            "pantone_color_of_year": {
                "name": "Not Available",
                "hex": "#888888",
                "description": "Trend data not loaded"
            },
            "emerging_palettes": [],
            "seasonal_shifts": {}
        },
        "illustration_trends": [],
        "typography_trends": [],
        "theme_motif_trends": [],
        "color_name_to_hex": {}
    }


@st.cache_data(ttl=3600)
def load_category_csv(filepath: Path) -> pd.DataFrame:
    """Load a 3-column category CSV (Metric, Card Name, Sends) and return a clean DataFrame."""
    if not filepath.exists():
        return pd.DataFrame()

    try:
        df = pd.read_csv(filepath)
        # Third column is the date-range sends column (name varies)
        cols = df.columns.tolist()
        df = df.rename(columns={cols[0]: "Metric", cols[1]: "Card Name", cols[2]: "Sends"})
        df = df[df["Metric"] == "Total Events of Sent"].copy()
        df["Sends"] = pd.to_numeric(df["Sends"], errors="coerce").fillna(0).astype(int)
        df["Card ID"] = df["Card Name"].apply(lambda x: str(x).split("_")[0] if "_" in str(x) else "")
        df["Display Name"] = df["Card Name"].apply(lambda x: "_".join(str(x).split("_")[1:]) if "_" in str(x) else str(x))
        df = df.sort_values("Sends", ascending=False).reset_index(drop=True)
        return df[["Card Name", "Card ID", "Display Name", "Sends"]]
    except Exception:
        return pd.DataFrame()


def get_card_image_path(card_name: str) -> Path | None:
    """Get the image path for a card."""
    for ext in [".jpg", ".jpeg", ".png", ".gif", ".webp"]:
        image_path = IMAGES_DIR / f"{card_name}{ext}"
        if image_path.exists():
            return image_path

    # Try by card ID
    card_id = card_name.split("_")[0] if "_" in card_name else ""
    if card_id:
        for image_file in IMAGES_DIR.glob(f"{card_id}_*"):
            if image_file.suffix.lower() in [".jpg", ".jpeg", ".png", ".gif", ".webp"]:
                return image_file
    return None


def get_image_base64(image_path: Path) -> str | None:
    """Convert image to base64 for HTML embedding."""
    try:
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception:
        return None


def create_analysis_lookup(analysis_data: list) -> dict:
    """Create a lookup dictionary from analysis data by card_id."""
    lookup = {}
    for item in analysis_data:
        if isinstance(item, dict):
            card_id = item.get("card_id", "")
            if card_id:
                lookup[card_id] = item
    return lookup


# =============================================================================
# ARTIST EXTRACTION FUNCTIONS
# =============================================================================
# Known artist names and studio brands for extraction
KNOWN_ARTISTS = [
    "Paper&Stuff", "Spaghetti & Meatballs", "Karen Schipper", "Melanie Johnsson",
    "Darlin' Spotted", "Aviva Atri", "Poketo", "jordan gadeke", "Jordan Gadeke",
    "Lucy Maggie", "Emily McDowell", "Rifle Paper Co", "Lisa Congdon",
    "Jess Phoenix", "Red Cap Cards", "Wrap Magazine", "1canoe2", "Egg Press",
    "Idlewild Co", "Slightly Stationery", "Dahlia Press", "Clap Clap Design",
    "Good Paper", "The Good Twin", "Belle & Union", "Bench Pressed",
    "Ladyfingers Letterpress", "Paper Bandit Press", "Printerette Press",
    "Blackbird Letterpress", "Hello Lucky", "Igloo Letterpress", "Paper Parasol Press",
    "Sapling Press", "The Social Type", "Wit & Whistle", "Yellow Owl Workshop",
    "Moglea", "Shorthand Press", "Thimblepress", "The Paper Cub",
    "Antiquaria", "Ilee Papergoods", "Pike Street Press", "Fugu Fugu Press",
    "The Little Red House", "Sycamore Street Press", "Happy Cactus Designs",
    "Quill & Fox", "Calliope Paperie", "Olive & Company", "E. Frances Paper",
    "Bloomwolf Studio", "Girl w/ Knife", "Elana Gabrielle", "Hatch Inc",
    "Fifty Five Hi's", "Ramona & Ruth", "And Here We Are", "Ohh Deer",
    "Gemma Correll", "Able & Game", "La Familia Green", "Near Modern Disaster"
]


def extract_artist_from_card_name(card_name: str) -> str:
    """
    Extract artist/studio name from card_name field.
    Artist names typically appear at the end of the card name after the main title,
    or at the beginning followed by the card description.
    Returns the artist name if found, or 'Unknown Artist' if not identifiable.
    """
    if not card_name:
        return "Unknown Artist"

    # First, check for known artists/studios (case-insensitive matching)
    card_name_lower = card_name.lower()
    for artist in KNOWN_ARTISTS:
        if artist.lower() in card_name_lower:
            return artist

    # Fallback: Try to extract artist using common patterns
    words = card_name.split()

    if len(words) >= 2:
        # Check the last 2-3 words for artist pattern
        for end_pos in range(min(3, len(words)), 0, -1):
            potential_artist = " ".join(words[-end_pos:])

            # Skip common card title endings
            skip_words = ["birthday", "cake", "wishes", "day", "happy", "you", "love",
                         "thanks", "thank", "card", "gradient", "balloon", "floral",
                         "flowers", "hearts", "confetti", "party", "celebration"]

            if any(skip.lower() in potential_artist.lower() for skip in skip_words):
                continue

            # Check if it looks like a name (capitalized, contains & or has multiple caps)
            if ("&" in potential_artist or
                sum(1 for c in potential_artist if c.isupper()) >= 2):
                return potential_artist

    return "Unknown Artist"


def build_artist_stats(analysis_data: list, csv_df) -> "pd.DataFrame":
    """
    Build comprehensive artist statistics from analysis data.
    Returns a DataFrame with artist metrics including:
    - Total sends, Number of cards, Average sends per card, Primary design style
    """
    import pandas as pd

    artist_data = {}

    # Create a lookup for sends from CSV data
    sends_lookup = {}
    for _, row in csv_df.iterrows():
        card_id = row.get("Card ID", "")
        if card_id:
            sends_lookup[card_id] = row.get("Current Period", 0)

    for card in analysis_data:
        if not isinstance(card, dict):
            continue

        card_name = card.get("card_name", "")
        card_id = card.get("card_id", "")

        artist = extract_artist_from_card_name(card_name)
        sends = card.get("sends_current", 0) or sends_lookup.get(card_id, 0)
        design_style = card.get("design_style", "unknown")

        if artist not in artist_data:
            artist_data[artist] = {
                "total_sends": 0,
                "card_count": 0,
                "design_styles": {},
                "cards": []
            }

        artist_data[artist]["total_sends"] += sends
        artist_data[artist]["card_count"] += 1
        artist_data[artist]["cards"].append(card_name)

        # Track design style frequency
        if design_style:
            style_counts = artist_data[artist]["design_styles"]
            style_counts[design_style] = style_counts.get(design_style, 0) + 1

    # Convert to DataFrame
    rows = []
    for artist, data in artist_data.items():
        # Find primary design style (most frequent)
        primary_style = "Unknown"
        if data["design_styles"]:
            primary_style = max(data["design_styles"].items(), key=lambda x: x[1])[0]

        avg_sends = data["total_sends"] / data["card_count"] if data["card_count"] > 0 else 0

        rows.append({
            "Artist": artist,
            "Total Sends": data["total_sends"],
            "Card Count": data["card_count"],
            "Avg Sends per Card": round(avg_sends, 0),
            "Primary Style": primary_style.replace("_", " ").title(),
        })

    df = pd.DataFrame(rows)
    df = df.sort_values("Total Sends", ascending=False).reset_index(drop=True)
    df["Rank"] = df.index + 1

    return df



# =============================================================================
# UI COMPONENT FUNCTIONS
# =============================================================================
def render_hero(df: pd.DataFrame):
    """Render the hero section with key statistics."""
    total_cards = len(df)
    total_sends = int(df["Current Period"].sum()) if not df.empty else 0
    avg_sends = int(df["Current Period"].mean()) if not df.empty else 0
    top_performer = int(df["Current Period"].max()) if not df.empty else 0

    # Hero header section
    hero_header = """
    <div class="hero-section">
        <div class="hero-masthead">Analytics Dashboard</div>
        <h1 class="hero-title">Greeting Cards<br/>Performance Report</h1>
        <p class="hero-subtitle">
            A comprehensive analysis of your top-performing greeting cards,
            revealing trends, patterns, and insights from the latest period data.
        </p>
    </div>
    """
    st.markdown(hero_header, unsafe_allow_html=True)

    # Stats using native Streamlit columns for reliable rendering
    st.markdown('<div class="hero-stats-container">', unsafe_allow_html=True)
    cols = st.columns(4)
    stats = [
        (f"{total_cards:,}", "Total Cards Tracked"),
        (f"{total_sends:,}", "Total Sends"),
        (f"{avg_sends:,}", "Average per Card"),
        (f"{top_performer:,}", "Top Performer Sends"),
    ]
    for col, (value, label) in zip(cols, stats):
        with col:
            st.markdown(f'<div class="hero-stat"><div class="hero-stat-value">{value}</div><div class="hero-stat-label">{label}</div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


def render_sidebar_filters(df: pd.DataFrame, analysis_lookup: dict) -> dict:
    """Render elegant sidebar filters."""

    # Sidebar header
    st.sidebar.markdown('<div class="sidebar-title">Filters</div>', unsafe_allow_html=True)
    st.sidebar.markdown('<div class="sidebar-subtitle">Refine your card selection</div>', unsafe_allow_html=True)

    filters = {}

    # Search
    st.sidebar.markdown('<div class="sidebar-section-title">Search</div>', unsafe_allow_html=True)
    search_query = st.sidebar.text_input(
        "Search",
        placeholder="Card name or artist...",
        key="search",
        label_visibility="collapsed"
    )
    filters["search"] = search_query

    # Get unique occasions from analysis data
    occasions = set()
    for item in analysis_lookup.values():
        occ = item.get("occasion", "")
        if occ:
            occasions.add(occ.title())
    occasions = ["All Occasions"] + sorted(list(occasions))

    st.sidebar.markdown('<div class="sidebar-section-title">Occasion</div>', unsafe_allow_html=True)
    selected_occasion = st.sidebar.selectbox(
        "Occasion",
        options=occasions,
        key="occasion_filter",
        label_visibility="collapsed"
    )
    filters["occasion"] = None if selected_occasion == "All Occasions" else selected_occasion.lower()

    # Design Style filter
    styles = set()
    for item in analysis_lookup.values():
        style = item.get("design_style", "")
        if style:
            styles.add(style.replace("_", " ").title())
    styles = ["All Styles"] + sorted(list(styles))

    st.sidebar.markdown('<div class="sidebar-section-title">Design Style</div>', unsafe_allow_html=True)
    selected_style = st.sidebar.selectbox(
        "Style",
        options=styles,
        key="style_filter",
        label_visibility="collapsed"
    )
    filters["style"] = None if selected_style == "All Styles" else selected_style.lower().replace(" ", "_")

    # Rank Range
    st.sidebar.markdown('<div class="sidebar-section-title">Rank Range</div>', unsafe_allow_html=True)
    max_rank = int(df["Rank"].max()) if not df.empty else 300
    rank_range = st.sidebar.slider(
        "Rank",
        min_value=1,
        max_value=max_rank,
        value=(1, min(50, max_rank)),
        key="rank_filter",
        label_visibility="collapsed"
    )
    filters["rank_range"] = rank_range

    # Divider
    st.sidebar.markdown("---")

    # Reset button
    if st.sidebar.button("Reset All Filters", use_container_width=True):
        st.rerun()

    return filters


def apply_filters(df: pd.DataFrame, filters: dict, analysis_lookup: dict) -> pd.DataFrame:
    """Apply filters to the dataframe."""
    filtered_df = df.copy()

    # Search filter
    if filters.get("search"):
        search_term = filters["search"].lower()
        filtered_df = filtered_df[
            filtered_df["Card Name"].str.lower().str.contains(search_term, na=False)
        ]

    # Occasion filter
    if filters.get("occasion"):
        card_ids_with_occasion = set()
        for card_id, data in analysis_lookup.items():
            if data.get("occasion", "").lower() == filters["occasion"]:
                card_ids_with_occasion.add(card_id)
        filtered_df = filtered_df[filtered_df["Card ID"].isin(card_ids_with_occasion)]

    # Style filter
    if filters.get("style"):
        card_ids_with_style = set()
        for card_id, data in analysis_lookup.items():
            if data.get("design_style", "").lower() == filters["style"]:
                card_ids_with_style.add(card_id)
        filtered_df = filtered_df[filtered_df["Card ID"].isin(card_ids_with_style)]

    # Rank range filter
    if filters.get("rank_range"):
        rank_min, rank_max = filters["rank_range"]
        filtered_df = filtered_df[
            (filtered_df["Rank"] >= rank_min) &
            (filtered_df["Rank"] <= rank_max)
        ]

    return filtered_df


def render_charts(df: pd.DataFrame, analysis_lookup: dict):
    """Render the charts section with editorial styling."""

    st.markdown("""
    <div class="section-container">
        <div class="section-header">
            <span class="section-number">01</span>
            <h2 class="section-title">Performance Analytics</h2>
            <div class="section-line"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        # Top 10 Horizontal Bar Chart
        st.markdown("""
        <div class="chart-container">
            <div class="chart-title">Top Performers</div>
            <div class="chart-subtitle">The ten most-sent cards this period</div>
        </div>
        """, unsafe_allow_html=True)

        top_10 = df.head(10).copy()
        if not top_10.empty:
            top_10["Short Name"] = top_10["Display Name"].apply(
                lambda x: x[:35] + "..." if len(str(x)) > 35 else x
            )

            fig_bar = go.Figure()
            fig_bar.add_trace(go.Bar(
                x=top_10["Current Period"].values[::-1],
                y=top_10["Short Name"].values[::-1],
                orientation='h',
                marker=dict(
                    color=CHART_COLORS[:10][::-1],
                    line=dict(width=0)
                ),
                hovertemplate="<b>%{y}</b><br>Sends: %{x:,.0f}<extra></extra>"
            ))

            fig_bar.update_layout(
                height=400,
                margin=dict(l=0, r=20, t=10, b=10),
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font=dict(family="Source Sans 3, sans-serif", color="#2D2A26"),
                xaxis=dict(
                    showgrid=True,
                    gridcolor="rgba(45, 42, 38, 0.06)",
                    zeroline=False,
                ),
                yaxis=dict(
                    showgrid=False,
                    zeroline=False,
                ),
                showlegend=False,
            )

            st.plotly_chart(fig_bar, use_container_width=True, config={"displayModeBar": False})

    with col2:
        # Category Donut Chart
        st.markdown("""
        <div class="chart-container">
            <div class="chart-title">Category Distribution</div>
            <div class="chart-subtitle">Sends by occasion type</div>
        </div>
        """, unsafe_allow_html=True)

        # Aggregate by occasion from analysis data
        occasion_sends = {}
        for _, row in df.iterrows():
            card_id = row["Card ID"]
            sends = row["Current Period"]

            if card_id in analysis_lookup:
                occasion = analysis_lookup[card_id].get("occasion", "other")
            else:
                occasion = "other"

            occasion = occasion.title() if occasion else "Other"
            occasion_sends[occasion] = occasion_sends.get(occasion, 0) + sends

        if occasion_sends:
            occasion_df = pd.DataFrame([
                {"Occasion": k, "Sends": v} for k, v in occasion_sends.items()
            ]).sort_values("Sends", ascending=False)

            # Limit to top 8 categories + Other
            if len(occasion_df) > 8:
                top_occasions = occasion_df.head(8)
                other_sends = occasion_df.iloc[8:]["Sends"].sum()
                top_occasions = pd.concat([
                    top_occasions,
                    pd.DataFrame([{"Occasion": "Other", "Sends": other_sends}])
                ], ignore_index=True)
                occasion_df = top_occasions

            fig_donut = go.Figure(data=[go.Pie(
                labels=occasion_df["Occasion"],
                values=occasion_df["Sends"],
                hole=0.55,
                marker=dict(
                    colors=CHART_COLORS[:len(occasion_df)],
                    line=dict(color='#FDFBF7', width=2)
                ),
                textposition='outside',
                textinfo='label+percent',
                textfont=dict(size=11),
                hovertemplate="<b>%{label}</b><br>Sends: %{value:,.0f}<br>Share: %{percent}<extra></extra>"
            )])

            fig_donut.update_layout(
                height=400,
                margin=dict(l=20, r=20, t=20, b=20),
                paper_bgcolor="rgba(0,0,0,0)",
                font=dict(family="Source Sans 3, sans-serif", color="#2D2A26"),
                showlegend=False,
                annotations=[dict(
                    text=f'<b>{len(df)}</b><br>Cards',
                    x=0.5, y=0.5,
                    font=dict(size=16, family="Playfair Display, serif", color="#2D2A26"),
                    showarrow=False
                )]
            )

            st.plotly_chart(fig_donut, use_container_width=True, config={"displayModeBar": False})


def render_executive_summary(df: pd.DataFrame, analysis_lookup: dict):
    """Render deep executive insights and analysis."""

    st.markdown("""
    <div class="section-container">
        <div class="section-header">
            <span class="section-number">02</span>
            <h2 class="section-title">Executive Insights</h2>
            <div class="section-line"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Gather statistics from analysis data
    design_styles = {}
    typography_styles = {}
    colors = {}
    themes = {}
    artists = {}

    for card_id, analysis in analysis_lookup.items():
        # Design styles
        style = analysis.get("design_style")
        if style:
            design_styles[style] = design_styles.get(style, 0) + 1

        # Typography
        typo = analysis.get("typography_style")
        if typo:
            typography_styles[typo] = typography_styles.get(typo, 0) + 1

        # Colors
        card_colors = analysis.get("primary_colors")
        if card_colors and isinstance(card_colors, list):
            for color in card_colors:
                colors[color] = colors.get(color, 0) + 1

        # Themes
        card_themes = analysis.get("themes")
        if card_themes and isinstance(card_themes, list):
            for theme in card_themes:
                themes[theme] = themes.get(theme, 0) + 1

        # Extract artist from card name
        card_name = analysis.get("card_name", "")
        if card_name:
            # Common artist patterns
            for sep in [" by ", " - "]:
                if sep in card_name:
                    artist = card_name.split(sep)[-1].strip()
                    artists[artist] = artists.get(artist, 0) + 1
                    break

    # Key insights cards
    st.markdown("""
    <div style="background: linear-gradient(135deg, #FDF8F3 0%, #FDFBF7 100%);
                border-radius: 12px; padding: 2rem; margin-bottom: 2rem;
                border: 1px solid rgba(198, 93, 59, 0.1);">
        <h3 style="font-family: 'Playfair Display', serif; color: #C65D3B; margin-bottom: 1rem; font-size: 1.4rem;">
            Key Findings at a Glance
        </h3>
        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem;">
    """, unsafe_allow_html=True)

    # Calculate key metrics
    top_style = max(design_styles.items(), key=lambda x: x[1]) if design_styles else ("N/A", 0)
    top_color = max(colors.items(), key=lambda x: x[1]) if colors else ("N/A", 0)
    top_theme = max(themes.items(), key=lambda x: x[1]) if themes else ("N/A", 0)
    top_typo = max(typography_styles.items(), key=lambda x: x[1]) if typography_styles else ("N/A", 0)

    insights = [
        (f"🎨 {top_style[0].replace('_', ' ').title()}", "Dominant Design Style", f"{top_style[1]} cards ({100*top_style[1]/len(analysis_lookup):.0f}%)"),
        (f"🎯 {top_color[0].title()}", "Most Used Color", f"Appears in {top_color[1]} cards"),
        (f"📝 {top_typo[0].replace('_', ' ').title()}", "Leading Typography", f"{top_typo[1]} cards use this style"),
        (f"✨ {top_theme[0].title()}", "Top Theme", f"Featured in {top_theme[1]} designs"),
    ]

    for value, label, detail in insights:
        st.markdown(f"""
        <div style="background: white; padding: 1rem; border-radius: 8px; border-left: 3px solid #C65D3B;">
            <div style="font-family: 'Playfair Display', serif; font-size: 1.1rem; color: #2D2A26; font-weight: 600;">{value}</div>
            <div style="font-size: 0.75rem; color: #8B8680; text-transform: uppercase; letter-spacing: 0.5px;">{label}</div>
            <div style="font-size: 0.85rem; color: #5C5955; margin-top: 0.25rem;">{detail}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div></div>", unsafe_allow_html=True)

    # Design Style Analysis
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <div class="chart-container">
            <div class="chart-title">Design Style Breakdown</div>
            <div class="chart-subtitle">Distribution of visual approaches across all cards</div>
        </div>
        """, unsafe_allow_html=True)

        if design_styles:
            style_df = pd.DataFrame([
                {"Style": k.replace("_", " ").title(), "Count": v}
                for k, v in sorted(design_styles.items(), key=lambda x: -x[1])[:10]
            ])

            fig_style = go.Figure()
            fig_style.add_trace(go.Bar(
                x=style_df["Count"],
                y=style_df["Style"],
                orientation='h',
                marker=dict(
                    color=['#C65D3B', '#D4846A', '#E0A48F', '#8B7355', '#A69076',
                           '#5C8A6E', '#7BA393', '#98BBB0', '#6B8E9B', '#8AABB5'][:len(style_df)],
                    line=dict(width=0)
                ),
                text=style_df["Count"],
                textposition='outside',
                hovertemplate="<b>%{y}</b><br>Cards: %{x}<extra></extra>"
            ))

            fig_style.update_layout(
                height=350,
                margin=dict(l=0, r=40, t=10, b=10),
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font=dict(family="Source Sans 3, sans-serif", color="#2D2A26"),
                xaxis=dict(showgrid=True, gridcolor="rgba(45,42,38,0.06)", zeroline=False),
                yaxis=dict(showgrid=False, zeroline=False, autorange="reversed"),
                showlegend=False,
            )
            st.plotly_chart(fig_style, use_container_width=True, config={"displayModeBar": False})

    with col2:
        st.markdown("""
        <div class="chart-container">
            <div class="chart-title">Typography Analysis</div>
            <div class="chart-subtitle">Font style preferences in top-performing cards</div>
        </div>
        """, unsafe_allow_html=True)

        if typography_styles:
            typo_df = pd.DataFrame([
                {"Typography": k.replace("_", " ").title(), "Count": v}
                for k, v in sorted(typography_styles.items(), key=lambda x: -x[1])
            ])

            fig_typo = go.Figure(data=[go.Pie(
                labels=typo_df["Typography"],
                values=typo_df["Count"],
                hole=0.4,
                marker=dict(
                    colors=['#C65D3B', '#5C8A6E', '#6B8E9B', '#8B7355', '#A69076',
                            '#D4846A', '#7BA393', '#98BBB0'][:len(typo_df)],
                    line=dict(color='#FDFBF7', width=2)
                ),
                textposition='outside',
                textinfo='label+percent',
                textfont=dict(size=10),
                hovertemplate="<b>%{label}</b><br>Cards: %{value}<br>Share: %{percent}<extra></extra>"
            )])

            fig_typo.update_layout(
                height=350,
                margin=dict(l=20, r=20, t=20, b=20),
                paper_bgcolor="rgba(0,0,0,0)",
                font=dict(family="Source Sans 3, sans-serif", color="#2D2A26"),
                showlegend=False,
            )
            st.plotly_chart(fig_typo, use_container_width=True, config={"displayModeBar": False})

    # Color Palette Section
    st.markdown("""
    <div class="chart-container" style="margin-top: 2rem;">
        <div class="chart-title">Color Palette Intelligence</div>
        <div class="chart-subtitle">The colors that drive engagement across your card portfolio</div>
    </div>
    """, unsafe_allow_html=True)

    # Color mapping for display
    color_hex = {
        "pink": "#FFB6C1", "white": "#FFFFFF", "orange": "#FF8C42", "green": "#5C8A6E",
        "blue": "#6B8E9B", "yellow": "#F4D03F", "red": "#C0392B", "cream": "#FDF8F3",
        "black": "#2D2A26", "teal": "#008080", "multicolor": "linear-gradient(90deg, #FF6B6B, #4ECDC4, #45B7D1)",
        "brown": "#8B7355", "gold": "#D4AF37", "coral": "#FF7F50", "purple": "#9B59B6",
        "navy": "#34495E", "tan": "#D2B48C", "mint": "#98D8C8", "lavender": "#E6E6FA",
        "peach": "#FFCBA4", "sage": "#9CAF88", "sage green": "#9CAF88"
    }

    top_colors = sorted(colors.items(), key=lambda x: -x[1])[:12]

    # Use st.columns for reliable rendering
    cols = st.columns(6)
    for idx, (color_name, count) in enumerate(top_colors):
        hex_color = color_hex.get(color_name.lower(), "#CCC")
        is_gradient = "gradient" in hex_color
        bg_style = f"background: {hex_color};" if is_gradient else f"background-color: {hex_color};"
        border_style = "border: 1px solid #DDD;" if color_name.lower() in ["white", "cream"] else ""

        with cols[idx % 6]:
            st.markdown(f'''<div style="text-align: center; padding: 0.5rem;">
<div style="width: 50px; height: 50px; border-radius: 50%; {bg_style} {border_style} margin: 0 auto; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"></div>
<div style="font-size: 0.8rem; color: #2D2A26; margin-top: 0.5rem; font-weight: 500;">{color_name.title()}</div>
<div style="font-size: 0.7rem; color: #8B8680;">{count} cards</div>
</div>''', unsafe_allow_html=True)

    # ==========================================================================
    # COLOR PERFORMANCE BY OCCASION ANALYSIS
    # ==========================================================================
    render_color_performance_by_occasion(df, analysis_lookup, color_hex)

    # Theme Analysis
    st.markdown("""
    <div class="chart-container" style="margin-top: 2.5rem;">
        <div class="chart-title">Theme & Motif Analysis</div>
        <div class="chart-subtitle">Visual elements that resonate with your audience</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1], gap="large")

    with col1:
        if themes:
            theme_df = pd.DataFrame([
                {"Theme": k.title(), "Count": v}
                for k, v in sorted(themes.items(), key=lambda x: -x[1])[:15]
            ])

            fig_theme = go.Figure()
            fig_theme.add_trace(go.Bar(
                x=theme_df["Theme"],
                y=theme_df["Count"],
                marker=dict(
                    color='#C65D3B',
                    line=dict(width=0)
                ),
                text=theme_df["Count"],
                textposition='outside',
                hovertemplate="<b>%{x}</b><br>Appears in %{y} cards<extra></extra>"
            ))

            fig_theme.update_layout(
                height=300,
                margin=dict(l=0, r=0, t=10, b=60),
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font=dict(family="Source Sans 3, sans-serif", color="#2D2A26"),
                xaxis=dict(showgrid=False, zeroline=False, tickangle=-45),
                yaxis=dict(showgrid=True, gridcolor="rgba(45,42,38,0.06)", zeroline=False),
                showlegend=False,
            )
            st.plotly_chart(fig_theme, use_container_width=True, config={"displayModeBar": False})

    with col2:
        st.markdown("""
        <div style="background: #FDF8F3; padding: 1.5rem; border-radius: 8px; height: 100%;">
            <h4 style="font-family: 'Playfair Display', serif; color: #C65D3B; margin-bottom: 1rem; font-size: 1rem;">
                Theme Insights
            </h4>
        """, unsafe_allow_html=True)

        theme_insights = [
            "🎂 **Food & Celebration** themes dominate birthday cards",
            "🌸 **Florals & Nature** lead in thank you and Mother's Day",
            "🎨 **Abstract patterns** show strong modern appeal",
            "❤️ **Hearts** are essential for Valentine's & love occasions",
        ]
        for insight in theme_insights:
            st.markdown(f'<p style="font-size: 0.85rem; color: #5C5955; margin-bottom: 0.75rem; line-height: 1.4;">{insight}</p>', unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    # Style Performance Recommendations
    st.markdown("""
    <div style="background: linear-gradient(135deg, #2D2A26 0%, #3D3A36 100%);
                border-radius: 12px; padding: 2rem; margin-top: 2rem; color: white;">
        <h3 style="font-family: 'Playfair Display', serif; color: #F4D03F; margin-bottom: 1.5rem; font-size: 1.3rem;">
            Strategic Recommendations
        </h3>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem;">
            <div>
                <div style="font-weight: 600; color: #C65D3B; margin-bottom: 0.5rem;">Expand Illustrated Style</div>
                <div style="font-size: 0.85rem; color: #CCC; line-height: 1.5;">
                    With 100+ cards, illustrated designs dominate the top 50. Continue investing in this proven style.
                </div>
            </div>
            <div>
                <div style="font-weight: 600; color: #5C8A6E; margin-bottom: 0.5rem;">Leverage Pink & Warm Tones</div>
                <div style="font-size: 0.85rem; color: #CCC; line-height: 1.5;">
                    Pink appears in 129 cards - nearly half the catalog. Warm palettes consistently outperform cool.
                </div>
            </div>
            <div>
                <div style="font-weight: 600; color: #6B8E9B; margin-bottom: 0.5rem;">Sans-Serif Typography Wins</div>
                <div style="font-size: 0.85rem; color: #CCC; line-height: 1.5;">
                    Clean, modern sans-serif fonts lead in 110 cards. Pair with handwritten accents for personality.
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)




def render_artist_performance(analysis_data: list, csv_df: pd.DataFrame):
    """Render the Artist Performance Intelligence section with leaderboard and charts."""

    st.markdown("""
    <div class="section-container">
        <div class="section-header">
            <span class="section-number">05</span>
            <h2 class="section-title">Artist Performance Intelligence</h2>
            <div class="section-line"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Build artist statistics
    artist_df = build_artist_stats(analysis_data, csv_df)

    if artist_df.empty:
        st.info("No artist data available for analysis.")
        return

    # Top 15 artists for the leaderboard
    top_15_artists = artist_df.head(15)

    # Section intro with key stats
    total_artists = len(artist_df)
    top_artist = artist_df.iloc[0] if not artist_df.empty else None

    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #FDF8F3 0%, #FDFBF7 100%);
                border-radius: 12px; padding: 2rem; margin-bottom: 2rem;
                border: 1px solid rgba(198, 93, 59, 0.1);">
        <h3 style="font-family: 'Playfair Display', serif; color: #C65D3B; margin-bottom: 1rem; font-size: 1.4rem;">
            Creative Talent Overview
        </h3>
        <p style="font-family: 'Source Sans 3', sans-serif; font-size: 1rem; color: #5C5955; line-height: 1.6; margin-bottom: 1.5rem;">
            Discover which artists and studios drive the most engagement. This analysis examines
            <strong>{total_artists}</strong> distinct creative contributors across your card portfolio.
        </p>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem;">
            <div style="background: white; padding: 1rem; border-radius: 8px; border-left: 3px solid #C65D3B;">
                <div style="font-family: 'Playfair Display', serif; font-size: 1.1rem; color: #2D2A26; font-weight: 600;">
                    {top_artist['Artist'] if top_artist is not None else 'N/A'}
                </div>
                <div style="font-size: 0.75rem; color: #8B8680; text-transform: uppercase; letter-spacing: 0.5px;">Top Artist</div>
                <div style="font-size: 0.85rem; color: #C65D3B; margin-top: 0.25rem; font-weight: 600;">
                    {int(top_artist['Total Sends']):,} sends
                </div>
            </div>
            <div style="background: white; padding: 1rem; border-radius: 8px; border-left: 3px solid #5C8A6E;">
                <div style="font-family: 'Playfair Display', serif; font-size: 1.1rem; color: #2D2A26; font-weight: 600;">
                    {total_artists}
                </div>
                <div style="font-size: 0.75rem; color: #8B8680; text-transform: uppercase; letter-spacing: 0.5px;">Total Artists</div>
                <div style="font-size: 0.85rem; color: #5C5955; margin-top: 0.25rem;">
                    Contributing to your catalog
                </div>
            </div>
            <div style="background: white; padding: 1rem; border-radius: 8px; border-left: 3px solid #6B8E9B;">
                <div style="font-family: 'Playfair Display', serif; font-size: 1.1rem; color: #2D2A26; font-weight: 600;">
                    {int(artist_df['Avg Sends per Card'].mean()):,}
                </div>
                <div style="font-size: 0.75rem; color: #8B8680; text-transform: uppercase; letter-spacing: 0.5px;">Avg Sends/Card</div>
                <div style="font-size: 0.85rem; color: #5C5955; margin-top: 0.25rem;">
                    Across all artists
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Two column layout: Leaderboard table + Bar chart
    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown("""
        <div class="chart-container">
            <div class="chart-title">Artist Leaderboard</div>
            <div class="chart-subtitle">Top 15 artists ranked by total sends</div>
        </div>
        """, unsafe_allow_html=True)

        # Create styled leaderboard - render each row individually for proper HTML rendering
        leaderboard_container = st.container()
        with leaderboard_container:
            for idx, row in top_15_artists.iterrows():
                rank = int(row['Rank'])
                artist = row['Artist']
                total_sends = int(row['Total Sends'])
                card_count = int(row['Card Count'])
                avg_sends = int(row['Avg Sends per Card'])
                style = row['Primary Style']

                # Medal colors for top 3
                if rank == 1:
                    rank_bg = "linear-gradient(135deg, #FFD700, #FFA500)"
                    rank_color = "white"
                elif rank == 2:
                    rank_bg = "linear-gradient(135deg, #C0C0C0, #A8A8A8)"
                    rank_color = "white"
                elif rank == 3:
                    rank_bg = "linear-gradient(135deg, #CD7F32, #B8860B)"
                    rank_color = "white"
                else:
                    rank_bg = "#F5F0EB"
                    rank_color = "#2D2A26"

                # Use columns for layout instead of complex nested divs
                c1, c2, c3 = st.columns([1, 6, 2])
                with c1:
                    st.markdown(f'''<div style="width: 32px; height: 32px; border-radius: 50%; display: flex;
                        align-items: center; justify-content: center; font-family: Playfair Display, serif;
                        font-size: 0.85rem; font-weight: 600; background: {rank_bg}; color: {rank_color};">{rank}</div>''',
                        unsafe_allow_html=True)
                with c2:
                    st.markdown(f'''<div style="font-family: Playfair Display, serif; font-size: 0.95rem;
                        color: #2D2A26; font-weight: 600;">{artist}</div>
                        <div style="font-size: 0.75rem; color: #8B8680;">{card_count} cards · {avg_sends:,} avg/card · <span style="color: #C65D3B;">{style}</span></div>''',
                        unsafe_allow_html=True)
                with c3:
                    st.markdown(f'''<div style="text-align: right;">
                        <div style="font-family: Playfair Display, serif; font-size: 1.1rem; color: #C65D3B; font-weight: 600;">{total_sends:,}</div>
                        <div style="font-size: 0.7rem; color: #8B8680; text-transform: uppercase;">sends</div>
                    </div>''', unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="chart-container">
            <div class="chart-title">Top Artists by Total Sends</div>
            <div class="chart-subtitle">Horizontal bar chart visualization</div>
        </div>
        """, unsafe_allow_html=True)

        # Create horizontal bar chart
        chart_data = top_15_artists.copy()
        chart_data = chart_data.sort_values('Total Sends', ascending=True)

        # Truncate long artist names
        chart_data['Display Name'] = chart_data['Artist'].apply(
            lambda x: x[:25] + '...' if len(str(x)) > 25 else x
        )

        fig_bar = go.Figure()
        fig_bar.add_trace(go.Bar(
            x=chart_data['Total Sends'],
            y=chart_data['Display Name'],
            orientation='h',
            marker=dict(
                color=['#C65D3B', '#D4785C', '#E8A87C', '#DEB887', '#B8860B',
                       '#CD853F', '#8B7355', '#A0522D', '#BC8F8F', '#C4A484',
                       '#D2B48C', '#DAA520', '#E9967A', '#F4A460', '#FFDAB9'][:len(chart_data)][::-1],
                line=dict(width=0)
            ),
            text=chart_data['Total Sends'].apply(lambda x: f'{x:,}'),
            textposition='outside',
            hovertemplate="<b>%{y}</b><br>Total Sends: %{x:,.0f}<extra></extra>"
        ))

        fig_bar.update_layout(
            height=500,
            margin=dict(l=0, r=60, t=10, b=10),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(family="Source Sans 3, sans-serif", color="#2D2A26"),
            xaxis=dict(
                showgrid=True,
                gridcolor="rgba(45, 42, 38, 0.06)",
                zeroline=False,
            ),
            yaxis=dict(
                showgrid=False,
                zeroline=False,
            ),
            showlegend=False,
        )

        st.plotly_chart(fig_bar, use_container_width=True, config={"displayModeBar": False})

    # Style specialty breakdown
    st.markdown("""
    <div class="chart-container" style="margin-top: 2rem;">
        <div class="chart-title">Design Style Specialties</div>
        <div class="chart-subtitle">Primary design approaches of top-performing artists</div>
    </div>
    """, unsafe_allow_html=True)

    # Aggregate styles from top 15
    style_counts = top_15_artists['Primary Style'].value_counts()

    cols = st.columns(min(len(style_counts), 6))
    for idx, (style, count) in enumerate(style_counts.items()):
        with cols[idx % 6]:
            st.markdown(f'''
            <div style="text-align: center; padding: 1rem; background: white; border-radius: 8px;
                        border: 1px solid rgba(45, 42, 38, 0.06);">
                <div style="font-family: \'Playfair Display\', serif; font-size: 1.5rem;
                            color: #C65D3B; font-weight: 600;">{count}</div>
                <div style="font-size: 0.8rem; color: #2D2A26; font-weight: 500;">{style}</div>
                <div style="font-size: 0.7rem; color: #8B8680;">artists</div>
            </div>
            ''', unsafe_allow_html=True)


def render_gallery(df: pd.DataFrame, analysis_lookup: dict):
    """Render the card gallery with beautiful styling."""

    st.markdown("""
    <div class="section-container">
        <div class="section-header">
            <span class="section-number">06</span>
            <h2 class="section-title">Card Gallery</h2>
            <div class="section-line"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if df.empty:
        st.info("No cards match the current filters.")
        return

    # Pagination settings
    total_cards = len(df)

    # Display options at the top
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        show_all = st.checkbox("Show all cards on one page", key="gallery_show_all")

    if show_all:
        page_df = df
        start_idx = 0
        end_idx = total_cards
        total_pages = 1
        current_page = 1
    else:
        total_pages = (total_cards + CARDS_PER_PAGE - 1) // CARDS_PER_PAGE
        # Initialize session state for page if not exists
        if "gallery_page_num" not in st.session_state:
            st.session_state.gallery_page_num = 1
        current_page = st.session_state.gallery_page_num
        # Ensure current page is valid
        if current_page > total_pages:
            current_page = 1
            st.session_state.gallery_page_num = 1
        start_idx = (current_page - 1) * CARDS_PER_PAGE
        end_idx = min(start_idx + CARDS_PER_PAGE, total_cards)
        page_df = df.iloc[start_idx:end_idx]

    # Filter status
    st.markdown(f"""
    <div class="filter-status">
        <span class="filter-status-text">
            Showing cards <span class="filter-status-count">{start_idx + 1}-{end_idx}</span>
            of <span class="filter-status-count">{total_cards}</span>
        </span>
    </div>
    """, unsafe_allow_html=True)

    # Build all card HTML for CSS grid layout
    cards_html = []
    card_data_list = []

    for idx, (_, card) in enumerate(page_df.iterrows()):
        card_name = card["Card Name"]
        card_id = card["Card ID"]
        display_name = card["Display Name"]
        rank = int(card["Rank"])
        sends = int(card["Current Period"])

        # Get occasion from analysis
        occasion = "General"
        if card_id in analysis_lookup:
            occasion = analysis_lookup[card_id].get("occasion", "general").title()

        # Get image
        image_path = get_card_image_path(card_name)

        if image_path:
            img_base64 = get_image_base64(image_path)
            if img_base64:
                img_html = f'<img src="data:image/jpeg;base64,{img_base64}" alt="{display_name}">'
            else:
                img_html = '<div class="no-image-placeholder">No Preview</div>'
        else:
            img_html = '<div class="no-image-placeholder">No Preview</div>'

        # Truncate title and escape HTML characters
        title_display = display_name[:45] + "..." if len(display_name) > 45 else display_name
        # Escape HTML special characters
        title_display = title_display.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
        occasion_safe = occasion.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

        card_html = f'<div class="card-item"><div class="card-image-container">{img_html}<div class="card-rank-badge">#{rank}</div><div class="card-occasion-tag">{occasion_safe}</div></div><div class="card-info"><div class="card-title">{title_display}</div><div class="card-sends"><span class="card-sends-value">{sends:,}</span><span class="card-sends-label">sends</span></div></div></div>'
        cards_html.append(card_html)
        card_data_list.append({
            "card_id": card_id,
            "rank": rank,
            "sends": sends,
            "previous": int(card["Previous Period"]),
            "change": card.get("Change", 0),
            "change_pct": card.get("Change %", 0)
        })

    # Render all cards in a CSS grid
    grid_html = f'<div class="gallery-grid">{"".join(cards_html)}</div>'
    st.markdown(grid_html, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Bottom pagination navigation (only show if not showing all)
    if not show_all and total_pages > 1:
        st.markdown("<br>", unsafe_allow_html=True)

        # Navigation buttons at the bottom using number_input for direct page control
        nav_col1, nav_col2, nav_col3, nav_col4, nav_col5 = st.columns([1, 1, 2, 1, 1])

        with nav_col1:
            if st.button("⏮ First", key="gallery_first", disabled=(current_page == 1)):
                st.session_state.gallery_page_num = 1

        with nav_col2:
            if st.button("◀ Prev", key="gallery_prev", disabled=(current_page == 1)):
                st.session_state.gallery_page_num = max(1, current_page - 1)

        with nav_col3:
            st.markdown(f"""
            <div style="text-align: center; padding: 8px; font-family: 'Source Sans 3', sans-serif; font-size: 0.95rem; color: #1a1a1a;">
                Page <strong>{current_page}</strong> of <strong>{total_pages}</strong>
            </div>
            """, unsafe_allow_html=True)

        with nav_col4:
            if st.button("Next ▶", key="gallery_next", disabled=(current_page == total_pages)):
                st.session_state.gallery_page_num = min(total_pages, current_page + 1)

        with nav_col5:
            if st.button("Last ⏭", key="gallery_last", disabled=(current_page == total_pages)):
                st.session_state.gallery_page_num = total_pages


def render_color_performance_by_occasion(df: pd.DataFrame, analysis_lookup: dict, color_hex: dict):
    """Render the Color Performance by Occasion analysis section."""
    import numpy as np
    from collections import defaultdict
    from itertools import combinations

    st.markdown("""
    <div class="chart-container" style="margin-top: 2.5rem;">
        <div class="chart-title">Color Performance by Occasion</div>
        <div class="chart-subtitle">Discover which color palettes drive the highest engagement for each occasion</div>
    </div>
    """, unsafe_allow_html=True)

    # Build data structures for analysis
    # occasion -> color -> list of sends
    occasion_color_sends = defaultdict(lambda: defaultdict(list))
    # occasion -> list of (color_combo_tuple, sends)
    occasion_palette_sends = defaultdict(list)
    # color pair -> total sends (for correlation)
    color_pair_sends = defaultdict(list)
    # all color pairs that appear together
    color_cooccurrence = defaultdict(int)
    # color -> occasion -> count (for underutilized analysis)
    color_occasion_count = defaultdict(lambda: defaultdict(int))
    # occasion -> total cards
    occasion_card_count = defaultdict(int)

    for card_id, analysis in analysis_lookup.items():
        occasion = analysis.get("occasion", "").lower()
        if not occasion:
            continue

        occasion_card_count[occasion] += 1
        card_colors = analysis.get("primary_colors", [])
        sends = analysis.get("sends_current", 0)

        if not card_colors or not isinstance(card_colors, list):
            continue

        # Track individual color performance per occasion
        for color in card_colors:
            color_lower = color.lower()
            occasion_color_sends[occasion][color_lower].append(sends)
            color_occasion_count[color_lower][occasion] += 1

        # Track color combinations (palette) performance
        # Sort colors to create consistent palette keys
        sorted_colors = tuple(sorted([c.lower() for c in card_colors]))
        if len(sorted_colors) >= 2:
            occasion_palette_sends[occasion].append((sorted_colors, sends))

        # Track color co-occurrence for correlation matrix
        for c1, c2 in combinations(sorted([c.lower() for c in card_colors]), 2):
            color_cooccurrence[(c1, c2)] += 1
            color_pair_sends[(c1, c2)].append(sends)

    # Get top 5 occasions by total sends
    occasion_total_sends = {}
    for occasion in occasion_color_sends.keys():
        total = sum(sum(sends_list) for sends_list in occasion_color_sends[occasion].values())
        occasion_total_sends[occasion] = total

    top_occasions = sorted(occasion_total_sends.items(), key=lambda x: -x[1])[:5]
    top_occasion_names = [occ[0] for occ in top_occasions]

    # Get top colors across all occasions
    all_color_sends = defaultdict(list)
    for occasion_data in occasion_color_sends.values():
        for color, sends_list in occasion_data.items():
            all_color_sends[color].extend(sends_list)

    top_colors = sorted(all_color_sends.items(), key=lambda x: -sum(x[1]))[:8]
    top_color_names = [c[0] for c in top_colors]

    # =========================================================================
    # 1. GROUPED BAR CHART: Average sends by color for top 5 occasions
    # =========================================================================
    st.markdown("""
    <div style="margin-top: 1.5rem; margin-bottom: 0.5rem;">
        <h4 style="font-family: 'Playfair Display', serif; color: #2D2A26; font-size: 1.1rem; margin-bottom: 0.25rem;">
            Average Sends by Color & Occasion
        </h4>
        <p style="font-size: 0.85rem; color: #8B8680; margin-bottom: 1rem;">
            How each color performs across the top 5 occasions
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Build data for grouped bar chart
    bar_data = []
    for occasion in top_occasion_names:
        for color in top_color_names:
            sends_list = occasion_color_sends[occasion].get(color, [])
            avg_sends = np.mean(sends_list) if sends_list else 0
            bar_data.append({
                "Occasion": occasion.replace("_", " ").title(),
                "Color": color.title(),
                "Average Sends": round(avg_sends),
                "Card Count": len(sends_list)
            })

    bar_df = pd.DataFrame(bar_data)

    # Create grouped bar chart
    fig_grouped = go.Figure()

    # Color palette for the chart bars
    bar_colors = {
        "Pink": "#FFB6C1", "White": "#E8E8E8", "Orange": "#FF8C42", "Green": "#5C8A6E",
        "Blue": "#6B8E9B", "Yellow": "#F4D03F", "Red": "#C0392B", "Cream": "#FDF8F3",
        "Black": "#2D2A26", "Teal": "#008080", "Multicolor": "#9B59B6",
        "Brown": "#8B7355", "Gold": "#D4AF37", "Coral": "#FF7F50", "Purple": "#9B59B6",
        "Mint": "#98D8C8", "Peach": "#FFCBA4"
    }

    for color in [c.title() for c in top_color_names]:
        color_data = bar_df[bar_df["Color"] == color]
        fig_grouped.add_trace(go.Bar(
            name=color,
            x=color_data["Occasion"],
            y=color_data["Average Sends"],
            marker_color=bar_colors.get(color, "#CCC"),
            marker_line_width=0,
            hovertemplate=f"<b>{color}</b><br>%{{x}}<br>Avg: %{{y:,.0f}} sends<extra></extra>"
        ))

    fig_grouped.update_layout(
        barmode='group',
        height=350,
        margin=dict(l=0, r=0, t=10, b=60),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Source Sans 3, sans-serif", color="#2D2A26"),
        xaxis=dict(showgrid=False, zeroline=False, tickangle=-15),
        yaxis=dict(showgrid=True, gridcolor="rgba(45,42,38,0.06)", zeroline=False, title="Average Sends"),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5,
            font=dict(size=10)
        ),
        bargap=0.15,
        bargroupgap=0.1
    )

    st.plotly_chart(fig_grouped, use_container_width=True, config={"displayModeBar": False})

    # =========================================================================
    # 2. COLOR CORRELATION MATRIX & WINNING PALETTES (side by side)
    # =========================================================================
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <div style="margin-top: 1rem; margin-bottom: 0.5rem;">
            <h4 style="font-family: 'Playfair Display', serif; color: #2D2A26; font-size: 1.1rem; margin-bottom: 0.25rem;">
                Color Correlation Matrix
            </h4>
            <p style="font-size: 0.85rem; color: #8B8680; margin-bottom: 1rem;">
                Which colors appear together in top performers
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Build correlation matrix for top colors
        matrix_colors = top_color_names[:6]  # Limit to 6 for readability
        matrix_size = len(matrix_colors)
        correlation_matrix = np.zeros((matrix_size, matrix_size))

        # Calculate average sends for each color pair
        for i, c1 in enumerate(matrix_colors):
            for j, c2 in enumerate(matrix_colors):
                if i == j:
                    # Diagonal: average sends for this color alone
                    correlation_matrix[i][j] = np.mean(all_color_sends.get(c1, [0])) if all_color_sends.get(c1) else 0
                else:
                    # Off-diagonal: average sends when these colors appear together
                    pair_key = tuple(sorted([c1, c2]))
                    pair_sends = color_pair_sends.get(pair_key, [])
                    correlation_matrix[i][j] = np.mean(pair_sends) if pair_sends else 0

        # Create heatmap
        fig_heatmap = go.Figure(data=go.Heatmap(
            z=correlation_matrix,
            x=[c.title() for c in matrix_colors],
            y=[c.title() for c in matrix_colors],
            colorscale=[
                [0, "#FDF8F3"],
                [0.25, "#FFCBA4"],
                [0.5, "#E8A87C"],
                [0.75, "#D4785C"],
                [1, "#C65D3B"]
            ],
            hovertemplate="<b>%{y} + %{x}</b><br>Avg Sends: %{z:,.0f}<extra></extra>",
            showscale=True,
            colorbar=dict(
                title=dict(text="Avg Sends", side="right"),
                tickformat=",.0f"
            )
        ))

        # Add text annotations
        annotations = []
        for i, row in enumerate(correlation_matrix):
            for j, val in enumerate(row):
                annotations.append(dict(
                    x=matrix_colors[j].title(),
                    y=matrix_colors[i].title(),
                    text=f"{int(val):,}" if val > 0 else "-",
                    showarrow=False,
                    font=dict(size=9, color="#2D2A26" if val < np.max(correlation_matrix) * 0.7 else "#FFF")
                ))

        fig_heatmap.update_layout(
            height=300,
            margin=dict(l=0, r=0, t=10, b=10),
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(family="Source Sans 3, sans-serif", color="#2D2A26"),
            xaxis=dict(side="bottom"),
            annotations=annotations
        )

        st.plotly_chart(fig_heatmap, use_container_width=True, config={"displayModeBar": False})

    with col2:
        st.markdown("""
        <div style="margin-top: 1rem; margin-bottom: 0.5rem;">
            <h4 style="font-family: 'Playfair Display', serif; color: #2D2A26; font-size: 1.1rem; margin-bottom: 0.25rem;">
                Winning Palettes
            </h4>
            <p style="font-size: 0.85rem; color: #8B8680; margin-bottom: 1rem;">
                Top 5 color combinations by average performance
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Calculate winning palettes across all occasions
        palette_performance = defaultdict(list)
        for occasion, palettes in occasion_palette_sends.items():
            for palette, sends in palettes:
                # Only consider 2-3 color combinations for clarity
                if 2 <= len(palette) <= 3:
                    palette_performance[palette].append(sends)

        # Get top 5 palettes by average sends
        winning_palettes = []
        for palette, sends_list in palette_performance.items():
            if len(sends_list) >= 2:  # Require at least 2 cards with this palette
                winning_palettes.append({
                    "palette": palette,
                    "avg_sends": np.mean(sends_list),
                    "card_count": len(sends_list),
                    "total_sends": sum(sends_list)
                })

        winning_palettes = sorted(winning_palettes, key=lambda x: -x["avg_sends"])[:5]

        # Display winning palettes with color swatches
        for i, wp in enumerate(winning_palettes, 1):
            palette_colors = wp["palette"]
            avg_sends = wp["avg_sends"]
            card_count = wp["card_count"]

            # Create color swatches HTML
            swatches_html = ""
            for color in palette_colors:
                hex_val = color_hex.get(color, "#CCC")
                is_gradient = "gradient" in str(hex_val)
                bg = f"background: {hex_val};" if is_gradient else f"background-color: {hex_val};"
                border = "border: 1px solid #DDD;" if color in ["white", "cream"] else ""
                swatches_html += f'<div style="width: 24px; height: 24px; border-radius: 50%; {bg} {border} display: inline-block; margin-right: 4px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);"></div>'

            palette_name = " + ".join([c.title() for c in palette_colors])

            st.markdown(f"""
            <div style="display: flex; align-items: center; padding: 0.75rem; background: {'#FDF8F3' if i % 2 == 1 else '#FFF'}; border-radius: 8px; margin-bottom: 0.5rem; border-left: 3px solid #C65D3B;">
                <div style="font-family: 'Playfair Display', serif; font-size: 1.1rem; color: #C65D3B; font-weight: 600; width: 24px;">#{i}</div>
                <div style="flex: 1; margin-left: 0.75rem;">
                    <div style="display: flex; align-items: center; margin-bottom: 0.25rem;">
                        {swatches_html}
                    </div>
                    <div style="font-size: 0.8rem; color: #5C5955;">{palette_name}</div>
                </div>
                <div style="text-align: right;">
                    <div style="font-family: 'Playfair Display', serif; font-size: 1rem; color: #2D2A26; font-weight: 600;">{avg_sends:,.0f}</div>
                    <div style="font-size: 0.7rem; color: #8B8680;">avg sends ({card_count} cards)</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # =========================================================================
    # 3. INSIGHTS PANEL
    # =========================================================================
    st.markdown("""
    <div style="background: linear-gradient(135deg, #FDF8F3 0%, #FDFBF7 100%);
                border-radius: 12px; padding: 1.5rem; margin-top: 1.5rem;
                border: 1px solid rgba(198, 93, 59, 0.15);">
        <h4 style="font-family: 'Playfair Display', serif; color: #C65D3B; margin-bottom: 1rem; font-size: 1.1rem;">
            Color-Occasion Insights
        </h4>
    """, unsafe_allow_html=True)

    # Generate dynamic insights
    insights = []

    # Insight 1: Best performing color combo for top occasion
    if winning_palettes and top_occasion_names:
        top_palette = winning_palettes[0]
        palette_name = " + ".join([c.title() for c in top_palette["palette"]])
        # Find which occasion this palette performs best in
        best_occasion_for_palette = None
        best_avg = 0
        for occasion, palettes in occasion_palette_sends.items():
            for palette, sends in palettes:
                if palette == top_palette["palette"]:
                    if sends > best_avg:
                        best_avg = sends
                        best_occasion_for_palette = occasion

        if best_occasion_for_palette:
            insights.append({
                "text": f"{palette_name} averages {top_palette['avg_sends']:,.0f} sends",
                "subtext": f"Top performer across {top_palette['card_count']} cards",
                "colors": top_palette["palette"],
                "type": "success"
            })

    # Insight 2: Find best color for Birthday (most common occasion)
    if "birthday" in occasion_color_sends:
        birthday_colors = occasion_color_sends["birthday"]
        best_birthday_color = max(birthday_colors.items(), key=lambda x: np.mean(x[1]) if x[1] else 0)
        avg_birthday = np.mean(best_birthday_color[1]) if best_birthday_color[1] else 0
        insights.append({
            "text": f"{best_birthday_color[0].title()} leads Birthday cards with {avg_birthday:,.0f} avg sends",
            "subtext": f"Featured in {len(best_birthday_color[1])} birthday designs",
            "colors": [best_birthday_color[0]],
            "type": "highlight"
        })

    # Insight 3: Find underutilized color-occasion combinations
    # Look for colors that are popular overall but underused in certain occasions
    underutilized = []
    for color in top_color_names[:5]:
        total_usage = sum(color_occasion_count[color].values())
        for occasion in top_occasion_names:
            occasion_usage = color_occasion_count[color].get(occasion, 0)
            occasion_total = occasion_card_count.get(occasion, 1)
            usage_rate = occasion_usage / occasion_total if occasion_total > 0 else 0

            # If this color is used in less than 10% of cards for this occasion
            # but is popular overall
            if usage_rate < 0.1 and total_usage > 20 and occasion_usage < 5:
                # Check if the color actually performs well when used
                sends_when_used = occasion_color_sends[occasion].get(color, [])
                if sends_when_used:
                    avg_when_used = np.mean(sends_when_used)
                    overall_avg = np.mean(all_color_sends[color]) if all_color_sends[color] else 0
                    if avg_when_used >= overall_avg * 0.8:  # Performs reasonably well
                        underutilized.append({
                            "color": color,
                            "occasion": occasion,
                            "usage_count": occasion_usage,
                            "total_cards": occasion_total
                        })

    if underutilized:
        underutil = underutilized[0]
        insights.append({
            "text": f"Underutilized: {underutil['color'].title()} in {underutil['occasion'].replace('_', ' ').title()} cards",
            "subtext": f"Only {underutil['usage_count']} of {underutil['total_cards']} cards use this proven color",
            "colors": [underutil['color']],
            "type": "opportunity"
        })

    # Insight 4: High-performing color pair
    if color_pair_sends:
        best_pair = max(color_pair_sends.items(), key=lambda x: np.mean(x[1]) if x[1] else 0)
        pair_avg = np.mean(best_pair[1]) if best_pair[1] else 0
        pair_count = len(best_pair[1])
        if pair_count >= 3:
            insights.append({
                "text": f"{best_pair[0][0].title()} + {best_pair[0][1].title()} combo averages {pair_avg:,.0f} sends",
                "subtext": f"A winning duo appearing in {pair_count} top cards",
                "colors": list(best_pair[0]),
                "type": "success"
            })

    # Render insights in a grid
    cols = st.columns(2)
    for idx, insight in enumerate(insights[:4]):
        with cols[idx % 2]:
            # Create color swatches for insight
            swatches = ""
            for color in insight.get("colors", []):
                hex_val = color_hex.get(color, "#CCC")
                is_gradient = "gradient" in str(hex_val)
                bg = f"background: {hex_val};" if is_gradient else f"background-color: {hex_val};"
                border = "border: 1px solid #DDD;" if color in ["white", "cream"] else ""
                swatches += f'<div style="width: 18px; height: 18px; border-radius: 50%; {bg} {border} display: inline-block; margin-right: 4px;"></div>'

            type_colors = {
                "success": "#5C8A6E",
                "highlight": "#C65D3B",
                "opportunity": "#6B8E9B"
            }
            accent_color = type_colors.get(insight.get("type", "success"), "#5C8A6E")

            st.markdown(f"""
            <div style="background: white; padding: 1rem; border-radius: 8px; margin-bottom: 0.75rem; border-left: 3px solid {accent_color};">
                <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                    {swatches}
                </div>
                <div style="font-family: 'Source Sans 3', sans-serif; font-size: 0.9rem; color: #2D2A26; font-weight: 500; line-height: 1.4;">
                    {insight['text']}
                </div>
                <div style="font-size: 0.75rem; color: #8B8680; margin-top: 0.25rem;">
                    {insight['subtext']}
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)




def get_card_image_by_id(card_id: str) -> Path | None:
    """Get the image path for a card by its ID."""
    # Try direct match with card_id.png
    image_path = IMAGES_DIR / f"{card_id}.png"
    if image_path.exists():
        return image_path

    # Try other extensions
    for ext in [".jpg", ".jpeg", ".gif", ".webp"]:
        image_path = IMAGES_DIR / f"{card_id}{ext}"
        if image_path.exists():
            return image_path

    # Try matching files that start with card_id
    for image_file in IMAGES_DIR.glob(f"{card_id}*"):
        if image_file.suffix.lower() in [".jpg", ".jpeg", ".png", ".gif", ".webp"]:
            return image_file

    return None


def render_card_comparison(df: pd.DataFrame, analysis_lookup: dict):
    """Render the Card Comparison Tool section."""

    # Color mapping for display
    color_hex = {
        "pink": "#FFB6C1", "white": "#FFFFFF", "orange": "#FF8C42", "green": "#5C8A6E",
        "blue": "#6B8E9B", "yellow": "#F4D03F", "red": "#C0392B", "cream": "#FDF8F3",
        "black": "#2D2A26", "teal": "#008080", "multicolor": "#9B59B6",
        "brown": "#8B7355", "gold": "#D4AF37", "coral": "#FF7F50", "purple": "#9B59B6",
        "navy": "#34495E", "tan": "#D2B48C", "mint": "#98D8C8", "lavender": "#E6E6FA",
        "peach": "#FFCBA4", "sage": "#9CAF88", "sage green": "#9CAF88"
    }

    st.markdown("""
    <div class="section-container">
        <div class="section-header">
            <span class="section-number">05</span>
            <h2 class="section-title">Card Comparison Tool</h2>
            <div class="section-line"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="comparison-header">
        <p>Select 2-4 cards from the filtered view to compare their attributes, performance, and design characteristics side by side.</p>
    </div>
    """, unsafe_allow_html=True)

    if df.empty:
        st.info("No cards available in the current filter. Adjust your filters to see cards.")
        return

    # Create card options for multiselect
    card_options = []
    for _, row in df.iterrows():
        card_id = row["Card ID"]
        display_name = row["Display Name"]
        rank = int(row["Rank"])
        # Format: "Rank #X - Card Name"
        card_options.append(f"#{rank} - {display_name[:50]}{'...' if len(display_name) > 50 else ''}")

    # Create mapping from display option to card data
    option_to_card = {opt: df.iloc[idx] for idx, opt in enumerate(card_options)}

    # Multiselect for choosing cards
    selected_options = st.multiselect(
        "Select Cards to Compare",
        options=card_options,
        max_selections=4,
        placeholder="Choose 2-4 cards to compare...",
        help="Select between 2 and 4 cards to see a detailed comparison"
    )

    # Validate selection
    if len(selected_options) < 2:
        st.markdown("""
        <div class="empty-comparison-state">
            <h3>Select Cards to Compare</h3>
            <p>Choose at least 2 cards from the dropdown above to begin comparing their attributes and performance metrics.</p>
        </div>
        """, unsafe_allow_html=True)
        return

    # Get selected card data
    selected_cards = [option_to_card[opt] for opt in selected_options]

    # Determine winner (highest current sends)
    max_sends = max(card["Current Period"] for card in selected_cards)

    # Render comparison cards
    num_cards = len(selected_cards)
    cols = st.columns(num_cards, gap="medium")

    for idx, (col, card) in enumerate(zip(cols, selected_cards)):
        with col:
            card_name = card["Card Name"]
            card_id = card["Card ID"]
            display_name = card["Display Name"]
            rank = int(card["Rank"])
            sends = int(card["Current Period"])
            prev_sends = int(card["Previous Period"])
            change = card.get("Change", 0)
            change_pct = card.get("Change %", 0)

            # Check if this card is the winner
            is_winner = sends == max_sends
            winner_class = "performance-winner" if is_winner else ""

            # Get analysis data
            analysis = analysis_lookup.get(card_id, {})
            occasion = analysis.get("occasion", "N/A")
            design_style = analysis.get("design_style", "N/A")
            primary_colors = analysis.get("primary_colors", [])
            themes = analysis.get("themes", [])
            typography = analysis.get("typography_style", "N/A")

            # Get image
            image_path = get_card_image_by_id(card_id)
            if image_path:
                img_base64 = get_image_base64(image_path)
                if img_base64:
                    img_html = f'<img class="comparison-card-image" src="data:image/png;base64,{img_base64}" alt="{display_name}">'
                else:
                    img_html = '<div class="comparison-no-image">No Preview Available</div>'
            else:
                img_html = '<div class="comparison-no-image">No Preview Available</div>'

            # Format change
            change_class = "positive" if change >= 0 else "negative"
            change_sign = "+" if change >= 0 else ""

            # Build color swatches HTML
            color_swatches = ""
            for color in primary_colors[:5]:
                hex_val = color_hex.get(color.lower(), "#CCC")
                border = "border: 1px solid #DDD;" if color.lower() in ["white", "cream"] else ""
                color_swatches += f'<span class="color-swatch" style="background-color: {hex_val}; {border}"></span>'

            # Build themes tags
            themes_html = ""
            for theme in themes[:4]:
                themes_html += f'<span class="comparison-tag">{theme.title()}</span>'

            card_html = f"""
            <div class="comparison-card {winner_class}">
                {img_html}
                <div class="comparison-card-body">
                    <div class="comparison-card-rank">#{rank}{' - Top Performer' if is_winner else ''}</div>
                    <div class="comparison-card-title">{display_name[:60]}{'...' if len(display_name) > 60 else ''}</div>

                    <div class="comparison-stat">
                        <span class="comparison-stat-label">Current Sends</span>
                        <span class="comparison-stat-value">{sends:,}</span>
                    </div>
                    <div class="comparison-stat">
                        <span class="comparison-stat-label">Previous Sends</span>
                        <span class="comparison-stat-value">{prev_sends:,}</span>
                    </div>
                    <div class="comparison-stat">
                        <span class="comparison-stat-label">Change</span>
                        <span class="comparison-stat-value {change_class}">{change_sign}{change:,.0f} ({change_sign}{change_pct:.1f}%)</span>
                    </div>

                    <hr style="border: none; border-top: 1px solid rgba(45,42,38,0.1); margin: 1rem 0;">

                    <div class="comparison-attribute">
                        <div class="comparison-attribute-label">Occasion</div>
                        <div class="comparison-attribute-value">{occasion.replace('_', ' ').title() if occasion != 'N/A' else 'N/A'}</div>
                    </div>

                    <div class="comparison-attribute">
                        <div class="comparison-attribute-label">Design Style</div>
                        <div class="comparison-attribute-value">{design_style.replace('_', ' ').title() if design_style != 'N/A' else 'N/A'}</div>
                    </div>

                    <div class="comparison-attribute">
                        <div class="comparison-attribute-label">Typography</div>
                        <div class="comparison-attribute-value">{typography.replace('_', ' ').title() if typography != 'N/A' else 'N/A'}</div>
                    </div>

                    <div class="comparison-attribute">
                        <div class="comparison-attribute-label">Colors</div>
                        <div class="comparison-tags">{color_swatches if color_swatches else '<span style="color: #8B8680; font-size: 0.85rem;">N/A</span>'}</div>
                    </div>

                    <div class="comparison-attribute">
                        <div class="comparison-attribute-label">Themes</div>
                        <div class="comparison-tags">{themes_html if themes_html else '<span style="color: #8B8680; font-size: 0.85rem;">N/A</span>'}</div>
                    </div>
                </div>
            </div>
            """
            st.markdown(card_html, unsafe_allow_html=True)

    # Generate comparison summary
    render_comparison_summary(selected_cards, analysis_lookup)


def render_comparison_summary(selected_cards: list, analysis_lookup: dict):
    """Render the comparison summary section."""

    # Collect attributes from all selected cards
    all_occasions = []
    all_styles = []
    all_colors = []
    all_themes = []
    all_typography = []
    performance_data = []

    for card in selected_cards:
        card_id = card["Card ID"]
        analysis = analysis_lookup.get(card_id, {})

        occasion = analysis.get("occasion", "")
        style = analysis.get("design_style", "")
        colors = analysis.get("primary_colors", [])
        themes = analysis.get("themes", [])
        typography = analysis.get("typography_style", "")

        if occasion:
            all_occasions.append(occasion)
        if style:
            all_styles.append(style)
        all_colors.extend(colors)
        all_themes.extend(themes)
        if typography:
            all_typography.append(typography)

        performance_data.append({
            "name": card["Display Name"][:30],
            "sends": card["Current Period"],
            "change_pct": card.get("Change %", 0),
            "rank": card["Rank"],
            "occasion": occasion,
            "style": style,
            "colors": colors,
            "themes": themes,
            "typography": typography
        })

    # Find commonalities
    common_occasions = set(all_occasions) if len(set(all_occasions)) == 1 and all_occasions else set()
    common_styles = set(all_styles) if len(set(all_styles)) == 1 and all_styles else set()
    common_colors = set(c for c in all_colors if all_colors.count(c) == len(selected_cards))
    common_themes = set(t for t in all_themes if all_themes.count(t) >= 2)  # At least 2 cards share
    common_typography = set(all_typography) if len(set(all_typography)) == 1 and all_typography else set()

    # Find differences
    unique_occasions = set(all_occasions)
    unique_styles = set(all_styles)
    unique_colors = set(all_colors)
    unique_themes = set(all_themes)

    # Find best performer
    best_performer = max(performance_data, key=lambda x: x["sends"])
    best_change = max(performance_data, key=lambda x: x["change_pct"])

    # Build commonalities list
    commonalities = []
    if common_occasions:
        commonalities.append(f"All cards are for <strong>{list(common_occasions)[0].replace('_', ' ').title()}</strong> occasions")
    if common_styles:
        commonalities.append(f"All share the <strong>{list(common_styles)[0].replace('_', ' ').title()}</strong> design style")
    if common_colors:
        commonalities.append(f"Common color palette: <strong>{', '.join(c.title() for c in list(common_colors)[:3])}</strong>")
    if common_themes:
        commonalities.append(f"Shared themes: <strong>{', '.join(t.title() for t in list(common_themes)[:3])}</strong>")
    if common_typography:
        commonalities.append(f"All use <strong>{list(common_typography)[0].replace('_', ' ').title()}</strong> typography")

    if not commonalities:
        commonalities.append("These cards have diverse attributes with no shared characteristics")

    # Build differences list
    differences = []
    if len(unique_occasions) > 1:
        differences.append(f"Different occasions: {', '.join(o.replace('_', ' ').title() for o in unique_occasions if o)}")
    if len(unique_styles) > 1:
        differences.append(f"Varied design styles: {', '.join(s.replace('_', ' ').title() for s in unique_styles if s)}")
    if len(unique_colors) > len(common_colors):
        diff_colors = unique_colors - common_colors
        if diff_colors:
            differences.append(f"Unique colors used: {', '.join(c.title() for c in list(diff_colors)[:5])}")

    if not differences:
        differences.append("Cards share most attributes - highly similar designs")

    # Build performance insights
    performance_insights = []

    # Insight about top performer
    performance_insights.append(f"<strong>{best_performer['name']}</strong> leads with {int(best_performer['sends']):,} sends (Rank #{int(best_performer['rank'])})")

    # Insight about growth
    if best_change["change_pct"] > 0:
        performance_insights.append(f"<strong>{best_change['name']}</strong> shows strongest growth at +{best_change['change_pct']:.1f}%")
    elif best_change["change_pct"] < 0:
        performance_insights.append(f"All cards show declining sends, with <strong>{best_change['name']}</strong> declining least at {best_change['change_pct']:.1f}%")

    # Correlation insight
    if best_performer["style"]:
        performance_insights.append(f"Top performer uses <strong>{best_performer['style'].replace('_', ' ').title()}</strong> style with <strong>{best_performer['typography'].replace('_', ' ').title() if best_performer['typography'] else 'mixed'}</strong> typography")

    if best_performer["colors"]:
        performance_insights.append(f"Winning color palette includes: <strong>{', '.join(c.title() for c in best_performer['colors'][:3])}</strong>")

    # Render summary box
    commonalities_html = "".join(f"<li>{c}</li>" for c in commonalities)
    differences_html = "".join(f"<li>{d}</li>" for d in differences)
    insights_html = "".join(f"<li>{i}</li>" for i in performance_insights)

    st.markdown(f"""
    <div class="comparison-summary-box">
        <div class="comparison-summary-title">Comparison Summary</div>

        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem;">
            <div class="comparison-summary-section">
                <h4>What They Have in Common</h4>
                <ul>{commonalities_html}</ul>
            </div>

            <div class="comparison-summary-section">
                <h4>Key Differences</h4>
                <ul>{differences_html}</ul>
            </div>

            <div class="comparison-summary-section">
                <h4>Performance Insights</h4>
                <ul>{insights_html}</ul>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Additional insight card
    st.markdown(f"""
    <div class="comparison-insight-card" style="margin-top: 1.5rem;">
        <h5>Performance Correlation Analysis</h5>
        <p>
            Among the selected cards, <strong>{best_performer['name']}</strong> performs best.
            {"This card's success may be attributed to its " + best_performer['style'].replace('_', ' ') + " style and " + (best_performer['colors'][0] if best_performer['colors'] else 'varied') + " color palette." if best_performer['style'] else "Consider analyzing what makes this card stand out from the others."}
            Cards with similar attributes might benefit from incorporating elements from the top performer.
        </p>
    </div>
    """, unsafe_allow_html=True)


def render_data_table(df: pd.DataFrame, analysis_lookup: dict):
    """Render the data table view."""

    st.markdown("""
    <div class="section-container">
        <div class="section-header">
            <span class="section-number">06</span>
            <h2 class="section-title">Data Table</h2>
            <div class="section-line"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if df.empty:
        st.info("No data available for the selected filters.")
        return

    # Prepare display dataframe
    display_df = df[["Rank", "Display Name", "Current Period", "Previous Period", "Change", "Change %"]].copy()
    display_df.columns = ["Rank", "Card Name", "Current Sends", "Previous Sends", "Change", "Change %"]

    # Add occasion column
    display_df["Occasion"] = df["Card ID"].apply(
        lambda x: analysis_lookup.get(x, {}).get("occasion", "").title() if x in analysis_lookup else ""
    )

    st.dataframe(
        display_df,
        use_container_width=True,
        height=500,
        column_config={
            "Rank": st.column_config.NumberColumn("Rank", format="%d", width="small"),
            "Card Name": st.column_config.TextColumn("Card Name", width="large"),
            "Current Sends": st.column_config.NumberColumn("Current", format="%d"),
            "Previous Sends": st.column_config.NumberColumn("Previous", format="%d"),
            "Change": st.column_config.NumberColumn("Change", format="%+d"),
            "Change %": st.column_config.NumberColumn("% Change", format="%+.1f%%"),
            "Occasion": st.column_config.TextColumn("Occasion", width="medium"),
        },
        hide_index=True
    )

    # Download button
    csv = df.to_csv(index=False)
    st.download_button(
        label="Download Full Dataset",
        data=csv,
        file_name="greeting_card_analytics.csv",
        mime="text/csv"
    )


# =============================================================================
# PORTFOLIO GAP ANALYSIS
# =============================================================================
def render_portfolio_gap_analysis(df: pd.DataFrame, analysis_lookup: dict, analysis_data: list):
    """Render the Portfolio Gap Analysis section with interactive heatmap."""
    import numpy as np

    st.markdown("""
    <div class="section-container">
        <div class="section-header">
            <span class="section-number">06</span>
            <h2 class="section-title">Portfolio Gap Analysis</h2>
            <div class="section-line"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background: linear-gradient(135deg, #FDF8F3 0%, #FDFBF7 100%);
                border-radius: 12px; padding: 1.5rem 2rem; margin-bottom: 2rem;
                border: 1px solid rgba(198, 93, 59, 0.1);">
        <p style="font-family: 'Source Sans 3', sans-serif; font-size: 1rem; color: #5C5955; line-height: 1.6; margin: 0;">
            This analysis reveals <strong>coverage gaps</strong> in your portfolio by cross-tabulating
            <em>occasions</em> with <em>design styles</em>. Identify untapped opportunities where demand
            may exist but inventory is sparse.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Build cross-tabulation data
    # Collect all occasions and styles
    occasions = set()
    styles = set()
    combo_cards = {}  # (occasion, style) -> list of card data

    for card in analysis_data:
        occasion = card.get("occasion", "")
        style = card.get("design_style", "")
        if occasion and style:
            occasions.add(occasion)
            styles.add(style)
            key = (occasion, style)
            if key not in combo_cards:
                combo_cards[key] = []
            combo_cards[key].append({
                "card_id": card.get("card_id"),
                "card_name": card.get("card_name"),
                "sends_current": card.get("sends_current", 0),
                "sends_previous": card.get("sends_previous", 0)
            })

    # Sort occasions and styles for display
    occasion_order = [
        "birthday", "thank_you", "mothers_day", "fathers_day", "love", "valentines",
        "christmas", "holiday", "anniversary", "congrats", "congratulations",
        "friendship", "thinking_of_you", "get_well", "sympathy", "new_year",
        "easter", "halloween", "thanksgiving", "general", "other"
    ]
    occasions_sorted = [o for o in occasion_order if o in occasions]
    occasions_sorted += [o for o in sorted(occasions) if o not in occasion_order]

    style_order = [
        "illustrated", "watercolor", "minimalist", "modern", "playful_cute", "playful",
        "whimsical", "bold_graphic", "geometric", "elegant", "retro_vintage", "vintage",
        "typography_focused", "photographic", "abstract"
    ]
    styles_sorted = [s for s in style_order if s in styles]
    styles_sorted += [s for s in sorted(styles) if s not in style_order]

    # Build matrix data
    z_values = []  # counts
    hover_texts = []  # hover information

    for occasion in occasions_sorted:
        row_counts = []
        row_hover = []
        for style in styles_sorted:
            key = (occasion, style)
            cards = combo_cards.get(key, [])
            count = len(cards)
            row_counts.append(count)

            if count > 0:
                avg_sends = sum(c["sends_current"] for c in cards) / count
                total_sends = sum(c["sends_current"] for c in cards)
                top_card = max(cards, key=lambda x: x["sends_current"])
                top_card_name = top_card['card_name'][:30] + "..." if len(top_card['card_name']) > 30 else top_card['card_name']
                hover = (
                    f"<b>{occasion.replace('_', ' ').title()} x {style.replace('_', ' ').title()}</b><br>"
                    f"Cards: {count}<br>"
                    f"Avg Sends: {avg_sends:,.0f}<br>"
                    f"Total Sends: {total_sends:,.0f}<br>"
                    f"Top: {top_card_name}"
                )
            else:
                hover = (
                    f"<b>{occasion.replace('_', ' ').title()} x {style.replace('_', ' ').title()}</b><br>"
                    f"<span style='color: #C65D3B;'>No cards - Opportunity!</span>"
                )
            row_hover.append(hover)

        z_values.append(row_counts)
        hover_texts.append(row_hover)

    # Create formatted labels
    occasion_labels = [o.replace("_", " ").title() for o in occasions_sorted]
    style_labels = [s.replace("_", " ").title() for s in styles_sorted]

    # Custom warm color scale (cream to terracotta)
    warm_colorscale = [
        [0.0, "#FDFBF7"],      # Cream (empty)
        [0.05, "#FDF5ED"],     # Very light cream
        [0.15, "#F5E6D8"],     # Light peach
        [0.3, "#EBCCB5"],      # Soft tan
        [0.5, "#DBA88A"],      # Medium terracotta
        [0.7, "#D4785C"],      # Light terracotta
        [0.85, "#C65D3B"],     # Terracotta
        [1.0, "#A84D2E"],      # Dark terracotta
    ]

    # Create heatmap
    fig_heatmap = go.Figure(data=go.Heatmap(
        z=z_values,
        x=style_labels,
        y=occasion_labels,
        text=[[str(v) if v > 0 else "" for v in row] for row in z_values],
        texttemplate="%{text}",
        textfont={"size": 11, "color": "#2D2A26"},
        hovertext=hover_texts,
        hovertemplate="%{hovertext}<extra></extra>",
        colorscale=warm_colorscale,
        showscale=True,
        colorbar=dict(
            title=dict(text="Cards", font=dict(size=12, family="Source Sans 3")),
            tickfont=dict(size=10, family="Source Sans 3"),
            thickness=15,
            len=0.7
        ),
        xgap=2,
        ygap=2
    ))

    fig_heatmap.update_layout(
        height=max(500, len(occasions_sorted) * 28),
        margin=dict(l=10, r=80, t=40, b=100),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Source Sans 3, sans-serif", color="#2D2A26"),
        xaxis=dict(
            title="",
            tickangle=-45,
            tickfont=dict(size=11),
            side="bottom"
        ),
        yaxis=dict(
            title="",
            tickfont=dict(size=11),
            autorange="reversed"
        ),
    )

    # Display heatmap in chart container
    st.markdown("""
    <div class="chart-container">
        <div class="chart-title">Occasion x Design Style Coverage Matrix</div>
        <div class="chart-subtitle">Cell intensity indicates portfolio depth; empty cells reveal market opportunities</div>
    </div>
    """, unsafe_allow_html=True)

    st.plotly_chart(fig_heatmap, use_container_width=True, config={"displayModeBar": False})

    # Calculate insights
    st.markdown("""
    <div style="margin-top: 2rem;">
        <h3 style="font-family: 'Playfair Display', serif; font-size: 1.4rem; color: #2D2A26; margin-bottom: 1.5rem;">
            Strategic Insights
        </h3>
    </div>
    """, unsafe_allow_html=True)

    # Gather insights data
    biggest_gaps = []  # combos with 0-1 cards
    saturated_areas = []  # combos with 10+ cards
    high_performing_gaps = []  # few cards but high avg performance

    # Calculate overall average performance for comparison
    all_sends = [c.get("sends_current", 0) for c in analysis_data if c.get("sends_current")]
    overall_avg = sum(all_sends) / len(all_sends) if all_sends else 0

    for i, occasion in enumerate(occasions_sorted):
        for j, style in enumerate(styles_sorted):
            key = (occasion, style)
            cards = combo_cards.get(key, [])
            count = len(cards)

            if count <= 1:
                # Check if it's a meaningful gap (not just obscure combos)
                occasion_total = sum(len(combo_cards.get((occasion, s), [])) for s in styles_sorted)
                style_total = sum(len(combo_cards.get((o, style), [])) for o in occasions_sorted)

                if occasion_total >= 3 and style_total >= 3:  # Both have some presence
                    biggest_gaps.append({
                        "occasion": occasion.replace("_", " ").title(),
                        "style": style.replace("_", " ").title(),
                        "count": count,
                        "occasion_total": occasion_total,
                        "style_total": style_total
                    })

            if count >= 10:
                avg_sends = sum(c["sends_current"] for c in cards) / count
                saturated_areas.append({
                    "occasion": occasion.replace("_", " ").title(),
                    "style": style.replace("_", " ").title(),
                    "count": count,
                    "avg_sends": avg_sends
                })

            if 1 <= count <= 3:
                avg_sends = sum(c["sends_current"] for c in cards) / count
                if avg_sends > overall_avg * 1.2:  # 20% above average
                    high_performing_gaps.append({
                        "occasion": occasion.replace("_", " ").title(),
                        "style": style.replace("_", " ").title(),
                        "count": count,
                        "avg_sends": avg_sends,
                        "vs_avg": (avg_sends / overall_avg - 1) * 100 if overall_avg > 0 else 0
                    })

    # Sort insights
    biggest_gaps.sort(key=lambda x: (x["occasion_total"] + x["style_total"]), reverse=True)
    saturated_areas.sort(key=lambda x: x["count"], reverse=True)
    high_performing_gaps.sort(key=lambda x: x["avg_sends"], reverse=True)

    # Display three columns of insights
    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        st.markdown("""
        <div style="background: #FFF8F5; border-radius: 12px; padding: 1.5rem; border-left: 4px solid #C65D3B; height: 100%;">
            <h4 style="font-family: 'Playfair Display', serif; color: #C65D3B; margin-bottom: 1rem; font-size: 1.1rem;">
                Biggest Gaps
            </h4>
            <p style="font-size: 0.8rem; color: #8B8680; margin-bottom: 1rem;">
                Occasion/style combos with 0-1 cards where both dimensions have presence
            </p>
        """, unsafe_allow_html=True)

        for gap in biggest_gaps[:6]:
            count_text = "No cards" if gap["count"] == 0 else "1 card"
            st.markdown(f"""
            <div style="background: white; padding: 0.75rem; border-radius: 6px; margin-bottom: 0.5rem;">
                <div style="font-weight: 600; color: #2D2A26; font-size: 0.9rem;">{gap['occasion']} + {gap['style']}</div>
                <div style="font-size: 0.75rem; color: #C65D3B;">{count_text}</div>
            </div>
            """, unsafe_allow_html=True)

        if not biggest_gaps:
            st.markdown('<div style="color: #8B8680; font-style: italic;">No significant gaps found</div>', unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background: #F5F9F7; border-radius: 12px; padding: 1.5rem; border-left: 4px solid #5C8A6E; height: 100%;">
            <h4 style="font-family: 'Playfair Display', serif; color: #5C8A6E; margin-bottom: 1rem; font-size: 1.1rem;">
                Saturated Areas
            </h4>
            <p style="font-size: 0.8rem; color: #8B8680; margin-bottom: 1rem;">
                Combos with 10+ cards - consider differentiation
            </p>
        """, unsafe_allow_html=True)

        for area in saturated_areas[:6]:
            st.markdown(f"""
            <div style="background: white; padding: 0.75rem; border-radius: 6px; margin-bottom: 0.5rem;">
                <div style="font-weight: 600; color: #2D2A26; font-size: 0.9rem;">{area['occasion']} + {area['style']}</div>
                <div style="font-size: 0.75rem; color: #5C8A6E;">{area['count']} cards | Avg: {area['avg_sends']:,.0f} sends</div>
            </div>
            """, unsafe_allow_html=True)

        if not saturated_areas:
            st.markdown('<div style="color: #8B8680; font-style: italic;">No saturated areas found</div>', unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="background: #F5F7FA; border-radius: 12px; padding: 1.5rem; border-left: 4px solid #6B8E9B; height: 100%;">
            <h4 style="font-family: 'Playfair Display', serif; color: #6B8E9B; margin-bottom: 1rem; font-size: 1.1rem;">
                High-Performing Gaps
            </h4>
            <p style="font-size: 0.8rem; color: #8B8680; margin-bottom: 1rem;">
                Few cards exist but those that do outperform average
            </p>
        """, unsafe_allow_html=True)

        for perf in high_performing_gaps[:6]:
            st.markdown(f"""
            <div style="background: white; padding: 0.75rem; border-radius: 6px; margin-bottom: 0.5rem;">
                <div style="font-weight: 600; color: #2D2A26; font-size: 0.9rem;">{perf['occasion']} + {perf['style']}</div>
                <div style="font-size: 0.75rem; color: #6B8E9B;">{perf['count']} cards | +{perf['vs_avg']:.0f}% vs avg</div>
            </div>
            """, unsafe_allow_html=True)

        if not high_performing_gaps:
            st.markdown('<div style="color: #8B8680; font-style: italic;">No high-performing gaps found</div>', unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    # Summary recommendation box
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #2D2A26 0%, #3D3A36 100%);
                border-radius: 12px; padding: 2rem; margin-top: 2rem; color: white;">
        <h3 style="font-family: 'Playfair Display', serif; color: #F4D03F; margin-bottom: 1rem; font-size: 1.2rem;">
            Portfolio Optimization Summary
        </h3>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; font-size: 0.9rem;">
            <div>
                <div style="font-size: 2rem; font-weight: 700; color: #C65D3B;">{len(biggest_gaps)}</div>
                <div style="color: #CCC;">Opportunity gaps identified</div>
            </div>
            <div>
                <div style="font-size: 2rem; font-weight: 700; color: #5C8A6E;">{len(saturated_areas)}</div>
                <div style="color: #CCC;">Saturated categories</div>
            </div>
            <div>
                <div style="font-size: 2rem; font-weight: 700; color: #6B8E9B;">{len(high_performing_gaps)}</div>
                <div style="color: #CCC;">High-potential niches</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)



# =============================================================================
# AI CREATIVE BRIEF GENERATOR
# =============================================================================
def analyze_high_performing_patterns(analysis_data: list) -> dict:
    """
    Analyze the card_analysis.json data to find high-performing pattern combinations.
    Returns a dictionary with pattern statistics and top combinations.
    """
    if not analysis_data:
        return {}

    # Calculate average sends for baseline
    total_sends = sum(card.get("sends_current", 0) for card in analysis_data)
    avg_sends = total_sends / len(analysis_data) if analysis_data else 0

    # Track performance by various combinations
    occasion_stats = defaultdict(lambda: {"total_sends": 0, "count": 0, "cards": []})
    style_stats = defaultdict(lambda: {"total_sends": 0, "count": 0, "cards": []})
    color_stats = defaultdict(lambda: {"total_sends": 0, "count": 0, "cards": []})
    theme_stats = defaultdict(lambda: {"total_sends": 0, "count": 0, "cards": []})

    # Combination tracking: occasion + style
    occasion_style_stats = defaultdict(lambda: {"total_sends": 0, "count": 0, "cards": []})
    # Combination tracking: occasion + style + dominant color
    full_combo_stats = defaultdict(lambda: {"total_sends": 0, "count": 0, "cards": []})

    for card in analysis_data:
        sends = card.get("sends_current", 0)
        occasion = card.get("occasion") or "general"
        style = card.get("design_style") or "unknown"
        colors = card.get("primary_colors") or []
        themes = card.get("themes") or []
        card_name = card.get("card_name", "")
        rank = card.get("rank", 999)

        # Occasion stats
        occasion_stats[occasion]["total_sends"] += sends
        occasion_stats[occasion]["count"] += 1
        occasion_stats[occasion]["cards"].append({"name": card_name, "sends": sends, "rank": rank})

        # Style stats
        style_stats[style]["total_sends"] += sends
        style_stats[style]["count"] += 1
        style_stats[style]["cards"].append({"name": card_name, "sends": sends, "rank": rank})

        # Color stats (for each color in the card)
        if colors:
            for color in colors[:2]:  # Focus on top 2 colors
                color_stats[color]["total_sends"] += sends
                color_stats[color]["count"] += 1
                color_stats[color]["cards"].append({"name": card_name, "sends": sends, "rank": rank})

        # Theme stats
        if themes:
            for theme in themes:
                theme_stats[theme]["total_sends"] += sends
                theme_stats[theme]["count"] += 1
                theme_stats[theme]["cards"].append({"name": card_name, "sends": sends, "rank": rank})

        # Occasion + Style combination
        combo_key = f"{occasion}|{style}"
        occasion_style_stats[combo_key]["total_sends"] += sends
        occasion_style_stats[combo_key]["count"] += 1
        occasion_style_stats[combo_key]["cards"].append({"name": card_name, "sends": sends, "rank": rank, "colors": colors, "themes": themes})

        # Full combination: occasion + style + dominant colors + themes
        color_key = "/".join(sorted(colors[:2])) if colors else "mixed"
        theme_key = "/".join(sorted(themes[:2])) if themes else "general"
        full_key = f"{occasion}|{style}|{color_key}|{theme_key}"
        full_combo_stats[full_key]["total_sends"] += sends
        full_combo_stats[full_key]["count"] += 1
        full_combo_stats[full_key]["cards"].append({"name": card_name, "sends": sends, "rank": rank})

    # Calculate averages for each category
    for stats_dict in [occasion_stats, style_stats, color_stats, theme_stats, occasion_style_stats, full_combo_stats]:
        for key in stats_dict:
            if stats_dict[key]["count"] > 0:
                stats_dict[key]["avg_sends"] = stats_dict[key]["total_sends"] / stats_dict[key]["count"]
            else:
                stats_dict[key]["avg_sends"] = 0

    return {
        "overall_avg": avg_sends,
        "occasion_stats": dict(occasion_stats),
        "style_stats": dict(style_stats),
        "color_stats": dict(color_stats),
        "theme_stats": dict(theme_stats),
        "occasion_style_stats": dict(occasion_style_stats),
        "full_combo_stats": dict(full_combo_stats)
    }


def generate_creative_briefs(pattern_stats: dict, num_briefs: int = 5, seed: int = None) -> list:
    """
    Generate actionable creative briefs based on high-performing patterns.
    Returns a list of brief dictionaries.
    """
    if not pattern_stats:
        return []

    if seed is not None:
        random.seed(seed)

    overall_avg = pattern_stats.get("overall_avg", 0)
    occasion_style_stats = pattern_stats.get("occasion_style_stats", {})

    briefs = []

    # Find high-performing combinations (above average with sufficient sample size)
    high_performers = []
    for combo_key, stats in occasion_style_stats.items():
        if stats["count"] >= 2 and stats["avg_sends"] > overall_avg:
            parts = combo_key.split("|")
            if len(parts) >= 2:
                occasion, style = parts[0], parts[1]

                # Get top colors from these cards
                all_colors = []
                all_themes = []
                for card in stats["cards"]:
                    all_colors.extend(card.get("colors", []))
                    all_themes.extend(card.get("themes", []))

                # Count color frequency
                color_freq = defaultdict(int)
                for c in all_colors:
                    color_freq[c] += 1
                top_colors = sorted(color_freq.items(), key=lambda x: -x[1])[:3]

                # Count theme frequency
                theme_freq = defaultdict(int)
                for t in all_themes:
                    theme_freq[t] += 1
                top_themes = sorted(theme_freq.items(), key=lambda x: -x[1])[:2]

                high_performers.append({
                    "occasion": occasion,
                    "style": style,
                    "avg_sends": stats["avg_sends"],
                    "count": stats["count"],
                    "pct_above_avg": ((stats["avg_sends"] - overall_avg) / overall_avg * 100) if overall_avg > 0 else 0,
                    "top_colors": [c[0] for c in top_colors],
                    "top_themes": [t[0] for t in top_themes],
                    "example_cards": sorted(stats["cards"], key=lambda x: x["rank"])[:3]
                })

    # Sort by performance and select top combinations
    high_performers.sort(key=lambda x: -x["avg_sends"])

    # Shuffle slightly to add variety while keeping top performers prominent
    if len(high_performers) > num_briefs:
        top_tier = high_performers[:num_briefs * 2]
        random.shuffle(top_tier)
        selected = top_tier[:num_briefs]
    else:
        selected = high_performers[:num_briefs]

    # Generate briefs
    brief_titles = [
        "High-Impact Opportunity",
        "Proven Winner",
        "Trending Combination",
        "Premium Performer",
        "Strategic Recommendation"
    ]

    for i, combo in enumerate(selected):
        occasion_display = combo["occasion"].replace("_", " ").title()
        style_display = combo["style"].replace("_", " ").title()
        colors_display = "/".join(c.title() for c in combo["top_colors"][:2]) if combo["top_colors"] else "Mixed"
        themes_display = " & ".join(t.title() for t in combo["top_themes"]) if combo["top_themes"] else "General"

        brief = {
            "number": i + 1,
            "title": brief_titles[i % len(brief_titles)],
            "occasion": occasion_display,
            "style": style_display,
            "colors": colors_display,
            "themes": themes_display,
            "avg_sends": int(combo["avg_sends"]),
            "pct_above_avg": round(combo["pct_above_avg"], 1),
            "sample_size": combo["count"],
            "example_cards": combo["example_cards"]
        }
        briefs.append(brief)

    return briefs


def render_creative_brief_generator(analysis_data: list):
    """Render the AI Creative Brief Generator section."""

    st.markdown("""
    <div class="section-container">
        <div class="section-header">
            <span class="section-number">07</span>
            <h2 class="section-title">AI Creative Brief Generator</h2>
            <div class="section-line"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Introduction text
    st.markdown("""
    <div style="background: linear-gradient(135deg, #FDF8F3 0%, #FDFBF7 100%);
                border-radius: 12px; padding: 1.5rem 2rem; margin-bottom: 2rem;
                border: 1px solid rgba(198, 93, 59, 0.15);">
        <p style="font-family: 'Source Sans 3', sans-serif; font-size: 1rem; color: #4A4641; margin: 0; line-height: 1.6;">
            <strong style="color: #C65D3B;">Powered by pattern analysis</strong> - These briefs are automatically generated
            by analyzing which combinations of occasion, design style, color palette, and themes
            correlate with the highest card performance in your portfolio.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Initialize or get the seed for randomization
    if "brief_seed" not in st.session_state:
        st.session_state.brief_seed = random.randint(1, 10000)

    # Generate New Briefs button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Generate New Briefs", key="generate_briefs_btn", use_container_width=True):
            st.session_state.brief_seed = random.randint(1, 10000)
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # Analyze patterns and generate briefs
    pattern_stats = analyze_high_performing_patterns(analysis_data)
    briefs = generate_creative_briefs(pattern_stats, num_briefs=5, seed=st.session_state.brief_seed)

    if not briefs:
        st.info("Not enough data to generate creative briefs. Please ensure card_analysis.json has sufficient entries.")
        return

    # Custom CSS for brief cards
    st.markdown("""
    <style>
        .brief-card {
            background: #FDFBF7;
            border-radius: 12px;
            padding: 1.75rem;
            margin-bottom: 1.5rem;
            border: 1px solid rgba(198, 93, 59, 0.12);
            box-shadow: 0 4px 16px rgba(45, 42, 38, 0.06);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .brief-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 4px;
            height: 100%;
            background: linear-gradient(180deg, #C65D3B 0%, #D4785C 100%);
        }

        .brief-card:hover {
            box-shadow: 0 8px 24px rgba(198, 93, 59, 0.12);
            transform: translateY(-2px);
        }

        .brief-header {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 1rem;
        }

        .brief-number {
            background: linear-gradient(135deg, #C65D3B 0%, #D4785C 100%);
            color: white;
            font-family: 'Playfair Display', serif;
            font-size: 1rem;
            font-weight: 600;
            width: 36px;
            height: 36px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }

        .brief-title {
            font-family: 'Playfair Display', serif;
            font-size: 1.25rem;
            font-weight: 600;
            color: #2D2A26;
            margin: 0;
        }

        .brief-subtitle {
            font-family: 'Source Sans 3', sans-serif;
            font-size: 0.85rem;
            color: #8B8680;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .brief-description {
            font-family: 'Source Sans 3', sans-serif;
            font-size: 1rem;
            color: #4A4641;
            line-height: 1.7;
            margin: 1rem 0;
            padding: 1rem;
            background: white;
            border-radius: 8px;
            border-left: 3px solid #C65D3B;
        }

        .brief-stats {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 1rem;
            margin: 1rem 0;
        }

        .brief-stat {
            background: white;
            padding: 0.75rem 1rem;
            border-radius: 8px;
            border: 1px solid rgba(45, 42, 38, 0.08);
        }

        .brief-stat-value {
            font-family: 'Playfair Display', serif;
            font-size: 1.4rem;
            font-weight: 600;
            color: #C65D3B;
        }

        .brief-stat-label {
            font-family: 'Source Sans 3', sans-serif;
            font-size: 0.75rem;
            color: #8B8680;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .brief-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-top: 1rem;
        }

        .brief-tag {
            background: white;
            color: #4A4641;
            font-family: 'Source Sans 3', sans-serif;
            font-size: 0.8rem;
            padding: 0.4rem 0.8rem;
            border-radius: 20px;
            border: 1px solid rgba(198, 93, 59, 0.2);
        }

        .brief-tag-label {
            color: #C65D3B;
            font-weight: 600;
        }

        .brief-examples {
            margin-top: 1rem;
            padding-top: 1rem;
            border-top: 1px solid rgba(45, 42, 38, 0.08);
        }

        .brief-examples-title {
            font-family: 'Source Sans 3', sans-serif;
            font-size: 0.75rem;
            color: #8B8680;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 0.5rem;
        }

        .brief-example-card {
            font-family: 'Source Sans 3', sans-serif;
            font-size: 0.85rem;
            color: #4A4641;
            padding: 0.5rem 0;
            display: flex;
            justify-content: space-between;
            border-bottom: 1px dashed rgba(45, 42, 38, 0.1);
        }

        .brief-example-card:last-child {
            border-bottom: none;
        }

        .brief-example-rank {
            color: #C65D3B;
            font-weight: 600;
        }
    </style>
    """, unsafe_allow_html=True)

    # Render brief cards in a 2-column layout
    cols = st.columns(2)

    for i, brief in enumerate(briefs):
        col_idx = i % 2

        with cols[col_idx]:
            # Render brief card with separate markdown calls for reliable rendering
            # Brief header
            st.markdown(f'''<div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 0.5rem;">
                <div style="width: 36px; height: 36px; border-radius: 50%; background: #C65D3B; color: white;
                    display: flex; align-items: center; justify-content: center; font-family: Playfair Display, serif;
                    font-size: 1rem; font-weight: 600;">{brief["number"]}</div>
                <div>
                    <div style="font-family: Playfair Display, serif; font-size: 1.15rem; font-weight: 600; color: #2D2A26;">{brief["title"]}</div>
                    <div style="font-size: 0.8rem; color: #8B8680; text-transform: uppercase; letter-spacing: 0.5px;">Creative Brief</div>
                </div>
            </div>''', unsafe_allow_html=True)

            # Brief description
            st.markdown(f'''<div style="font-size: 0.95rem; color: #4A4641; line-height: 1.7; margin: 0.75rem 0;
                padding: 0.75rem; background: white; border-radius: 8px; border-left: 3px solid #C65D3B;">
                Commission an <strong>{brief["style"].lower()}</strong> style card for
                <strong>{brief["occasion"]}</strong> with a <strong>{brief["colors"].lower()}</strong> palette
                and <strong>{brief["themes"].lower()}</strong> themes.
                Similar cards average <strong>{brief["avg_sends"]:,}</strong> sends -
                <strong>{brief["pct_above_avg"]:+.0f}%</strong> above category average.
            </div>''', unsafe_allow_html=True)

            # Stats using columns
            stat_cols = st.columns(2)
            with stat_cols[0]:
                st.markdown(f'''<div style="background: white; padding: 0.5rem; border-radius: 8px; text-align: center; border: 1px solid rgba(45,42,38,0.08);">
                    <div style="font-family: Playfair Display, serif; font-size: 1.3rem; color: #C65D3B; font-weight: 600;">{brief["avg_sends"]:,}</div>
                    <div style="font-size: 0.7rem; color: #8B8680; text-transform: uppercase;">Average Sends</div>
                </div>''', unsafe_allow_html=True)
            with stat_cols[1]:
                st.markdown(f'''<div style="background: white; padding: 0.5rem; border-radius: 8px; text-align: center; border: 1px solid rgba(45,42,38,0.08);">
                    <div style="font-family: Playfair Display, serif; font-size: 1.3rem; color: #C65D3B; font-weight: 600;">{brief["pct_above_avg"]:+.0f}%</div>
                    <div style="font-size: 0.7rem; color: #8B8680; text-transform: uppercase;">vs. Category Avg</div>
                </div>''', unsafe_allow_html=True)

            # Tags
            st.markdown(f'''<div style="display: flex; flex-wrap: wrap; gap: 0.4rem; margin: 0.75rem 0;">
                <span style="background: white; color: #4A4641; font-size: 0.75rem; padding: 0.3rem 0.6rem; border-radius: 15px; border: 1px solid rgba(198,93,59,0.2);">
                    <span style="color: #C65D3B; font-weight: 600;">Occasion:</span> {brief["occasion"]}</span>
                <span style="background: white; color: #4A4641; font-size: 0.75rem; padding: 0.3rem 0.6rem; border-radius: 15px; border: 1px solid rgba(198,93,59,0.2);">
                    <span style="color: #C65D3B; font-weight: 600;">Style:</span> {brief["style"]}</span>
                <span style="background: white; color: #4A4641; font-size: 0.75rem; padding: 0.3rem 0.6rem; border-radius: 15px; border: 1px solid rgba(198,93,59,0.2);">
                    <span style="color: #C65D3B; font-weight: 600;">Colors:</span> {brief["colors"]}</span>
                <span style="background: white; color: #4A4641; font-size: 0.75rem; padding: 0.3rem 0.6rem; border-radius: 15px; border: 1px solid rgba(198,93,59,0.2);">
                    <span style="color: #C65D3B; font-weight: 600;">Themes:</span> {brief["themes"]}</span>
            </div>''', unsafe_allow_html=True)

            # Reference cards
            st.markdown('''<div style="font-size: 0.7rem; color: #8B8680; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 0.5rem; padding-top: 0.5rem; border-top: 1px solid rgba(45,42,38,0.08);">Reference Cards with This Pattern</div>''', unsafe_allow_html=True)
            for example in brief["example_cards"]:
                card_name = example["name"][:35] + "..." if len(example["name"]) > 35 else example["name"]
                st.markdown(f'''<div style="font-size: 0.8rem; color: #4A4641; padding: 0.3rem 0; display: flex; justify-content: space-between;">
                    <span>{card_name}</span>
                    <span style="color: #C65D3B; font-weight: 600;">#{example["rank"]} - {example["sends"]:,}</span>
                </div>''', unsafe_allow_html=True)
            st.markdown("---")

    # Performance summary
    st.markdown("""
    <div style="background: linear-gradient(135deg, #2D2A26 0%, #3D3A36 100%);
                border-radius: 12px; padding: 2rem; margin-top: 2rem; color: white;">
        <h3 style="font-family: 'Playfair Display', serif; color: #F4D03F; margin-bottom: 1rem; font-size: 1.2rem;">
            How These Briefs Are Generated
        </h3>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem;">
            <div>
                <div style="font-weight: 600; color: #C65D3B; margin-bottom: 0.5rem;">1. Pattern Analysis</div>
                <div style="font-size: 0.85rem; color: #CCC; line-height: 1.5;">
                    We analyze all combinations of occasion, design style, colors, and themes in your top-performing cards.
                </div>
            </div>
            <div>
                <div style="font-weight: 600; color: #5C8A6E; margin-bottom: 0.5rem;">2. Performance Scoring</div>
                <div style="font-size: 0.85rem; color: #CCC; line-height: 1.5;">
                    Each combination is scored by average sends and compared against the overall portfolio average.
                </div>
            </div>
            <div>
                <div style="font-weight: 600; color: #6B8E9B; margin-bottom: 0.5rem;">3. Brief Generation</div>
                <div style="font-size: 0.85rem; color: #CCC; line-height: 1.5;">
                    Top-performing combinations are transformed into actionable creative briefs with specific recommendations.
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# =============================================================================
# TREND INTELLIGENCE HUB
# =============================================================================

def hex_to_rgb(hex_color: str) -> tuple:
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def calculate_color_similarity(hex1: str, hex2: str) -> float:
    """Calculate similarity between two hex colors (0-100 scale)."""
    try:
        r1, g1, b1 = hex_to_rgb(hex1)
        r2, g2, b2 = hex_to_rgb(hex2)
        distance = ((r1-r2)**2 + (g1-g2)**2 + (b1-b2)**2) ** 0.5
        # Max distance is ~441 (black to white), normalize to 0-100
        return max(0, 100 - (distance / 441 * 100))
    except:
        return 0


def get_card_trend_alignment(card_data: dict, trend_data: dict) -> dict:
    """Calculate how well a card aligns with current trends.

    Scoring methodology:
    - Each category scored 0-100 based on match quality
    - No match = 0, partial match = 30-60, strong match = 60-90, exact match = 90-100
    - Overall score is weighted average requiring multiple category matches for high scores
    """
    color_scores = []
    style_scores = []
    typo_scores = []
    theme_scores = []
    matching_trends = []

    # Get color name to hex mapping
    color_map = trend_data.get("color_name_to_hex", {}) or {}

    # Color trend alignment - check Pantone 2026 match
    card_colors = card_data.get("primary_colors") or []
    pantone = trend_data.get("color_trends", {}).get("pantone_color_of_year", {}) or {}
    pantone_hex = pantone.get("hex", "#888888")

    for color_name in card_colors:
        card_hex = color_map.get(color_name.lower(), "#888888")
        if card_hex != "#RAINBOW":
            sim = calculate_color_similarity(card_hex, pantone_hex)
            # Only count strong color matches (>70% similarity)
            if sim > 70:
                color_scores.append(sim)
                matching_trends.append(f"Pantone {pantone.get('name', '')}")

    # Check emerging palettes - require strong match
    for palette in (trend_data.get("color_trends", {}).get("emerging_palettes") or []):
        palette_matches = 0
        for p_color in (palette.get("colors") or []):
            for color_name in card_colors:
                card_hex = color_map.get(color_name.lower(), "#888888")
                if card_hex != "#RAINBOW":
                    sim = calculate_color_similarity(card_hex, p_color.get("hex", "#888888"))
                    if sim > 75:
                        palette_matches += 1
        # Award points based on how many palette colors match
        if palette_matches >= 2:
            color_scores.append(min(90, 50 + palette_matches * 15))
            matching_trends.append(palette.get("name", ""))
        elif palette_matches == 1:
            color_scores.append(40)

    # Style trend alignment - stricter matching
    card_style = (card_data.get("design_style") or "").lower()
    if card_style:
        for trend in (trend_data.get("illustration_trends") or []):
            compatible = [s.lower() for s in (trend.get("compatible_styles") or [])]
            # Exact match in compatible styles
            if card_style in compatible:
                # Score based on how specific the match is (not just raw weight)
                base_score = 70 + (len(compatible) <= 3) * 15  # More specific = higher score
                style_scores.append(base_score)
                matching_trends.append(trend.get("name", ""))
            # Partial match
            elif any(card_style in c or c in card_style for c in compatible):
                style_scores.append(40)

    # Typography trend alignment
    card_typo = (card_data.get("typography_style") or "").lower()
    if card_typo:
        for trend in (trend_data.get("typography_trends") or []):
            compatible = [t.lower() for t in (trend.get("compatible_typography") or [])]
            if card_typo in compatible:
                typo_scores.append(75)
                matching_trends.append(trend.get("name", ""))
            elif any(card_typo in c or c in card_typo for c in compatible):
                typo_scores.append(40)

    # Theme trend alignment - based on keyword overlap percentage
    card_themes = [t.lower() for t in (card_data.get("themes") or [])]
    if card_themes:
        for trend in (trend_data.get("theme_motif_trends") or []):
            keywords = [k.lower() for k in (trend.get("keywords") or [])]
            compatible = [t.lower() for t in (trend.get("compatible_themes") or [])]
            all_trend_terms = set(keywords) | set(compatible)
            matches = set(card_themes) & all_trend_terms

            if matches:
                # Score based on match percentage, not raw weight
                match_ratio = len(matches) / max(len(card_themes), 1)
                coverage_ratio = len(matches) / max(len(all_trend_terms), 1)

                # Require meaningful overlap
                if match_ratio >= 0.3 and len(matches) >= 2:
                    score = min(85, 40 + match_ratio * 30 + coverage_ratio * 20)
                    theme_scores.append(score)
                    matching_trends.append(trend.get("name", ""))
                elif len(matches) >= 1:
                    theme_scores.append(25 + match_ratio * 20)

    # Calculate category scores - default to 0 for no match
    color_score = max(color_scores) if color_scores else 0
    style_score = max(style_scores) if style_scores else 0
    typo_score = max(typo_scores) if typo_scores else 0
    theme_score = max(theme_scores) if theme_scores else 0

    # Count how many categories have meaningful matches
    categories_matched = sum([
        color_score >= 40,
        style_score >= 40,
        typo_score >= 40,
        theme_score >= 40
    ])

    # Weighted overall score with bonus for multi-category alignment
    base_overall = (color_score * 0.30 + style_score * 0.30 +
                    typo_score * 0.15 + theme_score * 0.25)

    # Apply penalty if only 1 category matches (single-dimension alignment)
    if categories_matched <= 1:
        overall = base_overall * 0.7
    else:
        overall = base_overall

    return {
        "color_score": round(color_score, 1),
        "style_score": round(style_score, 1),
        "typography_score": round(typo_score, 1),
        "theme_score": round(theme_score, 1),
        "overall_score": round(overall, 1),
        "categories_matched": categories_matched,
        "matching_trends": list(set(matching_trends))[:5]
    }


def aggregate_portfolio_trends(analysis_data: list, trend_data: dict) -> dict:
    """Analyze entire portfolio against trends."""
    alignments = []

    for card in analysis_data:
        alignment = get_card_trend_alignment(card, trend_data)
        alignments.append({
            "card_name": card.get("card_name", "Unknown"),
            "card_id": card.get("card_id", ""),
            "sends": card.get("sends_current", 0),
            "rank": card.get("rank", 999),
            **alignment
        })

    # Sort by overall score
    alignments.sort(key=lambda x: x["overall_score"], reverse=True)

    # Calculate stats
    scores = [a["overall_score"] for a in alignments]
    avg_score = sum(scores) / len(scores) if scores else 0

    # Tiered alignment counts (stricter thresholds)
    strong_aligned = sum(1 for a in alignments if a["overall_score"] >= 60 and a.get("categories_matched", 0) >= 2)
    moderate_aligned = sum(1 for a in alignments if 40 <= a["overall_score"] < 60 or
                          (a["overall_score"] >= 60 and a.get("categories_matched", 0) < 2))
    weak_aligned = sum(1 for a in alignments if 20 <= a["overall_score"] < 40)
    not_aligned = sum(1 for a in alignments if a["overall_score"] < 20)

    # Find opportunities - trends with high relevance but low card coverage
    opportunities = []
    for trend in trend_data.get("illustration_trends", [])[:3]:
        trend_cards = [a for a in alignments if trend.get("name", "") in a.get("matching_trends", [])]
        relevance = trend.get("relevance_weight", trend.get("popularity_score", 0))
        if len(trend_cards) < 10:
            opportunities.append({
                "trend": trend.get("name", ""),
                "relevance": relevance,
                "your_cards": len(trend_cards),
                "opportunity": "High" if relevance > 85 else "Medium"
            })

    for trend in trend_data.get("theme_motif_trends", [])[:3]:
        trend_cards = [a for a in alignments if trend.get("name", "") in a.get("matching_trends", [])]
        relevance = trend.get("relevance_weight", trend.get("popularity_score", 0))
        if len(trend_cards) < 15:
            opportunities.append({
                "trend": trend.get("name", ""),
                "relevance": relevance,
                "your_cards": len(trend_cards),
                "opportunity": "High" if relevance > 85 else "Medium"
            })

    return {
        "total_cards": len(alignments),
        "average_score": round(avg_score, 1),
        "strong_aligned": strong_aligned,
        "moderate_aligned": moderate_aligned,
        "weak_aligned": weak_aligned,
        "not_aligned": not_aligned,
        "aligned_count": strong_aligned,  # For backward compat, use strong as "aligned"
        "aligned_pct": round(strong_aligned / len(alignments) * 100, 1) if alignments else 0,
        "trend_leaders": alignments[:10],
        "trend_laggards": alignments[-10:],
        "opportunities": opportunities[:5]
    }


def render_trend_intelligence_hub(df: pd.DataFrame, analysis_lookup: dict, analysis_data: list):
    """Render the Trend Intelligence Hub tab."""

    # Load trend data
    trend_data = load_trend_data()

    # Section header
    st.markdown("""
    <div class="section-container">
        <div class="section-header">
            <span class="section-number">08</span>
            <h2 class="section-title">Trend Intelligence Hub</h2>
            <div class="section-line"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Header with refresh button
    col1, col2 = st.columns([4, 1])
    with col1:
        # Build source links from new structured format
        sources = trend_data.get("sources", [])
        if sources and isinstance(sources[0], dict):
            source_links = " • ".join([
                f'<a href="{s.get("url", "#")}" target="_blank" style="color: #C65D3B; text-decoration: none;">{s.get("name", "Source")}</a>'
                for s in sources[:3]
            ])
        else:
            source_links = ", ".join(sources[:3]) if sources else "N/A"

        st.markdown(f"""
        <div style="font-size: 0.9rem; color: #8B8680; margin-bottom: 1rem;">
            <strong>Data Version:</strong> {trend_data.get("version", "N/A")} |
            <strong>Last Updated:</strong> {trend_data.get("last_updated", "N/A")} |
            <strong>Sources:</strong> {source_links}
        </div>
        """, unsafe_allow_html=True)
    with col2:
        if st.button("Refresh Trends", key="refresh_trends"):
            load_trend_data.clear()
            st.rerun()

    # Trend Overview Cards
    st.markdown("""
    <div class="chart-container" style="margin-bottom: 2rem;">
        <div class="chart-title">2026 Trend Highlights</div>
        <div class="chart-subtitle">Key trends shaping the greeting card industry this year</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4, gap="medium")

    # Pantone Color of the Year
    pantone = trend_data.get("color_trends", {}).get("pantone_color_of_year", {})
    with col1:
        st.markdown(f"""
        <div style="background: white; border-radius: 12px; padding: 1.5rem; text-align: center;
                    box-shadow: 0 4px 16px rgba(45,42,38,0.08); height: 200px;">
            <div style="font-size: 0.7rem; color: #8B8680; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.5rem;">
                Pantone 2026
            </div>
            <div style="width: 70px; height: 70px; background: {pantone.get('hex', '#888')};
                        border-radius: 50%; margin: 0 auto 1rem;
                        box-shadow: 0 4px 20px {pantone.get('hex', '#888')}50;"></div>
            <div style="font-family: 'Playfair Display', serif; font-size: 1.1rem; color: #2D2A26; font-weight: 600;">
                {pantone.get('name', 'N/A')}
            </div>
            <div style="font-size: 0.75rem; color: #8B8680; margin-top: 0.25rem;">{pantone.get('hex', '')}</div>
        </div>
        """, unsafe_allow_html=True)

    # Top Illustration Trend
    illust_trends = trend_data.get("illustration_trends", [])
    top_illust = illust_trends[0] if illust_trends else {}
    illust_weight = top_illust.get('relevance_weight', top_illust.get('popularity_score', 0))
    with col2:
        st.markdown(f"""
        <div style="background: white; border-radius: 12px; padding: 1.5rem; text-align: center;
                    box-shadow: 0 4px 16px rgba(45,42,38,0.08); height: 200px;">
            <div style="font-size: 0.7rem; color: #8B8680; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.5rem;">
                Top Illustration Style
            </div>
            <div style="font-size: 2rem; margin: 0.5rem 0;">🎨</div>
            <div style="font-family: 'Playfair Display', serif; font-size: 1rem; color: #2D2A26; font-weight: 600;">
                {top_illust.get('name', 'N/A')}
            </div>
            <div style="background: #E8E4DE; border-radius: 10px; height: 8px; margin-top: 0.75rem; overflow: hidden;">
                <div style="background: #C65D3B; height: 100%; width: {illust_weight}%;"></div>
            </div>
            <div style="font-size: 0.75rem; color: #8B8680; margin-top: 0.5rem;">Relevance: {illust_weight}</div>
        </div>
        """, unsafe_allow_html=True)

    # Typography Trend
    typo_trends = trend_data.get("typography_trends", [])
    top_typo = typo_trends[0] if typo_trends else {}
    typo_weight = top_typo.get('relevance_weight', top_typo.get('popularity_score', 0))
    with col3:
        st.markdown(f"""
        <div style="background: white; border-radius: 12px; padding: 1.5rem; text-align: center;
                    box-shadow: 0 4px 16px rgba(45,42,38,0.08); height: 200px;">
            <div style="font-size: 0.7rem; color: #8B8680; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.5rem;">
                Typography Trend
            </div>
            <div style="font-size: 2rem; margin: 0.5rem 0;">Aa</div>
            <div style="font-family: 'Playfair Display', serif; font-size: 1rem; color: #2D2A26; font-weight: 600;">
                {top_typo.get('name', 'N/A')}
            </div>
            <div style="font-size: 0.8rem; color: #5C5955; margin-top: 0.5rem; font-style: italic;">
                {top_typo.get('mood', '')}
            </div>
            <div style="font-size: 0.75rem; color: #8B8680; margin-top: 0.5rem;">Relevance: {typo_weight}</div>
        </div>
        """, unsafe_allow_html=True)

    # Theme Trend
    theme_trends = trend_data.get("theme_motif_trends", [])
    top_theme = theme_trends[0] if theme_trends else {}
    theme_weight = top_theme.get('relevance_weight', top_theme.get('popularity_score', 0))
    with col4:
        keywords = ", ".join(top_theme.get("keywords", [])[:3])
        st.markdown(f"""
        <div style="background: white; border-radius: 12px; padding: 1.5rem; text-align: center;
                    box-shadow: 0 4px 16px rgba(45,42,38,0.08); height: 200px;">
            <div style="font-size: 0.7rem; color: #8B8680; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.5rem;">
                Trending Theme
            </div>
            <div style="font-size: 2rem; margin: 0.5rem 0;">🌸</div>
            <div style="font-family: 'Playfair Display', serif; font-size: 1rem; color: #2D2A26; font-weight: 600;">
                {top_theme.get('name', 'N/A')}
            </div>
            <div style="font-size: 0.75rem; color: #8B8680; margin-top: 0.5rem;">{keywords}</div>
            <div style="font-size: 0.75rem; color: #8B8680; margin-top: 0.25rem;">Relevance: {theme_weight}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Color Trends Section
    with st.expander("🎨 Color Trends", expanded=True):
        st.markdown(f"""
        <div style="padding: 1rem 0;">
            <h4 style="font-family: 'Playfair Display', serif; margin-bottom: 1rem;">Pantone Color of the Year 2026</h4>
            <div style="display: flex; align-items: center; gap: 2rem; margin-bottom: 2rem;">
                <div style="width: 120px; height: 120px; background: {pantone.get('hex', '#888')};
                            border-radius: 16px; box-shadow: 0 8px 32px {pantone.get('hex', '#888')}40;"></div>
                <div>
                    <div style="font-family: 'Playfair Display', serif; font-size: 1.5rem; font-weight: 600; color: #2D2A26;">
                        {pantone.get('name', 'N/A')}
                    </div>
                    <div style="color: #8B8680; margin: 0.5rem 0;">{pantone.get('hex', '')}</div>
                    <div style="color: #5C5955; max-width: 400px; line-height: 1.5;">{pantone.get('description', '')}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Emerging Palettes
        st.markdown("<h4 style='font-family: Playfair Display, serif; margin: 1.5rem 0 1rem;'>Emerging Color Palettes</h4>", unsafe_allow_html=True)
        palette_cols = st.columns(4)
        for idx, palette in enumerate(trend_data.get("color_trends", {}).get("emerging_palettes", [])[:4]):
            with palette_cols[idx]:
                colors_html = "".join([
                    f'<div style="width: 40px; height: 40px; background: {c.get("hex", "#888")}; border-radius: 8px;" title="{c.get("name", "")}"></div>'
                    for c in palette.get("colors", [])
                ])
                st.markdown(f"""
                <div style="background: #FDFBF7; border-radius: 12px; padding: 1rem; border: 1px solid #E8E4DE;">
                    <div style="font-weight: 600; color: #2D2A26; margin-bottom: 0.75rem;">{palette.get('name', '')}</div>
                    <div style="display: flex; gap: 0.5rem; margin-bottom: 0.75rem;">{colors_html}</div>
                    <div style="font-size: 0.8rem; color: #8B8680; font-style: italic;">{palette.get('mood', '')}</div>
                </div>
                """, unsafe_allow_html=True)

    # Illustration & Theme Trends
    with st.expander("✏️ Style & Theme Trends", expanded=False):
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("<h4 style='font-family: Playfair Display, serif;'>Illustration Trends</h4>", unsafe_allow_html=True)
            for trend in illust_trends[:5]:
                trend_weight = trend.get('relevance_weight', trend.get('popularity_score', 0))
                trend_source = trend.get('source', '')
                st.markdown(f"""
                <div style="background: white; border-radius: 8px; padding: 1rem; margin-bottom: 0.75rem; border: 1px solid #E8E4DE;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div style="font-weight: 600; color: #2D2A26;">{trend.get('name', '')}</div>
                        <div style="color: #8B8680; font-size: 0.75rem;">Relevance: {trend_weight}</div>
                    </div>
                    <div style="font-size: 0.85rem; color: #5C5955; margin: 0.5rem 0;">{trend.get('description', '')[:100]}...</div>
                    <div style="background: #E8E4DE; border-radius: 6px; height: 6px; overflow: hidden;">
                        <div style="background: #C65D3B; height: 100%; width: {trend_weight}%;"></div>
                    </div>
                    <div style="font-size: 0.7rem; color: #A8A49E; margin-top: 0.5rem; font-style: italic;">Source: {trend_source}</div>
                </div>
                """, unsafe_allow_html=True)

        with col2:
            st.markdown("<h4 style='font-family: Playfair Display, serif;'>Theme & Motif Trends</h4>", unsafe_allow_html=True)
            for trend in theme_trends[:5]:
                keywords = " • ".join(trend.get("keywords", [])[:4])
                trend_weight = trend.get('relevance_weight', trend.get('popularity_score', 0))
                trend_source = trend.get('source', '')
                st.markdown(f"""
                <div style="background: white; border-radius: 8px; padding: 1rem; margin-bottom: 0.75rem; border: 1px solid #E8E4DE;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div style="font-weight: 600; color: #2D2A26;">{trend.get('name', '')}</div>
                        <div style="background: #E8E4DE; color: #5C5955; padding: 0.2rem 0.5rem; border-radius: 4px; font-size: 0.75rem;">
                            {trend_weight}
                        </div>
                    </div>
                    <div style="font-size: 0.85rem; color: #5C5955; margin: 0.5rem 0;">{trend.get('description', '')[:100]}...</div>
                    <div style="font-size: 0.75rem; color: #8B8680;">{keywords}</div>
                    <div style="font-size: 0.7rem; color: #A8A49E; margin-top: 0.5rem; font-style: italic;">Source: {trend_source}</div>
                </div>
                """, unsafe_allow_html=True)

    # Portfolio Trend Alignment
    st.markdown("""
    <div class="chart-container" style="margin-top: 2rem;">
        <div class="chart-title">Portfolio Trend Alignment</div>
        <div class="chart-subtitle">How your card portfolio aligns with 2026 trends</div>
    </div>
    """, unsafe_allow_html=True)

    # Calculate portfolio alignment
    portfolio_stats = aggregate_portfolio_trends(analysis_data, trend_data)

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        # Tiered alignment donut chart
        fig = go.Figure(data=[go.Pie(
            labels=["Strong", "Moderate", "Weak", "Not Aligned"],
            values=[
                portfolio_stats.get("strong_aligned", 0),
                portfolio_stats.get("moderate_aligned", 0),
                portfolio_stats.get("weak_aligned", 0),
                portfolio_stats.get("not_aligned", 0)
            ],
            hole=0.65,
            marker=dict(colors=["#4CAF50", "#FF9800", "#FFC107", "#E8E4DE"]),
            textposition='outside',
            textinfo='percent',
            sort=False
        )])
        fig.update_layout(
            height=250,
            margin=dict(l=20, r=20, t=20, b=20),
            paper_bgcolor="rgba(0,0,0,0)",
            showlegend=False,
            annotations=[dict(
                text=f'<b>{portfolio_stats["aligned_pct"]:.0f}%</b><br>Strong',
                x=0.5, y=0.5,
                font=dict(size=14, family="Playfair Display, serif", color="#2D2A26"),
                showarrow=False
            )]
        )
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

    with col2:
        st.markdown(f"""
        <div style="padding: 1rem;">
            <div style="font-family: 'Playfair Display', serif; font-size: 1.2rem; margin-bottom: 1rem;">Alignment Breakdown</div>
            <div style="margin-bottom: 0.5rem; display: flex; justify-content: space-between; align-items: center;">
                <span style="color: #8B8680; display: flex; align-items: center;">
                    <span style="width: 10px; height: 10px; background: #4CAF50; border-radius: 2px; margin-right: 0.5rem;"></span>
                    Strong (60+, 2+ categories):
                </span>
                <span style="font-weight: 600; color: #4CAF50;">{portfolio_stats.get('strong_aligned', 0)}</span>
            </div>
            <div style="margin-bottom: 0.5rem; display: flex; justify-content: space-between; align-items: center;">
                <span style="color: #8B8680; display: flex; align-items: center;">
                    <span style="width: 10px; height: 10px; background: #FF9800; border-radius: 2px; margin-right: 0.5rem;"></span>
                    Moderate (40-59):
                </span>
                <span style="font-weight: 600; color: #FF9800;">{portfolio_stats.get('moderate_aligned', 0)}</span>
            </div>
            <div style="margin-bottom: 0.5rem; display: flex; justify-content: space-between; align-items: center;">
                <span style="color: #8B8680; display: flex; align-items: center;">
                    <span style="width: 10px; height: 10px; background: #FFC107; border-radius: 2px; margin-right: 0.5rem;"></span>
                    Weak (20-39):
                </span>
                <span style="font-weight: 600; color: #FFC107;">{portfolio_stats.get('weak_aligned', 0)}</span>
            </div>
            <div style="margin-bottom: 0.75rem; display: flex; justify-content: space-between; align-items: center;">
                <span style="color: #8B8680; display: flex; align-items: center;">
                    <span style="width: 10px; height: 10px; background: #E8E4DE; border-radius: 2px; margin-right: 0.5rem;"></span>
                    Not Aligned (&lt;20):
                </span>
                <span style="font-weight: 600; color: #9E9E9E;">{portfolio_stats.get('not_aligned', 0)}</span>
            </div>
            <div style="border-top: 1px solid #E8E4DE; padding-top: 0.5rem; margin-top: 0.5rem;">
                <span style="color: #8B8680;">Avg Score:</span>
                <span style="font-weight: 600; color: #2D2A26; margin-left: 0.5rem;">{portfolio_stats['average_score']}</span>
                <span style="color: #8B8680; margin-left: 1rem;">Total:</span>
                <span style="font-weight: 600; color: #2D2A26; margin-left: 0.5rem;">{portfolio_stats['total_cards']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("<div style='font-family: Playfair Display, serif; font-size: 1.2rem; margin-bottom: 1rem;'>Opportunities</div>", unsafe_allow_html=True)
        for opp in portfolio_stats.get("opportunities", [])[:3]:
            color = "#C65D3B" if opp["opportunity"] == "High" else "#FF9800"
            relevance = opp.get('relevance', opp.get('popularity', 0))
            st.markdown(f"""
            <div style="background: {color}15; border-left: 3px solid {color}; padding: 0.5rem 0.75rem; margin-bottom: 0.5rem; border-radius: 0 6px 6px 0;">
                <div style="font-weight: 600; font-size: 0.85rem; color: #2D2A26;">{opp['trend']}</div>
                <div style="font-size: 0.75rem; color: #8B8680;">You have {opp['your_cards']} cards • Relevance: {relevance}</div>
            </div>
            """, unsafe_allow_html=True)

    # Top Trend-Aligned Cards
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h4 style='font-family: Playfair Display, serif;'>Top Trend-Aligned Cards</h4>", unsafe_allow_html=True)

    leader_cols = st.columns(5)
    for idx, card in enumerate(portfolio_stats.get("trend_leaders", [])[:5]):
        with leader_cols[idx]:
            trends_display = ", ".join(card.get("matching_trends", [])[:2]) or "Classic"
            score_color = "#4CAF50" if card["overall_score"] >= 60 else "#FF9800" if card["overall_score"] >= 40 else "#9E9E9E"
            card_name_short = card["card_name"][:25] + "..." if len(card["card_name"]) > 25 else card["card_name"]
            st.markdown(f"""
            <div style="background: white; border-radius: 10px; padding: 1rem; border: 1px solid #E8E4DE; height: 140px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                    <span style="font-weight: 600; color: #2D2A26;">#{card['rank']}</span>
                    <span style="background: {score_color}20; color: {score_color}; padding: 0.2rem 0.5rem; border-radius: 10px; font-size: 0.75rem; font-weight: 600;">
                        {card['overall_score']:.0f}
                    </span>
                </div>
                <div style="font-size: 0.85rem; color: #2D2A26; margin-bottom: 0.5rem; line-height: 1.3;">{card_name_short}</div>
                <div style="font-size: 0.7rem; color: #C65D3B;">{trends_display}</div>
                <div style="font-size: 0.7rem; color: #8B8680; margin-top: 0.25rem;">{card['sends']:,} sends</div>
            </div>
            """, unsafe_allow_html=True)

    # Methodology & Sources Footer
    methodology = trend_data.get("methodology", {})
    sources = trend_data.get("sources", [])

    st.markdown("<br>", unsafe_allow_html=True)

    with st.expander("📚 Sources & Methodology", expanded=False):
        st.markdown("""
        <div style="padding: 1rem 0;">
            <h4 style="font-family: 'Playfair Display', serif; margin-bottom: 1rem; color: #2D2A26;">Data Sources</h4>
        </div>
        """, unsafe_allow_html=True)

        # Display sources with links
        if sources and isinstance(sources[0], dict):
            for src in sources:
                verified_badge = "✅" if src.get("verified", False) else "⚠️"
                st.markdown(f"""
                <div style="background: white; border-radius: 8px; padding: 0.75rem 1rem; margin-bottom: 0.5rem; border: 1px solid #E8E4DE;">
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <span>{verified_badge}</span>
                        <a href="{src.get('url', '#')}" target="_blank" style="color: #C65D3B; text-decoration: none; font-weight: 500;">
                            {src.get('name', 'Source')}
                        </a>
                    </div>
                    <div style="font-size: 0.8rem; color: #8B8680; margin-top: 0.25rem; margin-left: 1.5rem;">
                        {src.get('description', '')}
                    </div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("""
        <div style="padding: 1.5rem 0 1rem;">
            <h4 style="font-family: 'Playfair Display', serif; margin-bottom: 1rem; color: #2D2A26;">Methodology</h4>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div style="background: #FDFBF7; border-radius: 8px; padding: 1rem; border-left: 3px solid #C65D3B;">
            <div style="font-size: 0.85rem; color: #5C5955; line-height: 1.6;">
                <strong style="color: #2D2A26;">Relevance Weights:</strong> {methodology.get('note', 'Editorial estimates based on trend prominence in source coverage.')}
            </div>
            <div style="font-size: 0.85rem; color: #5C5955; line-height: 1.6; margin-top: 0.75rem;">
                <strong style="color: #2D2A26;">Scoring Method:</strong> {methodology.get('scoring', 'Weights range from 0-100 indicating relative importance for alignment.')}
            </div>
            <div style="font-size: 0.85rem; color: #5C5955; line-height: 1.6; margin-top: 0.75rem;">
                <strong style="color: #2D2A26;">Color Alignment:</strong> {methodology.get('color_alignment', 'Calculated using hex color distance formula.')}
            </div>
        </div>
        <div style="font-size: 0.75rem; color: #A8A49E; margin-top: 1rem; font-style: italic;">
            Note: Trend data is synthesized from verified industry sources. Relevance weights are editorial estimates, not market research percentages.
            Portfolio alignment scores help identify which cards align with current design trends but should not be used as the sole basis for business decisions.
        </div>
        """, unsafe_allow_html=True)


# =============================================================================
# CATEGORY BREAKDOWN
# =============================================================================
def render_category_breakdown(analysis_lookup: dict):
    """Render the Category Breakdown section for Valentine, Birthday, and Thank You."""

    st.markdown("""
    <div class="section-container">
        <div class="section-header">
            <span class="section-number">04</span>
            <h2 class="section-title">Category Breakdown</h2>
            <div class="section-line"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p style="font-family: 'Source Sans 3', sans-serif; font-size: 1rem; color: #5C5955;
              line-height: 1.6; margin-bottom: 1.5rem; max-width: 700px;">
        Deep-dive performance data for three key occasions — Valentine's Day, Birthday, and Thank You —
        sourced from dedicated category reports.
    </p>
    """, unsafe_allow_html=True)

    # Color hex mapping (same as executive summary)
    color_hex = {
        "pink": "#FFB6C1", "white": "#FFFFFF", "orange": "#FF8C42", "green": "#5C8A6E",
        "blue": "#6B8E9B", "yellow": "#F4D03F", "red": "#C0392B", "cream": "#FDF8F3",
        "black": "#2D2A26", "teal": "#008080", "multicolor": "linear-gradient(90deg, #FF6B6B, #4ECDC4, #45B7D1)",
        "brown": "#8B7355", "gold": "#D4AF37", "coral": "#FF7F50", "purple": "#9B59B6",
        "navy": "#34495E", "tan": "#D2B48C", "mint": "#98D8C8", "lavender": "#E6E6FA",
        "peach": "#FFCBA4", "sage": "#9CAF88", "sage green": "#9CAF88"
    }

    categories = [
        ("Valentine's Day", VALENTINE_CSV, "#C65D3B"),
        ("Birthday", BIRTHDAY_CSV, "#5C8A6E"),
        ("Thank You", THANKYOU_CSV, "#6B8E9B"),
    ]

    sub_tabs = st.tabs([cat[0] for cat in categories])

    for tab, (cat_name, csv_path, accent_color) in zip(sub_tabs, categories):
        with tab:
            cat_df = load_category_csv(csv_path)

            if cat_df.empty:
                st.info(f"No data available for {cat_name}. Ensure {csv_path.name} exists.")
                continue

            # ── Hero stat row ──────────────────────────────────────────────
            total_sends = int(cat_df["Sends"].sum())
            num_cards = len(cat_df)
            top_card = cat_df.iloc[0]["Display Name"] if not cat_df.empty else "N/A"
            avg_sends = int(total_sends / num_cards) if num_cards > 0 else 0

            hero_stats = [
                (f"{total_sends:,}", "Total Sends", accent_color),
                (f"{num_cards}", "Cards", "#8B7355"),
                (top_card[:30] + ("..." if len(str(top_card)) > 30 else ""), "Top Card", "#D4AF37"),
                (f"{avg_sends:,}", "Avg Sends/Card", "#A0522D"),
            ]

            cols = st.columns(4)
            for col, (value, label, border_color) in zip(cols, hero_stats):
                with col:
                    st.markdown(f"""
                    <div style="background: white; padding: 1rem; border-radius: 8px; border-left: 3px solid {border_color};">
                        <div style="font-family: 'Playfair Display', serif; font-size: 1.1rem; color: #2D2A26; font-weight: 600;">
                            {value}
                        </div>
                        <div style="font-size: 0.75rem; color: #8B8680; text-transform: uppercase; letter-spacing: 0.5px;">
                            {label}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

            # ── Top 10 horizontal bar chart ────────────────────────────────
            top_10 = cat_df.head(10).copy()
            top_10["Short Name"] = top_10["Display Name"].apply(
                lambda x: str(x)[:35] + "..." if len(str(x)) > 35 else str(x)
            )

            st.markdown(f"""
            <div class="chart-container" style="margin-top: 1.5rem;">
                <div class="chart-title">Top 10 {cat_name} Cards</div>
                <div class="chart-subtitle">Highest-performing cards by total sends</div>
            </div>
            """, unsafe_allow_html=True)

            fig_bar = go.Figure()
            fig_bar.add_trace(go.Bar(
                x=top_10["Sends"].values[::-1],
                y=top_10["Short Name"].values[::-1],
                orientation='h',
                marker=dict(
                    color=CHART_COLORS[:10][::-1],
                    line=dict(width=0)
                ),
                hovertemplate="<b>%{y}</b><br>Sends: %{x:,.0f}<extra></extra>"
            ))

            fig_bar.update_layout(
                height=400,
                margin=dict(l=0, r=20, t=10, b=10),
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font=dict(family="Source Sans 3, sans-serif", color="#2D2A26"),
                xaxis=dict(showgrid=True, gridcolor="rgba(45, 42, 38, 0.06)", zeroline=False),
                yaxis=dict(showgrid=False, zeroline=False),
                showlegend=False,
            )
            st.plotly_chart(fig_bar, use_container_width=True, config={"displayModeBar": False})

            # ── Top Cards Visual Gallery ───────────────────────────────────
            top_50 = cat_df.head(50)
            st.markdown(f"""
            <div class="chart-container" style="margin-top: 1.5rem;">
                <div class="chart-title">Top {len(top_50)} {cat_name} Cards</div>
                <div class="chart-subtitle">Visual gallery of the highest-performing cards</div>
            </div>
            """, unsafe_allow_html=True)

            gallery_cards_html = []
            for _, grow in top_50.iterrows():
                card_name = grow["Card Name"]
                card_id = grow["Card ID"]
                display_name = grow["Display Name"]
                sends = int(grow["Sends"])

                image_path = get_card_image_path(card_name)
                if image_path:
                    img_b64 = get_image_base64(image_path)
                    if img_b64:
                        img_html = f'<img src="data:image/jpeg;base64,{img_b64}" alt="{display_name}">'
                    else:
                        img_html = '<div class="no-image-placeholder">No Preview</div>'
                else:
                    img_html = '<div class="no-image-placeholder">No Preview</div>'

                title_display = str(display_name)[:45] + ("..." if len(str(display_name)) > 45 else "")
                title_display = title_display.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

                gallery_cards_html.append(
                    f'<div class="card-item">'
                    f'<div class="card-image-container">{img_html}'
                    f'<div class="card-occasion-tag">{cat_name}</div>'
                    f'</div>'
                    f'<div class="card-info">'
                    f'<div class="card-title">{title_display}</div>'
                    f'<div class="card-sends"><span class="card-sends-value">{sends:,}</span>'
                    f'<span class="card-sends-label">sends</span></div>'
                    f'</div></div>'
                )

            st.markdown(f'<div class="gallery-grid">{"".join(gallery_cards_html)}</div>', unsafe_allow_html=True)

            # ── Gather analysis metadata for this category ─────────────────
            cat_design_styles = {}
            cat_colors = {}
            cat_themes = {}
            cat_artists = {}

            for _, row in cat_df.iterrows():
                card_id = row["Card ID"]
                sends = row["Sends"]
                analysis = analysis_lookup.get(card_id, {})

                style = analysis.get("design_style")
                if style:
                    cat_design_styles[style] = cat_design_styles.get(style, 0) + 1

                card_colors = analysis.get("primary_colors")
                if card_colors and isinstance(card_colors, list):
                    for c in card_colors:
                        cat_colors[c] = cat_colors.get(c, 0) + 1

                card_themes = analysis.get("themes")
                if card_themes and isinstance(card_themes, list):
                    for t in card_themes:
                        cat_themes[t] = cat_themes.get(t, 0) + 1

                # Extract artist from display name
                display_name = row["Display Name"]
                artist = extract_artist_from_card_name(str(display_name))
                if artist != "Unknown Artist":
                    cat_artists[artist] = cat_artists.get(artist, 0) + sends

            # ── Design Style donut + Color swatches (side by side) ─────────
            col1, col2 = st.columns(2, gap="large")

            with col1:
                st.markdown(f"""
                <div class="chart-container" style="margin-top: 1.5rem;">
                    <div class="chart-title">Design Styles</div>
                    <div class="chart-subtitle">Visual approach distribution for {cat_name} cards</div>
                </div>
                """, unsafe_allow_html=True)

                if cat_design_styles:
                    style_df = pd.DataFrame([
                        {"Style": k.replace("_", " ").title(), "Count": v}
                        for k, v in sorted(cat_design_styles.items(), key=lambda x: -x[1])[:8]
                    ])

                    fig_donut = go.Figure(data=[go.Pie(
                        labels=style_df["Style"],
                        values=style_df["Count"],
                        hole=0.4,
                        marker=dict(
                            colors=['#C65D3B', '#5C8A6E', '#6B8E9B', '#8B7355', '#A69076',
                                    '#D4846A', '#7BA393', '#98BBB0'][:len(style_df)],
                            line=dict(color='#FDFBF7', width=2)
                        ),
                        textposition='outside',
                        textinfo='label+percent',
                        textfont=dict(size=10),
                        hovertemplate="<b>%{label}</b><br>Cards: %{value}<br>Share: %{percent}<extra></extra>"
                    )])

                    fig_donut.update_layout(
                        height=350,
                        margin=dict(l=20, r=20, t=20, b=20),
                        paper_bgcolor="rgba(0,0,0,0)",
                        font=dict(family="Source Sans 3, sans-serif", color="#2D2A26"),
                        showlegend=False,
                    )
                    st.plotly_chart(fig_donut, use_container_width=True, config={"displayModeBar": False})
                else:
                    st.caption("No design style data available.")

            with col2:
                st.markdown(f"""
                <div class="chart-container" style="margin-top: 1.5rem;">
                    <div class="chart-title">Color Palette</div>
                    <div class="chart-subtitle">Top colors used in {cat_name} cards</div>
                </div>
                """, unsafe_allow_html=True)

                top_cat_colors = sorted(cat_colors.items(), key=lambda x: -x[1])[:8]
                if top_cat_colors:
                    swatch_cols = st.columns(4)
                    for idx, (color_name, count) in enumerate(top_cat_colors):
                        hex_val = color_hex.get(color_name.lower(), "#CCC")
                        is_gradient = "gradient" in hex_val
                        bg_style = f"background: {hex_val};" if is_gradient else f"background-color: {hex_val};"
                        border_style = "border: 1px solid #DDD;" if color_name.lower() in ["white", "cream"] else ""

                        with swatch_cols[idx % 4]:
                            st.markdown(f'''<div style="text-align: center; padding: 0.5rem;">
<div style="width: 50px; height: 50px; border-radius: 50%; {bg_style} {border_style} margin: 0 auto; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"></div>
<div style="font-size: 0.8rem; color: #2D2A26; margin-top: 0.5rem; font-weight: 500;">{color_name.title()}</div>
<div style="font-size: 0.7rem; color: #8B8680;">{count} cards</div>
</div>''', unsafe_allow_html=True)
                else:
                    st.caption("No color data available.")

            # ── Top Themes bar chart ───────────────────────────────────────
            st.markdown(f"""
            <div class="chart-container" style="margin-top: 1.5rem;">
                <div class="chart-title">Top Themes</div>
                <div class="chart-subtitle">Most common visual themes in {cat_name} cards</div>
            </div>
            """, unsafe_allow_html=True)

            if cat_themes:
                theme_df = pd.DataFrame([
                    {"Theme": k.title(), "Count": v}
                    for k, v in sorted(cat_themes.items(), key=lambda x: -x[1])[:12]
                ])

                fig_theme = go.Figure()
                fig_theme.add_trace(go.Bar(
                    x=theme_df["Theme"],
                    y=theme_df["Count"],
                    marker=dict(color=accent_color, line=dict(width=0)),
                    text=theme_df["Count"],
                    textposition='outside',
                    hovertemplate="<b>%{x}</b><br>Appears in %{y} cards<extra></extra>"
                ))

                fig_theme.update_layout(
                    height=300,
                    margin=dict(l=0, r=0, t=10, b=60),
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    font=dict(family="Source Sans 3, sans-serif", color="#2D2A26"),
                    xaxis=dict(showgrid=False, zeroline=False, tickangle=-45),
                    yaxis=dict(showgrid=True, gridcolor="rgba(45,42,38,0.06)", zeroline=False),
                    showlegend=False,
                )
                st.plotly_chart(fig_theme, use_container_width=True, config={"displayModeBar": False})
            else:
                st.caption("No theme data available.")

            # ── Top Artists leaderboard ────────────────────────────────────
            st.markdown(f"""
            <div class="chart-container" style="margin-top: 1.5rem;">
                <div class="chart-title">Top Artists</div>
                <div class="chart-subtitle">Leading contributors to {cat_name} by total sends</div>
            </div>
            """, unsafe_allow_html=True)

            if cat_artists:
                top_artist_list = sorted(cat_artists.items(), key=lambda x: -x[1])[:10]

                table_rows = ""
                for rank, (artist, sends) in enumerate(top_artist_list, 1):
                    rank_style = f"color: {accent_color}; font-weight: 700;" if rank <= 3 else "color: #8B8680;"
                    table_rows += f"""
                    <tr style="border-bottom: 1px solid rgba(45, 42, 38, 0.06);">
                        <td style="padding: 0.6rem 0.75rem; font-family: 'Playfair Display', serif; {rank_style} font-size: 0.9rem;">{rank}</td>
                        <td style="padding: 0.6rem 0.75rem; font-family: 'Source Sans 3', sans-serif; color: #2D2A26; font-weight: 500;">{artist}</td>
                        <td style="padding: 0.6rem 0.75rem; font-family: 'Playfair Display', serif; color: #2D2A26; font-weight: 600; text-align: right;">{sends:,}</td>
                    </tr>"""

                st.markdown(f"""
                <table style="width: 100%; border-collapse: collapse; background: white; border-radius: 8px; overflow: hidden;">
                    <thead>
                        <tr style="background: #FDF8F3; border-bottom: 2px solid {accent_color};">
                            <th style="padding: 0.75rem; text-align: left; font-family: 'Source Sans 3', sans-serif; font-size: 0.75rem; color: #8B8680; text-transform: uppercase; letter-spacing: 0.5px; width: 50px;">Rank</th>
                            <th style="padding: 0.75rem; text-align: left; font-family: 'Source Sans 3', sans-serif; font-size: 0.75rem; color: #8B8680; text-transform: uppercase; letter-spacing: 0.5px;">Artist</th>
                            <th style="padding: 0.75rem; text-align: right; font-family: 'Source Sans 3', sans-serif; font-size: 0.75rem; color: #8B8680; text-transform: uppercase; letter-spacing: 0.5px;">Total Sends</th>
                        </tr>
                    </thead>
                    <tbody>{table_rows}</tbody>
                </table>
                """, unsafe_allow_html=True)
            else:
                st.caption("No artist data available.")


# =============================================================================
# MAIN APPLICATION
# =============================================================================
def main():
    """Main application entry point."""

    # Load data
    with st.spinner("Loading data..."):
        df = load_csv_data()
        analysis_data = load_analysis_data()
        analysis_lookup = create_analysis_lookup(analysis_data)

    # Check if data loaded
    if df.empty:
        st.error("Unable to load data. Please ensure the CSV file exists.")
        st.info(f"Expected file: {CSV_FILE}")
        return

    # Render hero section
    render_hero(df)

    # Show all 301 cards by default (no filtering)
    filtered_df = df

    # Render charts
    render_charts(filtered_df, analysis_lookup)

    # Render executive insights
    render_executive_summary(filtered_df, analysis_lookup)

    # Render artist performance intelligence
    render_artist_performance(analysis_data, df)

    # Tabs for Gallery, Data Table, Card Comparison, Portfolio Gap Analysis, Creative Briefs, Trend Intelligence, and Category Breakdown
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "Gallery", "Data Table", "Card Comparison",
        "Portfolio Gap Analysis", "Creative Briefs", "Trend Intelligence",
        "Category Breakdown"
    ])

    with tab1:
        render_gallery(filtered_df, analysis_lookup)

    with tab2:
        render_data_table(filtered_df, analysis_lookup)

    with tab3:
        render_card_comparison(filtered_df, analysis_lookup)

    with tab4:
        render_portfolio_gap_analysis(filtered_df, analysis_lookup, analysis_data)

    with tab5:
        render_creative_brief_generator(analysis_data)

    with tab6:
        render_trend_intelligence_hub(filtered_df, analysis_lookup, analysis_data)

    with tab7:
        render_category_breakdown(analysis_lookup)


if __name__ == "__main__":
    main()
