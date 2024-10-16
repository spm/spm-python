from spm.__wrapper__ import Runtime


def spm_eeg_test_coverage(*args, **kwargs):
  """  Return number of M/EEG functions and number of associated tests  
    FORMAT [coverage, tocover] = spm_eeg_test_coverage  
     
    Output:  
      coverage - number of M/EEG tested functions  
      tocover  - number of M/EEG functions   
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/spm_eeg_test_coverage.m)
  """

  return Runtime.call("spm_eeg_test_coverage", *args, **kwargs)
