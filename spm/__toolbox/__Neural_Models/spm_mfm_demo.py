from spm.__wrapper__ import Runtime


def spm_mfm_demo(*args, **kwargs):
    """
      Demo routine for mean-field models  
       ==========================================================================  
          
        This demo compares and contrasts neural-mass and mean-field models of a   
        single population, using the model described in Marreiros et al 2008).   
        We start by comparing the impulse response of an small ensemble that has   
        some (but not marked) finite size effects) with that of the mean-field  
        and neural-mass approximations.  The key difference between these models  
        is that the means-field has states that describe the change in dispersion   
        or covariance among the first-order states (current and voltage).  
          
        We then move on to comparing responses to inputs that are transient and   
        sustained, to show that the mean-field model retains key nonlinearities   
        and can show [plausible] bifurcations, as sustained input levels are  
        increased.  This is characterised using Fourier transforms, which are %  
        plotted alongside spiking responses.  See Marreiros et al:  
          
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/spm_mfm_demo.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mfm_demo", *args, **kwargs, nargout=0)
