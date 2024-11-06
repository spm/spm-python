from spm.__wrapper__ import Runtime


def mci_ramsay_fx(*args, **kwargs):
    """
      State equation for Ramsay model  
        FORMAT [F] = mci_ramsay_fx (x,U,P,M)  
         
        x     State vector  
              x(1) Voltage variable  
              x(2) Recovery variable  
        U     inputs  
        P     vector of model parameters - 2 params only  
        M     model  
         
        F     dx/dt  
         
        J Ramsay et al (2007) Parameter estimation for differential equations:  
        a generalised smoothing approach. J Roy Stat Soc B, 69(5):741-796.  
         
        See also section 10 (page 26) and contribution by W.Penny on page 75 of:   
         
        Girolami and Calderhead (2011) Riemann manifold Langevin and Hamiltonian  
        Monte Carlo methods. J Roy Stat Soc B,73(2):123-214.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/ramsay/mci_ramsay_fx.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mci_ramsay_fx", *args, **kwargs)
