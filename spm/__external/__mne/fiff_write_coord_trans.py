from spm.__wrapper__ import Runtime


def fiff_write_coord_trans(*args, **kwargs):
    """
       
        fiff_write_coord_trans(fid,trans)  
          
        Writes a coordinate transformation structure  
         
            fid           An open fif file descriptor  
            trans         The coordinate transfomation structure  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_write_coord_trans.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fiff_write_coord_trans", *args, **kwargs, nargout=0)
