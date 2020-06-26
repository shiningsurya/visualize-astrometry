import numpy as np
import matplotlib.pyplot as plt
import astropy.time as at
import astropy.coordinates as asc
import astropy.units as au
#################################################
def get_altaz_moon (el, times):
    """given astropy.coordinates.EarthLocation and astropy.Time 
    computes alt az
    """
    MOON    = asc.get_moon (times, el)
    AA      = asc.AltAz (obstime=times, location=el)
    AAM     = MOON.transform_to (AA)
    return AAM.alt, AAM.az
def get_radec_moon (el, times):
    """given astropy.coordinates.EarthLocation and astropy.Time 
    computes ra/dec
    """
    MOON    = asc.get_moon (times, el)
    AAM     = MOON.transform_to (asc.ICRS)
    return AAM.ra, AAM.dec
#################################################
def setup_plot (ax, lims=False, lines=False, legend=False):
    """setups the plot"""
    ## labels
    ax.set_xlabel ('Azimuth [deg]')
    ax.set_ylabel ('Altitude [deg]')
    if lines:
        ## lines
        ax.axhline (0,   label='Horizon', c='k', ls=':')
        ax.axvline (0,   label='North',   c='r', ls='--')
        ax.axvline (90,  label='East',    c='g', ls='--')
        ax.axvline (180, label='South',   c='b', ls='--')
        ax.axvline (270, label='West',    c='m', ls='--')
    if lims:
        ## lim
        ax.set_xlim (-5, 360)
        ax.set_ylim (-90, 90)
        ## ticks
        ax.set_xticks (np.arange (0, 360+60, 60))
        ax.set_yticks (np.arange (-90, 90+30, 30))
    if legend:
        ## legend
        ax.legend (loc='best')
#################################################
def plot_single (alt, az, ax, toffset=1.0, label=None, c='b'):
    """plots"""
    ax.scatter (az, alt, label=label, c=c)
    ## text
    for x, y, t in zip (az.value.tolist(), alt.value.tolist(), np.arange(len(alt))):
        ax.text (x+toffset, y+toffset, str(t+1))
#################################################
