from spm.__wrap__ import _Runtime


def mne_read_forward_solution(*args, **kwargs):
  """   
    [fwd] = mne_read_forward_solution(fname,force_fixed,surf_ori,include,exclude)  
     
    A forward solution from a fif file  
     
    fname        - The name of the file  
    force_fixed  - Force fixed source orientation mode? (optional)  
    surf_ori     - Use surface based source coordinate system? (optional)  
    include      - Include these channels (optional)  
    exclude      - Exclude these channels (optional)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_read_forward_solution.m)
  """

  return _Runtime.call("mne_read_forward_solution", *args, **kwargs)
