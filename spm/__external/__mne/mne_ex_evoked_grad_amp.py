from spm.__wrap__ import _Runtime


def mne_ex_evoked_grad_amp(*args, **kwargs):
  """   
      function [res] = mne_ex_evoked_grad_amp(inname,bmin,bmax,outname)  
     
      Compute the magnitude of the tangential gradient at each  
      sensor location using the planar gradiometer data and  
      optionally output the result to a fif file.  
     
      inname      The input file name. All average data sets are  
                  read and processed  
      bmin,bmax   Baseline limits in seconds  
      outname     Optional output file name  
     
     
      Function returns the data which was or would have been written  
      to the file  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_ex_evoked_grad_amp.m)
  """

  return _Runtime.call("mne_ex_evoked_grad_amp", *args, **kwargs)
