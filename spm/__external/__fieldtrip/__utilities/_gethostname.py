from spm._runtime import Runtime


def _gethostname(*args, **kwargs):
    """
      HOSTNAME returns the hostname of this computer  
         
        Use as  
          str = hostname;  
         
        See also GETUSERNAME, GETADDRESS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/gethostname.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("gethostname", *args, **kwargs)
