from spm._runtime import Runtime


def spm_VBX(*args, **kwargs):
    r"""
      variational Bayes estimate of categorical posterior over factors  
        FORMAT [Q,F] = spm_VBX(O,P,A,id)  
         
        O{g}    -  outcome probabilities over each of G modalities  
        P{f}    -  (empirical) prior over each of F factors  
        A{g}    -  likelihood tensor for modality g  
         
        Q{f}    -  variational posterior for each of F factors  
        F       -  (-ve)  variational free energy or ELBO  
         
        This routine is a simple implementation of variational Bayes for discrete  
        state space models under a mean field approximation, in which latent  
        states are partitioned into factors (and the distribution over outcomes  
        is also assumed to be conditionally independent). It takes cell arrays of  
        outcome probabilities, prior probabilities over factors and a likelihood  
        tensor parameterising the likelihood of an outcome for any combination of  
        latent states. This version uses belief propagation, read as:  
         
        Propagation:  a non-iterative heuristic but numerically accurate scheme  
        that replaces the variational density over hidden factors with the  
        marginal over the exact posterior  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_VBX.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_VBX", *args, **kwargs)
