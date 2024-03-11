import plotly.graph_objects as go

# Sample data
labels = ["A", "B", "C", "D", "E", "F"]
parents = ["", "A", "A", "B", "B", "C"]
values = [10, 20, 15, 25, 5, 10]

# Create Sunburst chart
fig = go.Figure(go.Sunburst(
    labels=labels,
    parents=parents,
    values=values
))

# Customize layout
fig.update_layout(
    title="Sunburst Chart",
    margin=dict(t=0, l=0, r=0, b=0)
)

# Show the chart
fig.show()
