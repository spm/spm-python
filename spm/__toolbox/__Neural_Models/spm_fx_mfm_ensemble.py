from spm.__wrapper__ import Runtime


def spm_fx_mfm_ensemble(*args, **kwargs):
    """
      state equations for a mean-field model  
        FORMAT [f] = spm_fx_mfm_ensemble(x,u,P)  
         
        X{i} - states and covariances of i-th particle x  
         
        x{1}(i,j,k)   - k-th state of j-th population on i-th source  
        x{2}(i,j,k,l) - covariance of l-th and k-th state  
         
          population: 1 - excitatory spiny stellate cells (input cells)  
                      2 - inhibitory interneurons  
                      3 - excitatory pyramidal cells      (output cells)  
         
               state: 1 V  - voltage  
                      2 gE - conductance (excitatory)  
                      3 gI - conductance (inhibitory)  
         
       --------------------------------------------------------------------------  
        refs:  
         
        Marreiros et al (2008) Population dynamics under the Laplac assumption   
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/spm_fx_mfm_ensemble.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_fx_mfm_ensemble", *args, **kwargs)
