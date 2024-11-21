from spm.__wrapper__ import Runtime


def spm_eeg_inv_vb_ecd_gui(*args, **kwargs):
    """
      GUI function for variational Bayesian ECD inversion  
         
        Fills in the following fields of the inverse structure:  
        inverse = struct( ...  
            'F',            % free energies as dipoles are removed  
            'pst',          % all time points in data epoch  
            'tb',           % time window/bin used  
            'ltb',          % list of time points used  
            'ltr',          % list of trial types used  
            'n_dip',        % number of dipoles used  
            'Lecd',         % dipole lead fields  
            'loc',          % loc of dipoles (n_dip x 3)  
            'exitflag',     % Converged (1) or not (0)  
            'P'             % forward model  
         
        In brief, this routine:  
        - load the necessary data, if not provided,  
        - fill in all the necessary bits for the VB-ECD inversion routine,  
        - launch variational Bayesian model inversion,  
        - eliminates redundant dipoles using Bayesian model reduction,  
        - displays the results.  
         
        This routine provides a Bayes optimal solution to the ECD problem. It  
        finesses the nonlinear inversion problem by starting with a large number  
        of dipoles (on the cortical surface). It then fits the principal spatial  
        modes of the data over a specified peristimulus time window using fixed  
        dipole orientations. Finally, it uses Bayesian model reduction to  
        eliminate the least likely dipoles, until the specified number of dipoles  
        is obtained.  
         
        The purpose of this routine is to find the location of a small number of  
        dipoles that accurately explain fluctuations in activity over  
        peristimulus time. It is anticipated that the moments of the dipoles will  
        be estimated as needed using a standard pseudo-inverse (ordinary least  
        squares) estimator - should it be required. examples of this are provided  
        during the presentation of the results below.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_inv_vb_ecd_gui.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_inv_vb_ecd_gui", *args, **kwargs)
