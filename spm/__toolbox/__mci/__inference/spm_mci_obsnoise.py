from spm.__wrapper__ import Runtime


def spm_mci_obsnoise(*args, **kwargs):
    """
      Update observation noise  
        FORMAT [noise,M] = spm_mci_obsnoise (w,v,assign,noise,M,U,Y)  
         
        w         random effects  
        v         fixed effects  
        assign    for dynamical models this structure specifies whether init  
                  states, flow and o/p params are random, fixed or known  
        noise     observation noise structure  
        M         model structures  
        U         input structures  
        Y         data structures  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_obsnoise.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_obsnoise", *args, **kwargs)
