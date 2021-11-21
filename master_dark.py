#!/usr/bin/env python

import numpy as np
from astropy.io import fits


hdu1=fits.open('dark_40.00000392.DARK.FIT')
hdu2=fits.open('dark_40.00000393.DARK.FIT')
hdu3=fits.open('dark_40.00000394.DARK.FIT')
hdu4=fits.open('dark_40.00000395.DARK.FIT')
hdu5=fits.open('dark_40.00000396.DARK.FIT')
hdu6=fits.open('dark_40.00000397.DARK.FIT')
hdu7=fits.open('dark_40.00000398.DARK.FIT')
hdu8=fits.open('dark_40.00000399.DARK.FIT')
hdu9=fits.open('dark_40.00000400.DARK.FIT')
hdu10=fits.open('dark_40.00000401.DARK.FIT')


imagedata1=hdu1[0].data
imagedata2=hdu2[0].data
imagedata3=hdu3[0].data
imagedata4=hdu4[0].data
imagedata5=hdu5[0].data
imagedata6=hdu6[0].data
imagedata7=hdu7[0].data
imagedata8=hdu8[0].data
imagedata9=hdu9[0].data
imagedata10=hdu10[0].data


allimages=np.array([imagedata1,imagedata2,imagedata3,imagedata4,imagedata5,imagedata6,imagedata7,imagedata8,imagedata9,imagedata10])

median=np.median(allimages,axis=0)

newhdu = fits.PrimaryHDU(median)
newhdu.writeto('master_dark.fits')
