from spm.__wrapper__ import Runtime


def spm_DesRep(*args, **kwargs):
    """
      Design reporting utilities  
        FORMAT varargout = spm_DesRep(action,varargin)  
         
        spm_DesRep (design reporting) is a suite of utility functions for various  
        graphical reports on a given experimental design, embodied in the design  
        matrix structure and other associated data structures.  
        For detailed programmers comments, see format specifications in main body  
        of code.  
         
                                  ----------------  
         
        By default, spm_DesRep prompts for selection of a SPM.mat file.  
         
        Given details of a design spm_DesRep sets up a "Design" menu in the  
        SPM 'Interactive' window.  The menu options launch various graphical  
        summaries of the current SPM design in the SPM 'Graphics' window.  
         
        * Design Matrix  - Displays graphical summary of the design matrix  
         
            The design is labelled with the corresponding parameter and  
            file names, and is displayed as an image scaled (using  
            spm_DesMtx('sca',...) such that zero is mid-grey, -1 is black, and +1  
            is white. Covariates exceeding this randge are scaled to fit.  
         
            The design matrix is "surfable": Clicking (and holding or dragging)  
            around the design matrix image reports the corresponding value of the  
            design matrix ('normal' click - "left" mouse button usually), the  
            image filename ('extend' mouse click - "middle" mouse), or parameter  
            name ('alt' click - "right" mouse). Double clicking the design matrix  
            image extracts the design matrix into the base MATLAB workspace.  
         
            Under the design matrix the parameter estimability is displayed as a  
            1xp matrix of grey and white squares. Parameters that are not  
            uniquely specified by the model are shown with a grey patch. Surfing  
            the estimability image reports the parameter names and their  
            estimability. Double clicking extracts the estimability vector into  
            the base MATLAB workspace.  
         
        * Design orthogonality - Displays orthogonality matrix for this design  
         
            The design matrix is displayed as in "Design Matrix" view above,  
            labelled with the parameter names.  
         
            Under the design matrix the design orthogonality matrix is  
            displayed. For each pair of columns of the design matrix, the  
            orthogonality matrix depicts the magnitude of the cosine of the  
            angle between them, with the range 0 to 1 mapped to white to  
            black. Orthogonal vectors (shown in white), have cosine of zero.  
            Colinear vectors (shown in black), have cosine of 1 or -1.  
         
            The cosine of the angle between two vectors a & b is obtained by  
            dividing the dot product of the two vectors by the product of  
            their lengths:  
         
                                a'*b  
                        ------------------------  
                        sqrt(sum(a.^2)*sum(b.^2)  
         
            If (and only if) both vectors have zero mean, i.e.  
            sum(a)==sum(b)==0, then the cosine of the angle between the  
            vectors is the same as the correlation between the two variates.  
              
            The design orthogonality matrix is "surfable": Clicking (and  
            holding or dragging) the cursor around the design orthogonality  
            image reports the orthogonality of the corresponding pair of  
            columns. Double clicking on the orthogonality matrix extracts  
            the contrast orthogonality matrix into the base MATLAB  
            workspace.  
         
        * Explore design - Sub-menu's for detailed design exploration.  
         
            If this is an fMRI design, then the session & trial/condition  
            structure of the design is reflected in the sub-menu structure.  
            Selecting a given session, and then trial/condition within the  
            session, launches a comprehensive display of the parameters of  
            that design.  
         
            If not an fMRI design, then the Explore sub-menu has two options:  
            "Files and factors" & "Covariates".  
         
        * Explore: Files and factors - Multi-page listing of filenames,   
                                       factor indices and covariates.  
         
            The covariates printed are the raw covariates as entered into  
            SPM, with the exception of the global value, which is printed  
            after any grand mean scaling.  
         
        * Explore: Covariates - Plots of the covariates, showing how they are  
                                included into the model.   
                           
            Covariates are plotted, one per page, overlaid on the design  
            matrix. The description strings in the xC covariate structure  
            array are displayed. The corresponding design matrix column(s)  
            is(are) highlighted.  
         
        * Clear    - clears Graphics window, re-instating Results section MIP  
                     & design matrix graphics (if in the results section).  
        * Help     - displays this text!  
         
                                  ----------------  
         
        spm_DesRep also handles "surfing" of contrast depictions, which are  
        bar-graphs for T-contrasts and images for F-contrasts. Clicking  
        ('normal' click - "left" mouse button usually) with the on the bars  
        of the bar-graphs, or anywhere in an image, and dragging, dynamically  
        reports the contrast weight depicted under the cursor. The format of  
        the report string is:  
          #{T/F}: <name> (ij) = <weight>  
        ...where # is the contrast number, T/F indicates the type of contrast,  
        <name> the name given to the contrast, ij the index into the contrast  
        vector/matrix weight under the cursor, and <weight> the corresponding  
        contrast weight.  
         
        Double clicking on a contrast depiction extracts the contrast weights  
        into the base workspace.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_DesRep.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_DesRep", *args, **kwargs)
