from spm.__wrap__ import _Runtime


def _closedf(*args, **kwargs):
  """  EDF=closedf(EDF)  
    Opens an EDF File (European Data Format for Biosignals) into MATLAB  
    <A HREF="http://www.medfac.leidenuniv.nl/neurology/knf/kemp/edf.htm">About EDF</A>   
     
    EDF   struct of EDF-Header of a EDF-File  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/closedf.m)
  """

  return _Runtime.call("closedf", *args, **kwargs)
