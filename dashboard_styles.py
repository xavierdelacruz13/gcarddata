"""
Comprehensive CSS stylesheet for Streamlit Greeting Card Analytics Dashboard
Editorial/Magazine aesthetic with warm, sophisticated design
"""

CSS_STYLES = """
/* ==========================================================================
   GOOGLE FONTS IMPORT
   ========================================================================== */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Source+Sans+3:wght@300;400;600&display=swap');

/* ==========================================================================
   CSS CUSTOM PROPERTIES (DESIGN TOKENS)
   ========================================================================== */
:root {
    /* Color Palette */
    --color-background: #FDFBF7;
    --color-primary: #C65D3B;
    --color-primary-dark: #A84D2F;
    --color-primary-light: #D97B5C;
    --color-secondary: #8B7355;
    --color-secondary-dark: #6E5A43;
    --color-text: #2D2A26;
    --color-text-muted: #5A5651;
    --color-light-gray: #E8E4DE;
    --color-card-bg: #FFFFFF;
    --color-success: #5B8C5A;
    --color-warning: #D4A84B;

    /* Typography */
    --font-heading: 'Playfair Display', Georgia, serif;
    --font-body: 'Source Sans 3', -apple-system, BlinkMacSystemFont, sans-serif;

    /* Spacing */
    --spacing-xs: 4px;
    --spacing-sm: 8px;
    --spacing-md: 16px;
    --spacing-lg: 24px;
    --spacing-xl: 32px;
    --spacing-2xl: 48px;
    --spacing-3xl: 64px;

    /* Shadows */
    --shadow-sm: 0 1px 3px rgba(45, 42, 38, 0.06);
    --shadow-md: 0 4px 12px rgba(45, 42, 38, 0.08);
    --shadow-lg: 0 8px 24px rgba(45, 42, 38, 0.12);
    --shadow-xl: 0 16px 48px rgba(45, 42, 38, 0.16);

    /* Border Radius */
    --radius-sm: 4px;
    --radius-md: 8px;
    --radius-lg: 12px;
    --radius-xl: 16px;
    --radius-full: 9999px;

    /* Transitions */
    --transition-fast: 0.2s ease;
    --transition-normal: 0.3s ease;
    --transition-slow: 0.5s ease;
}

/* ==========================================================================
   HIDE STREAMLIT DEFAULTS
   ========================================================================== */
#MainMenu {
    visibility: hidden !important;
}

footer {
    visibility: hidden !important;
}

header[data-testid="stHeader"] {
    visibility: hidden !important;
    height: 0 !important;
}

.stDeployButton {
    display: none !important;
}

div[data-testid="stToolbar"] {
    display: none !important;
}

div[data-testid="stDecoration"] {
    display: none !important;
}

/* ==========================================================================
   CUSTOM SCROLLBAR (WEBKIT)
   ========================================================================== */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

::-webkit-scrollbar-track {
    background: var(--color-light-gray);
    border-radius: var(--radius-full);
}

::-webkit-scrollbar-thumb {
    background: var(--color-secondary);
    border-radius: var(--radius-full);
    transition: background var(--transition-fast);
}

::-webkit-scrollbar-thumb:hover {
    background: var(--color-secondary-dark);
}

/* ==========================================================================
   BASE STYLES & PAGE CONTAINER
   ========================================================================== */
.stApp {
    background-color: var(--color-background) !important;
    font-family: var(--font-body) !important;
    color: var(--color-text) !important;
}

.main .block-container {
    max-width: 1400px !important;
    padding: var(--spacing-xl) var(--spacing-2xl) var(--spacing-3xl) !important;
    margin: 0 auto !important;
}

/* Page load animation */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

.main .block-container > div {
    animation: fadeInUp 0.6s ease-out forwards;
}

.main .block-container > div:nth-child(1) { animation-delay: 0.1s; }
.main .block-container > div:nth-child(2) { animation-delay: 0.15s; }
.main .block-container > div:nth-child(3) { animation-delay: 0.2s; }
.main .block-container > div:nth-child(4) { animation-delay: 0.25s; }
.main .block-container > div:nth-child(5) { animation-delay: 0.3s; }
.main .block-container > div:nth-child(6) { animation-delay: 0.35s; }

/* ==========================================================================
   TYPOGRAPHY
   ========================================================================== */
h1, h2, h3, h4, h5, h6,
.stMarkdown h1, .stMarkdown h2, .stMarkdown h3,
.stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {
    font-family: var(--font-heading) !important;
    color: var(--color-text) !important;
    font-weight: 600 !important;
    letter-spacing: -0.02em !important;
    line-height: 1.2 !important;
}

h1, .stMarkdown h1 {
    font-size: 3rem !important;
    font-weight: 700 !important;
    margin-bottom: var(--spacing-lg) !important;
}

h2, .stMarkdown h2 {
    font-size: 2.25rem !important;
    margin-bottom: var(--spacing-md) !important;
}

h3, .stMarkdown h3 {
    font-size: 1.75rem !important;
    margin-bottom: var(--spacing-md) !important;
}

h4, .stMarkdown h4 {
    font-size: 1.25rem !important;
}

p, .stMarkdown p {
    font-family: var(--font-body) !important;
    font-size: 1rem !important;
    line-height: 1.7 !important;
    color: var(--color-text-muted) !important;
    font-weight: 400 !important;
}

/* ==========================================================================
   HERO HEADER
   ========================================================================== */
.hero-header {
    background: linear-gradient(135deg, var(--color-background) 0%, #F5F0E8 50%, var(--color-light-gray) 100%);
    padding: var(--spacing-3xl) var(--spacing-2xl);
    margin: calc(-1 * var(--spacing-xl)) calc(-1 * var(--spacing-2xl)) var(--spacing-2xl);
    border-bottom: 1px solid var(--color-light-gray);
    position: relative;
    overflow: hidden;
}

.hero-header::before {
    content: '';
    position: absolute;
    top: 0;
    right: 0;
    width: 40%;
    height: 100%;
    background: linear-gradient(135deg, transparent 0%, rgba(198, 93, 59, 0.05) 100%);
    pointer-events: none;
}

.hero-header h1 {
    font-size: 3.5rem !important;
    font-weight: 700 !important;
    background: linear-gradient(135deg, var(--color-text) 0%, var(--color-primary) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: var(--spacing-sm) !important;
}

.hero-header .subtitle {
    font-family: var(--font-body);
    font-size: 1.25rem;
    font-weight: 300;
    color: var(--color-text-muted);
    letter-spacing: 0.02em;
}

/* ==========================================================================
   METRIC DISPLAYS (Elegant Inline Stats)
   ========================================================================== */
div[data-testid="stMetric"] {
    background: transparent !important;
    padding: var(--spacing-md) 0 !important;
    border-bottom: 1px solid var(--color-light-gray);
}

div[data-testid="stMetric"] > div {
    display: flex;
    flex-direction: column;
    gap: var(--spacing-xs);
}

div[data-testid="stMetric"] label {
    font-family: var(--font-body) !important;
    font-size: 0.75rem !important;
    font-weight: 600 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.1em !important;
    color: var(--color-secondary) !important;
}

div[data-testid="stMetric"] div[data-testid="stMetricValue"] {
    font-family: var(--font-heading) !important;
    font-size: 2.5rem !important;
    font-weight: 700 !important;
    color: var(--color-text) !important;
    line-height: 1 !important;
}

div[data-testid="stMetric"] div[data-testid="stMetricDelta"] {
    font-family: var(--font-body) !important;
    font-size: 0.875rem !important;
    font-weight: 600 !important;
}

div[data-testid="stMetric"] div[data-testid="stMetricDelta"] svg {
    width: 14px;
    height: 14px;
}

/* Positive delta (success) */
div[data-testid="stMetric"] div[data-testid="stMetricDelta"][data-testid-delta-type="positive"] {
    color: var(--color-success) !important;
}

/* Negative delta (warning) */
div[data-testid="stMetric"] div[data-testid="stMetricDelta"][data-testid-delta-type="negative"] {
    color: var(--color-primary) !important;
}

/* Custom metric container class */
.metric-container {
    display: flex;
    gap: var(--spacing-2xl);
    padding: var(--spacing-lg) 0;
    border-bottom: 2px solid var(--color-light-gray);
    margin-bottom: var(--spacing-xl);
}

.metric-item {
    flex: 1;
    text-align: left;
}

.metric-label {
    font-family: var(--font-body);
    font-size: 0.75rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--color-secondary);
    margin-bottom: var(--spacing-xs);
}

.metric-value {
    font-family: var(--font-heading);
    font-size: 2.5rem;
    font-weight: 700;
    color: var(--color-text);
    line-height: 1;
}

.metric-delta {
    font-family: var(--font-body);
    font-size: 0.875rem;
    font-weight: 600;
    margin-top: var(--spacing-xs);
}

.metric-delta.positive { color: var(--color-success); }
.metric-delta.negative { color: var(--color-primary); }

/* ==========================================================================
   SIDEBAR STYLES
   ========================================================================== */
section[data-testid="stSidebar"] {
    background-color: var(--color-card-bg) !important;
    border-right: 1px solid var(--color-light-gray) !important;
    padding-top: var(--spacing-xl) !important;
}

section[data-testid="stSidebar"] .block-container {
    padding: var(--spacing-lg) !important;
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    font-size: 1.25rem !important;
    color: var(--color-text) !important;
    padding-bottom: var(--spacing-sm);
    border-bottom: 2px solid var(--color-primary);
    margin-bottom: var(--spacing-md) !important;
}

/* Sidebar section labels */
.sidebar-section-label {
    font-family: var(--font-body);
    font-size: 0.7rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: var(--color-secondary);
    margin-top: var(--spacing-lg);
    margin-bottom: var(--spacing-sm);
}

/* ==========================================================================
   SELECT / DROPDOWN STYLING
   ========================================================================== */
div[data-baseweb="select"] {
    font-family: var(--font-body) !important;
}

div[data-baseweb="select"] > div {
    background-color: var(--color-card-bg) !important;
    border: 1px solid var(--color-light-gray) !important;
    border-radius: var(--radius-md) !important;
    transition: all var(--transition-fast) !important;
}

div[data-baseweb="select"] > div:hover {
    border-color: var(--color-secondary) !important;
}

div[data-baseweb="select"] > div:focus-within {
    border-color: var(--color-primary) !important;
    box-shadow: 0 0 0 2px rgba(198, 93, 59, 0.15) !important;
}

div[data-baseweb="select"] span {
    font-family: var(--font-body) !important;
    color: var(--color-text) !important;
}

/* Dropdown menu */
div[data-baseweb="popover"] {
    border-radius: var(--radius-md) !important;
    box-shadow: var(--shadow-lg) !important;
    border: 1px solid var(--color-light-gray) !important;
}

div[data-baseweb="popover"] ul {
    padding: var(--spacing-sm) !important;
}

div[data-baseweb="popover"] li {
    font-family: var(--font-body) !important;
    border-radius: var(--radius-sm) !important;
    transition: background var(--transition-fast) !important;
}

div[data-baseweb="popover"] li:hover {
    background-color: var(--color-light-gray) !important;
}

/* Multiselect tags */
span[data-baseweb="tag"] {
    background-color: var(--color-primary) !important;
    border-radius: var(--radius-full) !important;
    font-family: var(--font-body) !important;
    font-size: 0.8rem !important;
}

/* ==========================================================================
   INPUT FIELDS
   ========================================================================== */
input[type="text"],
input[type="number"],
div[data-baseweb="input"] input {
    font-family: var(--font-body) !important;
    background-color: var(--color-card-bg) !important;
    border: 1px solid var(--color-light-gray) !important;
    border-radius: var(--radius-md) !important;
    padding: var(--spacing-sm) var(--spacing-md) !important;
    transition: all var(--transition-fast) !important;
}

input[type="text"]:focus,
input[type="number"]:focus,
div[data-baseweb="input"] input:focus {
    border-color: var(--color-primary) !important;
    box-shadow: 0 0 0 2px rgba(198, 93, 59, 0.15) !important;
    outline: none !important;
}

/* Slider styling */
div[data-baseweb="slider"] div[role="slider"] {
    background-color: var(--color-primary) !important;
}

div[data-baseweb="slider"] div[data-testid="stTickBar"] > div {
    background-color: var(--color-primary) !important;
}

/* ==========================================================================
   CHART CONTAINERS
   ========================================================================== */
div[data-testid="stPlotlyChart"],
div[data-testid="stVegaLiteChart"],
div[data-testid="stArrowVegaLiteChart"],
.chart-container {
    background-color: var(--color-card-bg) !important;
    border-radius: var(--radius-lg) !important;
    box-shadow: var(--shadow-md) !important;
    padding: var(--spacing-lg) !important;
    margin: var(--spacing-md) 0 !important;
    border: 1px solid var(--color-light-gray) !important;
    transition: box-shadow var(--transition-normal) !important;
}

div[data-testid="stPlotlyChart"]:hover,
div[data-testid="stVegaLiteChart"]:hover,
.chart-container:hover {
    box-shadow: var(--shadow-lg) !important;
}

/* Chart title styling */
.chart-title {
    font-family: var(--font-heading);
    font-size: 1.25rem;
    font-weight: 600;
    color: var(--color-text);
    margin-bottom: var(--spacing-md);
    padding-bottom: var(--spacing-sm);
    border-bottom: 1px solid var(--color-light-gray);
}

/* ==========================================================================
   CARD GRID SYSTEM
   ========================================================================== */
.card-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: var(--spacing-lg);
    margin: var(--spacing-xl) 0;
}

@media (max-width: 1200px) {
    .card-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 768px) {
    .card-grid {
        grid-template-columns: 1fr;
    }
}

/* ==========================================================================
   CARD ITEMS
   ========================================================================== */
.card-item {
    background-color: var(--color-card-bg);
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-md);
    overflow: hidden;
    position: relative;
    transition: transform var(--transition-normal), box-shadow var(--transition-normal);
    cursor: pointer;
}

.card-item:hover {
    transform: translateY(-8px);
    box-shadow: var(--shadow-xl);
}

/* Card image */
.card-image {
    width: 100%;
    height: 200px;
    object-fit: cover;
    display: block;
}

.card-image-container {
    position: relative;
    overflow: hidden;
}

.card-image-container::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 60px;
    background: linear-gradient(to top, rgba(0,0,0,0.1), transparent);
    pointer-events: none;
}

/* Card content */
.card-content {
    padding: var(--spacing-lg);
}

.card-title {
    font-family: var(--font-heading);
    font-size: 1.125rem;
    font-weight: 600;
    color: var(--color-text);
    margin-bottom: var(--spacing-sm);
    line-height: 1.3;
}

.card-description {
    font-family: var(--font-body);
    font-size: 0.875rem;
    color: var(--color-text-muted);
    line-height: 1.6;
    margin-bottom: var(--spacing-md);
}

.card-meta {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: var(--font-body);
    font-size: 0.75rem;
    color: var(--color-secondary);
}

/* Rank badge overlay */
.rank-badge {
    position: absolute;
    top: var(--spacing-md);
    left: var(--spacing-md);
    background: var(--color-card-bg);
    color: var(--color-primary);
    font-family: var(--font-heading);
    font-size: 1rem;
    font-weight: 700;
    width: 36px;
    height: 36px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: var(--shadow-md);
    z-index: 2;
}

/* Occasion tag */
.occasion-tag {
    position: absolute;
    top: var(--spacing-md);
    right: var(--spacing-md);
    background: var(--color-primary);
    color: white;
    font-family: var(--font-body);
    font-size: 0.7rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    padding: var(--spacing-xs) var(--spacing-sm);
    border-radius: var(--radius-full);
    z-index: 2;
}

.occasion-tag.birthday { background: var(--color-primary); }
.occasion-tag.holiday { background: var(--color-success); }
.occasion-tag.wedding { background: var(--color-secondary); }
.occasion-tag.thank-you { background: var(--color-warning); }

/* ==========================================================================
   BUTTONS
   ========================================================================== */
button[kind="primary"],
.stButton > button,
button[data-testid="baseButton-primary"] {
    font-family: var(--font-body) !important;
    font-weight: 600 !important;
    font-size: 0.875rem !important;
    background-color: var(--color-primary) !important;
    color: white !important;
    border: none !important;
    border-radius: var(--radius-full) !important;
    padding: var(--spacing-sm) var(--spacing-lg) !important;
    transition: all var(--transition-fast) !important;
    text-transform: none !important;
    letter-spacing: 0.02em !important;
}

button[kind="primary"]:hover,
.stButton > button:hover,
button[data-testid="baseButton-primary"]:hover {
    background-color: var(--color-primary-dark) !important;
    box-shadow: var(--shadow-md) !important;
    transform: translateY(-1px) !important;
}

button[kind="primary"]:active,
.stButton > button:active {
    transform: translateY(0) !important;
}

/* Secondary button */
button[kind="secondary"],
button[data-testid="baseButton-secondary"] {
    font-family: var(--font-body) !important;
    font-weight: 600 !important;
    background-color: transparent !important;
    color: var(--color-primary) !important;
    border: 2px solid var(--color-primary) !important;
    border-radius: var(--radius-full) !important;
    padding: var(--spacing-sm) var(--spacing-lg) !important;
    transition: all var(--transition-fast) !important;
}

button[kind="secondary"]:hover,
button[data-testid="baseButton-secondary"]:hover {
    background-color: var(--color-primary) !important;
    color: white !important;
}

/* Custom button classes */
.btn-primary {
    display: inline-block;
    font-family: var(--font-body);
    font-weight: 600;
    font-size: 0.875rem;
    background-color: var(--color-primary);
    color: white;
    border: none;
    border-radius: var(--radius-full);
    padding: var(--spacing-sm) var(--spacing-lg);
    cursor: pointer;
    transition: all var(--transition-fast);
    text-decoration: none;
}

.btn-primary:hover {
    background-color: var(--color-primary-dark);
    box-shadow: var(--shadow-md);
    transform: translateY(-1px);
}

.btn-secondary {
    display: inline-block;
    font-family: var(--font-body);
    font-weight: 600;
    font-size: 0.875rem;
    background-color: transparent;
    color: var(--color-primary);
    border: 2px solid var(--color-primary);
    border-radius: var(--radius-full);
    padding: var(--spacing-sm) var(--spacing-lg);
    cursor: pointer;
    transition: all var(--transition-fast);
    text-decoration: none;
}

.btn-secondary:hover {
    background-color: var(--color-primary);
    color: white;
}

/* ==========================================================================
   DATA TABLE
   ========================================================================== */
div[data-testid="stDataFrame"],
div[data-testid="stTable"] {
    background-color: var(--color-card-bg) !important;
    border-radius: var(--radius-lg) !important;
    box-shadow: var(--shadow-md) !important;
    overflow: hidden !important;
    border: 1px solid var(--color-light-gray) !important;
}

div[data-testid="stDataFrame"] table,
div[data-testid="stTable"] table {
    font-family: var(--font-body) !important;
    border-collapse: collapse !important;
    width: 100% !important;
}

/* Table header */
div[data-testid="stDataFrame"] thead th,
div[data-testid="stTable"] thead th {
    font-family: var(--font-body) !important;
    font-weight: 600 !important;
    font-size: 0.75rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.08em !important;
    color: var(--color-secondary) !important;
    background-color: var(--color-light-gray) !important;
    padding: var(--spacing-md) var(--spacing-lg) !important;
    text-align: left !important;
    position: sticky !important;
    top: 0 !important;
    z-index: 1 !important;
    border-bottom: 2px solid var(--color-secondary) !important;
}

/* Table rows */
div[data-testid="stDataFrame"] tbody tr,
div[data-testid="stTable"] tbody tr {
    transition: background-color var(--transition-fast) !important;
}

/* Alternating row colors */
div[data-testid="stDataFrame"] tbody tr:nth-child(even),
div[data-testid="stTable"] tbody tr:nth-child(even) {
    background-color: rgba(232, 228, 222, 0.3) !important;
}

div[data-testid="stDataFrame"] tbody tr:hover,
div[data-testid="stTable"] tbody tr:hover {
    background-color: rgba(198, 93, 59, 0.05) !important;
}

/* Table cells */
div[data-testid="stDataFrame"] tbody td,
div[data-testid="stTable"] tbody td {
    font-family: var(--font-body) !important;
    font-size: 0.875rem !important;
    color: var(--color-text) !important;
    padding: var(--spacing-md) var(--spacing-lg) !important;
    border-bottom: 1px solid var(--color-light-gray) !important;
}

/* Custom table class */
.data-table {
    width: 100%;
    border-collapse: collapse;
    font-family: var(--font-body);
    background: var(--color-card-bg);
    border-radius: var(--radius-lg);
    overflow: hidden;
    box-shadow: var(--shadow-md);
}

.data-table thead {
    background: var(--color-light-gray);
    position: sticky;
    top: 0;
}

.data-table th {
    font-weight: 600;
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--color-secondary);
    padding: var(--spacing-md) var(--spacing-lg);
    text-align: left;
    border-bottom: 2px solid var(--color-secondary);
}

.data-table td {
    font-size: 0.875rem;
    color: var(--color-text);
    padding: var(--spacing-md) var(--spacing-lg);
    border-bottom: 1px solid var(--color-light-gray);
}

.data-table tr:nth-child(even) {
    background: rgba(232, 228, 222, 0.3);
}

.data-table tr:hover {
    background: rgba(198, 93, 59, 0.05);
}

/* ==========================================================================
   TABS STYLING
   ========================================================================== */
div[data-baseweb="tab-list"] {
    background-color: transparent !important;
    border-bottom: 2px solid var(--color-light-gray) !important;
    gap: var(--spacing-md) !important;
}

button[data-baseweb="tab"] {
    font-family: var(--font-body) !important;
    font-weight: 600 !important;
    font-size: 0.875rem !important;
    color: var(--color-text-muted) !important;
    background-color: transparent !important;
    border: none !important;
    padding: var(--spacing-md) var(--spacing-lg) !important;
    transition: all var(--transition-fast) !important;
    position: relative !important;
}

button[data-baseweb="tab"]:hover {
    color: var(--color-primary) !important;
}

button[data-baseweb="tab"][aria-selected="true"] {
    color: var(--color-primary) !important;
}

button[data-baseweb="tab"][aria-selected="true"]::after {
    content: '';
    position: absolute;
    bottom: -2px;
    left: 0;
    right: 0;
    height: 3px;
    background-color: var(--color-primary);
    border-radius: var(--radius-full);
}

div[data-baseweb="tab-highlight"] {
    background-color: var(--color-primary) !important;
}

/* ==========================================================================
   EXPANDER STYLING
   ========================================================================== */
div[data-testid="stExpander"] {
    background-color: var(--color-card-bg) !important;
    border: 1px solid var(--color-light-gray) !important;
    border-radius: var(--radius-lg) !important;
    overflow: hidden !important;
    margin: var(--spacing-sm) 0 !important;
}

div[data-testid="stExpander"] summary {
    font-family: var(--font-body) !important;
    font-weight: 600 !important;
    color: var(--color-text) !important;
    padding: var(--spacing-md) var(--spacing-lg) !important;
    transition: background-color var(--transition-fast) !important;
}

div[data-testid="stExpander"] summary:hover {
    background-color: var(--color-light-gray) !important;
}

div[data-testid="stExpander"] div[data-testid="stExpanderDetails"] {
    padding: var(--spacing-lg) !important;
    border-top: 1px solid var(--color-light-gray) !important;
}

/* ==========================================================================
   ALERT / INFO BOXES
   ========================================================================== */
div[data-testid="stAlert"] {
    font-family: var(--font-body) !important;
    border-radius: var(--radius-md) !important;
    border-left-width: 4px !important;
    padding: var(--spacing-md) var(--spacing-lg) !important;
}

/* Success alert */
div[data-testid="stAlert"][data-baseweb-alert-kind="success"],
.stSuccess {
    background-color: rgba(91, 140, 90, 0.1) !important;
    border-left-color: var(--color-success) !important;
}

/* Warning alert */
div[data-testid="stAlert"][data-baseweb-alert-kind="warning"],
.stWarning {
    background-color: rgba(212, 168, 75, 0.1) !important;
    border-left-color: var(--color-warning) !important;
}

/* Error alert */
div[data-testid="stAlert"][data-baseweb-alert-kind="error"],
.stError {
    background-color: rgba(198, 93, 59, 0.1) !important;
    border-left-color: var(--color-primary) !important;
}

/* Info alert */
div[data-testid="stAlert"][data-baseweb-alert-kind="info"],
.stInfo {
    background-color: rgba(139, 115, 85, 0.1) !important;
    border-left-color: var(--color-secondary) !important;
}

/* ==========================================================================
   PROGRESS BAR
   ========================================================================== */
div[data-testid="stProgress"] > div {
    background-color: var(--color-light-gray) !important;
    border-radius: var(--radius-full) !important;
    overflow: hidden !important;
}

div[data-testid="stProgress"] > div > div {
    background: linear-gradient(90deg, var(--color-primary) 0%, var(--color-primary-light) 100%) !important;
    border-radius: var(--radius-full) !important;
}

/* ==========================================================================
   DIVIDER
   ========================================================================== */
hr {
    border: none !important;
    height: 1px !important;
    background: linear-gradient(90deg, transparent, var(--color-light-gray), transparent) !important;
    margin: var(--spacing-xl) 0 !important;
}

/* Decorative divider */
.divider-decorative {
    display: flex;
    align-items: center;
    margin: var(--spacing-xl) 0;
}

.divider-decorative::before,
.divider-decorative::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--color-light-gray);
}

.divider-decorative span {
    padding: 0 var(--spacing-md);
    font-family: var(--font-heading);
    color: var(--color-secondary);
    font-size: 0.875rem;
}

/* ==========================================================================
   CHECKBOX & RADIO STYLING
   ========================================================================== */
div[data-testid="stCheckbox"] label span {
    font-family: var(--font-body) !important;
    color: var(--color-text) !important;
}

div[data-testid="stCheckbox"] label span[data-baseweb="checkbox"] {
    border-color: var(--color-secondary) !important;
    border-radius: var(--radius-sm) !important;
}

div[data-testid="stCheckbox"] label span[data-baseweb="checkbox"]:checked,
div[data-testid="stCheckbox"] label span[data-baseweb="checkbox"][aria-checked="true"] {
    background-color: var(--color-primary) !important;
    border-color: var(--color-primary) !important;
}

/* ==========================================================================
   FILE UPLOADER
   ========================================================================== */
div[data-testid="stFileUploader"] {
    border: 2px dashed var(--color-light-gray) !important;
    border-radius: var(--radius-lg) !important;
    background-color: rgba(253, 251, 247, 0.5) !important;
    transition: all var(--transition-fast) !important;
}

div[data-testid="stFileUploader"]:hover {
    border-color: var(--color-primary) !important;
    background-color: rgba(198, 93, 59, 0.02) !important;
}

div[data-testid="stFileUploader"] label {
    font-family: var(--font-body) !important;
    color: var(--color-text-muted) !important;
}

/* ==========================================================================
   SPINNER / LOADING
   ========================================================================== */
div[data-testid="stSpinner"] > div {
    border-top-color: var(--color-primary) !important;
}

/* ==========================================================================
   UTILITY CLASSES
   ========================================================================== */
.text-primary { color: var(--color-primary) !important; }
.text-secondary { color: var(--color-secondary) !important; }
.text-success { color: var(--color-success) !important; }
.text-warning { color: var(--color-warning) !important; }
.text-muted { color: var(--color-text-muted) !important; }

.bg-primary { background-color: var(--color-primary) !important; }
.bg-secondary { background-color: var(--color-secondary) !important; }
.bg-card { background-color: var(--color-card-bg) !important; }
.bg-light { background-color: var(--color-light-gray) !important; }

.shadow-sm { box-shadow: var(--shadow-sm) !important; }
.shadow-md { box-shadow: var(--shadow-md) !important; }
.shadow-lg { box-shadow: var(--shadow-lg) !important; }

.rounded-sm { border-radius: var(--radius-sm) !important; }
.rounded-md { border-radius: var(--radius-md) !important; }
.rounded-lg { border-radius: var(--radius-lg) !important; }
.rounded-full { border-radius: var(--radius-full) !important; }

.font-heading { font-family: var(--font-heading) !important; }
.font-body { font-family: var(--font-body) !important; }

.text-center { text-align: center !important; }
.text-left { text-align: left !important; }
.text-right { text-align: right !important; }

/* Spacing utilities */
.mt-sm { margin-top: var(--spacing-sm) !important; }
.mt-md { margin-top: var(--spacing-md) !important; }
.mt-lg { margin-top: var(--spacing-lg) !important; }
.mt-xl { margin-top: var(--spacing-xl) !important; }

.mb-sm { margin-bottom: var(--spacing-sm) !important; }
.mb-md { margin-bottom: var(--spacing-md) !important; }
.mb-lg { margin-bottom: var(--spacing-lg) !important; }
.mb-xl { margin-bottom: var(--spacing-xl) !important; }

.p-sm { padding: var(--spacing-sm) !important; }
.p-md { padding: var(--spacing-md) !important; }
.p-lg { padding: var(--spacing-lg) !important; }
.p-xl { padding: var(--spacing-xl) !important; }

/* ==========================================================================
   RESPONSIVE ADJUSTMENTS
   ========================================================================== */
@media (max-width: 768px) {
    .main .block-container {
        padding: var(--spacing-md) var(--spacing-lg) !important;
    }

    h1, .stMarkdown h1 {
        font-size: 2rem !important;
    }

    h2, .stMarkdown h2 {
        font-size: 1.5rem !important;
    }

    div[data-testid="stMetric"] div[data-testid="stMetricValue"] {
        font-size: 1.75rem !important;
    }

    .metric-value {
        font-size: 1.75rem;
    }

    .hero-header {
        padding: var(--spacing-xl) var(--spacing-lg);
    }

    .hero-header h1 {
        font-size: 2.25rem !important;
    }
}

/* ==========================================================================
   PRINT STYLES
   ========================================================================== */
@media print {
    .stButton,
    section[data-testid="stSidebar"],
    div[data-testid="stToolbar"] {
        display: none !important;
    }

    .main .block-container {
        max-width: 100% !important;
        padding: 0 !important;
    }

    .card-item:hover {
        transform: none !important;
        box-shadow: var(--shadow-sm) !important;
    }
}
"""


