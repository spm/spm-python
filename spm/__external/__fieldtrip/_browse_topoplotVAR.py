from spm._runtime import Runtime


def _browse_topoplotVAR(*args, **kwargs):
    r"""
      BROWSE_TOPOPLOTVAR is a simple helper function for FT_DATABROWSER that  
        computes the variance of band-pass filtered data and makes a topographic  
        plot. It serves to make a quick-and-dirty power topography.  
         
        See also BROWSE_MOVIEPLOTER, BROWSE_TOPOPLOTER, BROWSE_MULTIPLOTER, BROWSE_TOPOPLOTVAR, BROWSE_SIMPLEFFT  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/browse_topoplotVAR.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("browse_topoplotVAR", *args, **kwargs, nargout=0)
