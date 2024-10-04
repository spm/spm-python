from spm.__wrap__ import _Runtime


def write_eep_cnt(*args, **kwargs):
  """  WRITE_EEG_CNT writes continuous EEG data to an EEProbe *.cnt file  
     
    write_eep_cnt(filename, eeg)  
     
    eeg.label    ... labels of EEG channels  
    eeg.rate     ... sampling rate  
    eeg.npnt     ... number of sample in data segment  
    eeg.nchan    ... number of channels  
    eeg.nsample    
    eeg.time     ... array [1 x npnt] of time points (ms)  
    eeg.data     ... array [nchan x npnt] containing eeg data (uV)   
     
    Author: Robert Smies, A.N.T. Neuro, Mon Jul  3 12:36:02 CEST 2006  
     
    See also READ_EEP_TRG, READ_EEP_REJ, READ_EEP_AVR  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/eeprobe/write_eep_cnt.m)
  """

  return _Runtime.call("write_eep_cnt", *args, **kwargs)
