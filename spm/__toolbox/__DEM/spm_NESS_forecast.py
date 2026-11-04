from spm._runtime import Runtime


def spm_NESS_forecast(*args, **kwargs):
    r"""
      Analytic predictive density under the Laplace assumption  
        FORMAT [Ey,Cy,Vy] = spm_NESS_forecast(DEM)  
       --------------------------------------------------------------------------  
        DEM - inverted DEM structure  
         
        Ey  - posterior expectation  
        Cy  - posterior covariances  
        Vy  - posterior covariances  
         
        This routine integrates the Fokker Planck equation under a Laplace  
        (Gaussian) approximation to the evolving density over states. It uses the  
        Hessian at the current point in state space to approximate the (inverse)  
        covariance and assumes an initial density with a high precision. This  
        application involves some housekeeping because the parameters of the flow  
        pertain to a first-order approximation to the coefficients of a Helmholtz  
        decomposition (with the surprisal specified in terms of kernels), whereas  
        the Gaussian approximation requires a second-order polynomial expansion  
        (i.e., K = 3).  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_NESS_forecast.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_NESS_forecast", *args, **kwargs)
