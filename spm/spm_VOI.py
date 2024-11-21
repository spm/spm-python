from spm.__wrapper__ import Runtime


def spm_VOI(*args, **kwargs):
    """
      List of local maxima and adjusted p-values for a small Volume of Interest  
        FORMAT [TabDat,xSVC] = spm_VOI(SPM,xSPM,hReg,[xY])  
         
        SPM    - Structure containing analysis details (see spm_spm)  
         
        xSPM   - Structure containing SPM, distribution & filtering details  
                 Required fields are:  
        .swd     - SPM working directory - directory containing current SPM.mat  
        .Z       - minimum of n Statistics {filtered on u and k}  
        .n       - number of conjoint tests  
        .STAT    - distribution {Z, T, X or F}  
        .df      - degrees of freedom [df{interest}, df{residual}]  
        .u       - height threshold  
        .k       - extent threshold {resels}  
        .XYZ     - location of voxels {voxel coords}  
        .XYZmm   - location of voxels {mm}  
        .S       - search Volume {voxels}  
        .R       - search Volume {resels}  
        .FWHM    - smoothness {voxels}  
        .M       - voxels -> mm matrix  
        .VOX     - voxel dimensions {mm}  
        .DIM     - image dimensions {voxels} - column vector  
        .Vspm    - mapped statistic image(s)  
        .Ps      - uncorrected P values in searched volume (for voxel FDR)  
        .Pp      - uncorrected P values of peaks (for peak FDR)  
        .Pc      - uncorrected P values of cluster extents (for cluster FDR)  
        .uc      - 0.05 critical thresholds for FWEp, FDRp, FWEc, FDRc  
         
        hReg   - Handle of results section XYZ registry (see spm_results_ui.m)  
        xY     - VOI structure  
         
        TabDat - Structure containing table data (see spm_list.m)  
        xSVC   - Thresholded xSPM data (see spm_getSPM.m)  
       __________________________________________________________________________  
         
        spm_VOI is  called by the SPM results section and takes variables in  
        SPM to compute p-values corrected for a specified volume of interest.  
         
        The volume of interest may be defined as a box or sphere centred on  
        the current voxel or by a mask image.  
         
        If the VOI is defined by a mask this mask must have been defined  
        independently of the SPM (e.g. using a mask based on an orthogonal  
        contrast).  
         
        External mask images should be in the same orientation as the SPM  
        (i.e. as the input used in stats estimation). The VOI is defined by  
        voxels with values greater than 0.  
         
        See also: spm_list  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_VOI.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_VOI", *args, **kwargs)
