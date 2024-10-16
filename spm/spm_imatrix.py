from spm.__wrapper__ import Runtime


def spm_imatrix(*args, **kwargs):
  """  Return the parameters for creating an affine transformation matrix  
    FORMAT P = spm_imatrix(M)  
    M   - Affine transformation matrix  
    P   - Parameters (see spm_matrix for definitions)  
   __________________________________________________________________________  
     
    See also: spm_matrix.m  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_imatrix.m)
  """

  return Runtime.call("spm_imatrix", *args, **kwargs)
