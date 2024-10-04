from spm.__wrap__ import _Runtime


def spm_eeg_combineplanar(*args, **kwargs):
  """  Combine data from MEGPLANAR sensors  
    FORMAT D = spm_eeg_combineplanar(S)  
     
    S        - optional input struct  
     fields of S:  
      D        - MEEG object or filename  
      mode     -  
                 'append'     - add combined channels to the origal channels  
                 'replace'    - replace MEGPLANAR with combined [default]  
                 'replacemeg' - replace all MEG channels with combined but  
                                keep non-MEG  
                 'keep'       - only write out the combined channels  
     
      prefix   - prefix for the output file [default: 'P']  
     
    Output:  
    D        - MEEG object (also written on disk)  
     
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_combineplanar.m)
  """

  return _Runtime.call("spm_eeg_combineplanar", *args, **kwargs)
