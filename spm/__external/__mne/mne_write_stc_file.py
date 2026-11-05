from spm._runtime import Runtime


def mne_write_stc_file(*args, **kwargs):
    r"""
       
        mne_write_stc_file(filename,stc)  
          
        writes an stc file  
         
            filename      output file  
            stc           a stucture containing the stc data with fields:  
         
            tmin          The time of the first frame in seconds  
            tstep         Time between frames in seconds  
            vertices      Vertex indices (0 based)  
            data          The data matrix nvert * ntime  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_write_stc_file.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_write_stc_file", *args, **kwargs, nargout=0)
