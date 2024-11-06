from spm.__wrapper__ import Runtime


def spm_help(*args, **kwargs):
    """
      SPM help and manual facilities  
        FORMAT spm_help  
         
        The "Help" facilities are about software and implementation. The  
        underlying mathematics, concepts and operational equations have been (or  
        will be) published in the peer reviewed literature and the interested  
        user is referred to these sources. An intermediate theoretical exposition  
        is given in the SPM course notes. This and other resources are available  
        via the SPM Web site.  
        Visit https://www.fil.ion.ucl.ac.uk/spm/, or press the "SPMweb" button.  
         
       --------------------------------------------------------------------------  
         
        `spm_help('Topic')` or `spm_help Topic` displays the help for a  
        particular topic.  
         
       --------------------------------------------------------------------------  
        The SPM package provides help at three levels, the first two being  
        available via the SPM graphical help system:  
         
        (i)   Manual pages on specific topics.  
              These give an overview of specific components or topics its  
              relation to other components, the inputs and outputs and  
              references to further information.  
         
              Many of the buttons in the help menu window lead to such "man"  
              pages.  These are contained in Markdown files named spm_*.md.  
              These can be viewed on the MATLAB command line with the `help`  
              command, e.g. `help spm_help` prints out this manual file in  
              the MATLAB command window.  
         
        (ii)  Help information for each routine within SPM (E.g. This is the).  
              help information for spm_help.m - the help function.)  
              This help information is the help header of the actual MATLAB  
              function, and can be displayed on the command line with the  
              `help` command, e.g. `help spm_help`.  
         
        (iii) SPM is (mainly) implemented as MATLAB functions and scripts.  
              These are ASCII files named spm_*.m, which can be viewed in the  
              MATLAB command window with the `type` command, e.g. `type  
              spm_help`, or read in a text editor.  
         
         ---  MATLAB syntax is very similar to standard matrix notation that  
              would be found in much of the literature on matrices. In this  
              sense the SPM routines can be used (with MATLAB) for data  
              analysis, or they can be regarded as the ultimate pseudocode  
              specification of the underlying ideas.  
         
        In addition, the MATLAB help system provides keyword searching through  
        the H1 lines (the first comment line) of the help entries of *all*  
        M-files found on MATLABPATH. This can be used to identify routines from  
        keywords. Type `help lookfor` in the MATLAB command window for further  
        details.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_help.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_help", *args, **kwargs)
