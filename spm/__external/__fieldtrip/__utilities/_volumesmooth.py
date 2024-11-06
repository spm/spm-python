from spm.__wrapper__ import Runtime


def _volumesmooth(*args, **kwargs):
    """
      VOLUMESMOOTH is a helper function for segmentations  
         
        See also VOLUMETHRESHOLD, VOLUMEFILLHOLES  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/volumesmooth.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("volumesmooth", *args, **kwargs)
