from spm.__wrapper__ import Runtime


def mne_block_diag(*args, **kwargs):
    """
       
          function bd = mne_block_diag(A,n)  
         
          Make or extract a sparse block diagonal matrix  
         
          If A is not sparse, then returns a sparse block diagonal "bd", diagonalized from the  
          elements in "A".  
          "A" is ma x na, comprising bdn=(na/"n") blocks of submatrices.  
          Each submatrix is ma x "n", and these submatrices are  
          placed down the diagonal of the matrix.  
         
          If A is already sparse, then the operation is reversed, yielding a block  
          row matrix, where each set of n columns corresponds to a block element  
          from the block diagonal.  
         
          Routine uses NO for-loops for speed considerations.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_block_diag.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mne_block_diag", *args, **kwargs)
