from spm.__wrapper__ import Runtime


def _match_str(*args, **kwargs):
    """
      MATCH_STR looks for matching labels in two lists of strings  
        and returns the indices into both the 1st and 2nd list of the matches.  
        They will be ordered according to the first input argument.  
         
        Use as  
          [sel1, sel2] = match_str(strlist1, strlist2)  
         
        The strings can be stored as a char matrix or as an vertical array of  
        cells, the matching is done for each row.  
         
        When including a 1 as the third input argument, the output lists of  
        indices will be expanded to the size of the largest input argument.  
        Entries that occur only in one of the two inputs will correspond to a 0  
        in the output, in this case. This can be convenient in rare cases if the  
        size of the input lists is meaningful.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/match_str.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("match_str", *args, **kwargs)
