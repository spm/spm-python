from spm.__wrapper__ import Runtime


def spm_eeg_var_measures(*args, **kwargs):
  """  Function for computing Fourier coherence using Fieldtrip and VAR based directed measures  
    using SPM's spectral toolbox, developed by Will Penny.  
     
    Disclaimer: this code is provided as an example and is not guaranteed to work  
    with data on which it was not tested. If it does not work for you, feel  
    free to improve it and contribute your improvements to the MEEGtools toolbox  
    in SPM (http://www.fil.ion.ucl.ac.uk/spm)  
     
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_eeg_var_measures.m)
  """

  return Runtime.call("spm_eeg_var_measures", *args, **kwargs, nargout=0)
