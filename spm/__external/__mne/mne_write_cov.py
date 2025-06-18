from mpython import Runtime


def mne_write_cov(*args, **kwargs):
    """


          mne_write_cov(fid,cov)

          Write a covariance matrix to an open file

          fid     - an open file id
          cov     - the covariance matrix to write


    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_write_cov.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_write_cov", *args, **kwargs, nargout=0)
