from spm.__wrap__ import _Runtime


def spm_eeg_ft_artefact_visual(*args, **kwargs):
  """  Function for interactive artefact rejection using Fieldtrip  
     
    Disclaimer: this code is provided as an example and is not guaranteed to work  
    with data on which it was not tested. If it does not work for you, feel  
    free to improve it and contribute your improvements to the MEEGtools toolbox  
    in SPM (http://www.fil.ion.ucl.ac.uk/spm)  
     
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_eeg_ft_artefact_visual.m)
  """

  return _Runtime.call("spm_eeg_ft_artefact_visual", *args, **kwargs)
