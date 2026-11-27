from spm._runtime import Runtime


def _gethostname(*args, **kwargs):
    r"""
      HOSTNAME returns the hostname of this computer  
         
        Use as  
          str = hostname;  
         
        See also GETUSERNAME, GETADDRESS  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/gethostname.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("gethostname", *args, **kwargs)
