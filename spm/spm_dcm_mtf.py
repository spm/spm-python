from spm.__wrapper__ import Runtime


def spm_dcm_mtf(*args, **kwargs):
    """
      Compute transfer functions using the system's eigenspectrum  
        FORMAT [S,K,s,w,t,dfdx] = spm_dcm_mtf(P,M,[U])  
         
        P - model parameters  
        M - model (with flow M.f and expansion point M.x and M.u)  
        U - induces expansion around steady state (from spm_dcm_neural_x(P,M))  
         
        S    - modulation transfer functions (complex)  
        K    - Volterra kernels (real)  
        s    - eigenspectrum (complex)  
        w    - frequencies (Hz) = M.Hz  
        t    - time (seconds)   = M.pst  
        dfdx - Jacobian  
         
        This routine uses the eigensolution of a dynamical systems Jacobian to  
        complete the first-order Volterra terminals and transfer functions  in  
        peristimulus and frequency space respectively.  The advantage of using  
        the-solution is that unstable modes (eigenvectors of the Jacobian) can be  
        conditioned (suppressed). Furthermore, this provides for a  
        computationally efficient and transparent evaluation of the transfer  
        functions that draws on linear signal processing theory in frequency  
        space.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_mtf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_mtf", *args, **kwargs)
