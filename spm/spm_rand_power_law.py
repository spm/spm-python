from spm.__wrapper__ import Runtime


def spm_rand_power_law(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_rand_power_law.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_rand_power_law", *args, **kwargs)
