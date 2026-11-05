from spm._runtime import Runtime


def spm_MDP_arcade(*args, **kwargs):
    r"""
      Creates an MDP structure for a simple arcade game  
        FORMAT [MDP,RGB] = spm_MDP_arcade(Nr,Nc,Nd,Nb)  
       --------------------------------------------------------------------------  
        Nr    - number of rows  
        Nc    - number of columns  
        Nd    - number of initial states [default: 1]  
        Np    - number of bombs  
         
        RGB   - display structure  
         
        outcomes(1) - paddle  
        outcomes(2) - ball  
        outcomes(3) - target  
        outcomes(4) - bomb  
        outcomes(5) - background  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_MDP_arcade.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_MDP_arcade", *args, **kwargs)
