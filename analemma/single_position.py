import numpy as np
import matplotlib.pyplot as plt
import astropy.time as at
import astropy.coordinates as asc
import astropy.units as au
from   functions import get_altaz_moon
from   functions import plot_single
from   functions import setup_plot
#################################################
LONG    = asc.Angle (90, unit='degree')
LAT     = asc.Angle (30, unit='degree')
HEIGHT  = 10 * au.meter
#################################################
TSTART  = at.Time ('2020-02-05T20:22:12', format='isot')
TSTEP   = (1.0*au.day) + (50.0*au.minute) + (29.0*au.second)
# TSTEP   = (1.0*au.day) 
NSTEP   = 30
TRANGE  = TSTART + (TSTEP * np.arange(NSTEP))
#################################################
#### At equator 1000m above the see level
EQK     = asc.EarthLocation (LONG, LAT, HEIGHT)
eq_alt, eq_az    = get_altaz_moon (EQK, TRANGE)
## plotting
fig = plt.figure ()
ax  = fig.add_subplot (111)
plot_single (eq_alt, eq_az, ax)
setup_plot (ax)
ax.set_title ("Analemma at LONG={0} LAT={1}".format(LONG, LAT))
fig.tight_layout ()
fig.savefig ("analemma_moon_single.png", dpi=300)
