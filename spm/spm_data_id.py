from spm.__wrapper__ import Runtime


def spm_data_id(*args, **kwargs):
  """  Generate a specific real number in a deterministic way from any data structure  
    FORMAT ID = spm_data_id(X)  
    X  - numeric, character, cell or structure array[s]  
    ID - specific ID  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_data_id.m)
  """

  return Runtime.call("spm_data_id", *args, **kwargs)
