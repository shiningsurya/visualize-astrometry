import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mc
import astropy.time as at
import astropy.coordinates as asc
import astropy.units as au
from   functions import get_altaz_moon
from   functions import plot_single
from   functions import setup_plot
#################################################
LONG    = asc.Angle (0, unit='degree')
LSTEP   = 30
LATS    = asc.Angle (np.arange (-90, 90+LSTEP, LSTEP), unit='degree')
HEIGHT  = 10 * au.meter
#################################################
TSTART  = at.Time ('2020-02-01T20:22:12', format='isot')
# TSTEP   = 1.0 * au.day
TSTEP   = (1.0*au.day) + (50.0*au.minute) + (29.0*au.second)
NSTEP   = 30
TRANGE  = TSTART + (TSTEP * np.arange(NSTEP))
#################################################
#### For a range of latitudes,  1000m above the see level
lalt    = dict()
laz     = dict()
for LAT in LATS:
    EQK            = asc.EarthLocation (LONG, LAT, HEIGHT)
    eq_alt, eq_az  = get_altaz_moon (EQK, TRANGE)
    lalt[LAT]      = eq_alt
    laz[LAT]       = eq_az
#################################################
## plotting
plt.ion()
fig = plt.figure ()
ax  = fig.add_subplot (111)
norm= mc.Normalize (vmin=-90, vmax=90)
cmap=plt.cm.jet
sc  = plt.cm.ScalarMappable (norm=norm, cmap=cmap)
for LAT in LATS:
    plot_single (lalt[LAT], laz[LAT], ax, c=sc.to_rgba (LAT))
setup_plot (ax)
fig.colorbar (sc, orientation='horizontal', label='Latitude [deg]')
ax.set_title ("Analemma at multiple latitudes")
fig.tight_layout ()
fig.savefig ("analemma_moon_multiple.png", dpi=300)
