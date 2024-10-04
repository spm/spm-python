from spm.__wrap__ import _Runtime


def mne_read_morph_map(*args, **kwargs):
  """   
    [leftmap,rightmap] = mne_read_morph_map(from,to,subjects_dir)  
     
    Read the morphing map from subject 'from' to subject 'to'.  
    If subjects_dir is not specified, the SUBJECTS_DIR environment  
    variable is used  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_read_morph_map.m)
  """

  return _Runtime.call("mne_read_morph_map", *args, **kwargs)
