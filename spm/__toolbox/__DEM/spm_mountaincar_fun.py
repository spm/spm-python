from spm.__wrapper__ import Runtime


def spm_mountaincar_fun(*args, **kwargs):
    """
      [Cross-entropy] objective function for mountain car problem  
        FORMAT [f] = spm_mountaincar_fun(P,G)  
         
        P = spm_vec(P)  
        P.a - 0th order coefficients of force  
        P.b - 1st order coefficients of force  
        P.c - 2nd order coefficients of force  
        P.d - action efficacy  
         
        G   - world model; including  
           G.fq : function fq(x) returning desired equilibrium density at x  
           G.X  : matrix of locations in x  
         
        f   - KL divergence between actual and desired equilibrium densities  
        x   - cell of grid point support   
         
        see:  
        Gaussian Processes in Reinforcement Learning  
        Carl Edward Rasmussen and Malte Kuss  
        Max Planck Institute for Biological Cybernetics  
        Spemannstraße 38, 72076 T¨ubingen, Germany  
        {carl,malte.kuss}@tuebingen.mpg.de  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_mountaincar_fun.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mountaincar_fun", *args, **kwargs)
