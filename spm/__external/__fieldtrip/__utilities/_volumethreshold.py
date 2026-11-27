from spm._runtime import Runtime


def _volumethreshold(*args, **kwargs):
    r"""
      VOLUMETHRESHOLD is a helper function for segmentations. It applies a  
        relative threshold and subsequently looks for the largest connected part,  
        thereby removing small blobs such as vitamine E capsules.  
         
        See also VOLUMEFILLHOLES, VOLUMESMOOTH, VOLUMEPAD  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/volumethreshold.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("volumethreshold", *args, **kwargs)
