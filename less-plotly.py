# pip install plotly
# pip install matplotlib
# pip install pandas
# pip install numpy


import plotly
import plotly.graph_objs as go
import plotly.express as px
import matplotlib.pyplot as plt

from plotly.subplots import make_subplots

import numpy as np
import pandas as pd
import json

# x = np.arange(-10, 10, 0.2)
# # print(x)
# # print(type(x))
# # print(type(x[0]))
#
# y = x**2
# # print(y)
# # print(type(y))
# # print(type(y[0]))
# # print(len(x))
# # print(len(y))
#
# plt.plot(x, y)
# plt.show()




x = np.arange(-1, 1.2, 0.2)  #  [-1; 1)
# print(x, type(x))

# print(*dir(x), sep='\n')
# x1 = list(x)
# print(x1, type(x1))


def f(x):
    return x**2

def h(x):
    return np.sin(x)

def k(x):
    return np.cos(x)

def m(x):
    return np.tan(x)




#========================================== Простий графік 1 та 2 функцій
# fig = go.Figure()
#
# # print(*dir(fig), sep='\n')
# # print(fig.to_dict())
#
#
# #
# # print(json.dumps(fig.to_dict(), indent=4))
# # print('='*80)
#
# print(fig.to_dict()['data'])
# print('='*80)
#
# fig.add_trace(go.Scatter(x=x, y=f(x)))
# fig.add_trace(go.Scatter(x=x, y=5*x))
# fig.add_trace(go.Scatter(x=x, y=-4*x))
# fig.add_trace(go.Scatter(x=x, y=-x**2))
#
# print(fig.to_dict()['data'])
# # #
# fig.show()

#==================================== Легенда та підписи осей
# fig = go.Figure()
#
# fig.add_trace(go.Scatter(x=x, y=f(x), name='<b>f(x)=x<sup>2</sup></b>'))
# fig.add_trace(go.Scatter(x=x, y=x, name='<i>g(x)=x</i>'))
#
# # fig.update_layout(legend_orientation="h")
#
# fig.update_layout(legend_orientation="h",
#                   legend=dict(x=.5, xanchor="center"),
#                   title="<b>Plot Title</b>",
#                   xaxis_title="<b>x Axis Title</b>",
#                   yaxis_title="<b><i>y Axis Title</i></b>",
#                   margin=dict(l=100, r=100, t=100, b=100))
# fig.show()
# ============================ Маркери та підписи даних

# fig = go.Figure()
#
# fig.add_trace(go.Scatter(x=x, y=f(x), mode='lines+markers',  name='f(x)=x<sup>2</sup>'))
# fig.add_trace(go.Scatter(x=x, y=x, mode='markers', name='g(x)=x'))
# fig.update_layout(legend_orientation="h",
#                   # hovermode="x",
#                   hovermode="x unified",
#                   legend=dict(x=.5, xanchor="center"),
#                   margin=dict(l=50, r=50, t=50, b=50))
#
# # fig.update_traces(hoverinfo="x+y")
# fig.update_traces(hoverinfo="all", hovertemplate="Аргумент: %{x}<br>Функція: %{y}")
#
# fig.show()

# ============== Управліня маркерами, масштаб фрагменту, додавання графіків
#
# fig = go.Figure()
#
# # Масштабування
# # fig.update_yaxes(range=[-0.5, 1.5])
# # fig.update_xaxes(range=[-0.5, 1.5])
#
# fig.update_yaxes(range=[-2.5, 2.5], zeroline=True, zerolinewidth=3, zerolinecolor='Red')
# fig.update_xaxes(range=[-1.5, 1.5], zeroline=True, zerolinewidth=3, zerolinecolor='#0000ff') # RGB
#
# # # Додавання графіків (потрібно включити)
# fig.add_trace(go.Scatter(visible='legendonly', x=x, y=h(x),  name='h(x)=sin(x)'))
# fig.add_trace(go.Scatter(x=x, y=k(x),  name='k(x)=cos(x)'))
# fig.add_trace(go.Scatter(visible='legendonly', x=x, y=m(x),  name='m(x)=tg(x)'))
# #
# #
# fig.add_trace(go.Scatter(x=x, y=f(x), mode='lines+markers',  name='f(x)=x<sup>2</sup>'))
# fig.add_trace(go.Scatter(x=x, y=x, mode='markers', name='g(x)=x',
#                          marker=dict(color='Red', size=20, line=dict(color='MediumPurple', width=3))))
#
# fig.update_traces(hoverinfo="all", hovertemplate="Аргумент: %{x}<br>Функция: %{y}")
# fig.show()

