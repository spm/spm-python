from spm.__wrapper__ import Runtime


def DEM_coupled_oscillators(*args, **kwargs):
    """
      Dual estimation of the Lorenz system: Cross-validation of Laplace schemes  
       __________________________________________________________________________  
        This routine illustrates the inversion of a loosely coupled oscillator  
        model using generalised filtering. In this example, three regions are  
        coupled in terms of their amplitude and phase in a hierarchical fashion.  
        Data are generated under a particular set of parameters. The timeseries  
        are then transformed using a Hilbert transform into the corresponding  
        analytic signal. This then constitutes the data feature for subsequent  
        inversion using generalised filtering; here, in four generalised  
        coordinates of motion. By assuming fairly precise priors on the amplitude  
        of random fluctuations one can recover the parameters and use the  
        posterior density for subsequent Bayesian model comparison. In this  
        example, we used Bayesian model reduction to assess the evidence for  
        models with and without amplitude or phase coupling.  
         
        The parameters and orders of this example have been optimised to provide  
        proof of principle this sort of  model can be inverted using generalised  
        filtering.  The sensitivity to these parameters and orders can be  
        assessed numerically by editing the code.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_coupled_oscillators.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_coupled_oscillators", *args, **kwargs, nargout=0)
