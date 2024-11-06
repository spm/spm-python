from spm.__wrapper__ import Runtime


def _read_videomeg_aud(*args, **kwargs):
    """
      READ_VIDEOMEG_AUD  
         
        Use as  
          hdr = read_videomeg_aud(filename)  
        or  
          dat = read_videomeg_aud(filename, hdr, begsample, endsample)  
         
        See also READ_VIDEOMEG_VID, LOAD_AUDIO0123, LOAD_VIDEO123  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_videomeg_aud.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_videomeg_aud", *args, **kwargs)
