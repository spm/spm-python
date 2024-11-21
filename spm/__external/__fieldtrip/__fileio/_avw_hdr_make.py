from spm.__wrapper__ import Runtime


def _avw_hdr_make(*args, **kwargs):
    """
      AVW_HDR_MAKE - Create Analyze format data header (avw.hdr)  
          
        [ avw ] = avw_hdr_make  
          
        avw.hdr - a struct, all fields returned from the header.  
                  For details, find a good description on the web  
                  or see the Analyze File Format pdf in the   
                  mri_toolbox doc folder or see avw_hdr_read.m  
          
        See also, AVW_HDR_READ AVW_HDR_WRITE  
                  AVW_IMG_READ AVW_IMG_WRITE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/avw_hdr_make.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("avw_hdr_make", *args, **kwargs)
