#!/bin/bash

# Greeting Card Analytics Dashboard Launcher
# Double-click this file to start the dashboard

cd "$(dirname "$0")"

echo "Starting Greeting Card Analytics Dashboard..."
echo ""

# Check if streamlit is installed
if ! command -v streamlit &> /dev/null; then
    echo "Streamlit not found. Installing dependencies..."
    pip3 install -r requirements.txt
fi

# Launch the dashboard
streamlit run app.py
