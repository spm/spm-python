from spm._runtime import Runtime


def mne_write_cov(*args, **kwargs):
    r"""
       
         
          mne_write_cov(fid,cov)  
         
          Write a covariance matrix to an open file  
         
          fid     - an open file id  
          cov     - the covariance matrix to write  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_write_cov.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_write_cov", *args, **kwargs, nargout=0)
