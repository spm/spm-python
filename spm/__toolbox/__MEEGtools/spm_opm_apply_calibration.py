from spm._runtime import Runtime


def spm_opm_apply_calibration(*args, **kwargs):
    r"""
      [cal_D] = spm_opm_apply_calibration(S) applies position,  
        orientation and gain calibration to an existing dataset. Gain applied is  
        relative to the existing (assumed) calibration of the original data. If  
        positions and orientations are already available for channels then the  
        function will attempt to align the new calibration to the existing space.  
          Input:  
              S : structure with fields  
                  - D:         MEEG D object to be calibrated (required)  
                  - positions: positions file with gain column  
                  - chunkSize: max memory usage (for large datasets; default: 512)  
                  - prefix:    string, calibrated object prefix (default: 'cal_')  
                  - balance:   boolean, update existing forward model/s (default:  
                                   false)  
         
        Author: Nicholas Alexander (n.alexander@ucl.ac.uk)  
            Adapted from spm_opm_hfc  
        Copyright: Department of Imaging Neuroscience, UCL, 2026  
         
        TODO: Add delay correction  
              Improve stability of alignment  
              Set bad channels if uncalibrated MEG  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/MEEGtools/spm_opm_apply_calibration.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_opm_apply_calibration", *args, **kwargs)
