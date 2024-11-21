from spm.__wrapper__ import Runtime


def mci_nmm_fx_delay(*args, **kwargs):
    """
      State equations for a neural mass model of erps with first order delays  
        FORMAT [f] = mci_nmm_fx_delay (x,u,P,M)  
         
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
         
        Prior fixed parameter scaling [Defaults]  
         
         M.pF.E = [32 16 4];           % extrinsic rates (forward, backward, lateral)  
         M.pF.H = [1 4/5 1/4 1/4]*128; % intrinsic rates (g1, g2 g3, g4)  
         M.pF.D = [2 16];              % propogation delays (intrinsic, extrinsic)  
         M.pF.G = [4 32];              % receptor densities (excitatory, inhibitory)  
         M.pF.T = [8 16];              % synaptic constants (excitatory, inhibitory)  
         M.pF.R = [1 1/2];             % parameter of static nonlinearity  
         
       __________________________________________________________________________  
        David O, Friston KJ (2003) A neural mass model for MEG/EEG: coupling and  
        neuronal dynamics. NeuroImage 20: 1743-1755  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/nmm/mci_nmm_fx_delay.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mci_nmm_fx_delay", *args, **kwargs)
