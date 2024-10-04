from spm.__wrap__ import _Runtime


def spm_BMS_gibbs(*args, **kwargs):
  """  Bayesian model selection for group studies using Gibbs sampling  
    FORMAT [exp_r,xp,r_samp,g_post] = spm_BMS_gibbs (lme, alpha0, Nsamp)  
     
    INPUT:  
    lme      - array of log model evidences   
                 rows: subjects  
                 columns: models (1..Nk)  
    alpha0   - [1 x Nk] vector of prior model counts  
    Nsamp    - number of samples (default: 1e6)  
      
    OUTPUT:  
    exp_r    - [1 x  Nk] expectation of the posterior p(r|y)  
    xp       - exceedance probabilities  
    r_samp   - [Nsamp x Nk] matrix of samples from posterior  
    g_post   - [Ni x Nk] matrix of posterior probabilities with   
               g_post(i,k) being post prob that subj i used model k  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_BMS_gibbs.m)
  """

  return _Runtime.call("spm_BMS_gibbs", *args, **kwargs)
