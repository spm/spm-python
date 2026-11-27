from spm._runtime import Runtime


def bf_regularise_minkatrunc(*args, **kwargs):
    r"""
      Bayesian regularisation based on Minka's method  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DAiSS/bf_regularise_minkatrunc.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_regularise_minkatrunc", *args, **kwargs)