#============== Декілько графіків
#
# fig = make_subplots(rows=1, cols=2, subplot_titles=("Plot 1", "Plot 2"))
# # fig = make_subplots(rows=1, cols=2, subplot_titles=("Plot 1", "Plot 2"), column_widths=[5, 2])
# # #
# fig.update_yaxes(range=[-0.5, 1.5], zeroline=True, zerolinewidth=2, zerolinecolor='LightPink', col=2)
# fig.update_xaxes(range=[-0.5, 1.5], zeroline=True, zerolinewidth=2, zerolinecolor='#2980B9', col=2)
#
# fig.update_yaxes(range=[-1.5, 1.5], zeroline=True, zerolinewidth=2, zerolinecolor='LightGreen', col=1)
# fig.update_xaxes(range=[-1, 1], zeroline=True, zerolinewidth=2, zerolinecolor='#F4D03F', col=1)
#
#
# fig.add_trace(go.Scatter(x=x, y=h(x),  name='h(x)=sin(x)'), 1, 1)
# fig.add_trace(go.Scatter(x=x, y=k(x),  name='k(x)=cos(x)'), 1, 1)
# fig.add_trace(go.Scatter(visible='legendonly', x=x, y=m(x),  name='m(x)=tg(x)'), 1, 1)
#
# fig.add_trace(go.Scatter(x=x, y=f(x), mode='lines+markers',  name='f(x)=x<sup>2</sup>'), 1, 2)
# fig.add_trace(go.Scatter(x=x, y=x, mode='markers', name='g(x)=x',
#                          marker=dict(color='LightSkyBlue', size=20, line=dict(color='MediumPurple', width=3))), 1, 2)
#
# fig.update_layout(legend_orientation="h",
#                   legend=dict(x=.5, xanchor="center"),
#                   hovermode="x",
#                   margin=dict(l=50, r=50, t=50, b=50))
#
# fig.update_layout(title="Plot Title")
#
# fig.update_xaxes(title='Вісь X графіку 1', row=1, col=1)
# fig.update_xaxes(row=1, title='Вісь X графіку 2', col=2)
#
# fig.update_yaxes(title='Вісь Y графіку 1', col=1, row=1)
# fig.update_yaxes(title='Вісь Y графіку 2', row=1, col=2)
#
# fig.update_traces(hoverinfo="all", hovertemplate="Аргумент: %{x}<br>Функція: %{y}")
# fig.show()

