from spm.__wrapper__ import Runtime


def _artifact_level(*args, **kwargs):
  """  This function is shared between FT_REJECTVISUAL and FT_BADCHANNEL  
     
    Use as  
      level = artifact_level(dat, metric, mval, sd, connectivity)  
    where  
      dat           = nchan*ntime, data of a single trial  
      metric        = string, see below in the code  
      mval          = mean value over all trials  
      sd            = standard deviation over all trials  
      connectivity  = nchan*nchan connectivity matrix  
    and  
      level         = nchan*1 vector with values  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/artifact_level.m)
  """

  return Runtime.call("artifact_level", *args, **kwargs)
