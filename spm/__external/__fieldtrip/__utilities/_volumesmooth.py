from spm._runtime import Runtime


def _volumesmooth(*args, **kwargs):
    r"""
      VOLUMESMOOTH is a helper function for segmentations  
         
        See also VOLUMETHRESHOLD, VOLUMEFILLHOLES  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/volumesmooth.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("volumesmooth", *args, **kwargs)
