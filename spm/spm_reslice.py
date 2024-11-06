from spm.__wrapper__ import Runtime


def spm_reslice(*args, **kwargs):
    """
      Rigid body reslicing of images  
        FORMAT spm_reslice(P,flags)  
         
        P      - matrix or cell array of filenames {one string per row}  
                 All operations are performed relative to the first image.  
                 ie. Coregistration is to the first image, and resampling  
                 of images is into the space of the first image.  
         
        flags  - a structure containing various options.  The fields are:  
         
                mask   - mask output images (true/false) [default: true]  
                         To avoid artifactual movement-related variance the  
                         realigned set of images can be internally masked, within  
                         the set (i.e. if any image has a zero value at a voxel  
                         than all images have zero values at that voxel). Zero  
                         values occur when regions 'outside' the image are moved  
                         'inside' the image during realignment.  
         
                mean   - write mean image (true/false) [default: true]  
                         The average of all the realigned scans is written to  
                         an image file with 'mean' prefix.  
         
                interp - the B-spline interpolation method [default: 1]  
                         Non-finite values result in Fourier interpolation. Note  
                         that Fourier interpolation only works for purely rigid  
                         body transformations. Voxel sizes must all be identical  
                         and isotropic.  
         
                which  - values of 0, 1 or 2 are allowed [default: 2]  
                         0   - don't create any resliced images.  
                               Useful if you only want a mean resliced image.  
                         1   - don't reslice the first image.  
                               The first image is not actually moved, so it may  
                               not be necessary to resample it.  
                         2   - reslice all the images.  
                         If which is a 2-element vector, flags.mean will be set  
                         to flags.which(2).  
         
                wrap   - three values of either 0 or 1, representing wrapping in  
                         each of the dimensions. For fMRI, [1 1 0] would be used.  
                         For PET, it would be [0 0 0]. [default: [0 0 0]]  
         
                prefix - prefix for resliced images [default: 'r']  
         
       __________________________________________________________________________  
         
        The spatially realigned images are written to the original subdirectory  
        with the same (prefixed) filename. They are all aligned with the first.  
         
        Inputs:  
        A series of images conforming to SPM data format (see 'Data Format'). The  
        relative displacement of the images is stored in their header.  
         
        Outputs:  
        The routine uses information in their headers and writes the realigned   
        image files to the same subdirectory with a prefix.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_reslice.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_reslice", *args, **kwargs, nargout=0)
