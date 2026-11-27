from spm._runtime import Runtime


def ft_hastoolbox(*args, **kwargs):
    r"""
      FT_HASTOOLBOX tests whether an external toolbox is installed. Optionally it will  
        try to determine the path to the toolbox and install it automatically.  
         
        Use as  
          [status] = ft_hastoolbox(toolbox, autoadd, silent)  
         
        autoadd = -1 means that it will check and give an error when not yet installed  
        autoadd =  0 means that it will check and give a warning when not yet installed  
        autoadd =  1 means that it will check and give an error if it cannot be added  
        autoadd =  2 means that it will check and give a warning if it cannot be added  
        autoadd =  3 means that it will check but remain silent if it cannot be added  
         
        silent = 0 means that it will give some feedback about adding the toolbox  
        silent = 1 means that it will not give feedback  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/ft_hastoolbox.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_hastoolbox", *args, **kwargs)
