#!/usr/bin/env python3
"""
This script loads pre-created visualizations of the Iris dataset from JSON files
and generates HTML files for easy sharing.
"""

import os
import json
import plotly.graph_objects as go

# Create output directories if they don't exist
os.makedirs('visualizations', exist_ok=True)

print("Loading pre-created figures from JSON files...")

# Load figures from JSON files
try:
    with open('figure_data/scatter_plot.json', 'r') as f:
        fig1 = go.Figure(json.load(f))
    print("Loaded scatter plot.")
    
    with open('figure_data/scatter_3d_plot.json', 'r') as f:
        fig2 = go.Figure(json.load(f))
    print("Loaded 3D scatter plot.")
    
    with open('figure_data/pair_plot.json', 'r') as f:
        fig3 = go.Figure(json.load(f))
    print("Loaded pair plot.")
    
    with open('figure_data/parallel_plot.json', 'r') as f:
        fig4 = go.Figure(json.load(f))
    print("Loaded parallel coordinates plot.")
except FileNotFoundError as e:
    print(f"ERROR: {e}")
    print("Please run the Jupyter notebook first to create the figure files.")
    exit(1)

# Create a basic HTML template for the visualizations
html_template = """<!DOCTYPE html>
<html data-bs-theme="light">
<head>
    <meta charset="utf-8">
    <title>Iris Dataset Interactive Visualizations</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.0/font/bootstrap-icons.css">
    <style>
        :root {
            --text-color: #333;
            --bg-color: #f8f9fa;
            --card-bg-color: white;
            --heading-color: #2c3e50;
            --subheading-color: #3498db;
            --border-color: #eee;
            --plot-bg-color: white;
            --shadow-color: rgba(0,0,0,0.1);
            --nav-bg-color: #f8f9fa;
        }
        
        [data-bs-theme="dark"] {
            --text-color: #e1e1e1;
            --bg-color: #121212;
            --card-bg-color: #1e1e1e;
            --heading-color: #58a6ff;
            --subheading-color: #88c0fc;
            --border-color: #333;
            --plot-bg-color: #1e1e1e;
            --shadow-color: rgba(255,255,255,0.05);
            --nav-bg-color: #1e1e1e;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            margin: 0;
            padding: 0;
            background-color: var(--bg-color);
            transition: background-color 0.3s ease, color 0.3s ease;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: var(--card-bg-color);
            box-shadow: 0 0 10px var(--shadow-color);
            border-radius: 5px;
            transition: background-color 0.3s ease, box-shadow 0.3s ease;
        }
        
        h1 {
            color: var(--heading-color);
            margin-top: 20px;
            margin-bottom: 20px;
            text-align: center;
            transition: color 0.3s ease;
        }
        
        h2 {
            color: var(--subheading-color);
            margin-top: 30px;
            margin-bottom: 15px;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 10px;
            transition: color 0.3s ease, border-color 0.3s ease;
        }
        
        .plotly-graph {
            width: 100%;
            height: 600px;
            margin-bottom: 30px;
        }
        
        .plot-container {
            background-color: var(--plot-bg-color);
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 5px var(--shadow-color);
            margin-bottom: 30px;
            transition: background-color 0.3s ease, box-shadow 0.3s ease;
        }
        
        .description {
            margin-bottom: 20px;
        }
        
        .nav-link {
            color: var(--subheading-color);
            transition: color 0.3s ease;
        }
        
        .nav-link.active {
            font-weight: bold;
            color: var(--heading-color);
        }
        
        .navbar {
            background-color: var(--nav-bg-color) !important;
            transition: background-color 0.3s ease;
        }
        
        .theme-toggle {
            cursor: pointer;
            padding: 5px 10px;
            border-radius: 5px;
            display: inline-flex;
            align-items: center;
            margin-left: auto;
        }
        
        .theme-toggle i {
            font-size: 1.2rem;
            margin-right: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="d-flex justify-content-between align-items-center mb-3">
            <h1>Interactive Iris Dataset Visualizations</h1>
            <button class="btn btn-outline-secondary theme-toggle" id="theme-toggle">
                <i class="bi bi-moon-stars-fill" id="theme-icon"></i>
                <span id="theme-text">Dark Mode</span>
            </button>
        </div>
        
        <nav class="navbar navbar-expand-lg navbar-light">
            <div class="container-fluid">
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <a class="nav-link active" href="#scatter">Scatter Plot</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#3d-scatter">3D Scatter</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#pair-plot">Pair Plot</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#parallel">Parallel Coordinates</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
        
        <section id="introduction">
            <h2>Introduction</h2>
            <p class="description">
                The Iris dataset is a classic dataset in machine learning and statistics. It contains 
                measurements for 150 iris flowers from three different species: Setosa, Versicolor, and Virginica.
                Each species has 50 samples, and four features were measured from each sample: 
                sepal length, sepal width, petal length, and petal width (all in centimeters).
            </p>
            <p class="description">
                This page demonstrates interactive visualizations of the Iris dataset using Plotly.
                The visualizations were created in a Jupyter notebook and then integrated into this HTML report.
                Interact with the plots by hovering over data points, zooming, panning, and more!
            </p>
        </section>

        <section id="scatter">
            <h2>Interactive Scatter Plot</h2>
            <p class="description">
                This scatter plot shows the relationship between sepal length and sepal width for each species.
                The size of each point represents petal length, and the colors indicate the species.
            </p>
            <div class="plot-container">
                <div id="scatter-plot" class="plotly-graph"></div>
            </div>
        </section>
        
        <section id="3d-scatter">
            <h2>3D Scatter Plot</h2>
            <p class="description">
                This 3D scatter plot visualizes the relationship between sepal length, sepal width, and petal length.
                The colors represent different species, and you can rotate the plot to view it from different angles.
            </p>
            <div class="plot-container">
                <div id="scatter-3d-plot" class="plotly-graph"></div>
            </div>
        </section>
        
        <section id="pair-plot">
            <h2>Pair Plot</h2>
            <p class="description">
                This matrix of scatter plots shows the pairwise relationships between all four features,
                with colors indicating the species. This allows us to see patterns and correlations between variables.
            </p>
            <div class="plot-container">
                <div id="pair-plot" class="plotly-graph"></div>
            </div>
        </section>
        
        <section id="parallel">
            <h2>Parallel Coordinates Plot</h2>
            <p class="description">
                Parallel coordinates plots are ideal for visualizing multivariate data. Each vertical line represents 
                a feature, and each colored line represents a sample, connecting its values across all features.
                This helps identify patterns and clusters across multiple dimensions.
            </p>
            <div class="plot-container">
                <div id="parallel-plot" class="plotly-graph"></div>
            </div>
        </section>
        
        <footer class="text-center mt-5 mb-3 text-muted">
            <p>Created with Python, Plotly, and the Iris dataset</p>
        </footer>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    
    <script>
        // Theme toggling functionality
        document.addEventListener('DOMContentLoaded', function() {
            const themeToggle = document.getElementById('theme-toggle');
            const themeIcon = document.getElementById('theme-icon');
            const themeText = document.getElementById('theme-text');
            const htmlElement = document.documentElement;
            
            // Check for saved theme preference or use prefer-color-scheme
            const savedTheme = localStorage.getItem('theme');
            const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');
            
            if (savedTheme) {
                htmlElement.setAttribute('data-bs-theme', savedTheme);
                updateToggleUI(savedTheme);
            } else if (prefersDarkScheme.matches) {
                htmlElement.setAttribute('data-bs-theme', 'dark');
                updateToggleUI('dark');
            }
            
            // Theme toggle click handler
            themeToggle.addEventListener('click', function() {
                const currentTheme = htmlElement.getAttribute('data-bs-theme');
                const newTheme = currentTheme === 'light' ? 'dark' : 'light';
                
                htmlElement.setAttribute('data-bs-theme', newTheme);
                localStorage.setItem('theme', newTheme);
                
                updateToggleUI(newTheme);
                
                // Refresh the iframes to apply the theme changes
                const iframes = document.querySelectorAll('iframe');
                iframes.forEach(iframe => {
                    iframe.src = iframe.src;
                });
            });
            
            function updateToggleUI(theme) {
                if (theme === 'dark') {
                    themeIcon.className = 'bi bi-sun-fill';
                    themeText.textContent = 'Light Mode';
                } else {
                    themeIcon.className = 'bi bi-moon-stars-fill';
                    themeText.textContent = 'Dark Mode';
                }
            }
        });
    </script>
</body>
</html>
"""

