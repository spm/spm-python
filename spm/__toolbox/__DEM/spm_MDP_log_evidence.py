from spm._runtime import Runtime


def spm_MDP_log_evidence(*args, **kwargs):
    r"""
      Bayesian model reduction for Dirichlet hyperparameters  
        FORMAT [F,sA,dFdA] = spm_MDP_log_evidence(qA,pA,rA)  
         
        qA  - sufficient statistics of posterior of full model  
        pA  - sufficient statistics of prior of full model  
        rA  - sufficient statistics of prior of reduced model  
         
        F    - free energy or (negative) log evidence of reduced model  
        sA   - sufficient statistics of reduced posterior  
        dFdA - total free energy gradients with respect to rA  
         
        This routine computes the negative log evidence of a reduced model of a  
        categorical distribution parameterised in terms of Dirichlet parameters  
        (i.e., parameters encoding probabilities). It uses Bayesian model  
        reduction to evaluate the evidence for models with and without a  
        particular parameter.  
         
        A demonstration of the implicit pruning can be found at the end of this  
        routine  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_MDP_log_evidence.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_MDP_log_evidence", *args, **kwargs)
