from spm.__wrapper__ import Runtime


def spm_gen_par(*args, **kwargs):
    """
      Generate condition specific parameters using DCM for M/EEG  
        FORMAT Q = spm_gen_par(P,U)  
         
        P - parameters  
          P.xc - the index of the condition of interest  
        U - trial-effects  
          U.X  - between-trial effects (encodes the number of trials)  
          U.dt - time bins for within-trial effects  
         
        Q - Condition specific parameters   
       __________________________________________________________________________  
        Jafarian, A., Litvak, V., Cagnan, H., Friston, K.J. and Zeidman, P., 2019.  
        Neurovascular coupling: insights from multi-modal dynamic causal modelling  
        of fMRI and MEG. arXiv preprint arXiv:1903.07478.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/NVC/spm_gen_par.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_gen_par", *args, **kwargs)
