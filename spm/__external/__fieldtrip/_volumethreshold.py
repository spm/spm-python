from spm.__wrapper__ import Runtime


def _volumethreshold(*args, **kwargs):
    """
      VOLUMETHRESHOLD is a helper function for segmentations. It applies a  
        relative threshold and subsequently looks for the largest connected part,  
        thereby removing small blobs such as vitamine E capsules.  
         
        See also VOLUMEFILLHOLES, VOLUMESMOOTH, VOLUMEPAD  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/volumethreshold.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("volumethreshold", *args, **kwargs)
