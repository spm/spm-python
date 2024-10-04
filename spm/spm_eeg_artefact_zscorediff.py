from spm.__wrap__ import _Runtime


def spm_eeg_artefact_zscorediff(*args, **kwargs):
  """  Plugin for spm_eeg_artefact doing z-score thresholding on the diff time series  
    S            - input structure  
    fields of S:  
       S.D       - M/EEG object  
       S.chanind - vector of indices of channels that this plugin will look at  
     
       Additional parameters can be defined specific for each plugin.  
     
    Output:  
    res -  
       If no input is provided the plugin returns a cfg branch for itself.  
     
       If input is provided the plugin returns a matrix of size D.nchannels x D.ntrials  
       with zeros for clean channel/trials and ones for artefacts.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_artefact_zscorediff.m)
  """

  return _Runtime.call("spm_eeg_artefact_zscorediff", *args, **kwargs)
