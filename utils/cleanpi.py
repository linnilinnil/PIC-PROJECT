
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