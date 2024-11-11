from spm.__wrapper__ import Runtime


def _volumefillholes(*args, **kwargs):
    """
      VOLUMEFILLHOLES is a helper function for segmentations  
         
        See also VOLUMETHRESHOLD, VOLUMESMOOTH, VOLUMEPAD, VOLUMESELECTLARGEST  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/volumefillholes.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("volumefillholes", *args, **kwargs)
