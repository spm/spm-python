from spm.__wrapper__ import Runtime


def _write_edf(*args, **kwargs):
    """
      WRITE_EDF(filename, header, data)  
         
        Writes a EDF file from the given header (only label, Fs, nChans are of interest)  
        and the data (unmodified). Digital and physical limits are derived from the data  
        via min and max operators. The EDF file will contain N records of 1 sample each,  
        where N is the number of columns in 'data'.  
         
        For sampling rates > 1 Hz, this means that the duration of one data "record"  
        is less than 1s, which some EDF reading programs might complain about. At the  
        same time, there is an upper limit of how big (in bytes) a record should be,  
        which we could easily violate if we write the whole data as *one* record.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/write_edf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("write_edf", *args, **kwargs, nargout=0)
