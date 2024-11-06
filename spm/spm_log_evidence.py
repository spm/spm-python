from spm.__wrapper__ import Runtime


def spm_log_evidence(*args, **kwargs):
    """
      Return the log-evidence of a reduced model (under Laplace approximation)  
        FORMAT [F,sE,sC] = spm_log_evidence(qE,qC,pE,pC,rE,rC)  
        FORMAT [F,sE,sC] = spm_log_evidence(qE,qC,pE,pC,priorfun,varargin)  
        FORMAT [F,sE,sC] = spm_log_evidence(qE,qC,pE,pC)  
         
        qE,qC    - posterior expectation and covariance of full model  
        pE,pC    - prior expectation and covariance of full model  
        rE,rC    - prior expectation and covariance of reduced model  
        or   
        priorfun - inline function that returns prior moments  
                   {rE rC} = priorfun(varargin{:})  
         
        or (if omitted) rE = 0 and rC = 0;  
         
        F        - reduced log-evidence: ln p(y|reduced model) - ln p(y|full model)  
        [sE,sC]  - posterior expectation and covariance of reduced model  
         
       --------------------------------------------------------------------------  
        This routine assumes the reduced model is nested within a full model and  
        that the posteriors (and priors) are Gaussian. Nested here means that the  
        prior precision of the reduced model, minus the prior precision of the  
        full model is positive definite. We additionally assume that the prior  
        means are unchanged. The two input argument formats are for use with  
        spm_argmax.  
         
        See also: spm_log_evidence_reduce  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_log_evidence.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_log_evidence", *args, **kwargs)
