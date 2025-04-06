# Dataset Interactive Visualizations

This project demonstrates how to create interactive visualizations using Plotly, and how to generate a HTML dashboard.

## Features

- Interactive Plotly visualizations of the Iris dataset
- Multiple visualization types:
  - Scatter plots
  - 3D scatter plots
  - Pair plots (scatter matrix)
  - Parallel coordinates plots
- Responsive HTML dashboard
- Dark/Light mode toggle with automatic system preference detection
- Theme persistence across visits
- Workflow separation between data exploration and report generation

## Requirements

- Python 3.10+
- Libraries:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - plotly
  - scikit-learn
  - dash (for some examples)
  - kaleido (for static image export)

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/heesookiim/ipynb2html.git
   cd ipynb2html
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install pandas numpy matplotlib seaborn plotly scikit-learn dash kaleido
   ```

## Project Structure

- `create_iris_figures.ipynb`: Jupyter notebook for creating and exploring visualizations
- `generate_iris_visualizations.py`: Script for generating the HTML dashboard from saved figures
- `app.py`: Example Dash application demonstrating interactive and static rendering
- `figure_data/`: Directory containing saved Plotly figure JSON files
- `visualizations/`: Output directory for HTML visualization files

## Usage

### Step 1: Create visualizations (Jupyter Notebook)

Run the Jupyter notebook to explore the data and create visualizations:

```bash
jupyter notebook create_iris_figures.ipynb
```

The notebook will:
1. Load the Iris dataset
2. Create various interactive visualizations
3. Save the visualizations as JSON files in the `figure_data/` directory

### Step 2: Generate the HTML dashboard

Run the Python script to generate the HTML dashboard:

```bash
python generate_iris_visualizations.py
```

This script will:
1. Load the pre-created visualizations from JSON files
2. Generate individual HTML files for each visualization
3. Create a combined HTML dashboard with all visualizations
4. Apply dark mode support and theme persistence

### Step 3: View the dashboard

Open the HTML files in your web browser:
- `visualizations/iris_interactive_dashboard.html` (all visualizations)
- Or individual visualization files in the `visualizations/` directory

## How It Works

The project demonstrates a workflow for creating and sharing interactive visualizations:

1. **Data Exploration**: Use the Jupyter notebook for interactive exploration and creating visualizations. This provides a flexible environment for data scientists.

2. **Visualization Storage**: Save the visualizations as JSON files, which allows separating the data exploration from the report generation.

3. **Report Generation**: Use the Python script to load the saved visualizations and generate an HTML report. This step can be automated or integrated into a reporting pipeline.

4. **Interactive Dashboard**: The resulting HTML dashboard provides interactive visualizations with features like dark mode, responsive design, and theme persistence.

## Dark Mode

The dashboard includes a dark mode toggle that:
- Respects your system preference by default
- Remembers your preference between visits
- Provides a consistent dark/light theme across all elements
- Refreshes visualizations when the theme changes

## Examples

The repository also includes `app.py`, a Dash application example that demonstrates:
- How to create interactive visualizations with Dash
- How to export Plotly figures as static images
- How to handle user inputs for rendering options

To run the Dash example:
```bash
python app.py
```

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
