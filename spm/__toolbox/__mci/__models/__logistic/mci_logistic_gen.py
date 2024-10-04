from spm.__wrap__ import _Runtime


def mci_logistic_gen(*args, **kwargs):
  """  Output of logistic regression model  
    FORMAT [g,y] = mci_logistic_gen (P,M,U)  
     
    P         parameters  
    M         model structure  
    U         U.X contains design matrix  
     
    g         probabilities of y=1  
    y         binary decisions based on g  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/logistic/mci_logistic_gen.m)
  """

  return _Runtime.call("mci_logistic_gen", *args, **kwargs)
