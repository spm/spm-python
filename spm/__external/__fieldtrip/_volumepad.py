from spm._runtime import Runtime


def _volumepad(*args, **kwargs):
    r"""
      VOLUMEPAR is a helper function for segmentations. It adds a layer on all sides to  
        ensure that the tissue can be meshed all the way up to the edges this also ensures  
        that the mesh at the bottom of the neck will be closed.  
         
        See also VOLUMEFILLHOLES, VOLUMESMOOTH, VOLUMETHRESHOLD  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/volumepad.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("volumepad", *args, **kwargs)
