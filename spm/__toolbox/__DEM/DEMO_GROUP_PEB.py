from spm.__wrapper__ import Runtime


def DEMO_GROUP_PEB(*args, **kwargs):
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
        of parameters and differences in a further subset. In this demo, we  
        consider the full hierarchical inversion of a multisubject  study by  
        updating the priors at the first level, using the empirical priors from  
        the second level. Crucially, this is done during the optimisation  at the  
        first level (i.e., after  every iteration - or small number of iterations  
        - at the first level.  
         
        This provides a generic scheme for the hierarchical inversion of  
        nonlinear and possibly dynamic models in which the first level  
        optimisation is informed by the sufficient statistics of the second level  
        (namely the empirical priors). This should be contrasted with the summary  
        statistic approach, in which the second level optimisation, based upon  
        the sufficient statistics of the first level (posteriors and priors) are  
        computed after convergence of the first level. The results of inversion  
        are compared in terms of the second level posteriors (and the second  
        level free energy over iterations). Specifically, we compare a gold  
        standard (PEB) inversion, with the summary statistic approach to  
        empirical Bayes and the hierarchical inversion demonstrated in this  
        routine.  
          
        The parameterisation of the models uses the format of DCM. This means  
        parameters are specified as a structure with key parameters being in the  
        fields A, B and C.  
         
        See also: spm_dcm_bmr, spm_dcm_peb and spm_dcm_peb_bma  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEMO_GROUP_PEB.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEMO_GROUP_PEB", *args, **kwargs, nargout=0)
