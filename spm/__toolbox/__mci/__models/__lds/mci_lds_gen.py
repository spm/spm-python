from spm.__wrapper__ import Runtime


def mci_lds_gen(*args, **kwargs):
    """
      LDS constrained: generate data  
        FORMAT [Y] = mci_lds_gen (M,U,P)  
         
        M     Model structure  
        U     Inputs  
        P     Parameters  
         
        Y     Data  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/lds/mci_lds_gen.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mci_lds_gen", *args, **kwargs)
