from spm._runtime import Runtime


def spm_bsplins(*args, **kwargs):
    """
      Sample a volume using B-spline interpolation - a compiled routine  
        FORMAT [f,dfx,dfy,dfz] = spm_bsplins(c,x,y,z,d)  
          c - volume of B-spline coefficients (from spm_bsplinc)  
          x,y,z - coordinates of sampled points  
              d(1:3) - degree of B-spline (from 0 to 7) along different dimensions  
                       - these must be same as used by spm_bsplinc  
              d(4:6) - 1/0 to indicate wrapping along the dimensions  
          f - sampled data  
          dfx,dfy,dfz - sampled first derivatives  
         
        This function takes B-spline basis coefficients from spm_bsplinc,  
        and re-convolves them with B-splines centred at the new sample points.  
         
        Note that nearest neighbour interpolation is used instead of 0th  
        degree B-splines, and the derivatives of trilinear interpolation are  
        returned instead of those of 1st degree B-splines.  The difference is  
        extremely subtle.  
       __________________________________________________________________________  
         
        References:  
          M. Unser, A. Aldroubi and M. Eden.  
          "B-Spline Signal Processing: Part I-Theory,"  
          IEEE Transactions on Signal Processing 41(2):821-832 (1993).  
         
          M. Unser, A. Aldroubi and M. Eden.  
          "B-Spline Signal Processing: Part II-Efficient Design and  
          Applications,"  
          IEEE Transactions on Signal Processing 41(2):834-848 (1993).  
         
          M. Unser.  
          "Splines: A Perfect Fit for Signal and Image Processing,"  
          IEEE Signal Processing Magazine, 16(6):22-38 (1999)  
         
          P. Thevenaz and T. Blu and M. Unser.  
          "Interpolation Revisited"  
          IEEE Transactions on Medical Imaging 19(7):739-758 (2000).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_bsplins.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_bsplins", *args, **kwargs)
