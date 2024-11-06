from spm.__wrapper__ import Runtime


def _select3dtool(*args, **kwargs):
    """
     SELECT3DTOOL A simple tool for interactively obtaining 3-D coordinates   
         
        SELECT3DTOOL(FIG) Specify figure handle  
         
        Example:  
          surf(peaks);  
          select3dtool;  
          % click on surface  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/private/select3dtool.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("select3dtool", *args, **kwargs, nargout=0)
