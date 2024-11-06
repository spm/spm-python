from spm.__wrapper__ import Runtime


def _smooth_source(*args, **kwargs):
    """
     [SOURCE] = SMOOTH(SOURCE, VARARGIN)  
         
        computes location specific 3D gaussian kernels based on a FWHM estimate  
         source should contain the fields   
           fwhm, specifying for each voxel the FWHM of the smoothing kernel in the xyz-direction  
           pos,  allowing for the units to be correct  
         
         key-value pairs should contain  
           parameter = string, field to be used for the smoothing  
           maxdist   = scalar, maximum distance for filter kernel  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/smooth_source.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("smooth_source", *args, **kwargs)
