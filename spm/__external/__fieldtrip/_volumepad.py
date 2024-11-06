from spm.__wrapper__ import Runtime


def _volumepad(*args, **kwargs):
    """
      VOLUMEPAR is a helper function for segmentations. It adds a layer on all sides to  
        ensure that the tissue can be meshed all the way up to the edges this also ensures  
        that the mesh at the bottom of the neck will be closed.  
         
        See also VOLUMEFILLHOLES, VOLUMESMOOTH, VOLUMETHRESHOLD  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/volumepad.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("volumepad", *args, **kwargs)
