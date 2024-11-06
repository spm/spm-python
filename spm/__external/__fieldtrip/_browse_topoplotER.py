from spm.__wrapper__ import Runtime


def _browse_topoplotER(*args, **kwargs):
    """
      BROWSE_TOPOPLOTER is a simple helper function for FT_DATABROWSER and shows  
        the average topography of the selected data.  
         
        See also BROWSE_MOVIEPLOTER, BROWSE_TOPOPLOTER, BROWSE_MULTIPLOTER, BROWSE_TOPOPLOTVAR, BROWSE_SIMPLEFFT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/browse_topoplotER.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("browse_topoplotER", *args, **kwargs, nargout=0)
