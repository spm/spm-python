from spm.__wrapper__ import Runtime


def spm_peb_ppi(*args, **kwargs):
    """
      Bold deconvolution to create physio- or psycho-physiologic interactions  
        FORMAT PPI = spm_peb_ppi(SPMname,ppiflag,VOI,Uu,ppiname,showGraphics)  
         
        SPM          - Structure containing generic details about the analysis or  
                       the fully qualified filename of such a structure.  
        ppiflag      - Type of analysis. Must be one of:  
                         'simple deconvolution'          or 'sd'  
                         'psychophysiologic interaction' or 'ppi'  
                         'physiophysiologic interaction' or 'phipi'  
        VOI          - Structure containing details about a VOI (as produced by  
                       spm_regions) or the fully qualified filename of such a  
                       structure. If a structure, then VOI should be of size 1x1  
                       in the case of simple deconvolution, and psychophysiologic   
                       interactions) or 1x2, in the case of physiophysiologic  
                       interactions. If a file name it should be 1xN or 2xN.  
        Uu           - Matrix of input variables and contrast weights. This is an  
                       [n x 3] matrix. The first column indexes SPM.Sess.U(i). The  
                       second column indexes the name of the input or cause, see  
                       SPM.Sess.U(i).name{j}. The third column is the contrast  
                       weight. Unless there are parametric effects the second  
                       column will generally be a 1.  
        ppiname      - Basename of the PPI file to save. The saved file will be:  
                       <PATH_TO_SPM.MAT>/PPI_<ppiname>.mat  
        showGraphics - empty or 1 = yes, 0 = no.  
         
         
        PPI.ppi      - (PSY*xn  or xn1*xn2) convolved with the HRF  
        PPI.Y        - Original BOLD eigenvariate. Use as covariate of no interest  
        PPI.P        - PSY convolved with HRF for psychophysiologic interactions,  
                       or in the case of physiophysologic interactions contains  
                       the eigenvariate of the second region.   
        PPI.name     - Name of PPI  
        PPI.xY       - Original VOI information  
        PPI.xn       - Deconvolved neural signal(s)  
        PPI.psy.u    - Psychological variable or input function (PPIs only)  
        PPI.psy.w    - Contrast weights for psychological variable (PPIs only)  
        PPI.psy.name - Names of psychological conditions (PPIs only)  
       __________________________________________________________________________  
         
        This routine is effectively a hemodynamic deconvolution using full priors  
        and EM to deconvolve the HRF from a hemodynamic time series to give a   
        neuronal time series [that can be found in PPI.xn].  This deconvolution   
        conforms to Wiener filtering. The neuronal process is then used to form   
        PPIs. See help text within function for more details.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_peb_ppi.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_peb_ppi", *args, **kwargs)
