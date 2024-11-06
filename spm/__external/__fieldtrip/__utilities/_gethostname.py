from spm.__wrapper__ import Runtime


def _gethostname(*args, **kwargs):
    """
      HOSTNAME returns the hostname of this computer  
         
        Use as  
          str = hostname;  
         
        See also GETUSERNAME, GETADDRESS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/gethostname.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("gethostname", *args, **kwargs)
