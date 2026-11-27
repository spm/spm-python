from spm._runtime import Runtime


def spm_setup_data_attention(*args, **kwargs):
    r"""
      Sets up the Attention to Visual Motion dataset and runs analyses for use  
        in regression tests (either Matlab or Octave versions)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/tests/spm_setup_data_attention.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_setup_data_attention", *args, **kwargs, nargout=0)
