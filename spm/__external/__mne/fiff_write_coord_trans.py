from spm._runtime import Runtime


def fiff_write_coord_trans(*args, **kwargs):
    r"""
       
        fiff_write_coord_trans(fid,trans)  
          
        Writes a coordinate transformation structure  
         
            fid           An open fif file descriptor  
            trans         The coordinate transfomation structure  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_write_coord_trans.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_write_coord_trans", *args, **kwargs, nargout=0)
