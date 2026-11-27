from spm._runtime import Runtime


def _regularize_out(*args, **kwargs):
    r"""
    regularize_out is a function.  
          [out_remove] = regularize_out(int_order, ext_order, S, ismag, extended_remove)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/regularize_out.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("regularize_out", *args, **kwargs)
