from spm._runtime import Runtime


def spm_cornsweet(*args, **kwargs):
    r"""
      generative model for psychophysical responses  
        FORMAT [y] = spm_cornsweet(P,M,U)  
        P  - model parameters  
        M  - model  
        %  
         y{1} - matched contrast level for Cornsweet effect  
         y{2} - probability of seeing Mach bands  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_cornsweet.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cornsweet", *args, **kwargs)
