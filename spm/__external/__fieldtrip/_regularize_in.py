from spm._runtime import Runtime


def _regularize_in(*args, **kwargs):
    r"""
    regularize_in is a function.  
          [in_removes, out_removes] = regularize_in(int_order, ext_order, S, ismag, extended_remove)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/regularize_in.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("regularize_in", *args, **kwargs)
