from spm.__wrapper__ import Runtime


def spm_data_read(*args, **kwargs):
    """
      Read data from disk [Y = V(I)]  
        FORMAT Y = spm_data_read(V)  
        V        - a structure array (see spm_data_hdr_read)  
        Y        - an array of data values; the last dimension indexes numel(V)  
         
        FORMAT Y = spm_data_read(V,'slice',S)  
        V        - a structure array of image volumes (see spm_data_hdr_read)  
        S        - an array of slice indices  
        Y        - an array of data values with dimensions (x,y,s,v)  
         
        FORMAT Y = spm_data_read(V,'xyz',XYZ)  
        V        - a structure array (see spm_data_hdr_read)  
        XYZ      - a [n x m] array of m coordinates {voxel (n=3 or 4)/vertex (n=1)}  
        Y        - an array of data values with dimensions (v,m)  
         
        FORMAT Y = spm_data_read(V,I1,I2,...)  
        V        - a structure array (see spm_data_hdr_read)  
        I1,I2,...- subscript arrays  
        Y        - an array of data values with dimensions (v,m)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_data_read.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_data_read", *args, **kwargs)
