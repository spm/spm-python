from spm.__wrapper__ import Runtime


def spm_CLIMATE_priors(*args, **kwargs):
    """
      Prior expectation and covariance of parameters for a climate model  
        FORMAT [P,C,str] = spm_CLIMATE_priors  
         
        pE          - prior expectation (structure)  
        pC          - prior covariances (structure)  
        str.outcome - names  
        str.states  - names  
         
        This routine generates the prior density over model parameters in terms  
        of a prior expectation and covariance structure. Crucially, there are  
        three kinds of parameters. The first sets the initial values of the  
        latent states. The second comprises the parameters of the equations of  
        motion or flow of latent states correspond to the dynamic part of the  
        model. The third kind of parameters map from the latent states to  
        observable outcomes.  
          
        pE.x    - initial states   
        pE.P    - flow parameters  
        pE.Y    - outcome parameters  
         
        Because the flow parameters are (almost universally) rate or time  
        constants, they are scale parameters. In other words, they are always  
        greater than zero. This means that during estimation we will deal with  
        log scale parameters that can take any value between plus and minus  
        infinity. This allows one to place gaussian priors over nonnegative  
        (scale) parameters. Practically, this means that this routine returns the  
        logarithm of the flow parameters used to generate dynamics.  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_CLIMATE_priors.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_CLIMATE_priors", *args, **kwargs)
