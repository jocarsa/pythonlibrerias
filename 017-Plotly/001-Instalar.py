# pip install plotly

import plotly.graph_objects as go

# Sample data
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
parents = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
values = [20, 15, 10, 5, 8, 6, 7, 9]

# Create sunburst chart
fig = go.Figure(go.Sunburst(
    labels=labels,
    parents=parents,
    values=values,
))

# Customize layout (optional)
fig.update_layout(title='Sample Sunburst Chart')

# Show plot
fig.show()
