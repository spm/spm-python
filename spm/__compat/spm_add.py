from spm.__wrapper__ import Runtime


def spm_add(*args, **kwargs):
    """
      Add a series of images - a compiled routine  
        FORMAT s = spm_add(VI,VO)  
        VI    - Vector of mapped volumes (from spm_map or spm_vol).  
        VO    - Description of output volume that gets passed to  
                spm_write_plane.m  
        flags - Flags can be:  
                      'm' - masks the mean to zero or NaN wherever  
                            a zero occurs in the input images.  
        s     - Scalefactor for output image.  
       __________________________________________________________________________  
         
        spm_add computes a sum of a set of image volumes to produce an  
        integral image that is written to a named file (VI.fname).  
         
        A mean can be effected by modifying the scalefactors (and offsets) of  
        VI (see spm_mean_ui for an example). A weighted sum can be effected by  
        using different weightings for image scalefactors.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/compat/spm_add.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_add", *args, **kwargs)
