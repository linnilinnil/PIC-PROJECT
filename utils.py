import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
path = 'https://raw.githubusercontent.com/linnilinnil/NIH-Fundings-Dashboard/main/data/'

fatal = pd.read_csv(path+'fatal.csv')
nonfatal = pd.read_csv(path+'nonfatal.csv')
def cleanpi(pi):
    pi=pi[pi['ETHNICITY2']!="Unknown"]
    pi=pi[pi['ETHNICITY2']!="Withheld"]

    pi=pi[pi['gender']!="Unknown"]
    pi=pi[pi['gender']!="Withheld"]

    pi=pi[pi['race']!="Unknown"]
    pi=pi[pi['race']!="Withheld"]
    pi=pi[pi['age']!="Unknown"]

    pi['tot_doll']=round(pi['tot_doll'],2)

    cols=["FY","ETHNICITY2","gender","DEGREE","tot_doll","race","age"]
    pi=pi[cols]
    pi = pi.rename(columns={'ETHNICITY2':'hispanic','DEGREE':'degree'})
    return pi

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


import numpy as np
import sqlite3
import pandas as pd
FME = ['RPGs - SBIR/STTR',
 'RPGs - Non SBIR/STTR',
 'Other Research-Related',
 'Training - Individual',
 'Training - Institutional',
 'Research Centers',
 'Other',
 'Construction']
INST = ['None',
 'Research Institutes',
 'Domestic Higher Education',
 'Independent Hospitals']
col = ['ORGANIZATION NAME',
 'ORGANIZATION ID (IPF)',
 'PROJECT NUMBER',
 'FUNDING MECHANISM',
 'PI NAME',
 'PI PERSON ID',
 'PROJECT TITLE',
 'DIRECT COST',
 'INDIRECT COST',
 'FUNDING',
 'CITY',
 'STATE OR COUNTRY NAME',
 'INSTITUTION TYPE',
 'AWARD NOTICE DATE',
 'MONTH',
 'YEAR',
 'FULL_LOC',
 'CODE']
def map_que(year=list(np.arange(2012,2022)),month=list(np.arange(1,12)),
            fme = FME,
            inst = INST):
        cmd = '''
        SELECT D.*,C.COUNTY_FIPS,C.COUNTY_NAME,C.LAT,C.LNG
        FROM 
                (SELECT LNG,LAT,COUNTY_NAME,CITY,COUNTY_FIPS,STATE_ID
                FROM city) AS C
        LEFT JOIN decade as D
        ON D.CITY = C.CITY
        WHERE D.YEAR IN ''' + str(tuple(year))\
        + ''' AND MONTH IN ''' + str(tuple(month))\
        + ''' AND D.[FUNDING MECHANISM] IN ''' + str(tuple(fme))\
        + ''' AND D.[INSTITUTION TYPE] IN ''' + str(tuple(inst))#+'''LIMIT 1'''
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()

        cursor.execute(cmd)
        df = pd.DataFrame(cursor.fetchall(),columns=col+["COUNTY_FIPS","COUNTY_NAME","LAT","LNG"])
        print(df.head(n=1))
        conn.close()
        return df


def stacked_bar(divsum,par):
    subdiv = divsum.groupby([par,'FY'])['tot_doll'].agg(sum)
    subdiv = subdiv.reset_index(0).reset_index(0)
    subdiv = pd.pivot(subdiv, index='FY', columns=par, values='tot_doll')
    return px.bar(subdiv)



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
