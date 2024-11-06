from spm.__wrapper__ import Runtime


def _getusername(*args, **kwargs):
    """
      GETUSERNAME  
         
        Use as  
          str = getusername();  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/getusername.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("getusername", *args, **kwargs)
