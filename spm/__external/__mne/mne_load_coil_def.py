from spm.__wrap__ import _Runtime


def mne_load_coil_def(*args, **kwargs):
  """   
     
      [CoilDef,Header] = mne_load_coil_def(fname);  
      CoilDef          = mne_load_coil_def(fname);  
     
      If file name is not specified, the standard coil definition file  
      $MNE_ROOT/setup/mne/coil_def.dat or $MNE_ROOT/share/mne/coil_def.dat is read  
     
      The content of the coil definition file is described in  
      section 5.6 of the MNE manual  
     
      This routine is modified from the original BrainStorm routine  
      created by John C. Mosher  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_load_coil_def.m)
  """

  return _Runtime.call("mne_load_coil_def", *args, **kwargs)
