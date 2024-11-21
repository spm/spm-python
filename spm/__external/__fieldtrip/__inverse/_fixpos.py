from spm.__wrapper__ import Runtime


def _fixpos(*args, **kwargs):
    """
      FIXPOS helper function to ensure that meshes are described properly  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/inverse/private/fixpos.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fixpos", *args, **kwargs)