#========== Різні розміри графіків та функцій (стовбець)
# fig = make_subplots(rows=3, cols=2,
#                     specs=[[{"rowspan": 3}, {}], [None, {}], [None, {}]])
# # # # Об'єднує "секції" матриці графіків та "подавляє" графіки
# # #
# fig.update_yaxes(range=[-1.5, 1.5], zeroline=True, zerolinewidth=2, zerolinecolor='LightPink', col=2)
# fig.update_xaxes(range=[-2, 2], zeroline=True, zerolinewidth=2, zerolinecolor='#008000', col=2)
# #
# fig.add_trace(go.Scatter(x=x, y=h(x),  name='h(x)=sin(x)'), 2, 2)
# fig.add_trace(go.Scatter(x=x, y=k(x),  name='k(x)=cos(x)'), 3, 2)
# fig.add_trace(go.Scatter(x=x, y=m(x),  name='m(x)=tg(x)'), 1, 1)
# # #
# fig.add_trace(go.Scatter(x=x, y=f(x), mode='lines+markers',  name='f(x)=x<sup>2</sup>'), 1, 2)
# fig.add_trace(go.Scatter(x=x, y=x, mode='markers', name='g(x)=x',
#                          marker=dict(color='LightSkyBlue', size=10, line=dict(color='MediumPurple', width=3))), 1, 2)
#
# fig.update_layout(legend_orientation="h",
#                   legend=dict(x=.5, xanchor="center"),
#                   # hovermode="x",
#                   hovermode="x unified",
#                   margin=dict(l=50, r=50, t=50, b=50))
#
# fig.update_traces(hoverinfo="all", hovertemplate="Аргумент: %{x}<br>Функция: %{y}")
# fig.show()



#========== Різні розміри графіків та функцій (рядок)
# x = np.arange(-5, 10, 0.2)
#
# fig = make_subplots(rows=2, cols=3,
#                     specs=[[{"colspan": 3}, None, None], [{}, {}, {}]])
#
# fig.update_yaxes(range=[-1.5, 1.5], zeroline=True, zerolinewidth=2, zerolinecolor='LightPink', col=2)
# fig.update_xaxes(range=[-5, 5], zeroline=True, zerolinewidth=2, zerolinecolor='#008000', col=2)
#
# fig.update_yaxes(range=[-1.5, 1.5], zeroline=True, zerolinewidth=2, zerolinecolor='LightBlue', col=3)
# fig.update_xaxes(range=[-5, 5], zeroline=True, zerolinewidth=2, zerolinecolor='#25f3aa', col=3) # 000000 ffffff
# #
# fig.add_trace(go.Scatter(x=x, y=h(x),  name='h(x)=sin(x)'), 2, 2)
# fig.add_trace(go.Scatter(x=x, y=k(x),  name='k(x)=cos(x)'), 2, 3)
# fig.add_trace(go.Scatter(x=x, y=m(x),  name='m(x)=tg(x)'), 1, 1)
# #
# fig.add_trace(go.Scatter(x=x, y=f(x), mode='lines+markers',  name='f(x)=x<sup>2</sup>'), 2, 1)
# fig.add_trace(go.Scatter(x=x, y=x, mode='markers', name='g(x)=x',
#                          marker=dict(color='LightSkyBlue', size=5, line=dict(color='MediumPurple', width=2))), 2, 1)
# fig.update_layout(legend_orientation="h",
#                   legend=dict(x=.5, xanchor="center"),
#                   hovermode="x",
#                   margin=dict(l=40, r=40, t=40, b=40),
#                   # height=1500,
#                   # width=2600
#                   )
# fig.update_traces(hoverinfo="all", hovertemplate="Аргумент: %{x}<br>Функция: %{y}")
# fig.show()

#######################################################
#========Теплова карта
# aggrnyl     agsunset    blackbody   bluered     blues       blugrn      bluyl       brwnyl
# bugn        bupu        burg        burgyl      cividis     darkmint    electric    emrld
# gnbu        greens      greys       hot         inferno     jet         magenta     magma
# mint        orrd        oranges     oryel       peach       pinkyl      plasma      plotly3
# pubu        pubugn      purd        purp        purples     purpor      rainbow     rdbu
# rdpu        redor       reds        sunset      sunsetdark  teal        tealgrn     turbo
# viridis     ylgn        ylgnbu      ylorbr      ylorrd      algae       amp         deep
# dense       gray        haline      ice         matter      solar       speed       tempo
# thermal     turbid      armyrose    brbg        earth       fall        geyser      prgn
# piyg        picnic      portland    puor        rdgy        rdylbu      rdylgn      spectral
# tealrose    temps       tropic      balance     curl        delta       oxy         edge
# hsv         icefire     phase       twilight    mrybm       mygbm


