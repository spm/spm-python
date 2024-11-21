from spm.__wrapper__ import Runtime


def FieldMap_applyvdm(*args, **kwargs):
    """
      Apply VDM and reslice images  
        FORMAT FieldMap_applyvdm(job)  
        job.data(sessnum).scans   - images for session/run sessnum  
        job.data(sessnum).vdmfile - VDM file for session/run sessnum  
        job.roptions.rinterp - interpolation method  
        job.roptions.wrap    - perform warp around in specified dimensions  
        job.roptions.mask    - perform masking  
        job.roptions.which(1) - reslice images in time series only  
        job.roptions.which(2) - reslice images in time series and mean  
        job.roptions.prefix   - prefix for vdm applied files  
        job.roptions.pedir    - phase encode direction (i.e. aplly vdm file along  
        this dimension  
       __________________________________________________________________________  
         
        A VDM (voxel displacement map) created using the FieldMap toolbox  
        can be used to resample and reslice realigned images to the original  
        subdirectory with the same (prefixed) filename.  
         
        Voxels in the images will be shifted according to the values in the VDM  
        file along the direction specified by job.roptions.pedir (i.e. this is  
        usually the phase encode direction) and resliced to the space of the  
        first image in the time series.  
         
        Inputs:  
        A job structure containing fields for the input data and the processing  
        options. The input data contains the series of images conforming to  
        SPM data format (see 'Data Format'), the relative displacement of the images  
        is stored in their header and a VDM which has (probably) been created  
        using the FieldMap toolbox and matched to the first image in the time  
        series (this can also be done via the FieldMap toolbox).  
         
        Outputs:  
        The resampled and resliced images resliced to the same subdirectory with a prefix.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/FieldMap/FieldMap_applyvdm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("FieldMap_applyvdm", *args, **kwargs)
