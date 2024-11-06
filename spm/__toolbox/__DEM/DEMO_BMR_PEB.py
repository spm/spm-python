from spm.__wrapper__ import Runtime


def DEMO_BMR_PEB(*args, **kwargs):
    """
      Demonstration routine for empirical Bayes and Bayesian model reduction  
       --------------------------------------------------------------------------  
        This routine illustrates the use of Bayesian model reduction when  
        inverting hierarchical (linear) models - it is essentially a software  
        validation demo and proof of concept. It uses a parametric empirical  
        Bayesian model (i.e., nested linear models) to eschew local minima issues  
        and to assure the Laplace assumption is correct. In brief, the data are  
        generated for multiple subjects, under a linear model with subject  
        specific parameters at the first level and group specific parameters at  
        the second. These model a group effect common to all subjects in a subset  
        of parameters and differences in a further subset. The objective of  
        empirical Bayesian inversion is to recover the group effects in terms of  
        posteriors and perform Bayesian model comparison at the second (between  
        subject) level.  
         
        This provides empirical shrinkage priors at the first level, which can be  
        used to compute the predictive posterior for any subject. In turn, the  
        predictive posterior can be used for leave-one-out cross validation.  
         
        The key aspect of this approach to empirical Bayesian modelling is that  
        we use Bayesian model reduction throughout. In other words, after the  
        subject-specific models have been inverted the data are discarded and we  
        deal only with the free energies and posteriors for subsequent  
        hierarchical analysis. This can be computationally very efficient when  
        dealing with large first-level or complicated models: as in DCM.  
          
        The parameterisation of the models uses the format of DCM. This means  
        parameters are specified as a structure with key parameters being in the  
        fields A, B and C.  
         
        See also: spm_dcm_bmr, spm_dcm_peb and spm_dcm_peb_bma  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEMO_BMR_PEB.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEMO_BMR_PEB", *args, **kwargs, nargout=0)
