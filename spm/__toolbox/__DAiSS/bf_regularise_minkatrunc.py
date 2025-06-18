from mpython import Runtime


def bf_regularise_minkatrunc(*args, **kwargs):
    """
      Bayesian regularisation based on Minka's method
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_regularise_minkatrunc.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_regularise_minkatrunc", *args, **kwargs)
