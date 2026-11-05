from spm._runtime import Runtime


def covLin(*args, **kwargs):
    r"""
      Covariance function for linear regression/classification  
        FORMAT [K1,lambda] = covLin(lambda0,settings,args,lab)  
        No usage documentation yet  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/Shoot/covLin.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("covLin", *args, **kwargs)
