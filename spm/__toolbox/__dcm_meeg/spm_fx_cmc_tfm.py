from spm.__wrapper__ import Runtime


def spm_fx_cmc_tfm(*args, **kwargs):
    """
      State equations for a neural mass model (canonical microcircuit)  
        FORMAT [f,J,D]  = spm_fx_cmc_tfm(x,u,P,M)  
        FORMAT [f,J]    = spm_fx_cmc_tfm(x,u,P,M)  
        FORMAT [f]      = spm_fx_cmc_tfm(x,u,P,M)  
         
        x      - state vector  
          x(:,1) - voltage     (spiny stellate cells)  
          x(:,2) - conductance (spiny stellate cells)  
          x(:,3) - voltage     (superficial pyramidal cells)  
          x(:,4) - conductance (superficial pyramidal cells)  
          x(:,5) - current     (inhibitory interneurons)  
          x(:,6) - conductance (inhibitory interneurons)  
          x(:,7) - voltage     (deep pyramidal cells)  
          x(:,8) - conductance (deep pyramidal cells)  
        u        - exogenous input  
         
        f  - dx(t)/dt  = f(x(t))  
        J  - df(t)/dx(t)  
        D  - delay operator dx(t)/dt = f(x(t - d))  
                                           = D(d)*f(x(t))  
         
        FORMAT [u,v,w] = spm_fx_cmc_tfm(x,u,P,M,'activity')  
        u  - intrinsic presynaptic input (inhibitory)  
        v  - intrinsic presynaptic input (excitatory)  
        w  - extrinsic presynaptic input  
         
        Prior fixed parameter scaling [Defaults]  
         
        E  = (forward and backward) extrinsic rates   
        G  = intrinsic rates  
        D  = propagation delays (intrinsic, extrinsic)  
        T  = synaptic time constants  
        R  = slope of sigmoid activation function  
         
       __________________________________________________________________________  
        David O, Friston KJ (2003) A neural mass model for MEG/EEG: coupling and  
        neuronal dynamics. NeuroImage 20: 1743-1755  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_fx_cmc_tfm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_fx_cmc_tfm", *args, **kwargs)
