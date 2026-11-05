from spm._runtime import Runtime


def dts_meeg_prepare_mmn_eeg(*args, **kwargs):
    r"""
      Preprocess SPM EEG MMN raw BDF data into an ERP dataset.  
        Authored by Pranay Yadav in 2026  
         
        Inputs are explicit paths. Outputs is a struct with final_mat, final_dat,  
        and, when requested, gainmat_file.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/tests/DCM_Test_Suite/dts_meeg_prepare_mmn_eeg.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("dts_meeg_prepare_mmn_eeg", *args, **kwargs)
