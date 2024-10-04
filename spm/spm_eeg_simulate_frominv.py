from spm.__wrap__ import _Runtime


def spm_eeg_simulate_frominv(*args, **kwargs):
  """  Project a source inversion solution back out to the sensor level plus some noise  
    FORMAT [Dnew] = spm_eeg_simulate_frominv(D,prefix,val,whitenoise,SNRdB,trialind)  
    D          - original dataset  
    prefix     - prefix of new dataset  
    val        - use solution (and lead fields) corresponding to this index  
    whitenoise - total rms white noise in Tesla  
    SNRdB      - SNR in dBs (alternative to specifying white noise)  
    trialind   - trials in which the simulated signal is to appear  
                 (all other trials will be noise)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_simulate_frominv.m)
  """

  return _Runtime.call("spm_eeg_simulate_frominv", *args, **kwargs)
