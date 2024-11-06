from spm.__wrapper__ import Runtime


def spm_read_vols(*args, **kwargs):
    """
      Read in entire image volumes  
        FORMAT [Y,XYZmm] = spm_read_vols(V,mask)  
        V      - vector of mapped image volumes to read in (from spm_vol)  
        mask   - implicit zero mask?  
         
        Y      - 4D matrix of image data, fourth dimension indexes images  
        XYZmm  - 3xn matrix of XYZ locations returned {mm}  
       __________________________________________________________________________  
         
        For image data types without a representation of NaN (see spm_type),  
        implicit zero masking can be used. If mask is set, then zeros are  
        treated as masked, and returned as NaN.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_read_vols.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_read_vols", *args, **kwargs)
