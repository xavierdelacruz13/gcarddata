"""
Plotly Chart Configurations for Greeting Card Analytics Dashboard
Editorial/Magazine Aesthetic with Terracotta Color Palette
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from typing import Optional, List, Dict, Any


# =============================================================================
# COLOR PALETTE
# =============================================================================

COLORS = {
    'primary': '#C65D3B',        # Terracotta
    'secondary': '#8B7355',      # Warm brown
    'text': '#2D2A26',           # Dark charcoal
    'grid': '#E8E4DE',           # Light warm gray
    'background': 'rgba(0,0,0,0)',  # Transparent
}

ACCENT_PALETTE = [
    '#C65D3B',  # Terracotta
    '#D4A84B',  # Golden ochre
    '#5B8C5A',  # Sage green
    '#6B8E9B',  # Dusty blue
    '#9B6B8E',  # Mauve
    '#8E9B6B',  # Olive
    '#6B9B8E',  # Teal
    '#9B8E6B',  # Tan
]


# =============================================================================
# BASE LAYOUT CONFIGURATION
# =============================================================================

def get_base_layout(
    title: str = '',
    height: int = 400,
    showlegend: bool = False,
    legend_position: str = 'right'
) -> Dict[str, Any]:
    """
    Returns the base layout configuration for all charts.
    Establishes consistent editorial/magazine aesthetic.
    """
    layout = {
        'paper_bgcolor': COLORS['background'],
        'plot_bgcolor': COLORS['background'],
        'font': {
            'family': 'Source Sans 3, sans-serif',
            'color': COLORS['text'],
            'size': 12,
        },
        'title': {
            'text': title,
            'font': {
                'family': 'Source Sans 3, sans-serif',
                'size': 18,
                'color': COLORS['text'],
                'weight': 600,
            },
            'x': 0,
            'xanchor': 'left',
            'y': 0.98,
            'yanchor': 'top',
        },
        'margin': dict(l=20, r=20, t=40, b=20),
        'height': height,
        'hovermode': 'closest',
        'showlegend': showlegend,
    }

    if showlegend:
        if legend_position == 'right':
            layout['legend'] = {
                'orientation': 'v',
                'yanchor': 'middle',
                'y': 0.5,
                'xanchor': 'left',
                'x': 1.02,
                'bgcolor': 'rgba(0,0,0,0)',
                'font': {
                    'family': 'Source Sans 3, sans-serif',
                    'size': 11,
                    'color': COLORS['text'],
                },
            }
        elif legend_position == 'bottom':
            layout['legend'] = {
                'orientation': 'h',
                'yanchor': 'top',
                'y': -0.1,
                'xanchor': 'center',
                'x': 0.5,
                'bgcolor': 'rgba(0,0,0,0)',
                'font': {
                    'family': 'Source Sans 3, sans-serif',
                    'size': 11,
                    'color': COLORS['text'],
                },
            }

    return layout


def get_config() -> Dict[str, Any]:
    """
    Returns the Plotly config object with logo disabled.
    """
    return {
        'displaylogo': False,
        'modeBarButtonsToRemove': ['lasso2d', 'select2d'],
        'responsive': True,
    }


# =============================================================================
# CHART 1: TOP PERFORMERS HORIZONTAL BAR CHART
# =============================================================================

def create_top_performers_chart(
    df: pd.DataFrame,
    name_col: str = 'card_name',
    value_col: str = 'sends',
    top_n: int = 10,
    title: str = 'Top Performing Cards'
) -> go.Figure:
    """
    Creates a horizontal bar chart showing top performing cards by sends.

    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame containing card data
    name_col : str
        Column name for card names
    value_col : str
        Column name for the metric (sends)
    top_n : int
        Number of top cards to display (default: 10)
    title : str
        Chart title

    Returns:
    --------
    go.Figure
        Styled Plotly figure
    """
    # Prepare data - get top N performers
    df_sorted = df.nlargest(top_n, value_col).sort_values(value_col, ascending=True)

    # Create gradient colors from warm brown to terracotta
    n_bars = len(df_sorted)
    gradient_colors = []
    for i in range(n_bars):
        # Interpolate between secondary (warm brown) and primary (terracotta)
        ratio = i / (n_bars - 1) if n_bars > 1 else 1
        # Simple color interpolation for gradient effect
        gradient_colors.append(
            f'rgba({int(139 + (198-139)*ratio)}, {int(115 + (93-115)*ratio)}, {int(85 + (59-85)*ratio)}, 1)'
        )

    # Truncate long names for display
    display_names = df_sorted[name_col].apply(
        lambda x: x[:30] + '...' if len(str(x)) > 30 else x
    )

    # Create the bar trace
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=df_sorted[value_col],
        y=display_names,
        orientation='h',
        marker=dict(
            color=gradient_colors,
            line=dict(width=0),
        ),
        text=df_sorted[value_col].apply(lambda x: f'{x:,.0f}'),
        textposition='outside',
        textfont=dict(
            family='Source Sans 3, sans-serif',
            size=11,
            color=COLORS['text'],
        ),
        hovertemplate=(
            '<b>%{customdata}</b><br>'
            'Sends: %{x:,.0f}<extra></extra>'
        ),
        customdata=df_sorted[name_col],  # Full name for hover
    ))

    # Apply base layout
    layout = get_base_layout(title=title, height=400, showlegend=False)

    # Customize axes for horizontal bar chart
    layout.update({
        'xaxis': {
            'showgrid': False,
            'showline': False,
            'showticklabels': False,
            'zeroline': False,
        },
        'yaxis': {
            'showgrid': False,
            'showline': False,
            'tickfont': {
                'family': 'Source Sans 3, sans-serif',
                'size': 12,
                'color': COLORS['text'],
            },
            'automargin': True,
        },
        'margin': dict(l=20, r=80, t=50, b=20),
    })

    fig.update_layout(**layout)

    return fig


# =============================================================================
# CHART 2: CATEGORY DONUT CHART
# =============================================================================

def create_category_donut(
    df: pd.DataFrame,
    category_col: str = 'occasion',
    value_col: str = 'sends',
    title: str = 'Distribution by Occasion'
) -> go.Figure:
    """
    Creates a donut chart showing occasion/category distribution by sends.

    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame containing card data
    category_col : str
        Column name for categories/occasions
    value_col : str
        Column name for the metric (sends)
    title : str
        Chart title

    Returns:
    --------
    go.Figure
        Styled Plotly figure
    """
    # Aggregate by category
    category_totals = df.groupby(category_col)[value_col].sum().reset_index()
    category_totals = category_totals.sort_values(value_col, ascending=False)

    # Calculate percentages
    total = category_totals[value_col].sum()
    category_totals['percentage'] = (category_totals[value_col] / total * 100).round(1)

    # Assign colors from accent palette (cycle if more categories than colors)
    n_categories = len(category_totals)
    colors = [ACCENT_PALETTE[i % len(ACCENT_PALETTE)] for i in range(n_categories)]

    fig = go.Figure()

    fig.add_trace(go.Pie(
        labels=category_totals[category_col],
        values=category_totals[value_col],
        hole=0.45,
        marker=dict(
            colors=colors,
            line=dict(color='white', width=2),
        ),
        textinfo='percent',
        textposition='outside',
        textfont=dict(
            family='Source Sans 3, sans-serif',
            size=11,
            color=COLORS['text'],
        ),
        hovertemplate=(
            '<b>%{label}</b><br>'
            'Sends: %{value:,.0f}<br>'
            'Share: %{percent}<extra></extra>'
        ),
        rotation=90,
    ))

    # Apply base layout with legend on right
    layout = get_base_layout(
        title=title,
        height=400,
        showlegend=True,
        legend_position='right'
    )

    layout.update({
        'margin': dict(l=20, r=120, t=50, b=20),
    })

    fig.update_layout(**layout)

    return fig


# =============================================================================
# CHART 3: TREND SPARKLINES
# =============================================================================

def create_trend_sparkline(
    values: List[float],
    positive_color: str = COLORS['primary'],
    negative_color: str = '#888888',
    height: int = 40,
    width: int = 120,
) -> go.Figure:
    """
    Creates a minimal sparkline for showing trends inline.

    Parameters:
    -----------
    values : List[float]
        Time series values to plot
    positive_color : str
        Color for positive trend (default: terracotta)
    negative_color : str
        Color for negative/neutral trend
    height : int
        Chart height in pixels
    width : int
        Chart width in pixels

    Returns:
    --------
    go.Figure
        Minimal sparkline figure
    """
    if len(values) < 2:
        values = [0, 0]

    # Determine trend direction
    trend = values[-1] - values[0]
    line_color = positive_color if trend >= 0 else negative_color

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        y=values,
        x=list(range(len(values))),
        mode='lines',
        line=dict(
            color=line_color,
            width=2,
            shape='spline',
            smoothing=0.8,
        ),
        fill='tozeroy',
        fillcolor=f'{line_color}20',  # 20% opacity
        hoverinfo='skip',
    ))

    # Add endpoint marker
    fig.add_trace(go.Scatter(
        y=[values[-1]],
        x=[len(values) - 1],
        mode='markers',
        marker=dict(
            color=line_color,
            size=6,
        ),
        hoverinfo='skip',
    ))

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=height,
        width=width,
        margin=dict(l=0, r=0, t=0, b=0),
        showlegend=False,
        xaxis=dict(
            visible=False,
            showgrid=False,
            zeroline=False,
        ),
        yaxis=dict(
            visible=False,
            showgrid=False,
            zeroline=False,
        ),
    )

    return fig


def create_trend_indicator(
    current_value: float,
    previous_value: float,
    label: str = '',
    height: int = 80,
    width: int = 150,
) -> go.Figure:
    """
    Creates a trend indicator with value and change percentage.

    Parameters:
    -----------
    current_value : float
        Current period value
    previous_value : float
        Previous period value for comparison
    label : str
        Metric label
    height : int
        Chart height in pixels
    width : int
        Chart width in pixels

    Returns:
    --------
    go.Figure
        Trend indicator figure
    """
    # Calculate change
    if previous_value != 0:
        change_pct = ((current_value - previous_value) / previous_value) * 100
    else:
        change_pct = 0

    is_positive = change_pct >= 0
    trend_color = COLORS['primary'] if is_positive else '#888888'
    arrow = '↑' if is_positive else '↓'

    fig = go.Figure()

    # Add invisible trace for layout
    fig.add_trace(go.Scatter(
        x=[0], y=[0],
        mode='markers',
        marker=dict(size=0, opacity=0),
        hoverinfo='skip',
    ))

    # Add annotations for the indicator
    fig.add_annotation(
        x=0.5, y=0.7,
        xref='paper', yref='paper',
        text=f'{current_value:,.0f}',
        showarrow=False,
        font=dict(
            family='Source Sans 3, sans-serif',
            size=24,
            color=COLORS['text'],
            weight=600,
        ),
    )

    fig.add_annotation(
        x=0.5, y=0.25,
        xref='paper', yref='paper',
        text=f'{arrow} {abs(change_pct):.1f}%',
        showarrow=False,
        font=dict(
            family='Source Sans 3, sans-serif',
            size=14,
            color=trend_color,
        ),
    )

    if label:
        fig.add_annotation(
            x=0.5, y=0.95,
            xref='paper', yref='paper',
            text=label,
            showarrow=False,
            font=dict(
                family='Source Sans 3, sans-serif',
                size=11,
                color=COLORS['secondary'],
            ),
        )

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=height,
        width=width,
        margin=dict(l=0, r=0, t=0, b=0),
        showlegend=False,
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
    )

    return fig


# =============================================================================
# ADDITIONAL UTILITY CHARTS
# =============================================================================

def create_time_series_chart(
    df: pd.DataFrame,
    date_col: str = 'date',
    value_col: str = 'sends',
    title: str = 'Sends Over Time',
    height: int = 300,
) -> go.Figure:
    """
    Creates a clean area/line chart for time series data.

    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame with time series data
    date_col : str
        Column name for dates
    value_col : str
        Column name for values
    title : str
        Chart title
    height : int
        Chart height in pixels

    Returns:
    --------
    go.Figure
        Styled time series figure
    """
    df_sorted = df.sort_values(date_col)

    fig = go.Figure()

    # Area fill
    fig.add_trace(go.Scatter(
        x=df_sorted[date_col],
        y=df_sorted[value_col],
        mode='lines',
        line=dict(
            color=COLORS['primary'],
            width=2,
            shape='spline',
            smoothing=0.3,
        ),
        fill='tozeroy',
        fillcolor='rgba(198, 93, 59, 0.15)',
        hovertemplate='%{x|%b %d, %Y}<br>Sends: %{y:,.0f}<extra></extra>',
    ))

    layout = get_base_layout(title=title, height=height, showlegend=False)

    layout.update({
        'xaxis': {
            'showgrid': False,
            'showline': True,
            'linecolor': COLORS['grid'],
            'tickfont': {
                'family': 'Source Sans 3, sans-serif',
                'size': 10,
                'color': COLORS['secondary'],
            },
        },
        'yaxis': {
            'showgrid': True,
            'gridcolor': COLORS['grid'],
            'gridwidth': 1,
            'showline': False,
            'tickfont': {
                'family': 'Source Sans 3, sans-serif',
                'size': 10,
                'color': COLORS['secondary'],
            },
            'tickformat': ',.0f',
        },
        'margin': dict(l=50, r=20, t=50, b=40),
    })

    fig.update_layout(**layout)

    return fig


def create_comparison_bars(
    df: pd.DataFrame,
    category_col: str = 'category',
    current_col: str = 'current',
    previous_col: str = 'previous',
    title: str = 'Period Comparison',
    height: int = 350,
) -> go.Figure:
    """
    Creates a grouped bar chart comparing two periods.

    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame with comparison data
    category_col : str
        Column name for categories
    current_col : str
        Column name for current period values
    previous_col : str
        Column name for previous period values
    title : str
        Chart title
    height : int
        Chart height in pixels

    Returns:
    --------
    go.Figure
        Styled comparison bar chart
    """
    fig = go.Figure()

    # Previous period bars
    fig.add_trace(go.Bar(
        name='Previous',
        x=df[category_col],
        y=df[previous_col],
        marker_color=COLORS['grid'],
        hovertemplate='%{x}<br>Previous: %{y:,.0f}<extra></extra>',
    ))

    # Current period bars
    fig.add_trace(go.Bar(
        name='Current',
        x=df[category_col],
        y=df[current_col],
        marker_color=COLORS['primary'],
        hovertemplate='%{x}<br>Current: %{y:,.0f}<extra></extra>',
    ))

    layout = get_base_layout(
        title=title,
        height=height,
        showlegend=True,
        legend_position='bottom'
    )

    layout.update({
        'barmode': 'group',
        'bargap': 0.3,
        'bargroupgap': 0.1,
        'xaxis': {
            'showgrid': False,
            'showline': False,
            'tickfont': {
                'family': 'Source Sans 3, sans-serif',
                'size': 11,
                'color': COLORS['text'],
            },
        },
        'yaxis': {
            'showgrid': True,
            'gridcolor': COLORS['grid'],
            'showline': False,
            'tickfont': {
                'family': 'Source Sans 3, sans-serif',
                'size': 10,
                'color': COLORS['secondary'],
            },
            'tickformat': ',.0f',
        },
        'margin': dict(l=50, r=20, t=50, b=60),
    })

    fig.update_layout(**layout)

    return fig


# =============================================================================
# EXAMPLE USAGE / DEMO
# =============================================================================

if __name__ == '__main__':
    import numpy as np

    # Create sample data for demonstration
    np.random.seed(42)

    # Sample card data
    sample_cards = pd.DataFrame({
        'card_name': [
            'Happy Birthday Celebration',
            'Thank You Floral Design',
            'Congratulations Graduate',
            'Get Well Soon Sunshine',
            'Wedding Wishes Elegant',
            'New Baby Boy Blue',
            'Anniversary Love Hearts',
            'Holiday Greetings Winter',
            'Sympathy White Lilies',
            'Just Because Thinking of You',
            'Mother\'s Day Roses',
            'Father\'s Day Classic',
        ],
        'occasion': [
            'Birthday', 'Thank You', 'Congratulations', 'Get Well',
            'Wedding', 'Baby', 'Anniversary', 'Holiday',
            'Sympathy', 'Just Because', 'Mother\'s Day', 'Father\'s Day',
        ],
        'sends': np.random.randint(1000, 50000, 12),
    })

    # Generate charts
    print("Creating Top Performers Chart...")
    top_chart = create_top_performers_chart(sample_cards)

    print("Creating Category Donut Chart...")
    donut_chart = create_category_donut(sample_cards)

    print("Creating Trend Sparkline...")
    sparkline = create_trend_sparkline([10, 15, 12, 18, 22, 20, 25])

    print("Creating Trend Indicator...")
    indicator = create_trend_indicator(15420, 12350, label='Total Sends')

    # Sample time series data
    dates = pd.date_range(start='2024-01-01', periods=30, freq='D')
    time_series_df = pd.DataFrame({
        'date': dates,
        'sends': np.random.randint(500, 2000, 30).cumsum() // 30,
    })

    print("Creating Time Series Chart...")
    time_chart = create_time_series_chart(time_series_df)

    print("\nAll charts created successfully!")
    print(f"Color Palette: {COLORS}")
    print(f"Accent Colors: {ACCENT_PALETTE}")

    # Optionally show charts (uncomment to display)
    # top_chart.show(config=get_config())
    # donut_chart.show(config=get_config())
