from spm.__wrap__ import _Runtime


def _openedf(*args, **kwargs):
  """  EDF=openedf(FILENAME)  
    Opens an EDF File (European Data Format for Biosignals) in MATLAB (R)  
    <A HREF="http://www.medfac.leidenuniv.nl/neurology/knf/kemp/edf.htm">About EDF</A>  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/openedf.m)
  """

  return _Runtime.call("openedf", *args, **kwargs)