# Example usage in Streamlit app:
#
# import streamlit as st
# from dashboard_styles import CSS_STYLES
#
# st.set_page_config(
#     page_title="Greeting Card Analytics",
#     page_icon="📊",
#     layout="wide"
# )
#
# # Inject CSS styles
# st.markdown(f"<style>{CSS_STYLES}</style>", unsafe_allow_html=True)
#
# # Hero header example
# st.markdown('''
# <div class="hero-header">
#     <h1>Greeting Card Analytics</h1>
#     <p class="subtitle">Insights into card performance and trends</p>
# </div>
# ''', unsafe_allow_html=True)
#
# # Card grid example
# st.markdown('''
# <div class="card-grid">
#     <div class="card-item">
#         <div class="card-image-container">
#             <span class="rank-badge">1</span>
#             <span class="occasion-tag birthday">Birthday</span>
#             <img class="card-image" src="image.jpg" alt="Card">
#         </div>
#         <div class="card-content">
#             <h3 class="card-title">Birthday Celebration</h3>
#             <p class="card-description">A cheerful card for birthday wishes.</p>
#             <div class="card-meta">
#                 <span>1,234 sales</span>
#                 <span>4.8 rating</span>
#             </div>
#         </div>
#     </div>
# </div>
# ''', unsafe_allow_html=True)
