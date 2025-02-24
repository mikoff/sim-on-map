# Simulator on the Route
**Warning**: the code is super raw and dirty, it was meant to be used for educational purposes.
This repository contains a Jupyter Notebook (`simulator-on-the-route.ipynb`) intended for route simulation and visualization using Folium.

## Overview
The notebook showcases how to:
1. Create an interactive map using [Folium](https://python-visualization.github.io/folium/).
2. Plot and simulate routes or trajectories.
3. Analyze or demonstrate path-related functionality.

## Requirements
- **Python 3.x**
- **Jupyter Notebook**
- **folium**: for map visualizations
- **PyQt5** and **PyQtWebEngine** (if you plan to integrate or reference `trajectory_picker.py`)

Install the dependencies using pip.

## Usage
1. Open a terminal and navigate to the directory containing `simulator-on-the-route.ipynb`.
2. Launch the Jupyter Notebook:
   ```bash
   jupyter notebook simulator-on-the-route.ipynb
   ```
3. Run the notebook cells sequentially to generate and visualize the interactive map.

## Additional Script
- **`trajectory_picker.py`**: A supporting script that provides an interactive tool for drawing polylines on a Folium map and printing their coordinates. This can be integrated into the notebook or used separately.

Run it with:
```bash
python trajectory_picker.py
```

## License
This project is licensed under the MIT License.

## References
The inspiration for implementation was taken from:
- https://github.com/Aceinna/gnss-ins-sim
- http://www.instk.org/
- Principles of GNSS, Inertial, and Multisensor Integrated Navigation Systems (GNSS Technology and Applications) by Paul D. Groves.