#
# x = np.arange(-5, 10, 0.2)
# fig = go.Figure()
#
# fig.add_trace(go.Scatter(x=x, y=f(x), mode='lines+markers',  name='f(x)=x<sup>2</sup>',
#                          marker=dict(color=h(x), colorbar=dict(title="h(x)=sin(x)"),
#                                      # colorscale='Inferno',
#                                      colorscale='icefire',
#                                      # colorscale='earth',
#                                      size=100 * abs(k(x))
#                                      )
#                         ))
# fig.add_trace(go.Scatter(visible='legendonly', x=x, y=10*h(x),  name='h(x)=10*sin(x)'))
# fig.add_trace(go.Scatter(visible='legendonly', x=x, y=15*k(x),  name='k(x)=15*cos(x)'))
#
# fig.update_layout(legend_orientation="h",
#                   legend=dict(x=.5, xanchor="center"),
#                   margin=dict(l=30, r=30, t=30, b=30))
# fig.update_traces(hoverinfo="all", hovertemplate="Аргумент: %{x}<br>Функция: %{y}")
# fig.show()


#========= Анімація 1 ===================================================
# x = np.arange(-7, 15, 0.2)
# fig = go.Figure()
#
# fig.update_yaxes(range=[-25, 250])
# fig.update_xaxes(range=[-8, 16])
#
# fig.add_trace(go.Scatter(x=[x[0]], y=[f(x)[0]], mode='lines+markers',  name='f(x)=x<sup>2</sup>',
#                          marker=dict(color=h(x[0]), colorbar=dict(title="h(x)=sin(x)"), colorscale='Inferno', size=50*abs(h(x[0])))
#                         ))
#
# frames = []
# for i in range(1, len(x)):
#     frames.append(go.Frame(data=[go.Scatter(x=x[:i+1], y=f(x[:i+1]), marker=dict(color=h(x[:i+1]), size=50*abs(h(x[:i+1]))))]))
#
# fig.frames = frames
#
# fig.update_layout(legend_orientation="h",
#                   legend=dict(x=.5, xanchor="center"),
#                   updatemenus=[dict(type="buttons", buttons=[dict(label="►", method="animate", args=[None, {"fromcurrent": True}]),
#                                                              dict(label="❚❚", method="animate", args=[[None], {"frame": {"duration": 0, "redraw": False},
#                                                                                                                "mode": "immediate",
#                                                                                                                "transition": {"duration": 0}}])])],
#                   margin=dict(l=0, r=0, t=0, b=0))
# fig.update_traces(hoverinfo="all", hovertemplate="Аргумент: %{x}<br>Функция: %{y}")
# fig.show()






