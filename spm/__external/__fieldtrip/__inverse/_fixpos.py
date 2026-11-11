from spm._runtime import Runtime


def _fixpos(*args, **kwargs):
    r"""
      FIXPOS helper function to ensure that meshes are described properly  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/inverse/private/fixpos.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fixpos", *args, **kwargs)
