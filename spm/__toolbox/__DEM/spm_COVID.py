from spm.__wrapper__ import Runtime


def spm_COVID(*args, **kwargs):
    """
      Variational inversion of COVID model  
        FORMAT [F,Ep,Cp,pE,pC,Eh] = spm_COVID(Y,pE,pC,hC)  
        Y   - timeseries data  
        pE  - prior expectation of parameters  
        pC  - prior covariances of parameters  
        hC  - prior covariances of precisions  
          
        F   - log evidence (negative variational free energy)  
        Ep  - posterior expectation of parameters  
        Cp  - posterior covariances of parameters  
        pE  - prior expectation of parameters  
        pC  - prior covariances of parameters  
         
        This routine inverts a generative model of some timeseries data (Y),  
        returning a variational (free energy) bound on log model evidence, and  
        posterior densities of the model parameters (in terms of posterior  
        expectations and covariances). This inversion uses standard variational  
        Laplace; i.e., a (natural) gradient ascent on variational free energy  
        under the Laplace assumption (i.e.,Gaussian priors and likelihood  
        model).  
         
        Model inversion entails specifying the generative model in terms of a log  
        likelihood function and priors. These priors cover the model parameters  
        and precision parameters that determine the likelihood of any given data.  
        The precision priors (sometimes referred to as hyper priors) are  
        specified in terms of the expectation and covariance of the log precision  
        of random fluctuations about the predicted outcome variable. In this  
        instance, the outcome variables are campus. This means that a square root  
        transform allows a Gaussian approximation to the implicit (Poisson)  
        likelihood distribution over observations.  
          
        The log likelihood function is provided as a subroutine in the (Matlab)  
        code (spm_COVID_LL) below. However, because of Gaussian assumptions about  
        the likelihood, we can use a simpler scheme, using the predicted outcomes  
        from spm_COVID_gen, following a square root transform. The square root  
        transform is treated as a feature selection or link function; please see  
        the subroutine spm_COVID_FS.  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_COVID.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_COVID", *args, **kwargs)
