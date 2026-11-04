from spm._runtime import Runtime


def _select_grad(*args, **kwargs):
    r"""
      SELECT_GRAD make a selection of channels  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/select_grad.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("select_grad", *args, **kwargs)
