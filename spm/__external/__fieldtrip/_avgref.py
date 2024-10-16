from spm.__wrapper__ import Runtime


def _avgref(*args, **kwargs):
  """  AVGREF computes the average reference in each column  
      [data] = avgref(data)  
     
    or it computes the re-referenced data relative to the  
    average over the selected channels  
      [data] = avgref(data, sel)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/avgref.m)
  """

  return Runtime.call("avgref", *args, **kwargs)
