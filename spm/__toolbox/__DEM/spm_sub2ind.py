from spm._runtime import Runtime


def spm_sub2ind(*args, **kwargs):
    r"""
     SUB2IND Linear index from multiple subscripts (without error checking).  
          SUB2IND is used to determine the equivalent single index  
          corresponding to a given set of subscript values.  
         
          IND = SUB2IND(SIZ,I,J) returns the linear index equivalent to the  
          row and column subscripts in the arrays I and J for a matrix of  
          size SIZ.   
         
          IND = SUB2IND(SIZ,I1,I2,...,IN) returns the linear index  
          equivalent to the N subscripts in the arrays I1,I2,...,IN for an  
          array of size SIZ.  
         
          I1,I2,...,IN must have the same size, and IND will have the same size  
          as I1,I2,...,IN. For an array A, if IND = SUB2IND(SIZE(A),I1,...,IN)),  
          then A(IND(k))=A(I1(k),...,IN(k)) for all k.  
         
          Class support for inputs I,J:   
             float: double, single  
             integer: uint8, int8, uint16, int16, uint32, int32, uint64, int64  
         
          See also IND2SUB.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_sub2ind.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_sub2ind", *args, **kwargs)
