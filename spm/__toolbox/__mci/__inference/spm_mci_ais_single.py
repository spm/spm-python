from spm.__wrapper__ import Runtime


def spm_mci_ais_single(*args, **kwargs):
    """
      Produce a single independent sample using AIS  
        FORMAT [P,E,logw,acc,traj] = spm_mci_ais_single (mcmc,M,U,Y)  
         
        mcmc      Sampling settings  
        M         Model structure  
        U         Input structure  
        Y         Data  
         
        P         [Np x 1] sample  
        E         Negative log joint  
        logw      Contribution to model evidence  
        acc       acc(j) is acceptance rate at temperature j  
        traj      traj(p,j) is value of parameter p at temperature j  
                  (only set if mcmc.rec_traj=1)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_ais_single.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_ais_single", *args, **kwargs)
