from spm._runtime import Runtime


def _select3dtool(*args, **kwargs):
    r"""
     SELECT3DTOOL A simple tool for interactively obtaining 3-D coordinates   
         
        SELECT3DTOOL(FIG) Specify figure handle  
         
        Example:  
          surf(peaks);  
          select3dtool;  
          % click on surface  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/plotting/private/select3dtool.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("select3dtool", *args, **kwargs, nargout=0)
