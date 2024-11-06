from spm.__wrapper__ import Runtime


def spm_data_write(*args, **kwargs):
    """
      Write data to disk [V(I) = Y]  
        FORMAT V = spm_data_write(V,Y)  
        V        - a structure array (see spm_data_hdr_read)  
        Y        - an array of data values  
         
        FORMAT V = spm_data_write(V,Y,I)  
        V        - a structure array (see spm_data_hdr_read)  
        Y        - an array of data values  
        I        - linear index to data values  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_data_write.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_data_write", *args, **kwargs)
