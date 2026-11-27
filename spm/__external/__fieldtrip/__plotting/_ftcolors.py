from spm._runtime import Runtime


def _ftcolors(*args, **kwargs):
    r"""
      FTCOLORS returns an Nx3 rgb matrix with the  
        colors of the fieldtrip logo at its extremes.  
        Can be used as a colormap by FT_COLORMAP  
         
        Use as:  
          rgb = ftcolors(N), or  
          rgb = ftcolors  
         
        Without input arguments, N will be set to 64  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/plotting/private/ftcolors.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ftcolors", *args, **kwargs)
