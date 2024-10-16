from spm.__wrapper__ import Runtime


def spm_eeg_spmft_chan_dictionary(*args, **kwargs):
  """  Return a table of corresponce between SPM and FieldTrip channel types  
    FORMAT dictionary = spm_eeg_spmft_chan_dictionary  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_spmft_chan_dictionary.m)
  """

  return Runtime.call("spm_eeg_spmft_chan_dictionary", *args, **kwargs)
