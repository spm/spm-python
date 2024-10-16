from spm.__wrapper__ import Runtime


def _read_tobii_tsv(*args, **kwargs):
  """  READ_TOBII_TSV  
     
    Use as  
      hdr = read_tobii_tsv(filename)  
    or  
      dat = read_tobii_tsv(filename, tsv, begsample, endsample)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_tobii_tsv.m)
  """

  return Runtime.call("read_tobii_tsv", *args, **kwargs)
