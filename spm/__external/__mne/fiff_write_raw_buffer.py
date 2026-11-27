from spm._runtime import Runtime


def fiff_write_raw_buffer(*args, **kwargs):
    r"""
       
        function fiff_write_raw_buffer(fid,buf,cals,datatype)  
         
        fid        of an open raw data file  
        buf        the buffer to write  
        cals       calibration factors  
        datatype   (optional) datatype to write, default float  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_write_raw_buffer.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_write_raw_buffer", *args, **kwargs, nargout=0)
