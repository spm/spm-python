from spm.__wrapper__ import Runtime


def spm_dcm_spem(*args, **kwargs):
    """
      Estimate parameters of a DCM of smooth pursuit eye movements  
        FORMAT DCM = spm_dcm_spem(DCM)  
         
        DCM  
           DCM.name: name string  
           DCM.xY: data   {1 x nc struct}  
         
               xY.Y{i}  - eye-gaze position for i-th condition  
               xY.C{i}  - target position for i-th condition  
               xY.DT    - time bin (ms)  
               xY.occ   - occlusion function occ(x) = {0,1}: -1 > x > 1  
               xY.C{i}  - target position for i-th condition  
         
           DCM.xU: design [nu x nc array]  
           DCM.pE: prior expectation  
           DCM.pC: prior covariance  
         
        This routine checks the data and inverts a meta-model of observed slow  
        pursuit eye movements using the standard variational Laplacian scheme  
         
        See also: spm_SEM_gen; spm_dcm_spem_data; spm_dcm_spem_results  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/SPEM_and_DCM/spm_dcm_spem.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_spem", *args, **kwargs)
