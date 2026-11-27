from spm._runtime import Runtime


def _volumefillholes(*args, **kwargs):
    r"""
      VOLUMEFILLHOLES is a helper function for segmentations  
         
        See also VOLUMETHRESHOLD, VOLUMESMOOTH, VOLUMEPAD, VOLUMESELECTLARGEST  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/volumefillholes.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("volumefillholes", *args, **kwargs)
