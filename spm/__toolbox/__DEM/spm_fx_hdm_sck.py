from spm.__wrapper__ import Runtime


def spm_fx_hdm_sck(*args, **kwargs):
    """
      state equation for the hemodynamic model  
        FORMAT [f] = spm_fx_hdm_sck(x,u,P,M)  
        x      - state vector  
          x(1) - vascular signal                                    s  
          x(2) - rCBF                                           log(f)  
          x(3) - venous volume                                  log(v)  
          x(4) - dHb                                            log(q)  
        u      - input (neuronal activity)                      (u)  
        P      - free parameter vector  
          P(1) - signal decay                                   d(ds/dt)/ds)  
          P(2) - autoregulation                                 d(ds/dt)/df)  
          P(3) - transit time                                   (t0)  
          P(4) - exponent for Fout(v)                           (alpha)  
          P(5) - resting oxygen extraction                      (E0)  
          P(6) - ratio of intra- to extra-vascular components   (epsilon)  
                 of the gradient echo signal     
         
          P(6 + 1:m)   - input efficacies                       d(ds/dt)/du)  
         
        y      - dx/dt  
       __________________________________________________________________________  
         
        Ref Buxton RB, Wong EC & Frank LR. Dynamics of blood flow and oxygenation  
        changes during brain activation: The Balloon model. MRM 39:855-864 (1998)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_fx_hdm_sck.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_fx_hdm_sck", *args, **kwargs)
