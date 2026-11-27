from spm._runtime import Runtime


def _read_mat(*args, **kwargs):
    r"""
      READ_MAT reads a matrix from an ascii or binary MBF format file  
         
         Usage: m         = loadmat('file');  
            or  [m,extra] = loadmat('file');  
           
         LOADMAT('file') returns the matrix stored in 'file' and  
         the extra information stored at the bottom of that file.  
         LOADMAT works for binary as well as asci matrix files.  
           
         See also WRITE_MAT  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_mat.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_mat", *args, **kwargs)
