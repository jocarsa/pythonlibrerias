import plotly.graph_objects as go


labels = ['A', 'B', 'C', 'D']
values = [30, 25, 20, 25]

fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

fig.show()
