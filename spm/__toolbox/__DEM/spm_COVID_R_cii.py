from spm.__wrapper__ import Runtime


def spm_COVID_R_cii(*args, **kwargs):
    """
      Graphics for coronavirus simulations - with confidence intervals  
        FORMAT dSYdP = spm_COVID_R_ci(DCM,U)  
        DCM.Ep - posterior expectations  
        DCM.Cp - posterior covariances  
        DCM.Y  - empirical data  
        DCM.M  - model  
         
        U      - output to evaluate [default: 1]  
         
        dSYdP  - first-order sensitivity (with respect to outcome U)  
         
        This routine evaluates a trajectory of outcome variables from a COVID  
        model and plots the expected trajectory and accompanying Bayesian  
        credible intervals (of 90%). If empirical data are supplied, these will  
        be overlaid on the confidence intervals. By default, 365 days are  
        evaluated. In addition, posterior and prior expectations are provided in  
        a panel. this confidence interval potting routine handles multiple region  
        models and returns both a sensitivity analysis and posterior predictive  
        density over specified outcomes (in U).  
         
        Although the covid model is non-linear in the parameters, one can use a  
        first-order Taylor expansion to evaluate the confidence intervals in  
        terms of how the outcomes change with parameters. This, in combination  
        with the well-known overconfidence of variational inference, usually  
        requires a slight inflation of uncertainty. Here, the posterior  
        covariance is multiplied by a factor of four.  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_COVID_R_cii.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_COVID_R_cii", *args, **kwargs)
