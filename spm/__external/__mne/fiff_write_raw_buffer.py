from spm.__wrapper__ import Runtime


def fiff_write_raw_buffer(*args, **kwargs):
    """
       
        function fiff_write_raw_buffer(fid,buf,cals,datatype)  
         
        fid        of an open raw data file  
        buf        the buffer to write  
        cals       calibration factors  
        datatype   (optional) datatype to write, default float  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_write_raw_buffer.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fiff_write_raw_buffer", *args, **kwargs, nargout=0)
