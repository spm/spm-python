from spm.__wrap__ import _Runtime


def pm_smooth_phasemap(*args, **kwargs):
  """  Performs a weighted (by 1/angvar) gaussian smoothing of a phasemap  
    FORMAT pm = pm_smooth_phasemap(pm,angvar,vxs,fwhm)  
     
    Input:  
    pm         : Phase-map  
    angvar     : Map of uncertainty of the angular estimate.  
    vxs        : Voxel sizes (mm) in the three directions.  
    fwhm       : FWHM (mm) of gaussian kernel for the three  
                 directions (or scalar for isotropic kernel).  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/FieldMap/pm_smooth_phasemap.m)
  """

  return _Runtime.call("pm_smooth_phasemap", *args, **kwargs)
