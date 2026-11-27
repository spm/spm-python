from spm._runtime import Runtime


def spm_data_write(*args, **kwargs):
    r"""
      Write data to disk [V(I) = Y]  
        FORMAT V = spm_data_write(V,Y)  
        V        - a structure array (see spm_data_hdr_read)  
        Y        - an array of data values  
         
        FORMAT V = spm_data_write(V,Y,I)  
        V        - a structure array (see spm_data_hdr_read)  
        Y        - an array of data values  
        I        - linear index to data values  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_data_write.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_data_write", *args, **kwargs)
