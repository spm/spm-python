from spm.__wrapper__ import Runtime


def spm_VBX(*args, **kwargs):
    """
      vvariational Bayes estimate of categorical posterior over factors  
        FORMAT [Q,F] = spm_VBX(O,P,A,[METHOD])  
         
        O{g}    -  outcome probabilities over each of G modalities  
        P{f}    -  (empirical) prior over each of F factors  
        A{g}    -  likelihood tensor for modality g  
         
        Q{f}    -  variational posterior for each of F factors  
        F       -  (-ve)  variational free energy or ELBO  
         
        This routine is a simple implementation of variational Bayes for discrete  
        state space models  under a mean field approximation, in which latent  
        states are partitioned into factors (and the distribution over outcomes  
        is also assumed to be conditionally independent). It takes cell arrays of  
        outcome probabilities,  prior probabilities over factors and a likelihood  
        tensor parameterising the  likelihood of an outcome for any combination  
        of latent states. The optional argument METHOD [default: exact] switches  
        among number of approximate schemes:  
         
        'full'    :  a vanilla variational scheme that uses a coordinate descent  
        over a small number (four) iterations  
         
        'exact'   :  a non-iterative heuristic but numerically accurate scheme  
        that replaces the variational density over hidden factors with the  
        marginal over the exact posterior  
         
        'sparse'  :  as for the exact scheme but suitable for sparse tensors  
         
        'marginal':  a heuristic scheme  that uses the log of the marginalised  
        likelihood and log prior to estimate the lot posterior  
         
        see: spm_MDP_VB_XXX.m (NOTES)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_VBX.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_VBX", *args, **kwargs)
