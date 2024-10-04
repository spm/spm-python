from spm.__wrap__ import _Runtime


def mci_linear_struct(*args, **kwargs):
  """  Set up data structures for linear model  
    FORMAT [M,U,Xfull] = mci_linear_struct (Nobs,lambda,des)  
     
    Nobs      number of data points  
    lambda    noise precision  
    des       type of design   
     
    M         model structure  
    U         U.X is the design matrix  
    Xfull     Design matrix for data points [1:T]  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/linear/mci_linear_struct.m)
  """

  return _Runtime.call("mci_linear_struct", *args, **kwargs)
