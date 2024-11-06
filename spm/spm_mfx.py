from spm.__wrapper__ import Runtime


def spm_mfx(*args, **kwargs):
    """
      Convert a 1st-level design specification into a MFX specification  
        FORMAT [SPM] = spm_mfx(SPM,c)  
        SPM {in} - design and estimation structure after a 1st-level analysis  
        c        - contrast used to define 2nd level design matrix. If this is  
                   not specified spm_mfx will (1) suggest the ones(n,1) contrast  
                   where n is the number of sessions/subjects, (2) call  
                   spm_conman to allow this contrast to be modified interactively  
         
                   Note: the specification of a contrast that is not ones(n,1) allows,   
                   for example, specified sessions/subjects to be ignored.  
                     
        SPM {out} is saved in fullfile(SPM.swd,'mfx','SPM.mat')  
         
        spm_mfx takes the SPM.mat of a 1st-level estimation of a repeated-measure  
        multi-session study and produces the SPM design specification for a  
        full mixed-effects (MFX) analysis. The 1st-level design (X1) must have  
        the same number of parameters for each session. These are assumed to  
        represent session-specific realisations of 2nd-level effects.  
         
        spm_mfx prompts for a 2nd-level design matrix (X2) in the form of an  
        F-contrast. This is expanded using the Kronecker tensor product to  
        model the effects of each 2nd-level parameter separately. A new  
        SPM.mat structure is saved in a subdirectory of the 1st-level results  
        directory and can be estimated in the usual way. 2nd-level contrasts  
        can then be used to test specific hypotheses at the 2nd-level in terms  
        of compounds of 1st-level parameters specified by X2 (e.g. their  
        mean).  
         
        spm_mfx is a full mixed effects analysis in the sense that it allows  
        for unbalanced designs at the 1st-level and different 1st-level error  
        covariances. Operationally, ReML estimates of the 1st and 2nd-level  
        covariance components are computed by projecting the 2nd-level effects  
        down to the 1st-level and partitioning the covariance of the data in  
        observation space. The 2nd-level parameter estimates are then computed  
        as linear mixtures of the 1st-level estimates, using the appropriate  
        non-sphericity. This non-sphericity is a mixture of 1st- and 2nd-level  
        components that renders the ensuing 2nd-level estimates ML.  
         
        In summary;  
         
        ReML estimates of V1 are obtained where  
         
                       y    = X1*B1 + X0*B0 + e1  
                       B1   = X2*B2 + e2;  
         
        giving;        y    = X1*X2*B2 + X0*B0 + X1*e2 + e1  
         
        where          V1   = cov(X1*e2 + e1)  
         
        V1 is now used to give the covariance components of any 1st-level  
        parameter estimators B1h  
         
                       B1h  = M1*y  
        such that      V2   = cov(B1h) = M1*V1*M1'  
         
        is the error covariance for the single level model  
         
                       B1h  = X2*B2 + r2  
         
        where cov(r2) = cov(B1h) = V2, which can be estimated non-iteratively  
        in the usual way to give the ML estimates of B2.  
         
        Note that with balanced designs and equal error covariances over  
        sessions, at the 1st level there is no need to compute multiple  
        covariance components because, at the 2nd-level, they are exactly the  
        same (i.e. M1*X1*cov(e2)*X1*M1 has the same form as M1*cov(e1)*M1).  
         
        The ReML hyperparameters are estimated using the covariance of y over  
        voxels. This means that the relative amounts of within and  
        between-session variance are assumed to be fixed over voxels but can  
        vary in their overall expression. The voxels used for this pooling are  
        those that show 1st-level responses.  
         
        See spm_reml.m  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mfx.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mfx", *args, **kwargs)
