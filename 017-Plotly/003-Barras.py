import plotly.graph_objects as go

# Sample data
categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 78]

# Create bar chart
fig = go.Figure(data=[go.Bar(x=categories, y=values)])

# Customize layout
fig.update_layout(title='Bar Chart Example',
                  xaxis_title='Categories',
                  yaxis_title='Values')

# Show the plot
fig.show()
