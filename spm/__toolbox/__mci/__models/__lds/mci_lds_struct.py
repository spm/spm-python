from spm.__wrapper__ import Runtime


def mci_lds_struct(*args, **kwargs):
    """
      LDS constrained: Initialise model structure  
        FORMAT [M,U,names] = mci_lds_struct (M)  
         
        M.d       Number of regions  
        M.sd      Observation noise SD  
        M.name    'uncoupled','forward','backward','bidirectional'  
        M.R       Initial state  
        M.t       Vector of Times  
        M.drop    final value as proportion of initial value  
                  eg. 0.5 indicates typical state at M.t(end) is  
                  half of M.t(1). Used to set M.a_typical, typical  
                  self connection values  
         
        M         Model structure  
        U         Inputs  
        names     Names of variables  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/lds/mci_lds_struct.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mci_lds_struct", *args, **kwargs)
