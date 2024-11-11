from spm.__wrapper__ import Runtime


def spm_write_plane(*args, **kwargs):
    """
      Write transverse plane(s) of image data  
        FORMAT V = spm_write_plane(V,dat,n)  
        V   - data structure containing image information (see spm_vol)  
        dat - the two/three dimensional image to write  
        n   - the plane number(s) (beginning from 1). If an entire volume  
              should be written, n should contain the single character ':'  
              instead of plane numbers.  
         
        V   - (possibly) modified data structure containing image information.  
              It is possible that future versions of spm_write_plane may  
              modify scalefactors (for example).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_write_plane.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_write_plane", *args, **kwargs)
