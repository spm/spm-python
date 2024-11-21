from spm.__wrapper__ import Runtime


def ROBOT_DCM_EEG(*args, **kwargs):
    """
      test routine to check current implementations of DCM (electrophysiology)  
       ==========================================================================  
          options.analysis     - 'ERP','CSD', 'IND' or 'TFM  
          options.model        - 'ERP','SEP','LFP','CMC','CMM','NMM' or 'MFM'  
          options.spatial      - 'ECD','LFP' or 'IMG'  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/tests/ROBOT_DCM_EEG.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ROBOT_DCM_EEG", *args, **kwargs)
