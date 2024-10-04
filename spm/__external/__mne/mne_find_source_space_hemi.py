from spm.__wrap__ import _Runtime


def mne_find_source_space_hemi(*args, **kwargs):
  """   
    function mne_find_source_space_hemi(src)  
     
    Return the hemisphere id for a source space  
     
    src      - The source space to investigate  
    hemi     - Deduced hemisphere id  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_find_source_space_hemi.m)
  """

  return _Runtime.call("mne_find_source_space_hemi", *args, **kwargs)
