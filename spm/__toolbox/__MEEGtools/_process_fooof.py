from spm.__wrap__ import _Runtime


def _process_fooof(*args, **kwargs):
  """  PROCESS_FOOOF: Applies the "Fitting Oscillations and One Over F" (specparam) algorithm on a Welch's PSD  
     
    REFERENCE: Please cite the original algorithm:  
       Donoghue T, Haller M, Peterson E, Varma P, Sebastian P, Gao R, Noto T,  
       Lara AH, Wallis JD, Knight RT, Shestyuk A, Voytek B. Parameterizing   
       neural power spectra into periodic and aperiodic components.   
       Nature Neuroscience (2020)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/MEEGtools/private/process_fooof.m)
  """

  return _Runtime.call("process_fooof", *args, **kwargs)
