from spm._runtime import Runtime


def spm_SHC_fx(*args, **kwargs):
    r"""
      equations of motion for Lotka-Volterra dynamics  
        FORMAT [f] = spm_SHC_fx(x,v,P)  
         
        x   - hidden states  
        v   - exogenous inputs  
        P.f - lateral connectivity  
        P.k - rate [default 1]  
         
        returns f = dx/dt = P.f*S(x) - x/8 + 1;  
                     S(x) = 1./(1 + exp(-x))  
         
        where C determines the order of unstable fixed points visited in the  
        stable heteroclinic channel.  
         
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_SHC_fx.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_SHC_fx", *args, **kwargs)
