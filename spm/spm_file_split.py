from spm._runtime import Runtime


def spm_file_split(*args, **kwargs):
    r"""
      Convert a 4D volume file into a series of 3D volume files  
        FORMAT Vo = spm_file_split(V, odir)  
        V         - filename or spm_vol struct  
        odir      - output directory [default: same as input]  
         
        Vo        - spm_vol struct array of output files  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_file_split.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_file_split", *args, **kwargs)
