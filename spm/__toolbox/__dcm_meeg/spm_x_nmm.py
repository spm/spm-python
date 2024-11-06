from spm.__wrapper__ import Runtime


def spm_x_nmm(*args, **kwargs):
    """
      Initialise a state structure for a mean field model  
        FORMAT [x,M] = spm_x_nmm(P)  
         
        P - parameter structure  
        M - model structure  
         
        x        - array of states  
        x(i,j,k) - k-th state of j-th population on i-th source  
         
          population: 1 - excitatory spiny stellate cells (input cells)  
                      2 - inhibitory interneurons  
                      3 - excitatory pyramidal cells      (output cells)  
         
               state: 1 V  - voltage  
                      2 gE - conductance (excitatory)  
                      3 gI - conductance (inhibitory)  
         
        M - model structure  
         
        see also: spm_x_mfm  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_x_nmm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_x_nmm", *args, **kwargs)
