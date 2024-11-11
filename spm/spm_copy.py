from spm.__wrapper__ import Runtime


def spm_copy(*args, **kwargs):
    """
      Copy file(s)  
        FORMAT spm_copy(source, dest [,opts])  
        source  - pathnames of files or directories to be copied  
                  character vector or cellstr  
        dest    - pathnames of destination files or directories [default: pwd]  
                  character vector or cellstr  
        opts    - structure or list of name/value pairs of optional parameters:  
                    gzip: compress uncompressed copied files at destination  
                    gunzip: uncompress compressed copied files at destination  
                    nifti: also copy sidecar .hdr/.img/.mat/.json if present  
                    gifti: also copy sidecar .dat file if present  
                    mode: copy mode (see copyfile's help)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_copy.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_copy", *args, **kwargs, nargout=0)
