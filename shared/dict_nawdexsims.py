import numpy as np

# define dictionary for coloring resolutions
def colordictionary():
    # manually defined colors
    mymaroon= np.array([128,   0,   0])/255
    myred   = np.array([230,  25,  75])/255
    myorange= np.array([245, 130,  48])/255
    mymagenta=np.array([240, 50, 230 ])/255
    myolive = np.array([128, 128,   0])/255
    myteal  = np.array([  0, 128, 128])/255
    myblue  = np.array([  0, 130, 200])/255
    mynavy  = np.array([  0,   0, 128])/255

    return {'80km': mymaroon, '40km': myred, '20km': myorange, '10km': myolive, '5km': myteal, '2km': myblue}

# create dictionary for simulations with resolution, start date, convection scheme on/off and microphysics
def simdictionary():
    simdict = {
           'nawdexnwp-80km-mis-0001': {'res':'80km', 'start':'20160922', 'conv':1, 'mphys':1},
           'nawdexnwp-80km-mis-0002': {'res':'80km', 'start':'20160922', 'conv':1, 'mphys':2},
           'nawdexnwp-80km-mis-0003': {'res':'80km', 'start':'20160920', 'conv':1, 'mphys':1},
           'nawdexnwp-80km-mis-0004': {'res':'80km', 'start':'20160920', 'conv':1, 'mphys':2},
           'nawdexnwp-80km-mis-0005': {'res':'80km', 'start':'20160929', 'conv':1, 'mphys':1},
           'nawdexnwp-80km-mis-0006': {'res':'80km', 'start':'20160929', 'conv':1, 'mphys':2},
           'nawdexnwp-80km-mis-0007': {'res':'80km', 'start':'20161002', 'conv':1, 'mphys':1},
           'nawdexnwp-80km-mis-0008': {'res':'80km', 'start':'20161002', 'conv':1, 'mphys':2},
           'nawdexnwp-80km-mis-0009': {'res':'80km', 'start':'20161013', 'conv':1, 'mphys':1},
           'nawdexnwp-80km-mis-0010': {'res':'80km', 'start':'20161013', 'conv':1, 'mphys':2},
           
           'nawdexnwp-40km-mis-0001': {'res':'40km', 'start':'20160922', 'conv':1, 'mphys':1},
           'nawdexnwp-40km-mis-0002': {'res':'40km', 'start':'20160922', 'conv':1, 'mphys':2},
           'nawdexnwp-40km-mis-0003': {'res':'40km', 'start':'20160920', 'conv':1, 'mphys':1},
           'nawdexnwp-40km-mis-0004': {'res':'40km', 'start':'20160920', 'conv':1, 'mphys':2},
           'nawdexnwp-40km-mis-0005': {'res':'40km', 'start':'20160929', 'conv':1, 'mphys':1},
           'nawdexnwp-40km-mis-0006': {'res':'40km', 'start':'20160929', 'conv':1, 'mphys':2},
           'nawdexnwp-40km-mis-0007': {'res':'40km', 'start':'20161002', 'conv':1, 'mphys':1},
           'nawdexnwp-40km-mis-0008': {'res':'40km', 'start':'20161002', 'conv':1, 'mphys':2},
           'nawdexnwp-40km-mis-0009': {'res':'40km', 'start':'20161013', 'conv':1, 'mphys':1},
           'nawdexnwp-40km-mis-0010': {'res':'40km', 'start':'20161013', 'conv':1, 'mphys':2},
                    
           'nawdexnwp-20km-mis-0001': {'res':'20km', 'start':'20160922', 'conv':1, 'mphys':1},
           'nawdexnwp-20km-mis-0002': {'res':'20km', 'start':'20160922', 'conv':1, 'mphys':2},
           'nawdexnwp-20km-mis-0003': {'res':'20km', 'start':'20160920', 'conv':1, 'mphys':1},
           'nawdexnwp-20km-mis-0004': {'res':'20km', 'start':'20160920', 'conv':1, 'mphys':2},
           'nawdexnwp-20km-mis-0005': {'res':'20km', 'start':'20160929', 'conv':1, 'mphys':1},
           'nawdexnwp-20km-mis-0006': {'res':'20km', 'start':'20160929', 'conv':1, 'mphys':2},
           'nawdexnwp-20km-mis-0007': {'res':'20km', 'start':'20161002', 'conv':1, 'mphys':1},
           'nawdexnwp-20km-mis-0008': {'res':'20km', 'start':'20161002', 'conv':1, 'mphys':2},
           'nawdexnwp-20km-mis-0009': {'res':'20km', 'start':'20161013', 'conv':1, 'mphys':1},
           'nawdexnwp-20km-mis-0010': {'res':'20km', 'start':'20161013', 'conv':1, 'mphys':2},
           
           'nawdexnwp-10km-mis-0001': {'res':'10km', 'start':'20160922', 'conv':1, 'mphys':1},
           'nawdexnwp-10km-mis-0002': {'res':'10km', 'start':'20160922', 'conv':1, 'mphys':2},
           'nawdexnwp-10km-mis-0003': {'res':'10km', 'start':'20160922', 'conv':0, 'mphys':1},
           'nawdexnwp-10km-mis-0004': {'res':'10km', 'start':'20160922', 'conv':0, 'mphys':2},
           'nawdexnwp-10km-mis-0005': {'res':'10km', 'start':'20160920', 'conv':1, 'mphys':1},
           'nawdexnwp-10km-mis-0006': {'res':'10km', 'start':'20160920', 'conv':1, 'mphys':2},
           'nawdexnwp-10km-mis-0007': {'res':'10km', 'start':'20160929', 'conv':1, 'mphys':1},
           'nawdexnwp-10km-mis-0008': {'res':'10km', 'start':'20160929', 'conv':1, 'mphys':2},
           'nawdexnwp-10km-mis-0009': {'res':'10km', 'start':'20161002', 'conv':1, 'mphys':1},
           'nawdexnwp-10km-mis-0010': {'res':'10km', 'start':'20161002', 'conv':1, 'mphys':2},
           'nawdexnwp-10km-mis-0011': {'res':'10km', 'start':'20161013', 'conv':1, 'mphys':1},
           'nawdexnwp-10km-mis-0012': {'res':'10km', 'start':'20161013', 'conv':1, 'mphys':2},
           
           'nawdexnwp-5km-mis-0001':  {'res':'5km', 'start':'20160922', 'conv':1, 'mphys':1},
           'nawdexnwp-5km-mis-0002':  {'res':'5km', 'start':'20160922', 'conv':1, 'mphys':2},
           'nawdexnwp-5km-mis-0003':  {'res':'5km', 'start':'20160922', 'conv':0, 'mphys':1},
           'nawdexnwp-5km-mis-0004':  {'res':'5km', 'start':'20160922', 'conv':0, 'mphys':2},
           'nawdexnwp-5km-mis-0005':  {'res':'5km', 'start':'20160920', 'conv':1, 'mphys':1},
           'nawdexnwp-5km-mis-0006':  {'res':'5km', 'start':'20160920', 'conv':1, 'mphys':2},
           'nawdexnwp-5km-mis-0007':  {'res':'5km', 'start':'20160929', 'conv':1, 'mphys':1},
           'nawdexnwp-5km-mis-0008':  {'res':'5km', 'start':'20160929', 'conv':1, 'mphys':2},
           'nawdexnwp-5km-mis-0009':  {'res':'5km', 'start':'20161002', 'conv':1, 'mphys':1},
           'nawdexnwp-5km-mis-0010':  {'res':'5km', 'start':'20161002', 'conv':1, 'mphys':2},
           'nawdexnwp-5km-mis-0011':  {'res':'5km', 'start':'20161013', 'conv':1, 'mphys':1},
           'nawdexnwp-5km-mis-0012':  {'res':'5km', 'start':'20161013', 'conv':1, 'mphys':2},
           
           'nawdexnwp-2km-mis-0001':  {'res':'2km', 'start':'20160922', 'conv':0, 'mphys':1},
           'nawdexnwp-2km-mis-0002':  {'res':'2km', 'start':'20160922', 'conv':0, 'mphys':2},
           'nawdexnwp-2km-mis-0003':  {'res':'2km', 'start':'20160922', 'conv':1, 'mphys':1},
           'nawdexnwp-2km-mis-0004':  {'res':'2km', 'start':'20160922', 'conv':1, 'mphys':2},
           'nawdexnwp-2km-mis-0005':  {'res':'2km', 'start':'20160920', 'conv':0, 'mphys':1},
           'nawdexnwp-2km-mis-0006':  {'res':'2km', 'start':'20160920', 'conv':0, 'mphys':2},
           'nawdexnwp-2km-mis-0007':  {'res':'2km', 'start':'20160929', 'conv':0, 'mphys':1},
           'nawdexnwp-2km-mis-0008':  {'res':'2km', 'start':'20160929', 'conv':0, 'mphys':2},
           'nawdexnwp-2km-mis-0009':  {'res':'2km', 'start':'20161002', 'conv':0, 'mphys':1},
           'nawdexnwp-2km-mis-0010':  {'res':'2km', 'start':'20161002', 'conv':0, 'mphys':2},
           'nawdexnwp-2km-mis-0011':  {'res':'2km', 'start':'20161013', 'conv':0, 'mphys':1},
           'nawdexnwp-2km-mis-0012':  {'res':'2km', 'start':'20161013', 'conv':0, 'mphys':2},
        
           # simulations with only shallow convection scheme enabled
           'nawdexnwp-2km-mis-0001-shcon':  {'res':'2km', 'start':'20160922', 'conv':2, 'mphys':1},
           'nawdexnwp-2km-mis-0002-shcon':  {'res':'2km', 'start':'20160922', 'conv':2, 'mphys':2},
           'nawdexnwp-2km-mis-0005-shcon':  {'res':'2km', 'start':'20160920', 'conv':2, 'mphys':1},
           'nawdexnwp-2km-mis-0006-shcon':  {'res':'2km', 'start':'20160920', 'conv':2, 'mphys':2},
           'nawdexnwp-2km-mis-0007-shcon':  {'res':'2km', 'start':'20160929', 'conv':2, 'mphys':1},
           'nawdexnwp-2km-mis-0008-shcon':  {'res':'2km', 'start':'20160929', 'conv':2, 'mphys':2},
           'nawdexnwp-2km-mis-0009-shcon':  {'res':'2km', 'start':'20161002', 'conv':2, 'mphys':1},
           'nawdexnwp-2km-mis-0010-shcon':  {'res':'2km', 'start':'20161002', 'conv':2, 'mphys':2},
           'nawdexnwp-2km-mis-0011-shcon':  {'res':'2km', 'start':'20161013', 'conv':2, 'mphys':1},
           'nawdexnwp-2km-mis-0012-shcon':  {'res':'2km', 'start':'20161013', 'conv':2, 'mphys':2}
          }

    return simdict

# create dictionary for the days to be analyzed depending on the start date of a simulation
# in this way, we eliminate the first day from the analysis, and we also simulate "extra" days
# that might be available for some but not all simulations
def anadaysdictionary():
    anadaysdict = {
           '20160920': ['2016-09-21', '2016-09-22'],
           '20160922': ['2016-09-23', '2016-09-24', '2016-09-25'],
           '20160929': ['2016-09-30', '2016-10-01', '2016-10-02'],
           '20161002': ['2016-10-03', '2016-10-04', '2016-10-05'],
           '20161013': ['2016-10-14', '2016-10-15', '2016-10-16']
                  }
    return anadaysdict
