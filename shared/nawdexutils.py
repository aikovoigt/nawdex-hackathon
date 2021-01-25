# remove first day from dataset
def drop_first_day(ds):
    ntime = ds.time.size                   # number of time steps
    firstday = ds.isel(time=0).time.dt.day # first day 
    t_list = []                            # list of timesteps that do not belong to first day
    for i in range(ntime):
        if ds.isel(time=i).time.dt.day != firstday:
            t_list.append(i)
    return ds.isel(time=t_list)

# only select analysis days as defined in anadaysdictionary
def select_analysis_days(ds, expid):
    
    import sys
    sys.path.append('/pf/b/b380459/nawdex-hackathon/shared')

    import dict_nawdexsims
    simdict     = dict_nawdexsims.simdictionary()
    anadaysdict = dict_nawdexsims.anadaysdictionary()
    
    startday  = simdict[expid]['start']
    anadays   = anadaysdict[startday]
    
    return ds.sel(time=slice(anadays[0], anadays[-1]))
