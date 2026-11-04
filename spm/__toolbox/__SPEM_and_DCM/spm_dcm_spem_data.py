from spm._runtime import Runtime


def spm_dcm_spem_data(*args, **kwargs):
    r"""
      Prepare (decimate and normalise) data DCM for SPEM  
        FORMAT xY = spm_dcm_spem_data(xY)  
         
          xY.Y{i}  - original data  
          xY.C{i}  - original target  
          xY.DT    - original timing  
         
        creates:  
         
          xY.y{i} - normalised (decimated) lag (data - target)  
          xY.u{i} - normalised (decimated) target  
          xY.R(i) - decimation  
          xY.x(i) - initial states  
          xY.dt   - mean normalised (decimated) timing  
         
         This auxiliary routine  decimates and normalises eye movement data to a  
         single period of a (negative) cosine wave - of unit amplitude.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/SPEM_and_DCM/spm_dcm_spem_data.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dcm_spem_data", *args, **kwargs)
