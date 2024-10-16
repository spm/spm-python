from spm.__wrapper__ import Runtime


def mci_logistic_like(*args, **kwargs):
  """  Compute log likelihood of logistic model  
    FORMAT [L,E,st] = mci_logistic_like (P,M,U,Y)  
     
    P         parameters  
    M         model  
    U         inputs  
    Y         data  
      
    L         Log likelihood  
    E         Errors  
    st        Status flag (0 for OK, -1 for problem)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/logistic/mci_logistic_like.m)
  """

  return Runtime.call("mci_logistic_like", *args, **kwargs)
