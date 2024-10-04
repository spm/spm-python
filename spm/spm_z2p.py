from spm.__wrap__ import _Runtime


def spm_z2p(*args, **kwargs):
  """  Compute the p-value of a test statistic  
    FORMAT P = spm_z2p(Z,df,STAT,n)  
     
    Z     - test statistic {minimum over n values}  
    df    - [df{interest} df{error}]  
    STAT  - Statistical field  
            'Z' - Gaussian field  
            'T' - T - field  
            'X' - Chi squared field  
            'F' - F - field  
    n     - number of conjoint tests  
     
    P     - p-value  - P(STAT > Z)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_z2p.m)
  """

  return _Runtime.call("spm_z2p", *args, **kwargs)