#========= Анімація 2 ==================================================
# x = np.arange(-7, 15, 0.2)
# num_steps = len(x)
#
#
#
#
# fig = go.Figure(data=[go.Scatter(x=[x[0]], y=[h(x)[0]], mode='lines+markers', name='h(x)=sin(x)',
#                                  marker=dict(color=[f(x[0])], colorbar=dict(yanchor='top', y=0.8, title="f(x)=x<sup>2</sup>"), colorscale='Inferno', size=[50*abs(h(x[0]))])),
#                       go.Scatter(x=[x[0]], y=[k(x)[0]], mode='lines+markers', name='k(x)=cos(x)',
#                                  marker=dict(color=[m(x[0])], colorscale='Inferno', size=[50*abs(k(x[0]))]))])
# fig.update_yaxes(range=[-2, 2])
# fig.update_xaxes(range=[-8, 16])
#
# frames = []
# for i in range(0, len(x)):
#     frames.append(go.Frame(name=str(i),
#                            data=[go.Scatter(x=x[:i+1], y=h(x[:i+1]), mode='lines+markers', name='h(x)=sin(x)',
#                                             marker=dict(color=f(x[:i+1]), colorscale='Inferno', size=50*abs(h(x[:i+1])))),
#                                  go.Scatter(x=x[:i+1], y=k(x[:i+1]), mode='lines+markers', name='k(x)=cos(x)',
#                                             marker=dict(color=f(x[:i+1]), colorscale='Inferno', size=50*abs(k(x[:i+1]))))]))
#
# steps = []
# for i in range(num_steps):
#     step = dict(
#         label = str(i),
#         method = "animate",
#         args = [[str(i)]]
#     )
#     steps.append(step)
#
# sliders = [dict(
#     steps = steps,
# )]
#
# fig.update_layout(updatemenus=[dict(direction="left",
#                                     x=0.5,
#                                     xanchor="center",
#                                     y=0,
#                                     showactive=False,
#                                     type="buttons",
#                                     buttons=[dict(label="►", method="animate", args=[None, {"fromcurrent": True}]),
#                                              dict(label="❚❚", method="animate", args=[[None], {"frame": {"duration": 0, "redraw": False},
#                                                                                                "mode": "immediate",
#                                                                                                "transition": {"duration": 0}}])])],
#                   )
#
#
# fig.layout.sliders = sliders
# fig.frames = frames
#
# fig.show()

#
# #================ Діаграми (кругова)
# dices = pd.DataFrame(np.random.randint(low=1, high=7, size=(10000, 2)), columns=('Кість 1', 'Кість 2'))
# #
# dices['Сумма'] = dices['Кість 1'] + dices['Кість 2']
# # # Перші 5 кидків гральних костей
# # # display(dices.head())
# # print(dices.head())
# # print('====== Статистика ===========')
# #
# sum_counts = dices['Сумма'].value_counts().sort_index()
# # # кількість випавших сум
# # # display(sum_counts)
# # print(sum_counts)
# #
# fig = go.Figure()
# pull = [0]*len(sum_counts)
# # print(pull)
#
# # fig.add_trace(go.Pie(values=sum_counts, labels=sum_counts.index, sort=False))
#
# pull[sum_counts.tolist().index(sum_counts.max())] = 0.1 # Сдвиг
# # fig.add_trace(go.Pie(values=sum_counts, labels=sum_counts.index, sort=False, pull=pull))
# fig.add_trace(go.Pie(values=sum_counts, labels=sum_counts.index, sort=False, pull=pull, hole=0.5))
# fig.update_layout(
#     title="Приклад кільцевої/кругової діаграми",
#     title_x=0.5,
#     margin=dict(l=0, r=0, t=30, b=0),
#     legend_orientation="h",
#     annotations=[dict(text='Суми очков<br>при киданні<br>2 гральних костей', x=0.5, y=0.5, font_size=20, showarrow=False)])
# fig.show()

#========= Діаграма "Сонячні промені"

# dices = pd.DataFrame(np.random.randint(low=1, high=7, size=(100000, 2)), columns=('Кість 1', 'Кість 2'))
# dices['Сума'] = dices['Кість 1'] + dices['Кість 2']
# sum_counts = dices['Сума'].value_counts().sort_index()
#
# # 1-й рівень, центр діаграми
# labels = ["Всього подій: " + str(sum(sum_counts))]
# parents = [""]
# values = [sum(sum_counts)]
#
# # 2-й рівень, "проміжний"
# second_level_dict = {x:'Подій: ' + str(sum_counts[x]) + '<br>Σ = ' + str(x) for x in sum_counts.index}
# labels += map(lambda x: second_level_dict[x], sum_counts.index)
# parents += [labels[0]]*len(sum_counts)
# values += sum_counts.tolist()
#
# # Готовимо DataFrame для 3 рівня (групуємо )
# third_level = dices.groupby(['Кість 1', 'Кість 2']).count().reset_index()
# third_level.rename(columns={'Сума':'Value'}, inplace=True)
# third_level['Сума'] = third_level['Кість 1'] + third_level['Кість 2']
# third_level['Label'] = third_level['Кість 1'].map(str) + ' + ' + third_level['Кість 2'].map(str)
# third_level['Parent'] = third_level['Сума'].map(lambda x: second_level_dict[x])
# # 3-й рівень, "пелюстки" діаграми
# values += third_level['Value'].tolist()
# parents += third_level['Parent'].tolist()
# labels += third_level['Label'].tolist()
#
# fig = go.Figure(go.Sunburst(
#     labels=labels,
#     parents=parents,
#     values=values,
#     branchvalues="total"
# ))
# fig.update_layout(margin=dict(t=30, l=30, r=30, b=30))
#
# fig.show()

