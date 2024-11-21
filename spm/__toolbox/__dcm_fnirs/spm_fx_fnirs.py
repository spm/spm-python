from spm.__wrapper__ import Runtime


def spm_fx_fnirs(*args, **kwargs):
    """
      State equation for a dynamic model of fNIRS responses  
        FORMAT [f] = spm_fx_fnirs(x,u,P,M)  
         
        x      - state vector  
       --------------------------------------------------------------------------  
          x(:,1) - excitatory neuronal activity            ue  
          x(:,2) - vasodilatory signal                          s  
          x(:,3) - rCBF                                  ln(f)  
          x(:,4) - venous volume                         ln(v)  
          x(:,5) - deoxyHb                               ln(q)  
          x(:,6) - totalHb                               ln(p)  
          [x(:,7)] - inhibitory neuronal activity            ui  
       --------------------------------------------------------------------------  
        u     experimental inputs   
        P     prior of latent variables   
        M    model structure  
         
        f      - dx/dt  
       ___________________________________________________________________________  
         
        References for hemodynamic & neuronal state equations:  
        1. Friston KJ, Mechelli A, Turner R, Price CJ. Nonlinear responses in  
           fMRI: the Balloon model, Volterra kernels, and other hemodynamics.  
           Neuroimage 12:466-477, 2000.  
        2. Stephan KE, Kasper L, Harrison LM, Daunizeau J, den Ouden HE,  
           Breakspear M, Friston KJ. Nonlinear dynamic causal models for fMRI.  
           Neuroimage 42:649-662, 2008.  
        3. Marreiros AC, Kiebel SJ, Friston KJ. Dynamic causal modelling for  
           fMRI: a two-state model.  
           Neuroimage. 39(1):269-78, 2008.   
        4. Buxton RB, Uludag, K, Dubowitz, DJ, Liu, TT. Modeling the hemodynamic  
           response to brain activation. Neuroimage. 2004, 23: 220-233.   
        5. X Cui and S Bray and A Reiss. Functional near infrared spectroscopy (NIRS)  
           signal improvement based on negative correlation between oxygenated and  
           deoxygenated hemoglobin dynamics.  
           Neuroimage 49:3039-3046, 2010.  
         
        This script is based on spm_fx_fmri.m written by   
        Karl Friston & Klaas Enno Stephan.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_fnirs/spm_fx_fnirs.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_fx_fnirs", *args, **kwargs)
