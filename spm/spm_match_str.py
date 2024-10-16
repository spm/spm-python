from spm.__wrapper__ import Runtime


def spm_match_str(*args, **kwargs):
  """  MATCH_STR looks for matching labels in two listst of strings  
    and returns the indices into both the 1st and 2nd list of the matches.  
    They will be ordered according to the first input argument.  
       
    [sel1, sel2] = match_str(strlist1, strlist2)  
     
    The strings can be stored as a char matrix or as an vertical array of  
    cells, the matching is done for each row.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_match_str.m)
  """

  return Runtime.call("spm_match_str", *args, **kwargs)
