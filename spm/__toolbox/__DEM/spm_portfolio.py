from spm._runtime import Runtime


def spm_portfolio(*args, **kwargs):
    r"""
      FORMAT spm_portfolio(L,DEM)  
        simulate portfolio managment  
       --------------------------------------------------------------------------  
        L   - rate of log return per week  
        I   - indicator variables  
        U   - exogenous variables  
        DEM - generative model  
        T   - time of inital investment  
        dT  - time between rebalancing  
        Sr  - Shaarpe ratio  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_portfolio.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_portfolio", *args, **kwargs)
