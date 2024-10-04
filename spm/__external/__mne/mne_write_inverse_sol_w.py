from spm.__wrap__ import _Runtime


def mne_write_inverse_sol_w(*args, **kwargs):
  """   
    function mne_write_inverse_sol_w(stem,inv,sol)  
     
    Save static inverse solution data into stc files  
     
    stem      - Stem for the w files  
    inv       - The inverse operator structure (can be the forward operator as well)  
    sol       - The solution matrix (number of locations)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_write_inverse_sol_w.m)
  """

  return _Runtime.call("mne_write_inverse_sol_w", *args, **kwargs, nargout=0)
