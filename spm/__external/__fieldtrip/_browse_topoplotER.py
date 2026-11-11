from spm._runtime import Runtime


def _browse_topoplotER(*args, **kwargs):
    r"""
      BROWSE_TOPOPLOTER is a simple helper function for FT_DATABROWSER and shows  
        the average topography of the selected data.  
         
        See also BROWSE_MOVIEPLOTER, BROWSE_TOPOPLOTER, BROWSE_MULTIPLOTER, BROWSE_TOPOPLOTVAR, BROWSE_SIMPLEFFT  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/browse_topoplotER.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("browse_topoplotER", *args, **kwargs, nargout=0)
