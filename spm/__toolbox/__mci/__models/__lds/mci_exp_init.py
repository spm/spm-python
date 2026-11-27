from spm._runtime import Runtime


def mci_exp_init(*args, **kwargs):
    r"""
      Exponentially interpolate to t=0  
        FORMAT [w0,a] = mci_exp_init (Y,M,doplot)  
         
        Y         Cell of data from multiple subjects  
                  Y{n}.y, Y{n}.ind for n=1..N  
        M         Model structure  
        doplot    plot fits  
         
        w0        [d x N] matrix of initial states  
                  where d is number of states  
        a         [d x N] matrix of exponential coefficients  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/models/lds/mci_exp_init.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_exp_init", *args, **kwargs)
