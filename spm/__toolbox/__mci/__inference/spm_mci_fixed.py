from spm.__wrapper__ import Runtime


def spm_mci_fixed(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_fixed.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_fixed", *args, **kwargs)
