from spm.__wrap__ import _Runtime


def read_eep_avr(*args, **kwargs):
  """  READ_EEP_AVR reads averaged EEG data from an EEProbe *.avr file  
    and returns a structure containing the header and data information.  
     
    eeg = read_eep_avr(filename)  
     
    eeg.label     ... array of labels (1 x nchan)  
    eeg.rate      ... sample rate (Hz)  
    eeg.npnt      ... number of data points  
    eeg.nchan     ... number of channels  
    eeg.nsweeps   ... number of trials averaged  
    eeg.xmin      ...   
    eeg.xmax      ...   
    eeg.time      ... array of time (1 x npnt)  
    eeg.data      ... data array (nchan x npnt)  
    eeg.variance  ... variance (nchan x npnt)  
    eeg.condlab   ... string with condition label  
    eeg.condcol   ... string with color code for condition  
    eeg.psi       ... pre-stimulus interval  
    eeg.trialc    ... total number of trial in original data  
    eeg.rejtrialc ... number of rejected trials  
     
    Use plot(eeg.time,eeg.data) to plot the traces at all channels  
     
    Author: Robert Oostenveld, Aalborg University, Denmark, 11 March 2003  
     
    See also READ_EEP_CNT, READ_EEP_TRG, READ_EEP_REJ  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/eeprobe/read_eep_avr.m)
  """

  return _Runtime.call("read_eep_avr", *args, **kwargs)
