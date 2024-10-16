from spm.__wrapper__ import Runtime


def spm_create_labels(*args, **kwargs):
  """  Create n  numbered labels using a base string as template  
    FORMAT labels = spm_create_labels(S)  
      S           - input structure  
      Fields of S:  
      S.base      - Template string     - Default: 'T'  
      S.n         - number of labels    - Default:  1   
     
    Output:  
     labels       - cell array of labels  
     
    Example:  
          S = [];  
          S.base = 'TRIG';  
          S.n = 100;  
          labels = spm_create_labels(S);  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_create_labels.m)
  """

  return Runtime.call("spm_create_labels", *args, **kwargs)
