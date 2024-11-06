from spm.__wrapper__ import Runtime


def DEM_demo_convolution_LAP(*args, **kwargs):
    """
      Linear convolution revisited: A dual estimation problem  
       __________________________________________________________________________  
        This demonstration compares generalised filtering and a state-of-the-art   
        Bayesian smoother (SCKS) in the context of dual estimation. Note that the  
        parameter estimates are smaller then the true values for generalised   
        schemes (LAP and DEM). This is largely due to the shrinkage priors and   
        optimisation of model evidence (marginal likelihood), as opposed to the  
        likelihood optimised by the Square-root Cubature Kalman Smoother (SCKS).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_convolution_LAP.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_convolution_LAP", *args, **kwargs, nargout=0)
