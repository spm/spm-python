from spm.__wrapper__ import Runtime


def _read_imotions_txt(*args, **kwargs):
  """  READ_IMOTIONS_TXT reads *.txt files that are exported from the iMotions software.  
     
    Use as  
      dat = read_imotions_txt(filename  
     
    See also TEXTSCAN  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/read_imotions_txt.m)
  """

  return Runtime.call("read_imotions_txt", *args, **kwargs)
