from spm.__wrapper__ import Runtime


def spm_BMS_F_smpl(*args, **kwargs):
    """
      Get sample and lower bound approx. for model evidence p(y|r) in group BMS  
        FORMAT [s_samp,s_bound] = spm_BMS_F_smpl(alpha,lme,alpha0)  
          
        See spm_BMS_F.m for details.  
         
        Reference:  
        Stephan KE, Penny WD, Daunizeau J, Moran RJ, Friston KJ  
        Bayesian Model Selection for Group Studies. Neuroimage 2009 46(4):1004-17  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_BMS_F_smpl.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_BMS_F_smpl", *args, **kwargs)
