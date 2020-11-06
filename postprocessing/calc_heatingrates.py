# Diagnose all-sky and clear-sky radiative heating rates within the atmosphere from radiative fluxes
#
# The radiative heating rates are calculated by mimicking the relevant ICON code of version icon-2.1.00, which is pasted below for reference:
#
# 1. from subroutine radheat of atm_phy_schemes/mo_radiation.f90:
#    ! Conversion factor for heating rates
#    zconv(jcs:jce,1:klev) = 1._wp/(pmair(jcs:jce,1:klev)*(pcd+(pcv-pcd)*pqv(jcs:jce,1:klev)))
#   
#    !     4.2  Fluxes and heating rates except for lowest layer
#    !
#    pdtdtradsw(jcs:jce,1:klev) = (zflxsw(jcs:jce,1:klev)-zflxsw(jcs:jce,2:klev+1)) * &
#      & zconv(jcs:jce,1:klev)
#    pdtdtradlw(jcs:jce,1:klev) = (zflxlw(jcs:jce,1:klev)-zflxlw(jcs:jce,2:klev+1)) * &
#      & zconv(jcs:jce,1:klev)
# 
# 2. from subroutine compute_airmass
#    p_nh_diag%airmass_now(jc,jk,jb) = p_prog%rho(jc,jk,jb)*p_metrics%ddqz_z_full(jc,jk,jb)
#
# 3. from subroutine set_nh_metrics:
#    p_nh(jg)%metrics%ddqz_z_full(1:nlen,jk,jb) = &
#     & p_nh(jg)%metrics%z_ifc(1:nlen,jk  ,jb)- &
#     & p_nh(jg)%metrics%z_ifc(1:nlen,jk+1,jb)
#    
# 4. from mo_physical_constants:
#    !> Dry air
#    REAL(wp), PARAMETER :: rd    = 287.04_wp        !> [J/K/kg] gas constant
#    REAL(wp), PARAMETER :: cpd   = 1004.64_wp       !! [J/K/kg] specific heat at constant pressure
#    REAL(wp), PARAMETER :: cvd   = cpd-rd           !! [J/K/kg] specific heat at constant volume
#    !> H2O
#    !! - gas
#    REAL(wp), PARAMETER :: rv    = 461.51_wp        !> [J/K/kg] gas constant for water vapor
#    REAL(wp), PARAMETER :: cpv   = 1869.46_wp       !! [J/K/kg] specific heat at constant pressure
#    REAL(wp), PARAMETER :: cvv   = cpv-rv           !! [J/K/kg] specific heat at constant volume
#    
#    note: pcd in radheat is cvd, pcv is cvv
#
# Author: Aiko Voigt, KIT IMK-TRO, 12 Oct 2020

def calc_heatingrates(ds):
    # expected input: xarray dataset that besides the radiative fluxes contains height at interface levels, air density and specific humidity
    # specific heat at constant volume for dry air and water vapor
    pcd = 1004.64 - 287.04
    pcv = 1869.46 - 461.51
    # geometric thickness of full levels, label='lower' for xr.diff is important for correct result
    dz_full = -1*ds['z_ifc'].diff(dim='height_ifc', n=1, label='lower').rename('dz_full').rename({'height_ifc': 'height'})
    # mass of air
    pmair = ds['rho'] * dz_full
    # conversion factor for flux divergence to heating rate
    zconv = 1.0/(pmair*(pcd+(pcv-pcd)*ds['qv']))
    # calculate radiative heating rates from radiative fluxes, use "\_fromflux" to indicate that these were from fluxes
    ds['ddt_temp_radsw_fromflux'] = ( 
        -1*ds['swflxall'].diff(dim='height_ifc', n=1, label='lower').rename({'height_ifc':'height'})*zconv )
    ds['ddt_temp_radlw_fromflux'] = ( 
        -1*ds['lwflxall'].diff(dim='height_ifc', n=1, label='lower').rename({'height_ifc':'height'})*zconv )
    ds['ddt_temp_radswclr_fromflux'] = ( 
        -1*ds['swflxclr'].diff(dim='height_ifc', n=1, label='lower').rename({'height_ifc':'height'})*zconv )
    ds['ddt_temp_radlwclr_fromflux'] = ( 
        -1*ds['lwflxclr'].diff(dim='height_ifc', n=1, label='lower').rename({'height_ifc':'height'})*zconv )
    return ds
