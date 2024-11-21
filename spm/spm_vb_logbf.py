from spm.__wrapper__ import Runtime


def spm_vb_logbf(*args, **kwargs):
    """
      Compute and write log Bayes factor image  
        FORMAT [xCon,SPM] = spm_vb_logbf(SPM,XYZ,xCon,ic)  
         
        SPM    - SPM data structure  
        XYZ    - voxel list  
        xCon   - contrast info  
        ic     - contrast number  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_vb_logbf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_vb_logbf", *args, **kwargs)
