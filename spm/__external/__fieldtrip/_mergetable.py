from spm.__wrapper__ import Runtime


def _mergetable(*args, **kwargs):
    """
      MERGETABLE merges two tables where the rows and columns can be partially  
        overlapping or different. Values from the 2nd input have precedence in case the  
        same row and column is also present in the 1st.  
         
        Use as  
          t3 = mergetable(t1, t2)  
        or  
          t3 = mergetable(t1, t2, key)  
         
        See also MERGESTRUCT, JOIN, INNERJOIN, OUTERJOIN  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/mergetable.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mergetable", *args, **kwargs)
