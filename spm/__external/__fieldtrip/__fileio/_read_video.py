from spm.__wrapper__ import Runtime


def _read_video(*args, **kwargs):
    """
      READ_VIDEO  
         
        Use as  
          hdr = read_video(filename)  
        or  
          dat = read_video(filename, hdr, begsample, endsample)  
         
        See also READ_VIDEOMEG_VID, LOAD_VIDEO123  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_video.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_video", *args, **kwargs)
