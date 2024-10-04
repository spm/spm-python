from spm.__wrap__ import _Runtime


def match_val(*args, **kwargs):
  """  MATCH_VAL looks for matching values in two arrays of values  
    and returns the indices into both the 1st and 2nd list of the matches.  
    They will be ordered according to the first input argument.  
     
    Use as  
      [sel1, sel2] = match_str(vallist1, vallist2)  
     
    See also MATCH_STR  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/match_val.m)
  """

  return _Runtime.call("match_val", *args, **kwargs)
