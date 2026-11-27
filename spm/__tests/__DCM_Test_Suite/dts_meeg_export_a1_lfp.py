from spm._runtime import Runtime


def dts_meeg_export_a1_lfp(*args, **kwargs):
    r"""
      Make a single bilateral A1 LFP-like M/EEG dataset from a fitted ERP DCM.  
        Authored by Pranay Yadav in 2026  
         
        Inputs:  
          dcm_file     - path to a fitted ERP DCM .mat  
          output_file  - path to write the LFP M/EEG .mat  
          opts (struct, optional fields and defaults):  
              a1_source_indices    : [1 2]    indices of lA1/rA1 in DCM.Sname  
              Nm                   : 1        local source modes per ROI  
              alpha                : 0.005    ridge regularization  
              anchor_first_sample  : true     subtract sample-1 from each LFP  
              overwrite_outputs    : true     remove existing output before writing  
         
        Output struct:  
              lfp_file         - path to written LFP M/EEG .mat  
              diagnostics_file - path to diagnostics .mat  
         
        Pipeline:  
          1. Load fitted ERP DCM,  
          2. Rebuild IMG regional lead field for lA1 and rA1 only,  
          3. Estimate lA1/rA1 source waveforms from DCM-prepared sensor data using  
             a ridge-regularized minimum-norm inverse,  
          4. Sign-align the two A1 waveforms,  
          5. Average them into one waveform per condition,  
          6. Write the waveform as an SPM M/EEG object with channel type LFP.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/tests/DCM_Test_Suite/dts_meeg_export_a1_lfp.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("dts_meeg_export_a1_lfp", *args, **kwargs)
