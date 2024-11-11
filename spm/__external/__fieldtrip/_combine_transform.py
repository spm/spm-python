from spm.__wrapper__ import Runtime


def _combine_transform(*args, **kwargs):
    """
      COMBINE_TRANSFORM combines the 4x4 homogenous transformation  
        matrices of the rotation, the scaling and the translation and  
        combines them in the desired order.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/combine_transform.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("combine_transform", *args, **kwargs)
