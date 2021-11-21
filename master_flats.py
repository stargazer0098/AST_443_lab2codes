#!/usr/bin/env python

import numpy as np
from astropy.io import fits


hdu1=fits.open('Dark_new2.00000469.FIT')
hdu2=fits.open('Dark_new2.00000470.FIT')
hdu3=fits.open('Dark_new2.00000471.FIT')
hdu4=fits.open('Dark_new2.00000472.FIT')
hdu5=fits.open('Dark_new2.00000473.FIT')
hdu6=fits.open('Dark_new2.00000474.FIT')
hdu7=fits.open('Dark_new2.00000475.FIT')
hdu8=fits.open('Dark_new2.00000476.FIT')
hdu9=fits.open('Dark_new2.00000477.FIT')
hdu10=fits.open('Dark_new2.00000478.FIT')


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
#newhdu.writeto('master_flat.fits')


hdu11=fits.open('master_flat.fits')

imagedata1=hdu1[0].data

mode_norm_mas_flat=imagedata1/19019.0
newhdu = fits.PrimaryHDU(mode_norm_mas_flat)
newhdu.writeto('mode_norm_mas_flat.fits',overwrite=True)
