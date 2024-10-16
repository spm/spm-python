from spm.__wrapper__ import Runtime


def spm_eeg_ft2spm(*args, **kwargs):
  """  Converter from FieldTrip data structures to SPM file format  
    FORMAT D = spm_eeg_ft2spm(ftdata, filename)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_ft2spm.m)
  """

  return Runtime.call("spm_eeg_ft2spm", *args, **kwargs)
