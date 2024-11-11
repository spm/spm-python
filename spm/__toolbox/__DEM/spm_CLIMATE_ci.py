from spm.__wrapper__ import Runtime


def spm_CLIMATE_ci(*args, **kwargs):
    """
      Graphics for climate simulations - with confidence intervals  
        FORMAT [Y,C] = spm_CLIMATE_ci(Ep,Cp,Z,U,M,NPI)  
        Ep     - posterior expectations  
        Cp     - posterior covariances  
        Z      - optional empirical data  
        U      - indices of outcome  
        M      - model  
        NPI    - intervention array  
         
        Y      - posterior expectation of outcomes  
        C      - posterior covariances of outcomes  
         
        This routine evaluates a trajectory of outcome variables from a dynamic  
        causal model and plots the expected trajectory and accompanying Bayesian  
        credible intervals (of 90%). If empirical data are supplied, these will  
        be overlaid on the confidence intervals.  
         
        Although the DCM is non-linear in the parameters, one can use a  
        first-order Taylor expansion to evaluate the confidence intervals in  
        terms of how the outcomes change with parameters. This, in combination  
        with the well-known overconfidence of variational inference, usually  
        requires a slight inflation of uncertainty. Here, the posterior  
        covariance is multiplied by a factor of four.  
         
        For computational expediency, the confidence intervals are usually  
        evaluated as a proportion of the expected value. To evaluate the  
        confidence intervals properly, set the global variable CIPLOT to 'true'  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_CLIMATE_ci.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_CLIMATE_ci", *args, **kwargs)
