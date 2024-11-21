from spm.__wrapper__ import Runtime


def spm_fx_sep(*args, **kwargs):
    """
      State equations for a neural mass model of erps  
        FORMAT [f,J,D] = spm_fx_sep(x,u,P,M)  
        FORMAT [f,J]   = spm_fx_sep(x,u,P,M)  
        FORMAT [f]     = spm_fx_sep(x,u,P,M)  
        x      - state vector  
          x(:,1) - voltage (spiny stellate cells)  
          x(:,2) - voltage (pyramidal cells) +ve  
          x(:,3) - voltage (pyramidal cells) -ve  
          x(:,4) - current (spiny stellate cells)    depolarizing  
          x(:,5) - current (pyramidal cells)         depolarizing  
          x(:,6) - current (pyramidal cells)         hyperpolarizing  
          x(:,7) - voltage (inhibitory interneurons)  
          x(:,8) - current (inhibitory interneurons) depolarizing  
          x(:,9) - voltage (pyramidal cells)  
         
        f        - dx(t)/dt  = f(x(t))  
        J        - df(t)/dx(t)  
        D        - delay operator dx(t)/dt = f(x(t - d))  
                                           = D(d)*f(x(t))  
         
        Prior fixed parameter scaling [Defaults]  
         
         M.pF.E = [32 16 4];           % extrinsic rates (forward, backward, lateral)  
         M.pF.H = [1 1 1 1/4]*128;     % intrinsic rates (g1, g2 g3, g4)  
         M.pF.D = [1 16];              % propagation delays (intrinsic, extrinsic)  
         M.pF.G = [4 64];              % receptor densities (excitatory, inhibitory)  
         M.pF.T = [4 8];               % synaptic constants (excitatory, inhibitory)  
         M.pF.R = [1 0];               % parameter of static nonlinearity  
         
        This is just a faster version of spm_fx_erp  
         
       __________________________________________________________________________  
        David O, Friston KJ (2003) A neural mass model for MEG/EEG: coupling and  
        neuronal dynamics. NeuroImage 20: 1743-1755  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_fx_sep.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_fx_sep", *args, **kwargs)
