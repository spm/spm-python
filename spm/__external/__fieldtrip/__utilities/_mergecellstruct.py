from spm._runtime import Runtime


def _mergecellstruct(*args, **kwargs):
    r"""
      MERGECELLSTRUCT is a helper function for FT_TEST  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/mergecellstruct.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mergecellstruct", *args, **kwargs)
