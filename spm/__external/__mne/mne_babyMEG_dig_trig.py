from spm.__wrapper__ import Runtime


def mne_babyMEG_dig_trig(*args, **kwargs):
  """   
    function mne_baby_meg_dig_trig(infile,outfile,threshold,invert,want_eeg);  
     
    Read and write raw data in 60-sec blocks  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_babyMEG_dig_trig.m)
  """

  return Runtime.call("mne_baby_meg_dig_trig", *args, **kwargs, nargout=0)
