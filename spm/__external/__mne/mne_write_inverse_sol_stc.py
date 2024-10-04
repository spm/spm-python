from spm.__wrap__ import _Runtime


def mne_write_inverse_sol_stc(*args, **kwargs):
  """   
    function mne_write_inverse_sol_stc(stem,inv,sol,tmin,tstep)  
     
    Save dynamic inverse solution data into stc files  
     
    stem      - Stem for the stc files  
    inv       - The inverse operator structure (can be the forward operator as well)  
    sol       - A solution matrix (locations x time)  
    tmin      - Time of the first data point in seconds  
    tstep     - Time between data points in seconds  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_write_inverse_sol_stc.m)
  """

  return _Runtime.call("mne_write_inverse_sol_stc", *args, **kwargs, nargout=0)
