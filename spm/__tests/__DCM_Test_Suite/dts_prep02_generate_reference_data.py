from spm._runtime import Runtime


def dts_prep02_generate_reference_data(*args, **kwargs):
    r"""
      Generate deterministic DCM fit references under SPM tests/data.  
        Authored by Pranay Yadav in 2026  
         
        This is an explicit maintenance script. Runtime tests do not call it.  
         
        Input:  
          parallel - optional logical scalar. Default false. When true,  
                     model fits use the suite default 8-worker pool.  
          cleanup_generated - optional logical scalar. Default false. When true,  
                              removes generated fit outputs and prep/local after  
                              writing dts_meeg_reference.mat/.csv.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/tests/DCM_Test_Suite/dts_prep02_generate_reference_data.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("dts_prep02_generate_reference_data", *args, **kwargs)
