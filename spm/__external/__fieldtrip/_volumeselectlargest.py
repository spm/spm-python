from spm._runtime import Runtime


def _volumeselectlargest(*args, **kwargs):
    r"""
      VOLUMESELECTLARGEST is a helper function for segmentations  
         
        See also VOLUMEFILLHOLES, VOLUMETHRESHOLD, VOLUMESMOOTH, VOLUMEPAD  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/volumeselectlargest.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("volumeselectlargest", *args, **kwargs)
