from spm.__wrapper__ import Runtime


def spm_write_vol(*args, **kwargs):
    """
      Write an image volume to disk, setting scales and offsets as appropriate  
        FORMAT V = spm_write_vol(V,Y)  
        V (input)  - a structure containing image volume information (see spm_vol)  
        Y          - a one, two or three dimensional matrix containing the image voxels  
        V (output) - data structure after modification for writing.  
         
        Note that if there is no 'pinfo' field, then SPM will figure out the  
        max and min values from the data and use these to automatically determine  
        scalefactors.  If 'pinfo' exists, then the scalefactor in this is used.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_write_vol.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_write_vol", *args, **kwargs)
