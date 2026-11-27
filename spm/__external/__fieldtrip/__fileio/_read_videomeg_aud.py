from spm._runtime import Runtime


def _read_videomeg_aud(*args, **kwargs):
    r"""
      READ_VIDEOMEG_AUD  
         
        Use as  
          hdr = read_videomeg_aud(filename)  
        or  
          dat = read_videomeg_aud(filename, hdr, begsample, endsample)  
         
        See also READ_VIDEOMEG_VID, LOAD_AUDIO0123, LOAD_VIDEO123  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_videomeg_aud.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_videomeg_aud", *args, **kwargs)
