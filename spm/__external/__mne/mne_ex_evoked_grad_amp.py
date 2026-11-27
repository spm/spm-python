from spm._runtime import Runtime


def mne_ex_evoked_grad_amp(*args, **kwargs):
    r"""
       
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_ex_evoked_grad_amp.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_ex_evoked_grad_amp", *args, **kwargs)
