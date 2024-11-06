from spm.__wrapper__ import Runtime


def spm_fx_mmc(*args, **kwargs):
    """
      State equations for a neural mass model of motor cortex  
        Bhatt et al. 2016 Neuroimage  
         
        FORMAT [f,J,D] = spm_fx_mmc(x,u,P,M)  
        FORMAT [f,J]   = spm_fx_mmc(x,u,P,M)  
        FORMAT [f]     = spm_fx_mmc(x,u,P,M)  
        x      - state vector  
          x(:,1) - voltage     (middle pyramidal cells)  
          x(:,2) - conductance (middle pyramdidal cells)  
          x(:,3) - voltage     (superficial pyramidal cells)  
          x(:,4) - conductance (superficial pyramidal cells)  
          x(:,5) - current     (inhibitory interneurons)  
          x(:,6) - conductance (inhibitory interneurons)  
          x(:,7) - voltage     (deep pyramidal cells)  
          x(:,8) - conductance (deep pyramidal cells)  
         
        f        - dx(t)/dt  = f(x(t))  
        J        - df(t)/dx(t)  
        D        - delay operator dx(t)/dt = f(x(t - d))  
                                           = D(d)*f(x(t))  
         
        Prior fixed parameter scaling [Defaults]  
         
        E  = (forward, backward, lateral) extrinsic rates   
        G  = intrinsic rates  
        D  = propagation delays (intrinsic, extrinsic)  
        T  = synaptic time constants  
        S  = slope of sigmoid activation function  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_fx_mmc.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_fx_mmc", *args, **kwargs)
