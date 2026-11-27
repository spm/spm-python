from spm._runtime import Runtime


def pm_smooth_phasemap(*args, **kwargs):
    r"""
      Performs a weighted (by 1/angvar) gaussian smoothing of a phasemap  
        FORMAT pm = pm_smooth_phasemap(pm,angvar,vxs,fwhm)  
         
        Input:  
        pm         : Phase-map  
        angvar     : Map of uncertainty of the angular estimate.  
        vxs        : Voxel sizes (mm) in the three directions.  
        fwhm       : FWHM (mm) of gaussian kernel for the three  
                     directions (or scalar for isotropic kernel).  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/FieldMap/pm_smooth_phasemap.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("pm_smooth_phasemap", *args, **kwargs)
