from spm.__wrap__ import _Runtime


def _read_nmc_archive_k_hdr(*args, **kwargs):
  """  READ_NMC_ARCHIVE_K_HDR extracts 'header-data' for nmc_archive_k datasets  
     
    Use as  
      hdr = read_nmc_archive_k_hdr(paramfile)  
     
     
    This function specifically only reads data from one of the archived  
    datasets of the Neurophysiological Mechanisms of Cognition group of  
    Eric Maris, at the Donders Centre for Cognition, Radboud University,  
    Nijmegen, the Netherlands. It should not be used for any other data  
    format.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_nmc_archive_k_hdr.m)
  """

  return _Runtime.call("read_nmc_archive_k_hdr", *args, **kwargs)
