from spm.__wrapper__ import Runtime


def spm_fx_lfp(*args, **kwargs):
    """
      state equations for a neural mass model of erps  
        FORMAT [f,J] = spm_fx_lfp(x,u,P,M)  
        x      - state vector  
          x(:,1)  - voltage (spiny stellate cells)  
          x(:,2)  - voltage (pyramidal cells)         +ve  
          x(:,3)  - voltage (pyramidal cells)         -ve  
          x(:,4)  - current (spiny stellate cells)    +ve   
          x(:,5)  - current (pyramidal cells)         +ve  
          x(:,6)  - current (pyramidal cells)         -ve  
          x(:,7)  - voltage (inhibitory interneurons) +ve  
          x(:,8)  - current (inhibitory interneurons) +ve  
          x(:,9)  - voltage (pyramidal cells)  
          x(:,10) - voltage (inhibitory interneurons) -ve  
          x(:,11) - current (inhibitory interneurons) -ve  
          x(:,12) - voltage (inhibitory interneurons)  
         
          x(:,13) - slow potassium conductance  
         
        f    = dx(t)/dt  = f(x(t))  
        J    = df/dx  
         
        Fixed parameter scaling [Defaults]  
         
         E = [32 16 4];             % extrinsic rates (forward, backward, lateral)  
         G = [1 1 1/2 1/2 1/8]*128; % intrinsic rates (g1, g2, g3, g4, g5)  
         D = [2 16];                % propagation delays (intrinsic, extrinsic)  
         H = [4 32];                % receptor densities (excitatory, inhibitory)  
         T = [4 16];                % synaptic constants (excitatory, inhibitory)  
         R = [2 1];                 % parameters of static nonlinearity  
         
       __________________________________________________________________________  
         
        This is a simplified version of spm_fx_erp  
         
        David O, Friston KJ (2003) A neural mass model for MEG/EEG: coupling and  
        neuronal dynamics. NeuroImage 20: 1743-1755  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/spm_fx_lfp.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_fx_lfp", *args, **kwargs)
