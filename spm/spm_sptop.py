from spm.__wrapper__ import Runtime


def spm_sptop(*args, **kwargs):
    """
      Sparse Toeplitz convolution matrix given convolution kernel  
        FORMAT [K] = spm_sptop(sigma,q,c)  
         
        sigma - of Gaussian kernel K (or kernel itself)  
        q     - order of matrix  
        c     - kernel index at t = 0 {default c = length(sigma)/2)   
        K     - q x q sparse convolution matrix  
       __________________________________________________________________________  
         
        Returns a q x q sparse convolution matrix.  If sigma is a scalar then  
        a symmetrical Gaussian convolution matrix is returned with kernel width  
        = sigma.  If sigma is a vector than sigma constitutes the kernel.  To  
        obtain an asymmetrical convolution matrix (i.e. implement a phase shift  
        set c = 1.  
         
        Boundary handling: The row-wise sum of K is set to unity (kernel truncation)  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_sptop.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_sptop", *args, **kwargs)
