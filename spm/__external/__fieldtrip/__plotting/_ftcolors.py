from spm.__wrapper__ import Runtime


def _ftcolors(*args, **kwargs):
    """
      FTCOLORS returns an Nx3 rgb matrix with the  
        colors of the fieldtrip logo at its extremes.  
        Can be used as a colormap by FT_COLORMAP  
         
        Use as:  
          rgb = ftcolors(N), or  
          rgb = ftcolors  
         
        Without input arguments, N will be set to 64  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/private/ftcolors.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ftcolors", *args, **kwargs)
