from spm._runtime import Runtime


def spm_BMS_F_smpl(*args, **kwargs):
    r"""
      Get sample and lower bound approx. for model evidence p(y|r) in group BMS  
        FORMAT [s_samp,s_bound] = spm_BMS_F_smpl(alpha,lme,alpha0)  
          
        See spm_BMS_F.m for details.  
         
        Reference:  
        Stephan KE, Penny WD, Daunizeau J, Moran RJ, Friston KJ  
        Bayesian Model Selection for Group Studies. Neuroimage 2009 46(4):1004-17  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_BMS_F_smpl.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_BMS_F_smpl", *args, **kwargs)
