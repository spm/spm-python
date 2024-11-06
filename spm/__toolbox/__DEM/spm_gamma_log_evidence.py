from spm.__wrapper__ import Runtime


def spm_gamma_log_evidence(*args, **kwargs):
    """
      Bayesian model reduction for gamma distibutions  
        FORMAT [F,sA] = spm_gamma_log_evidence(qA,pA,rA)  
         
        qA  - 2-vector with shape/rate parameter of posterior of full model  
        pA  - 2-vector with shape/rate parameter of prior of full model  
        rA  - 2-vector with shape/rate parameter of prior of reduced model  
         
         
        F   - (negative) free energy or log evidence of reduced model  
        sA  - shape/rate parameter of reduced posterior  
         
        This routine computes the negative log evidence of a reduced model of a  
        gamma distribution parameterised in terms of its shape parameter.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_gamma_log_evidence.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_gamma_log_evidence", *args, **kwargs)
