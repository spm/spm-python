from spm.__wrapper__ import Runtime


def spm_write_sn(*args, **kwargs):
    """
      Write out warped images  
        FORMAT VO = spm_write_sn(V,prm,flags,msk)  
        V         - Images to transform (filenames or volume structure).  
        prm       - Transformation information (filename or structure).  
        flags     - flags structure, with fields...  
                  interp   - interpolation method (0-7)  
                  wrap     - wrap edges (e.g., [1 1 0] for 2D MRI sequences)  
                  vox      - voxel sizes (3 element vector - in mm)  
                             Non-finite values mean use template vox.  
                  bb       - bounding box (2x3 matrix - in mm)  
                             Non-finite values mean use template bb.  
                  preserve - either 0 or 1.  A value of 1 will "modulate"  
                             the spatially normalised images so that total  
                             units are preserved, rather than just  
                             concentrations.  
                  prefix   - Prefix for normalised images. Defaults to 'w'.  
        msk       - An optional cell array for masking the spatially  
                    normalised images (see below).  
         
        Warped images are written prefixed by "w".  
         
        Non-finite vox or bounding box suggests that values should be derived  
        from the template image.  
         
        Don't use interpolation methods greater than one for data containing  
        NaNs.  
       __________________________________________________________________________  
         
        FORMAT msk = spm_write_sn(V,prm,flags,'mask')  
        V          - Images to transform (filenames or volume structure).  
        prm        - Transformation information (filename or structure).  
        flags      - flags structure, with fields...  
                   wrap - wrap edges (e.g., [1 1 0] for 2D MRI sequences)  
                   vox  - voxel sizes (3 element vector - in mm)  
                          Non-finite values mean use template vox.  
                   bb   - bounding box (2x3 matrix - in mm)  
                          Non-finite values mean use template bb.  
        msk        - a cell array for masking a series of spatially normalised  
                     images.  
         
         
       _________________________________________________________________________  
         
        FORMAT VO = spm_write_sn(V,prm,'modulate')  
        V         - Spatially normalised images to modulate (filenames or  
                    volume structure).  
        prm       - Transformation information (filename or structure).  
         
         After nonlinear spatial normalization, the relative volumes of some  
         brain structures will have decreased, whereas others will increase.  
         The resampling of the images preserves the concentration of pixel  
         units in the images, so the total counts from structures that have  
         reduced volumes after spatial normalization will be reduced by an  
         amount proportional to the volume reduction.  
         
         This routine rescales images after spatial normalization, so that  
         the total counts from any structure are preserved.  It was written  
         as an optional step in performing voxel based morphometry.  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/OldNorm/spm_write_sn.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_write_sn", *args, **kwargs)
