from spm.__wrapper__ import Runtime


def mne_ex_average_epochs(*args, **kwargs):
  """   
      An example of averaging over epochs  
     
      function mne_ex_average_epochs(dataname,origname,outname)  
     
      dataname  - Name of a epoch data. The description file will  
                  be <dataname>_desc.mat and the epoch file <dataname>.epochs  
      origname  - Name of the file from which the epochs were extracted.  
      outname   - Name of the output file (optional)  
     
      Returns an evoked data structure identical to the ones   
      returned from fiff_read_evoked  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_ex_average_epochs.m)
  """

  return Runtime.call("mne_ex_average_epochs", *args, **kwargs)
