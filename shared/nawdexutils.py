# remove first day from dataset
def drop_first_day(ds):
    ntime = ds.time.size                   # number of time steps
    firstday = ds.isel(time=0).time.dt.day # first day 
    t_list = []                            # list of timesteps that do not belong to first day
    for i in range(ntime):
        if ds.isel(time=i).time.dt.day != firstday:
            t_list.append(i)
    return ds.isel(time=t_list)