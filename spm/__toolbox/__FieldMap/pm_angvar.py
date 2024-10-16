from spm.__wrapper__ import Runtime


def pm_angvar(*args, **kwargs):
  """  Estimates the (voxelwise) variance of the angle  
    estimated from the complex map cmap.  
    FORMAT: angvar = pm_angvar(cmap)  
     
    Input:  
    cmap     : Complex-valued MR intensity image. When used to  
               estimate the variance of a delta_phi map estimated  
               from two measurements with different echo-time this  
               should be the image with the longer echo-time.  
     
    Output:  
    angvar   : Map with an estimate of the variance of a phasemap  
               estimated using cmap as one of its constituents.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/FieldMap/pm_angvar.m)
  """

  return Runtime.call("pm_angvar", *args, **kwargs)
