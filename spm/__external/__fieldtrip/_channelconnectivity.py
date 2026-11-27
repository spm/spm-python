from spm._runtime import Runtime


def _channelconnectivity(*args, **kwargs):
    r"""
      CHANNELCONNECTIVIY creates a NxN matrix that describes whether channels  
        are connected as neighbours  
         
        See also FT_PREPARE_NEIGHBOURS, TRIANGLE2CONNECTIVITY  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/channelconnectivity.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("channelconnectivity", *args, **kwargs)
