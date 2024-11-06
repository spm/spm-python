from spm.__wrapper__ import Runtime


def spm_mix_demo1d(*args, **kwargs):
    """
      Demonstrate use of spm_mix on 1D data  
        FORMAT [vbmix logev mixdata] = spm_mix_demo1d (data, maxcomps, plotfits)  
         
        data      - either scalar number of clusters to simulate or your own data  
        maxcomps  - maximum number of components in mixture model to consider  
        verbosity - 0 = silent, 1 = basic output (with figures), 2 = full output  
         
        vbmix     - cell array of fitted mixtures for all numbers of components  
        logev     - log evidence for each number of components  
        mix       - mix structure for simulated mixtures if scalar data given  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mixture/spm_mix_demo1d.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mix_demo1d", *args, **kwargs)
