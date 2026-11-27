from spm._runtime import Runtime


def mne_write_cov_file(*args, **kwargs):
    r"""
       
          function mne_write_cov_file(name,cov)  
         
          Write a complete fif file containing a covariance matrix  
         
          fname    filename  
          cov      the covariance matrix to write  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_write_cov_file.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_write_cov_file", *args, **kwargs, nargout=0)
