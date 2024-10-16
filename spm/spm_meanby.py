from spm.__wrapper__ import Runtime


def spm_meanby(*args, **kwargs):
  """  Means of data in columns by group  
    FORMAT [M,Mi,i] = spm_meanby(Y,I)  
    Y  - Data matrix, data in columns. (Row vector Y also accepted.)  
    I  - Column of indicator vectors, indicating group membership of rows of Y  
       - Multi-column I are treated as multiple factors to be interacted, and  
         means are computed within each unique combination of the factor levels  
    M  - Matrix of same size as Y, with observations replaced by the  
         appropriate group mean  
    Mi - Mean for observations in each group, one column for each column of Y,  
         one row for each group (or unique factor level combination)  
    i  - Group indicator values corresponding to rows of Mi  
   __________________________________________________________________________  
     
    spm_meanby computes means for grouped data presented as columns of data  
    with a vector of group indicators.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_meanby.m)
  """

  return Runtime.call("spm_meanby", *args, **kwargs)
