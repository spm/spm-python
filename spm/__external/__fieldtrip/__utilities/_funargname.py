from spm.__wrapper__ import Runtime


def _funargname(*args, **kwargs):
  """  FUNARGNAME returns the input and output arguments of the function  
    by parsing the m-file  
     
    Use as  
       [input, output] = funargname(fname)  
    where the input and output function arguments will be returned  
    as cell-arrays containing strings.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/funargname.m)
  """

  return Runtime.call("funargname", *args, **kwargs)
