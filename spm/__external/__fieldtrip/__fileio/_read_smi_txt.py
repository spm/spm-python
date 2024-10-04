from spm.__wrap__ import _Runtime


def _read_smi_txt(*args, **kwargs):
  """  READ_SMI_TXT reads the header information, input triggers, messages  
    and all data points from an SensoMotoric Instruments (SMI) *.txt file  
     
    Use as  
      smi = read_smi_txt(filename)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_smi_txt.m)
  """

  return _Runtime.call("read_smi_txt", *args, **kwargs)
