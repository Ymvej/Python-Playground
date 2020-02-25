dataset = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,17,19,21,25,32,42,52,62,80,111,121,144]
data2 = [5,8,15,62,300,380,700,754,956,1200,1522,1833,2152,2188,1556,9865,2115,6987,4156,1255,1588,1452,6963,3365,3658,7,8]

import plotly.graph_objs as go 
import plotly.express as px

fig = px.scatter(x = dataset, y = data2)
# fig.show()

fig2 = go.Figure(data=go.Scatter(
    x=dataset,
    y=data2,
    mode='markers',
    marker=dict(size=[40, 60, 80, 100],
                color=[0, 1, 2, 3])
))
# fig2.show()

df = px.data.gapminder().query("country=='Canada'")
fig3 = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
# fig3.show()

fig4 = px.bar(df, x='year', y='pop')
# fig4.show()

fig5 = px.box(df, y="year")
fig5.show()