from spm._runtime import Runtime


def ROBOT_DCM_EEG(*args, **kwargs):
    r"""
      test routine to check current implementations of DCM (electrophysiology)  
       ==========================================================================  
          options.analysis     - 'ERP','CSD', 'IND' or 'TFM  
          options.model        - 'ERP','SEP','LFP','CMC','CMM','NMM' or 'MFM'  
          options.spatial      - 'ECD','LFP' or 'IMG'  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/tests/ROBOT_DCM_EEG.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ROBOT_DCM_EEG", *args, **kwargs)
