from spm._runtime import Runtime


def spm_MDP_BMR(*args, **kwargs):
    r"""
      returns the likelihood of reduced (Dirichlet) models  
        FORMAT [L] = spm_MDP_BMR(qp,rp)  
         
        qp    - posterior Dirichlet parameters (tensor or numeric array)  
        rp{m} - cell array of m reduced priors  
         
        L(m)  - likelihood of model m  
         
        This auxillary routine assumes the priors are the (model) average of  
        reduced priors.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_MDP_BMR.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_MDP_BMR", *args, **kwargs)
