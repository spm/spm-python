from spm.__wrapper__ import Runtime


def spm_conman(*args, **kwargs):
    """
      Contrast manager: GUI for defining valid contrasts  
        FORMAT varargout=spm_conman(varargin)  
              - An embedded callback, multi-function function  
              - For detailed programmers comments,  
                see format specifications in main body of program (below user help)  
       __________________________________________________________________________  
         
        The contrast manager is a user interface for the selection and definition  
        of contrasts for a given SPM design. At present, the contrast manager  
        provides only interactive GUI facilities.  
         
        See also: spm_getSPM.m, spm_contrasts.m  
         
       ==========================================================================  
        U s i n g   t h e   S P M   C o n t r a s t   M a n a g e r   G U I  
       ==========================================================================  
         
        The contrast manager graphicsl user interface (GUI) is a dialog box for  
        the specification and selection of contrasts. The contrast selection   
        interface is presented initially, pressing the "Define new contrast..."   
        button pops up the contrast definition interface:  
         
       __________________________________________________________________________  
                                             ConMan: Contrast selection interface  
         
        The contrast selection interface consists of:  
         
        * "Show" statistic type radio-buttons: "t-contrasts", "F-contrasts", "All":  
          Selects the types of contrast that are presented for selection in the  
          contrast selection list box. Depending on the use of the contrast  
          manager, some options may be unavailable.  
         
        * List-box of currently defined contrasts.  
          Each contrast is listed by number, type ("T" or "F"), and name. Only  
          contrasts of types specified by the settings of the "show"  
          radiobuttons are shown.  
          Select contrasts by clicking on their entry in the list-box. To  
          select multiple contrasts (for conjunctions or masking, if  
          appropriate), the standard techniques of drag selection and  
          shift-clicking can be used for selecting a set of adjacent contrasts,  
          control-click to select individual contrasts separated in the list.  
          Selected contrasts are highlit in black.  
         
        * Image of the design matrix:  
          A grey-scale representation of the design matrix, to aid interpretation  
          of the contrasts.  
         
          The design matrix is "surfable": Clicking (and holding or dragging)  
          around the design matrix image reports the corresponding value of the  
          design matrix ('normal' click - "left" mouse button usually), the  
          image filename ('extend' mouse click - "middle" mouse), or parameter  
          name ('alt' click - "right" mouse). Double clicking the design matrix  
          image extracts the design matrix into the base MATLAB workspace.  
          (Surfing is handled by spm_DesRep.m)  
         
        * Parameter estimability bar  
          Under the design matrix the parameter estimability is displayed as  
          a 1xp matrix of grey and white squares. Parameters that are not  
          uniquely specified by the model are shown with a grey patch.  
         
          Recall that only uniquely estimable parameters can be examined  
          individually with [0,...,0,1,0,...,0] type contrats.  
         
          Surfing the estimability image reports the parameter names and  
          their estimability. Double clicking extracts the estimability  
          vector into the base MatLab workspace.  
         
        * Contrast weights plot/image:  
          The weights of the selected contrast(s) are imaged above the design  
          matrix, labelled by their contrast number. t-contrasts are displayed  
          as bar-charts, F-contrasts have their weights matrix c' depicted as a  
          grey-scale image.  
         
          Again, the contrast representation is "surfable": Clicking and  
          dragging over the contrast image reports the contrast name, type and  
          number, and the value of the contrast at the mouse location.  
         
        * "Define new contrast..." button:  
          Pops up the contrast definition interface (described below)  
         
        * "Reset" button:  
          Clears the current contrast selection.  
         
        * "Done" button:  
          Press when the required contrasts have been selected.  
         
        * Status line:  
          This indicates how many contrasts have been selected, how  
          multi-contrast selections will be handled, and whether you can press  
          "Done" yet!  
         
        In addition, the dialog has a figure ContextMenu, accessed by  
        right-clicking in the figure background: In addition to providing  
        repeats of the "Define new contrast...", "Reset" & "Done" buttons  
        described above, there are two additional options:  
         
          - crash out: this bails out of the contrast manager in a nice way!  
          - rename:    This permits a single contrast to be re-named. You  
                   must select the contrast to be renamed before pulling  
                       up the context menu for this option to be available.  
         
       __________________________________________________________________________  
                                            ConMan: Contrast definition interface  
         
        To define a contrast, you must specify:  
         1) a name  
         2) the statistic type: "t-contrast" for SPM{T} or "F-contrast" for SPM{F}  
         3) a valid set of contrast weights  
            (for F-contrasts, this can also be generated given a reduced  
            (design as a partition of the existing design  
         
        The contrast definition interface consists of:  
         
        * A lilac "name" edit widget for naming the new contrast  
          Type the name of the contrast in this widget.  
          Press return or move the focus to enter the name.  
         
        * Radio-buttons for selecting statistic type: "t-contrast" or "F-contrast"  
         
        * A large lilac edit widget for entering "contrast weights matrix"  
          - Note that contrast weights should be entered transposed, with  
            contrast weights in rows.  
          - Zero's will be automatically added to the right hand side of  
            contrast weights as needed to give contrast weights matching the  
            number of parameters. For example, if you are interested in  
            contrasting the first two conditions of a design four parameters  
            (design matrix with 4 columns), you need only enter "+1 -1". The  
            contrast manager will parse this to [+1 -1 0 0].  
          - For t-contrasts, this will only accept a single line of input,  
            since contrast weights c' for an SPM{T} must be a row-vector.  
            Pressing <return> or moving the focus (by clicking on another GUI  
            element, such as the "Submit" button) will enter the contrast  
            weights for parsing.  
          - For F-contrasts, the widget accepts multi-line input.  
            Pressing <return> will move to a new line. Press <ctrl>-<return> or  
            move the focus (by clicking on another GUI element, such as the  
            "Submit" button) to enter the contrast weights for parsing.  
          - Text entered in the "contrast weights matrix" is evaluated in the  
            base workspace. Thus, matlab functions can be used in the widget,  
            and base workspace variables can be referred to. (See the help for  
            spm_input.m for more tips on using evaluated input widgets.)  
         
        * For F-contrasts, a "columns for reduced design" edit widget appears:  
          - Here you can specify SPM{F}s by specifying the reduced design as  
            a sub-partition of the current design matrix.  
          - Enter the indices of the design matrix columns you wish to retain  
            in the reduced design.  
          - Pressing <return> or moving the focus (by clicking on another GUI  
            element, such as the "Submit" button) will enter the column indices  
            for parsing.  
          - An F-contrast weights matrix is constructed from the specified  
            partitioning. (The corresponding F-contrast weights are imaged  
            above the design matrix picture. Double click (or "surf") the  
            contrast image to see the actual values of the F-contrast weights  
            matrix.)  
          - Again, text entered in the "columns for reduced design" is  
            evaluated in the base workspace, permitting the use of functions  
            and variables available in the base workspace.  
          - (Note that the F-contrast weights matrix produced may not be the  
            simplest F-contrast possible for this test, and that the F-contrast  
            weights matrix may not be full rank (e.g. may have two rows where  
            one would do). Nonetheless, the F-test is equivalent for the  
            specified partitioning.  
         
        * "Submit" button:  
          This button can be used to force parsing of the contrast weights (or  
          columns for reduced design).  
         
        * contrast parsing errors pane & contrast parsing info pane:  
          - Once the contrast weights matrix has been entered in the GUI, the  
            inout is parsed.  
          - First, each line is evaluated.  
          - Then, the results for each line are checked to ensure they define  
            valid contrasts, with trailing zeros added as necessary so the  
            contrast length matches the number of parameters.  
          - Errors encountered during parsing, and invalid contrast weights,  
            are reported in the "contrast parsing errors" pane in red text.  
            Usually the contrast cannot be defined if there are any errors!  
          - Information messages regarding contrast parsing appear in the lower  
            "contrast parsing info" pane in green text.  
          - When defining an F-contrast via "columns for reduced design", the  
            string defining the indices is similarly parsed, with errors and  
            information messages appearing in the two panes.  
         
        * Contrast weights plot/image:  
          Depicts the contrast once valid contrast weights have been specified.  
         
        * Image of the design matrix:  
          (As described above for the contrast selection interface)  
         
        * Parameter estimability bar  
          (As described above for the contrast selection interface)  
         
        * "Reset" button:  
           Resets the contrast definition interface, clearing any contrast  
           currently being defined.  
         
        * "Cancel" button:  
          Returns to the contrast selection interface without defining a new  
          contrast.  
         
        * "OK" button:  
          Once a valid set of contrast weights has been defined, and the  
          contrast named, pressing "OK" defines the contrast and returns to the  
          contrast selection interface, with the newly defined contrast  
          selected.  
         
        * Status line:  
          This indicates progress in contrast definition.  
          Once a valid set of contrast weights have been specified, and a  
          the contrast named, then the status line turns green, indicating  
          that the current contrast can be defined by pressing "OK".  
         
         
       ==========================================================================  
        S P M   C o n t r a s t   m a n a g e m e n t  
       ==========================================================================  
         
        Contrasts are stored by SPM in a single structure (See spm_FcUtil.m  
        for the definition and handling of the contrast structure.)  
         
        Note that the xCon structure for each contrast contains data specific  
        to the current experimental design. Therefore, contrast structures  
        can only be copied between analyses (to save re-entering contrasts)  
        if the designs are *identical*.  
         
        Although the contrasts are named by the user, they are referred to  
        internally and on the corresponding contrast, ESS and SPM images (see  
        spm_getSPM.m) by their contrast number, which indexes them in the  
        order in which they were created. Because of this, it can be rather  
        involved to delete any but the most recently defined contrast: All  
        file references and indices would have to be canonicalised! Thus, no  
        "delete" function is provided (as yet).  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_conman.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_conman", *args, **kwargs)
