from spm._runtime import Runtime


def spm_COVID_ci(*args, **kwargs):
    """
      Graphics for coronavirus simulations - with confidence intervals  
        FORMAT [S,CS,Y,C] = spm_COVID_ci(Ep,Cp,Z,U,M)  
        Ep     - posterior expectations  
        Cp     - posterior covariances  
        Z      - optional empirical data  
        U      - outcomes to evaluate [default: 1:3]  
        M      - model  
         
        S      - posterior expectation of cumulative outcomes  
        CS     - posterior covariances of cumulative outcomes  
        Y      - posterior expectation of outcomes  
        C      - posterior covariances of outcomes  
         
        This routine evaluates a trajectory of outcome variables from a COVID  
        model and plots the expected trajectory and accompanying Bayesian  
        credible intervals (of 90%). If empirical data are supplied, these will  
        be overlaid on the confidence intervals. By default, 128 days  
        are evaluated. In addition, posterior and prior expectations are provided  
        in a panel.  
         
        A single panel is plotted if one output in U is specified  
         
        Although the covid model is non-linear in the parameters, one can use a  
        first-order Taylor expansion to evaluate the confidence intervals in  
        terms of how the outcomes change with parameters. This, in combination  
        with the well-known overconfidence of variational inference, usually  
        requires a slight inflation of uncertainty. Here, the posterior  
        covariance is multiplied by a factor of four.  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_COVID_ci.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_COVID_ci", *args, **kwargs)
