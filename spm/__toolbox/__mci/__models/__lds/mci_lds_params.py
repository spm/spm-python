from spm._runtime import Runtime


def mci_lds_params(*args, **kwargs):
    r"""
      LDS constrained: sample params from prior  
        FORMAT [P] = mci_lds_params (M,U)  
         
        M     Model structure  
        U     Inputs  
         
        P     Parameters  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/models/lds/mci_lds_params.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_lds_params", *args, **kwargs)
