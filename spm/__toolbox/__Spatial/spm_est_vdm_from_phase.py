from spm._runtime import Runtime


def spm_est_vdm_from_phase(*args, **kwargs):
    r"""
     ==========================================================================  
        Estimate Voxel Displacement Map (VDM) from phase images using ROMEO phase  
        unwrapping tool.  
        FORMAT:  
        vdm_pha = spm_est_vdm_from_phase(vol1, vol1_mean, vol1_pha,  
                                                total_readout_time, TE, PE_dir, outdir)  
         
        Input:  
          vol1                - cell array of file names of magnitude images with  
                                the same PE direction as the fMRI data to be corrected  
          vol1_mean          - file name of mean magnitude image with the same PE  
                                direction as the fMRI data to be corrected  
          vol1_pha           - cell array of file names of phase images with the  
                                same PE direction as the fMRI data to be corrected  
          total_readout_time - total readout time in seconds  
          TE                 - echo time in seconds  
          PE_dir             - phase-encoding direction (+1 or -1)  
          outdir             - output directory for temporary files  
         
        Output:  
          vdm_pha            - Voxel Displacement Map (in mm) estimated from phase  
                                images  
         
        Barbara Dymerska  
        Copyright (C) 2025 Department of Imaging Neuroscience, UCL  
       ==========================================================================  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/Spatial/spm_est_vdm_from_phase.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_est_vdm_from_phase", *args, **kwargs)
