from spm.__wrapper__ import Runtime


def _neuralynx_getheader(*args, **kwargs):
    """
     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  
        SUBFUNCTION for reading the 16384 byte header from any Neuralynx file  
       %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/neuralynx_getheader.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("neuralynx_getheader", *args, **kwargs)
