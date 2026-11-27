from spm._runtime import Runtime


def _read_video(*args, **kwargs):
    r"""
      READ_VIDEO  
         
        Use as  
          hdr = read_video(filename)  
        or  
          dat = read_video(filename, hdr, begsample, endsample)  
         
        See also READ_VIDEOMEG_VID, LOAD_VIDEO123  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_video.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_video", *args, **kwargs)
