from spm.__wrapper__ import Runtime


def spm_dcm_optimise(*args, **kwargs):
    """
      Optimise the priors of a model (under Laplace approximation)  
        FORMAT [rE,rC] = spm_dcm_optimise(qE,qC,pE,pC,priorfun,varargin)  
         
        qE,qC    - posterior expectation and covariance of model  
        pE,pC    - prior expectation and covariance of model  
        priorfun - inline function that returns priors  
                   {rE rC} = priorfun(varargin{:})  
         
        rE,rC    - optimal priors defining a reduced model  
         
       --------------------------------------------------------------------------  
        This routine optimizes the prior covariance on the free parameters of any   
        model (DCM) under the Laplace approximation. In other words, it assumes   
        that the prior means are fixed and will maximise model evidence with   
        respect to the hyperparameters of a function that returns the prior   
        covariance. This optimization uses the reduced free-energy, based upon   
        the posterior and prior densities of the full model supplied. If the   
        prior covariance function is not specified, this routine will assume a   
        simple diagonal form with a single hyperparameter. In principle, this   
        routine can be used in a flexible and powerful way to emulate   
        hierarchical modeling by using suitable prior covariance functions with   
        unknown hyperparameters. The outputs are the prior moments (mean and   
        covariance) of the optimum model.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_optimise.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_optimise", *args, **kwargs)
