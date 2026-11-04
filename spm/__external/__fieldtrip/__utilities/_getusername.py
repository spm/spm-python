from spm._runtime import Runtime


def _getusername(*args, **kwargs):
    r"""
      GETUSERNAME  
         
        Use as  
          str = getusername();  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/getusername.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("getusername", *args, **kwargs)
