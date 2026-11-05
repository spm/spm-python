from spm._runtime import Runtime


def spm_rand_power_law(*args, **kwargs):
    r"""
      Generate random variates with a power law spectral density  
        FORMAT [y,K] = spm_rand_power_law(csd,Hz,dt,N)  
        csd - spectral densities (one per column)  
        Hz  - frequencies  
        dt  - sampling interval  
        N   - number of time bins  
         
        y   - random variate  
        K   - convolution (kernel) operator: y(:,i) = K*randn(N,1)  
         
        see also: spm_rand_mar; spm_Q  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_rand_power_law.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_rand_power_law", *args, **kwargs)
