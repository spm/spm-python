from spm.__wrap__ import _Runtime


def ROBOT_DCM_EEG(*args, **kwargs):
  """  test routine to check current implementations of DCM (electrophysiology)  
   ==========================================================================  
      options.analysis     - 'ERP','CSD', 'IND' or 'TFM  
      options.model        - 'ERP','SEP','LFP','CMC','CMM','NMM' or 'MFM'  
      options.spatial      - 'ECD','LFP' or 'IMG'  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/ROBOT_DCM_EEG.m)
  """

  return _Runtime.call("ROBOT_DCM_EEG", *args, **kwargs)
