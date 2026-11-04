from spm._runtime import Runtime


def match_val(*args, **kwargs):
    r"""
      MATCH_VAL looks for matching values in two arrays of values  
        and returns the indices into both the 1st and 2nd list of the matches.  
        They will be ordered according to the first input argument.  
         
        Use as  
          [sel1, sel2] = match_str(vallist1, vallist2)  
         
        See also MATCH_STR  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/match_val.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("match_val", *args, **kwargs)
