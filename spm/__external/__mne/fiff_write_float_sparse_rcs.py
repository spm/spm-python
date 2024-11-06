from spm.__wrapper__ import Runtime


def fiff_write_float_sparse_rcs(*args, **kwargs):
    """
       
        fiff_write_float_sparsce_rcs(fid,kind,mat)  
          
        Writes a single-precision sparse (RCS) floating-point matrix tag  
         
            fid           An open fif file descriptor  
            kind          The tag kind  
            mat           The data matrix  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_write_float_sparse_rcs.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fiff_write_float_sparse_rcs", *args, **kwargs, nargout=0)
