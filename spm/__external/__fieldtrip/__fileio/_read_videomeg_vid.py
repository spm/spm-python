from spm.__wrapper__ import Runtime


def _read_videomeg_vid(*args, **kwargs):
    """
      READ_VIDEOMEG_VID  
         
        Use as  
          hdr = read_videomeg_vid(filename)  
        or  
          dat = read_videomeg_vid(filename, hdr, begsample, endsample)  
         
        See also READ_VIDEOMEG_AUD, LOAD_AUDIO0123, LOAD_VIDEO123  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_videomeg_vid.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_videomeg_vid", *args, **kwargs)
