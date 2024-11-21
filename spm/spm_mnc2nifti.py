from spm.__wrapper__ import Runtime


def spm_mnc2nifti(*args, **kwargs):
    """
      Import MINC images into NIfTI  
        FORMAT spm_mnc2nifti(fname)  
        fname - a MINC filename  
        opts  - options structure  
         
        N     - NIfTI object (written in current directory)  
        cdf   - NetCDF data structure  
          
        The MINC file format was developed by Peter Neelin at the Montreal  
        Neurological Institute, and is based upon the NetCDF libraries.  
        The NetCDF documentation specifically recommends that people do not  
        write their own libraries for accessing the data.  This suggestion  
        was ignored.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mnc2nifti.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mnc2nifti", *args, **kwargs)
