from spm._runtime import Runtime


def spm_write_plane(*args, **kwargs):
    r"""
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_write_plane.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_write_plane", *args, **kwargs)
