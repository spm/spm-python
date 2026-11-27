from spm._runtime import Runtime


def pan_tompkin(*args, **kwargs):
    r"""
      function [qrs_amp_raw,qrs_i_raw,delay]=pan_tompkin(ecg,fs)  
        Complete implementation of Pan-Tompkins algorithm  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/external/fileexchange/pan_tompkin.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("pan_tompkin", *args, **kwargs)
