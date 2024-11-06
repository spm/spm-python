from spm.__wrapper__ import Runtime


def spm_cornsweet(*args, **kwargs):
    """
      generative model for psychophysical responses  
        FORMAT [y] = spm_cornsweet(P,M,U)  
        P  - model parameters  
        M  - model  
        %  
         y{1} - matched contrast level for Cornsweet effect  
         y{2} - probability of seeing Mach bands  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_cornsweet.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_cornsweet", *args, **kwargs)
