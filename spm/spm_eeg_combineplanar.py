from spm._runtime import Runtime


def spm_eeg_combineplanar(*args, **kwargs):
    r"""
      Combine data from MEGPLANAR sensors  
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_combineplanar.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_combineplanar", *args, **kwargs)
