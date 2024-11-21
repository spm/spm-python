from spm.__wrapper__ import Runtime


def spm_fx_fmri(*args, **kwargs):
    """
      State equation for a dynamic [bilinear/nonlinear/Balloon] model of fMRI  
        responses  
        FORMAT [f,dfdx,D,dfdu] = spm_fx_fmri(x,u,P,M)  
        x      - state vector  
          x(:,1) - excitatory neuronal activity            ue  
          x(:,2) - vascular signal                          s  
          x(:,3) - rCBF                                  ln(f)  
          x(:,4) - venous volume                         ln(v)  
          x(:,5) - deoyxHb                               ln(q)  
         [x(:,6) - inhibitory neuronal activity             ui  
         
        f      - dx/dt  
        dfdx   - df/dx  
        dfdu   - df/du  
        D      - delays  
         
       __________________________________________________________________________  
         
        References for hemodynamic & neuronal state equations:  
        1. Buxton RB, Wong EC & Frank LR. Dynamics of blood flow and oxygenation  
           changes during brain activation: The Balloon model. MRM 39:855-864,  
           1998.  
        2. Friston KJ, Mechelli A, Turner R, Price CJ. Nonlinear responses in  
           fMRI: the Balloon model, Volterra kernels, and other hemodynamics.  
           Neuroimage 12:466-477, 2000.  
        3. Stephan KE, Kasper L, Harrison LM, Daunizeau J, den Ouden HE,  
           Breakspear M, Friston KJ. Nonlinear dynamic causal models for fMRI.  
           Neuroimage 42:649-662, 2008.  
        4. Marreiros AC, Kiebel SJ, Friston KJ. Dynamic causal modelling for  
           fMRI: a two-state model.  
           Neuroimage. 2008 Jan 1;39(1):269-78.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_fx_fmri.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_fx_fmri", *args, **kwargs)
