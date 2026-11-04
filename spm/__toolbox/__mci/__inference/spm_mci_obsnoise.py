from spm._runtime import Runtime


def spm_mci_obsnoise(*args, **kwargs):
    r"""
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/inference/spm_mci_obsnoise.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mci_obsnoise", *args, **kwargs)
