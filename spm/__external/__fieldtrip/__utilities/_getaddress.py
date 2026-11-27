from spm._runtime import Runtime


def _getaddress(*args, **kwargs):
    r"""
      GETADDRESS returns the IP address  
         
        Use as  
          address = getaddress();  
        or  
          address = getaddress(hostname);  
         
        See also GETUSERNAME, GETHOSTNAME  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/getaddress.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("getaddress", *args, **kwargs)
