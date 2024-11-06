from spm.__wrapper__ import Runtime


def spm_ind2sub(*args, **kwargs):
    """
     IND2SUB Multiple subscripts from linear index.  
          IND2SUB is used to determine the equivalent subscript values  
          corresponding to a given single index into an array.  
         
          [I,J] = IND2SUB(SIZ,IND) returns the arrays I and J containing the  
          equivalent row and column subscripts corresponding to the index  
          matrix IND for a matrix of size SIZ.    
          For matrices, [I,J] = IND2SUB(SIZE(A),FIND(A>5)) returns the same  
          values as [I,J] = FIND(A>5).  
         
          [I1,I2,I3,...,In] = IND2SUB(SIZ,IND) returns N subscript arrays  
          I1,I2,..,In containing the equivalent N-D array subscripts  
          equivalent to IND for an array of size SIZ.  
         
          Class support for input IND:  
             float: double, single  
             integer: uint8, int8, uint16, int16, uint32, int32, uint64, int64  
         
          See also SUB2IND, FIND.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_ind2sub.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_ind2sub", *args, **kwargs)
