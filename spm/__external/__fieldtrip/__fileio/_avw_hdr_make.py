from spm.__wrap__ import _Runtime


def _avw_hdr_make(*args, **kwargs):
  """  AVW_HDR_MAKE - Create Analyze format data header (avw.hdr)  
      
    [ avw ] = avw_hdr_make  
      
    avw.hdr - a struct, all fields returned from the header.  
              For details, find a good description on the web  
              or see the Analyze File Format pdf in the   
              mri_toolbox doc folder or see avw_hdr_read.m  
      
    See also, AVW_HDR_READ AVW_HDR_WRITE  
              AVW_IMG_READ AVW_IMG_WRITE  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/avw_hdr_make.m)
  """

  return _Runtime.call("avw_hdr_make", *args, **kwargs)
