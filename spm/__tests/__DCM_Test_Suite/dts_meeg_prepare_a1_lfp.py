from spm._runtime import Runtime


def dts_meeg_prepare_a1_lfp(*args, **kwargs):
    r"""
      Derive A1_LFP.mat from a preprocessed EEG_MMN dataset.  
        Authored by Pranay Yadav in 2026  
         
        Specifies a baseline ERP+IMG DCM on EEG_MMN, prepares its data and  
        one-mode IMG lead fields, and then derives the bilateral A1 LFP via  
        dts_meeg_export_a1_lfp. No DCM inversion is required for this export.  
         
        Inputs:  
          eeg_mmn_file - preprocessed EEG_MMN .mat with forward model + gainmat  
          lfp_out_file - target path for A1_LFP.mat  
          work_dir     - scratch directory for the specified DCM  
          cfg          - cfg-like struct (uses the selected fit Nmax and integrator if present)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/tests/DCM_Test_Suite/dts_meeg_prepare_a1_lfp.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("dts_meeg_prepare_a1_lfp", *args, **kwargs)
