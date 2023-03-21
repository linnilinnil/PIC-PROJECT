# helper function to create time serie
def draw_line(df, selected):
    area = "Research/Disease Areas \n (Dollars in millions and rounded)"
    sub = df[df[area]== selected]
    sub.rename(columns={'2022 Estimated': '2022','2023 Estimated':'2023'})
    melted = pd.melt(sub, id_vars=[area], 
            value_vars=fatal.columns[1:17],
            var_name='year', value_name='value')
    melted['value'] = melted['value'].astype(int)
    
    fig = px.line(melted,x='year',y='value',title="Change in "+ selected+'\n'+"research fund, M.USD")
    fig.update_layout(
        xaxis = dict(
            tickmode = 'linear',
            tick0 = 1,
            dtick = 1
        )
    )
    return fig
