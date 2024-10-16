from spm.__wrapper__ import Runtime


def mne_read_bem_surfaces(*args, **kwargs):
  """   
    [surf] = mne_read_bem_surfaces(source,add_geom,tree)  
     
    Reads source spaces from a fif file  
     
    source      - The name of the file or an open file id  
    add_geom    - Add geometry information to the surfaces  
    tree        - Required if source is an open file id, search for the  
                  BEM surfaces here  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_read_bem_surfaces.m)
  """

  return Runtime.call("mne_read_bem_surfaces", *args, **kwargs)
