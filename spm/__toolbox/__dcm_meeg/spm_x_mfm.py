from spm.__wrapper__ import Runtime


def spm_x_mfm(*args, **kwargs):
    """
      Initialise a state structure for a mean field model  
        FORMAT [x,M] = spm_x_mfm(P)  
         
        P - parameter structure (encoding extrinsic connections)  
        M - model structure  
         
        x - states and covariances  
        M - model structure  
         
        x{1}(i,j,k)   - k-th state of i-th source in j-th population  
        x{2}(i,j,k,l) - covariance of i-th and j-th state (k-th source in l-th  
                        population  
         
          population: 1 - excitatory spiny stellate cells (input cells)  
                      2 - inhibitory interneurons  
                      3 - excitatory pyramidal cells      (output cells)  
         
               state: 1 V  - voltage  
                      2 gE - conductance (excitatory)  
                      3 gI - conductance (inhibitory)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_x_mfm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_x_mfm", *args, **kwargs)
