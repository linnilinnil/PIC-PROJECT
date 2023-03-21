def stacked_bar(divsum,par):
    subdiv = divsum.groupby([par,'FY'])['tot_doll'].agg(sum)
    subdiv = subdiv.reset_index(0).reset_index(0)
    subdiv = pd.pivot(subdiv, index='FY', columns=par, values='tot_doll')
    return px.bar(subdiv)