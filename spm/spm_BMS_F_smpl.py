from spm.__wrap__ import _Runtime


def spm_BMS_F_smpl(*args, **kwargs):
  """  Get sample and lower bound approx. for model evidence p(y|r) in group BMS  
    FORMAT [s_samp,s_bound] = spm_BMS_F_smpl(alpha,lme,alpha0)  
      
    See spm_BMS_F.m for details.  
     
    Reference:  
    Stephan KE, Penny WD, Daunizeau J, Moran RJ, Friston KJ  
    Bayesian Model Selection for Group Studies. Neuroimage 2009 46(4):1004-17  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_BMS_F_smpl.m)
  """

  return _Runtime.call("spm_BMS_F_smpl", *args, **kwargs)
