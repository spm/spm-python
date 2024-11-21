from spm.__wrapper__ import Runtime


def spm_fp_cmc_tfm(*args, **kwargs):
    """
      Parameter equations for a neural mass model (canonical microcircuit)  
        FORMAT [f] = spm_fp_cmc_tfm(x,u,P,M)  
         
        x      - state vector  
          x(:,1) - voltage     (spiny stellate cells)  
          x(:,2) - conductance (spiny stellate cells)  
          x(:,3) - voltage     (superficial pyramidal cells)  
          x(:,4) - conductance (superficial pyramidal cells)  
          x(:,5) - voltage     (inhibitory interneurons)  
          x(:,6) - conductance (inhibitory interneurons)  
          x(:,7) - voltage     (deep pyramidal cells)  
          x(:,8) - conductance (deep pyramidal cells)  
         
        f        - dP = h(x(t),u(t),P,M)  
         
        Prior fixed parameter scaling  
         
        G  = intrinsic rates  
        D  = propagation delays (intrinsic, extrinsic)  
        T  = synaptic time constants  
        R  = slope of sigmoid activation function  
         
       __________________________________________________________________________  
        David O, Friston KJ (2003) A neural mass model for MEG/EEG: coupling and  
        neuronal dynamics. NeuroImage 20: 1743-1755  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_fp_cmc_tfm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_fp_cmc_tfm", *args, **kwargs)
