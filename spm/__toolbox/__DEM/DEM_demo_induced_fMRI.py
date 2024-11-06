from spm.__wrapper__ import Runtime


def DEM_demo_induced_fMRI(*args, **kwargs):
    """
      Demonstration of DCM for CSD (fMRI) with simulated responses  
       __________________________________________________________________________  
        This demonstration compares generalised filtering and deterministic DCM   
        (generating complex cross spectra) in the context of a nonlinear   
        convolution (fMRI) model using simulated data. Here, the dynamic  
        convolution model for fMRI responses is converted into a static  
        non-linear model by generating not the timeseries per se but their  
        second-order statistics - in the form of cross spectra and covariance  
        functions. This enables model parameters to the estimated using the  
        second order data features through minimisation of variational free  
        energy. For comparison, the same data are inverted (in timeseries form)  
        using generalised filtering. This example uses a particularly difficult  
        problem - with limited data - to emphasise the differences.  
         
        NB - the generalised filtering trakes much longer than the deterministic  
        scheme  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_induced_fMRI.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_induced_fMRI", *args, **kwargs, nargout=0)
