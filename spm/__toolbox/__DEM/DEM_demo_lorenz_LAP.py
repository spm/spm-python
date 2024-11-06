from spm.__wrapper__ import Runtime


def DEM_demo_lorenz_LAP(*args, **kwargs):
    """
      Dual estimation of the Lorenz system: Cross-validation of Laplace schemes  
       __________________________________________________________________________  
        Inversion of the Lorenz attractor with DEM, LAP and SCKS schemes: This  
        demo tackles the difficult problem of deconvolving (chaotic) hidden states  
        from a single response variable, while estimating the parameters of the  
        underlying equations of motion. It calls generalised filtering, DEM and  
        a state-of-the-art Bayesian smoother (SCKS).  This example is chosen to  
        show that it is, in principle, possible to perform dual estimation in the  
        context of chaotic dynamics (although small variations in this problem  
        will cause the schemes to fail due it its inherently nonlinear nature and  
        non-identifiability); however, the results are imperfect.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_lorenz_LAP.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_lorenz_LAP", *args, **kwargs, nargout=0)
