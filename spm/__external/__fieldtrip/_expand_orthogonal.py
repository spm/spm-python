from spm.__wrapper__ import Runtime


def _expand_orthogonal(*args, **kwargs):
    """
      EXPAND_ORTHOGONAL determines an orthogonal expansion of the orthogonal basis  
        for the subspace spanned by the columns of the matrix input argument, which  
        must have more rows than columns, using either singular value decomposition  
        (svd) or the Gram-Schmidt method, see e.g., [1], (reference in code header).  
         
        Usage:  
          B = expand_orthogonal(A);  
          B = expand_orthogonal(A,flg);  
          B = expand_orthogonal(A,flg,method);  
         
        Input (Required):  
          A is a [nrows by ncols] matrix of (finite) numbers with nrows>=ncols  
         
        Input (Optional):  
          flg is a number specifying whether the output should contain the columns  
          of A (flg = 0; default) normalized to unit length, or the orthogonal basis  
          for the subspace spanned by the columns of A (flg = 1)  
         
          method  = 'svd' (default) or 'gram-schmidt' specifies which method to use  
          for generating the orthogonal expansion of the input matrix  
         
        Output:  
          B is a [nrows by nrows] matrix whose first ncols columns reflect either the  
          (normalized) columns of the intput or an orthonormal basis for the subspace  
          spanned by A; and the remaining (nrows-ncols) columns contain the orthogonal  
          expansions of the subspace spanned by A.  
         
        See also: SVD  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/expand_orthogonal.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("expand_orthogonal", *args, **kwargs)
