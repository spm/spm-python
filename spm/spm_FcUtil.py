from spm.__wrapper__ import Runtime


def spm_FcUtil(*args, **kwargs):
    """
      Contrast utilities  
        FORMAT varargout = spm_FcUtil(action,varargin)  
       _______________________________________________________________________  
         
        spm_FcUtil is a multi-function function containing various utilities  
        for contrast construction and manipulation. In general, it accepts  
        design matrices as plain matrices or as space structures setup by  
        spm_sp (that is preferable in general).  
          
        The use of spm_FcUtil should help with robustness issues and  
        maintainability of SPM.  % Note that when space structures are passed  
        as arguments is is assumed that their basic fields are filled in.  
        See spm_sp for details of (design) space structures and their  
        manipulation.  
         
         
        ======================================================================  
        case 'fconfields'             %- fields of F contrast  
        Fc = spm_FcUtil('FconFields')  
         
       - simply returns the fields of a contrast structure.  
         
       =======================================================================  
        case 'set'                    %- Create an F contrast  
        Fc = spm_FcUtil('Set',name, STAT, set_action, value, sX)  
         
       - Set will fill in the contrast structure, in particular   
       - c (in the contrast space), X1o (the space actually tested) and  
       - X0 (the space left untested), such that space([X1o X0]) == sX.  
       - STAT is either 'F' or 'T';  
       - name is a string describing the contrast.  
         
       - There are three ways to set a contrast :  
       - set_action is 'c','c+'   : value can then be zeros.  
       -                dimensions are in X',   
       -                f c+ is used, value is projected onto sX';  
       -                                iX0 is set to 'c' or 'c+';  
       - set_action is 'iX0'      : defines the indices of the columns   
       -                that will not be tested. Can be empty.  
       - set_action is 'X0'       : defines the space that will remain   
       -                unchanged. The orthogonal complement is  
       -                tested; iX0 is set to 'X0';  
       -                                    
       =======================================================================  
        case 'isfcon'                 %- Is it an F contrast ?  
        b = spm_FcUtil('IsFcon',Fc)  
         
       =======================================================================  
        case 'fconedf'                    %- F contrast edf  
        [edf_tsp edf_Xsp] = spm_FcUtil('FconEdf', Fc, sX [, V])  
         
       - compute the effective degrees of freedom of the numerator edf_tsp  
       - and (optionally) the denominator edf_Xsp of the contrast.  
         
       =======================================================================  
        case 'hsqr' %-Extra sum of squares sqr matrix for beta's from contrast  
        hsqr = spm_FcUtil('Hsqr',Fc, sX)  
         
       - This computes the matrix hsqr such that a the numerator of an F test  
       - will be beta'*hsqr'*hsqr*beta  
         
       =======================================================================  
        case 'h'     %-Extra sum of squares matrix for beta's from contrast  
        H = spm_FcUtil('H',Fc, sX)  
         
       - This computes the matrix H such that a the numerator of an F test  
       - will be beta'*H*beta  
       -                                    
       =======================================================================  
        case 'yc' %- Fitted data corrected for confounds defined by Fc   
        Yc = spm_FcUtil('Yc',Fc, sX, b)  
         
       - Input : b : the betas                              
       - Returns the corrected data Yc for given contrast. Y = Yc + Y0 + error  
         
       =======================================================================  
        case 'y0' %-  Confounds data defined by Fc   
        Y0 = spm_FcUtil('Y0',Fc, sX, b)  
         
       - Input : b : the betas                              
       - Returns the confound data Y0 for a given contrast. Y = Yc + Y0 + error  
         
       =======================================================================  
        case {'|_'}       %-  Fc orthogonalisation   
        Fc = spm_FcUtil('|_',Fc1, sX, Fc2)  
         
       - Orthogonolise a (list of) contrasts Fc1 wrt a (list of) contrast Fc2  
       - such that the space these contrasts test are orthogonal.  
       - If contrasts are not estimable contrasts, works with the estimable   
       - part. In any case, returns estimable contrasts.    
         
       =======================================================================  
        case {'|_?'}      %-  Are contrasts orthogonals   
        b = spm_FcUtil('|_?',Fc1, sX [, Fc2])  
         
       - Tests whether a (list of) contrast is orthogonal. Works with the  
       - estimable part if they are not estimable. With only one argument,  
       - tests whether the list is made of orthogonal contrasts. With Fc2  
       - provided, tests whether the two (list of) contrast are orthogonal.   
         
       =======================================================================  
        case 'in'    %-  Fc1 is in list of  contrasts Fc2  
        [iFc2 iFc1] = spm_FcUtil('In', Fc1, sX, Fc2)  
         
       - Tests whether a (list of) contrast Fc1 is in a list of contrast Fc2.  
       - returns the indices iFc2 where element of Fc1 have been found  
       - in Fc2 and the indices iFc1 of the element of Fc1 found in Fc2.  
       - These indices are not necessarily unique.  
         
       =======================================================================  
        case '~unique'     %-  Fc list unique   
        idx = spm_FcUtil('~unique', Fc, sX)  
         
       - returns indices ofredundant contrasts in Fc  
       - such that Fc(idx) = [] makes Fc unique.  
         
       =======================================================================  
        case {'0|[]','[]|0'}     %-  Fc is null or empty   
        b = spm_FcUtil('0|[]', Fc, sX)  
         
       - NB : for the "null" part, checks if the contrast is in the null space   
       - of sX (completely non estimable !)  
       =======================================================================  
       _______________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_FcUtil.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_FcUtil", *args, **kwargs)