# Apply dark theme to the figures
print("\nApplying theme templates to figures...")

# Create dark and light templates
dark_template = dict(
    layout=dict(
        paper_bgcolor='#1e1e1e',
        plot_bgcolor='#1e1e1e',
        font=dict(color='#e1e1e1'),
        title=dict(font=dict(color='#58a6ff')),
        xaxis=dict(gridcolor='#333', zerolinecolor='#333'),
        yaxis=dict(gridcolor='#333', zerolinecolor='#333'),
        legend=dict(font=dict(color='#e1e1e1'))
    )
)

# Update figure templates to have dark mode support
for fig in [fig1, fig2, fig3, fig4]:
    # We don't change the default template but ensure figures work with both themes
    fig.update_layout(
        template=dict(
            data=fig.layout.template.data,
            layout=fig.layout.template.layout
        )
    )

# Save individual plots to HTML files
print("\nSaving individual HTML files...")
fig1.write_html("visualizations/scatter_plot.html")
fig2.write_html("visualizations/scatter_3d_plot.html")
fig3.write_html("visualizations/pair_plot.html")
fig4.write_html("visualizations/parallel_plot.html")

# Combine all plots into a single HTML file using iframes
print("\nCombining plots into a single HTML file using iframes...")

# Start with the template
html_template_modified = html_template

# Replace the plot div placeholders with iframes pointing to the individual HTML files
html_template_modified = html_template_modified.replace(
    "<div id=\"scatter-plot\" class=\"plotly-graph\"></div>", 
    "<iframe src=\"scatter_plot.html\" class=\"plotly-graph\" style=\"border:none;\"></iframe>"
)
html_template_modified = html_template_modified.replace(
    "<div id=\"scatter-3d-plot\" class=\"plotly-graph\"></div>", 
    "<iframe src=\"scatter_3d_plot.html\" class=\"plotly-graph\" style=\"border:none;\"></iframe>"
)
html_template_modified = html_template_modified.replace(
    "<div id=\"pair-plot\" class=\"plotly-graph\"></div>", 
    "<iframe src=\"pair_plot.html\" class=\"plotly-graph\" style=\"border:none;\"></iframe>"
)
html_template_modified = html_template_modified.replace(
    "<div id=\"parallel-plot\" class=\"plotly-graph\"></div>", 
    "<iframe src=\"parallel_plot.html\" class=\"plotly-graph\" style=\"border:none;\"></iframe>"
)

# Write the final HTML file
with open("visualizations/iris_interactive_dashboard.html", "w") as f:
    f.write(html_template_modified)

print("\nAll done! HTML report generated successfully with dark mode support.")
print("Open the following files in your browser to view them:")
print("  - visualizations/iris_interactive_dashboard.html (all visualizations)")
print("  - visualizations/scatter_plot.html")
print("  - visualizations/scatter_3d_plot.html")
print("  - visualizations/pair_plot.html")
print("  - visualizations/parallel_plot.html") 