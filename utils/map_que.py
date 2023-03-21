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
df = map_que() 

