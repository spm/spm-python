from spm._runtime import Runtime


def spm_NESS_forecasting(*args, **kwargs):
    r"""
      Generates paths into the future over size(DEM.U,2) time points  
        FORMAT [Ey,Cy,Vy,pY] = spm_NESS_forecasting(DEM)  
       --------------------------------------------------------------------------  
        DEM - inverted DEM structure (with future causes DEM.U)  
         DEM.Y - past responses  
         DEM.U - future casues  
         
        Ey  - posterior expectation  
        Cy  - posterior covariances  
        Vy  - posterior covariances  
         
        pY(:,:,i) - i-th path  
         
        This routine takes a DEM structure that has been inverted given some data  
        Y and generates trajectories into the future over nT time points. The  
        sample density is then recorded in terms of the first Ey and second order  
        Cy moments. The ensuing trajectories are plotted; along with the  
        preceding timeseries data (and posteriors over latent states).  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_NESS_forecasting.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_NESS_forecasting", *args, **kwargs)