#============== Діаграма "Гістограма"
#
# dices = pd.DataFrame(np.random.randint(low=1, high=7, size=(100, 2)), columns=('Кість 1', 'Кість 2'))
# dices['Сума'] = dices['Кість 1'] + dices['Кість 2']
#
# dices2 = pd.DataFrame(np.random.randint(low=1, high=7, size=(100, 2)), columns=('Кість 1', 'Кість 2'))
# dices2['Сума'] = dices2['Кість 1'] + dices2['Кість 2']
#
# dices3 = pd.DataFrame(np.random.randint(low=1, high=7, size=(10000, 2)), columns=('Кість 1', 'Кість 2'))
# dices3['Сума'] = dices3['Кість 1'] + dices3['Кість 2']
#
#
# fig = go.Figure()
#
# fig.add_trace(go.Histogram(x=dices['Сума'], histnorm='probability density', name='100 кидків v.1'))
# fig.add_trace(go.Histogram(x=dices2['Сума'], histnorm='probability density', name='100 кидків v.2'))
# fig.add_trace(go.Histogram(x=dices3['Сума'], histnorm='probability density', name='1000 кидків'))
#
# fig.update_layout(
#     title="Приклад гістограми на основі кидків пари гральних костей",
#     title_x=0.5,
#     xaxis_title="<b>сума очков</b>",
#     yaxis_title="<b>Плотність верогідності</b>",
#     legend=dict(x=.5, xanchor="center", orientation="h"),
#     margin=dict(l=30, r=30, t=30, b=30))
#
# fig.show()
#



#####################################  END !!!!!





#========== ??????????????????????? Map Rail (((((((((
# def to_int_year(value):
#     try:
#         return int(value)
#     except:
#         return None
#
# def to_int_size(value):
#     try:
#         return np.log10(int(value))
#     except:
#         return np.log10(int(value.split('[')[0]))
#
#
#
# # ========= 1
# fig = go.Figure(go.Scattermapbox(lat=cities['geo_lat'], lon=cities['geo_lon']))
# fig.update_layout(mapbox_style="open-street-map")
# fig.show()

#========== 2
# fig = go.Figure(go.Scattermapbox(lat=cities['geo_lat'], lon=cities['geo_lon']))
# capital = cities[cities['region']=='Москва']
# map_center = go.layout.mapbox.Center(lat=capital['geo_lat'].values[0], lon=capital['geo_lon'].values[0])
# fig.update_layout(mapbox_style="open-street-map",
#                   mapbox=dict(center=map_center, zoom=2))
# fig.show()


