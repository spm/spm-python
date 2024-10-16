from spm.__wrapper__ import Runtime


def _read_bti_ascii(*args, **kwargs):
  """  READ_BTI_ASCII reads general data from a BTI configuration file  
     
    The file should be formatted like  
       Group:  
         item1 : value1a value1b value1c  
         item2 : value2a value2b value2c  
         item3 : value3a value3b value3c  
         item4 : value4a value4b value4c  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_bti_ascii.m)
  """

  return Runtime.call("read_bti_ascii", *args, **kwargs)
