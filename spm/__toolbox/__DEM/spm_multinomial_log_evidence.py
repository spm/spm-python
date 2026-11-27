from spm._runtime import Runtime


def spm_multinomial_log_evidence(*args, **kwargs):
    r"""
      Bayesian model reduction for multinomial distibutions  
        FORMAT [F,sA] = spm_multinomial_log_evidence(qA,pA,rA)  
         
        qA  - parameter of posterior of full model  
        pA  - parameter of prior of full model  
        rA  - parameter of prior of reduced model  
         
         
        F   - (negative) free energy or log evidence of reduced model  
        sA  - parameter of reduced posterior  
         
        This routine computes the negative log evidence of a reduced model of a  
        mutinomial distribution. This also applies for Bernoulli, Binomial, and  
        Categorical distributions.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_multinomial_log_evidence.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_multinomial_log_evidence", *args, **kwargs)
