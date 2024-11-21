from spm.__wrapper__ import Runtime


def _loadvar(*args, **kwargs):
    """
      LOADVAR is a helper function for cfg.inputfile  
         
        See also SAVEVAR  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/loadvar.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("loadvar", *args, **kwargs)
