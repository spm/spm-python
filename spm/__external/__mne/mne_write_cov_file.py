from spm.__wrapper__ import Runtime


def mne_write_cov_file(*args, **kwargs):
    """
       
          function mne_write_cov_file(name,cov)  
         
          Write a complete fif file containing a covariance matrix  
         
          fname    filename  
          cov      the covariance matrix to write  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_write_cov_file.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mne_write_cov_file", *args, **kwargs, nargout=0)
