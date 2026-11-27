from spm._runtime import Runtime


def spm_mci_fixed(*args, **kwargs):
    r"""
      Group fixed effects estimation  
        FORMAT [Psamp,noise,M] = spm_mci_fixed (mcmc,w,fixed,noise,M,U,Y)  
         
        mcmc      Sampling parameters  
        w(:,n)    Random effects for nth subject  
        fixed     [fixed.pE, fixed.pC] prior over fixed effects  
        noise     noise structure  
        M,U,Y     Model, input, data structures  
         
        Psamp     Samples, [maxits x M{1}.Np]   
        noise     updated noise model  
        M         updated model structures  
         
        Uses Langevin Monte Carlo  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/inference/spm_mci_fixed.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mci_fixed", *args, **kwargs)
