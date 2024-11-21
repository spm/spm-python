from spm.__wrapper__ import Runtime


def FEP_lorenz_surprise(*args, **kwargs):
    """
     __________________________________________________________________________  
        This demo provides an elementary characterisation of stochastic chaos  
        using the Lorenz system. Effectively, it uses iterated least-squares to  
        solve the Helmholtz decomposition of nonequilibrium steady-state flow  
        (i.e., the solution to the Fokker Planck equation) using the Lorentz  
        system as an example. This furnishes a generative model for stochastic  
        chaos in terms of the underlying potential (log nonequilibrium  
        steady-state density) and flow operator, with symmetric and antisymmetric  
        (skew symmetric) components. The latter (solenoidal) part of the flow  
        operator breaks detailed balance and renders the solution a  
        nonequilibrium steady-state (NESS) density.  
         
        In virtue of using a polynomial expansion for the nonequilibrium  
        potential (i.e., surprisal or self information) one can approximate the  
        expected flow with a second order polynomial. This can be regarded as a  
        Laplace approximation to the nonequilibrium steady-state density. Further  
        constraints can be used to specify the stochastic chaos as (state  
        dependent) solenoidal flow around a multivariate Gaussian, which might be  
        a reasonable approximation in the setting of random fluctuations.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/FEP_lorenz_surprise.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("FEP_lorenz_surprise", *args, **kwargs, nargout=0)