#======= Map
# train_russia = pd.read_csv('https://gist.githubusercontent.com/lexnekr/2da07b5fc12b5be24068e4d68ed47ca5/raw/d6256765a3223282fbfec7e0b040cbfb21593fff/train_russia.scv')
#
# fig = go.Figure(go.Scattermapbox(legendgroup="group",
#                                  name='Города России',
#                                  lat=cities['geo_lat'],
#                                  lon=cities['geo_lon'],
#                                  text=cities['city'],
#                                  marker=dict(colorbar=dict(title="Год основания"),
#                                              color=cities['foundation_year'].map(to_int_year),
#                                              size=cities['population'].map(to_int_size))))
#
# for df_for_today in train_russia.groupby(['day number']):
#     fig.add_trace(go.Scattermapbox(name='День {}'.format(df_for_today[0]),
#                                    mode = "lines",
#                                    hoverinfo='skip',
#                                    lat=df_for_today[1]['geo_lat'],
#                                    lon=df_for_today[1]['geo_lon']))
#
# map_center = go.layout.mapbox.Center(lat=(cities['geo_lat'].max()+cities['geo_lat'].min())/2,
#                                      lon=(cities['geo_lon'].max()+cities['geo_lon'].min())/2)
# fig.update_layout(title='По России на поезде',
#                   legend_orientation="h",
#                   mapbox_style="open-street-map",
#                   mapbox=dict(center=map_center, zoom=2))
#
# fig.show()



#========= Animation
#
# cities = pd.read_csv('https://raw.githubusercontent.com/hflabs/city/master/city.csv')
# train_russia = pd.read_csv('https://gist.githubusercontent.com/lexnekr/2da07b5fc12b5be24068e4d68ed47ca5/raw/d6256765a3223282fbfec7e0b040cbfb21593fff/train_russia.scv')
#
# data = [go.Scattermapbox(legendgroup="group",
#                          name='Города России',
#                          lat=cities['geo_lat'],
#                          lon=cities['geo_lon'],
#                          text=cities['city'],
#                          marker=dict(colorbar=dict(title="Год основания"),
#                                      color=cities['foundation_year'].map(to_int_year),
#                                      size=cities['population'].map(to_int_size)))]
# for df_for_today in train_russia.groupby(['day number']):
#     data.append(go.Scattermapbox(visible=False,
#                                  name='День {}'.format(df_for_today[0]),
#                                  mode="lines",
#                                  hoverinfo='skip',
#                                  lat=df_for_today[1]['geo_lat'],
#                                  lon=df_for_today[1]['geo_lon']))
#
# fig = go.Figure(data)
#
# frames = []
# for i in range(len(data) + 1):
#     temp_frame = go.Frame(name=str(i), data=data)
#
#     for j in range(1, i):
#         temp_frame['data'][j]['visible'] = True
#
#     frames.append(temp_frame)
#
# steps = []
# for i in range(len(data)):
#     step = dict(
#         label=str(i),
#         method="animate",
#         args=[[str(i + 1)]]
#     )
#     steps.append(step)
#
# sliders = [dict(
#     currentvalue={"prefix": "День №", "font": {"size": 20}},
#     len=0.9,
#     x=0.1,
#     pad={"b": 10, "t": 50},
#     steps=steps,
# )]
#
# map_center = go.layout.mapbox.Center(lat=(cities['geo_lat'].max() + cities['geo_lat'].min()) / 2,
#                                      lon=(cities['geo_lon'].max() + cities['geo_lon'].min()) / 2)
# fig.update_layout(title='По России на поезде',
#                   legend_orientation="h",
#                   mapbox_style="open-street-map",
#                   mapbox=dict(center=map_center, zoom=2),
#                   updatemenus=[dict(direction="left",
#                                     pad={"r": 10, "t": 80},
#                                     x=0.1,
#                                     xanchor="right",
#                                     y=0,
#                                     yanchor="top",
#                                     showactive=False,
#                                     type="buttons",
#                                     buttons=[dict(label="►", method="animate", args=[None, {"fromcurrent": True}]),
#                                              dict(label="❚❚", method="animate",
#                                                   args=[[None], {"frame": {"duration": 0, "redraw": False},
#                                                                  "mode": "immediate",
#                                                                  "transition": {"duration": 0}}])])],
#                   )
#
# fig.layout.sliders = sliders
# fig.frames = frames
#
# fig.show()





