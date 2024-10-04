from spm.__wrap__ import _Runtime


def spm_DEM_z(*args, **kwargs):
  """  Create hierarchical innovations for generating data  
    FORMAT [z,w] = spm_DEM_z(M,N)  
    M    - model structure  
    N    - length of data sequence  
     
    z{i} - innovations for level i (N.B. z{end} corresponds to causes)  
    w{i} - innovations for level i (state noise)  
     
    If there is no fixed or hyper parameterized precision, then unit noise is  
    created. It is assumed that this will be later modulated by state  
    dependent terms, specified by M.ph and M.pg in spm_DEM_int  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_DEM_z.m)
  """

  return _Runtime.call("spm_DEM_z", *args, **kwargs)
