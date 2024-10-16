from spm.__wrapper__ import Runtime


def _mergestruct(*args, **kwargs):
  """  MERGESTRUCT merges the fields of a structure with another structure. The fields of  
    the 2nd structure are only copied in case they are absent in the 1st structure.  
     
    Use as  
      s3 = mergestruct(s1, s2, emptymeaningful)  
     
    See also PRINTSTRUCT, APPENDSTRUCT, COPYFIELDS, KEEPFIELDS, REMOVEFIELDS, MERGETABLE  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/mergestruct.m)
  """

  return Runtime.call("mergestruct", *args, **kwargs)
