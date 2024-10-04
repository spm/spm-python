from spm.__wrap__ import _Runtime


def mne_read_source_spaces(*args, **kwargs):
  """   
    [src] = mne_read_source_spaces(source,add_geom,tree)  
     
    Reads source spaces from a fif file  
     
    source      - The name of the file or an open file id  
    add_geom    - Add geometry information to the source spaces  
    tree        - Required if source is an open file id, search for the  
                  source spaces here  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_read_source_spaces.m)
  """

  return _Runtime.call("mne_read_source_spaces", *args, **kwargs)
