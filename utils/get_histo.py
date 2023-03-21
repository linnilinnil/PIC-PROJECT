def get_histo(type,ten):
    area = "Area(M.USD)"
    
    sem = pd.melt(ten, id_vars=['Research/Disease Areas \n (Dollars in millions and rounded)'], 
            value_vars=fatal.columns[1:17],
            var_name='year', value_name='value')
    sem = sem.rename(columns={'2022 Estimated': '2022','2023 Estimated': '2023',
                            'Research/Disease Areas \n (Dollars in millions and rounded)':area})
    sem['value'] = sem['value'].astype(int)
    if type == 'nonfatal':
        up = 800
    else:
        up = 8000
    histo = px.bar(sem, x=area, 
                y="value", color=area,
                title='Top 10 funded '+type+ ' diseases',
                hover_name = area,
                hover_data = [area],
                color_continuous_scale="PuBu",
                animation_frame="year",range_y=[0,up],
                height=600)
    histo.update_layout(showlegend=False)
    histo.update_xaxes(tickangle=60)
    return histo
#histo = get_histo()
