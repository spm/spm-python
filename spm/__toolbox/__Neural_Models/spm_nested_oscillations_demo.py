from spm.__wrapper__ import Runtime


def spm_nested_oscillations_demo(*args, **kwargs):
    """
      Demo routine for neural mass models of nested oscillations  
       ==========================================================================  
          
        This demo simply illustrates nested oscillations in a three-subpopulation  
        source that are caused by nonlinear interactions between voltage and  
        conductance. Put simply, a slow sinusoidal drive elicits periods of bursting  
        to produce phase-amplitude coupling in the ensuing dynamics.  We look at  
        this using both neural-mass and mean-field models.  See Marreiros et al:  
          
        Population dynamics under the Laplace assumption.  
          
        A Marreiros, J Daunizeau, S Kiebel, L Harrison & Karl Friston  
          
        Abstract  
        In this paper, we describe a generic approach to modelling dynamics in  
        neuronal populations.  This approach retains a full density on the states  
        of neuronal populations but resolves the problem of solving  
        high-dimensional problems by re-formulating density dynamics in terms of  
        ordinary differential equations on the sufficient statistics of the  
        densities considered.  The particular form for the population density we  
        adopt is a Gaussian density (c.f., a Laplace assumption). This means  
        population dynamics are described completely by equations governing the  
        evolution of the population's mean and covariance.  We derive these  
        equations from the Fokker-Planck formalism and illustrate their  
        application to a reasonably simple conductance-based model of neuronal  
        exchanges.  One interesting aspect of this formulation is that we can  
        uncouple the mean and covariance to furnish a neural-mass model, which  
        rests only on the populations mean.  This enables to compare equivalent  
        mean-field and neural-mass models of the same populations and evaluate,  
        quantitatively, the contribution of population variance to the expected  
        dynamics.  The mean-field model presented here will form the basis of a  
        dynamic causal model of observed electromagnetic signals in future work.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/spm_nested_oscillations_demo.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_nested_oscillations_demo", *args, **kwargs, nargout=0)
