from spm._runtime import Runtime


def _ReadHeader(*args, **kwargs):
    """
      H = ReadHeader(fp)  
         
         Reads NSMA header, leaves file-read-location at end of header  
         
         INPUT:  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/ReadHeader.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ReadHeader", *args, **kwargs)
