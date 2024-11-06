from spm.__wrapper__ import Runtime


def spm_dcm_spem_data(*args, **kwargs):
    """
      Prepare (decimate and normalise) data DCM for SPEM  
        FORMAT xY = spm_dcm_spem_data(xY)  
         
          xY.Y{i}  - original data  
          xY.C{i}  - original target  
          xY.DT    - original timing  
         
        creates:  
         
          xY.y{i} - normalised (decimated) lag (data - target)  
          xY.u{i} - normalised (decimated) target  
          xY.R(i) - decimation  
          xY.x(i) - intial states  
          xY.dt   - mean normalised (decimated) timing  
         
         This auxiliary routine  decimates and normalises eye movement data to a  
         single period of a (negative) cosine wave - of unit amplitude.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/SPEM_and_DCM/spm_dcm_spem_data.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_spem_data", *args, **kwargs)
