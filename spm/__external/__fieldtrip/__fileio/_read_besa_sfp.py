from spm.__wrapper__ import Runtime


def _read_besa_sfp(*args, **kwargs):
  """  READ_BESA_SFP reads a besa style electrode location file.  
     
    Use as:  
      [lab, pos] = read_besa_sfp(filename, uniqueonly)  
     
    Input arguments:  
      filename   = the file name  
      uniqueonly = flag to determine behavior, to return the positions of the  
                   unique labels only (default behavior: uniqueonly=1), or  
                   also return double occurrences, which may be useful when  
                   headshape information is represented in the file (as is  
                   done in SPM)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_besa_sfp.m)
  """

  return Runtime.call("read_besa_sfp", *args, **kwargs)
