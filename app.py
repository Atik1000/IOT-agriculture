
# df['created_at'] = pd.to_datetime(df['created_at'])
# df['created_at'] = df['created_at'].dt.round('1H')
# df = df.groupby('created_at').mean()
# df.reset_index(inplace=True)
# df['created_at'] = df['created_at'].dt.strftime('%Y-%m-%d %H:%M:%S')
# print(df)
# fig =px.line(df,x='created_at',y='SoilMoisture',title='SoilMoisture wise time')
# fig.show()

# In the upper code when graph is upper then I need to added a text box "Motor is ON" and when graph is lower then "Motor is OFF" in the graph


# df['created_at'] = pd.to_datetime(df['created_at'])
# df['created_at'] = df['created_at'].dt.round('1H')
# df = df.groupby('created_at').mean()
# df.reset_index(inplace=True)
# df['created_at'] = df['created_at'].dt.strftime('%Y-%m-%d %H:%M:%S')
# print(df)
# fig =px.line(df,x='created_at',y='SoilMoisture',title='SoilMoisture wise time')
# fig.show()
