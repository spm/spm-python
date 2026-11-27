from spm._runtime import Runtime


def mne_ex_average_epochs(*args, **kwargs):
    r"""
       
          An example of averaging over epochs  
         
          function mne_ex_average_epochs(dataname,origname,outname)  
         
          dataname  - Name of a epoch data. The description file will  
                      be <dataname>_desc.mat and the epoch file <dataname>.epochs  
          origname  - Name of the file from which the epochs were extracted.  
          outname   - Name of the output file (optional)  
         
          Returns an evoked data structure identical to the ones   
          returned from fiff_read_evoked  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_ex_average_epochs.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_ex_average_epochs", *args, **kwargs)
