from spm.__wrapper__ import Runtime


def pm_smooth_phasemap(*args, **kwargs):
    """
      Performs a weighted (by 1/angvar) gaussian smoothing of a phasemap  
        FORMAT pm = pm_smooth_phasemap(pm,angvar,vxs,fwhm)  
         
        Input:  
        pm         : Phase-map  
        angvar     : Map of uncertainty of the angular estimate.  
        vxs        : Voxel sizes (mm) in the three directions.  
        fwhm       : FWHM (mm) of gaussian kernel for the three  
                     directions (or scalar for isotropic kernel).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/FieldMap/pm_smooth_phasemap.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("pm_smooth_phasemap", *args, **kwargs)
