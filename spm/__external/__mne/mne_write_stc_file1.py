from spm.__wrapper__ import Runtime


def mne_write_stc_file1(*args, **kwargs):
    """
       
        mne_write_stc_file1(filename,stc)  
          
        writes an stc file  
         
            filename      output file  
            stc           a stucture containing the stc data with fields:  
         
            tmin          The time of the first frame in seconds  
            tstep         Time between frames in seconds  
            vertices      Vertex indices (1 based)  
            data          The data matrix nvert * ntime  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_write_stc_file1.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mne_write_stc_file1", *args, **kwargs, nargout=0)
