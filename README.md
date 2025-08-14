# Blinkit Analysis Python Project
Overview

A Python-based exploratory data analysis project focused on Blinkit sales data. This repository includes data cleaning, KPI computation, and visualization scripts to uncover insights such as sales distribution by item attributes, outlet sizes and locations, and store establishment year.

Table of Contents

Repository Structure

Getting Started

Requirements

Installation

Usage

Project Breakdown

Results & Visualizations

Contributing

License

Repository Structure
blinkit_analysis_python_project/
├── charts/                     # Exported visualizations (images)
├── code/                       # Python scripts for data processing and plotting
├── dataset/                    # Source data files (e.g., blinkit_data.csv)
├── Blinkit Sales Data Summary.docx  # Analysis report (Word format)
├── LICENSE                     # MIT license
└── README.md                   # Project overview and instructions

Getting Started
Requirements

Python 3.x

Libraries:

pandas

numpy

matplotlib

seaborn

reportlab (optional, for PDF generation)

Installation

You can install the required libraries via pip:

pip install pandas numpy matplotlib seaborn reportlab

Usage

Place your data into the dataset/ directory (e.g., blinkit_data.csv).

Run the analysis script, located in code/ (e.g., analysis.py):

python code/analysis.py


Outputs generated:

Charts in the charts/ folder (e.g., pie charts, bar charts, line plots).

Summary report in .docx format (Blinkit Sales Data Summary.docx), and optionally a PDF if configured in the script.

Project Breakdown

Data Cleaning

Standardizing categorical values (e.g., mapping 'LF', 'low fat', and 'reg' to normalized labels such as 'Low Fat' and 'Regular').

Key Performance Indicators (KPIs)

Total Sales: Overall revenue sum.

Average Sales: Mean sales per item.

Items Sold: Record count.

Average Rating: Mean product rating.

Visual Analytics

Sales by Fat Content (pie chart)

Sales by Item Type (bar chart)

Sales by Outlet Location & Fat Content (grouped bar chart)

Sales by Establishment Year (line chart)

Sales by Outlet Size (pie chart)

Sales by Outlet Location Type (horizontal bar chart)

Results & Visualizations

Visual Summary: The charts/ folder contains all plots illustrating key insights:

Dominance of Regular vs Low-Fat items in revenue share.

Top-selling item categories (e.g., Fruits & Vegetables, Snack Foods, Household).

Sales breakdown by outlet tier, size, and establishment year.

Narrative Insights (from the accompanying .docx report):

Regular-fat products account for the largest share of sales.

Medium-sized outlets in Tier 3 locations generate the highest revenue.

Sales performance doesn't always align with outlet age—older and newer stores can both perform strongly depending on other factors.

License

Distributed under the MIT License. See LICENSE for details.
