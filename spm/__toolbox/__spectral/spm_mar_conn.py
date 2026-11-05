from spm._runtime import Runtime


def spm_mar_conn(*args, **kwargs):
    r"""
      Test for significance of connections  
        FORMAT [psig,chi2] = spm_mar_conn (mar,conn)  
         
        mar            MAR data structure (see spm_mar.m)  
        conn           conn(i,j)=1 if we are testing significance  
                       of connection from time series i to time  
                       series j - zero otherwise  
          
        psig           significance of connection  
        chi2           associated Chi^2 value  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/spectral/spm_mar_conn.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mar_conn", *args, **kwargs)
