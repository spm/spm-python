from spm.__wrapper__ import Runtime


def _channelconnectivity(*args, **kwargs):
    """
      CHANNELCONNECTIVIY creates a NxN matrix that describes whether channels  
        are connected as neighbours  
         
        See also FT_PREPARE_NEIGHBOURS, TRIANGLE2CONNECTIVITY  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/channelconnectivity.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("channelconnectivity", *args, **kwargs)
