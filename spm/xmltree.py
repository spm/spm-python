from spm.__wrap__ import _Runtime, _MatlabClassWrapper


class xmltree(_MatlabClassWrapper):
  def __init__(self, *args, _objdict=None, **kwargs):
    """  XMLTREE/XMLTREE Constructor of the XMLTree class  
    FORMAT tree = xmltree(varargin)  
      
    varargin - XML filename or XML string  
    tree     - XMLTree Object  
     
        tree = xmltree;             % creates a minimal XML tree: '<tag/>'  
        tree = xmltree('foo.xml');  % creates a tree from XML file 'foo.xml'  
        tree = xmltree('<tag>content</tag>') % creates a tree from string  
   __________________________________________________________________________  
     
    This is the constructor of the XMLTree class.   
    It creates a tree of an XML 1.0 file (after parsing) that is stored   
    using a Document Object Model (DOM) representation.  
    See http://www.w3.org/TR/REC-xml for details about XML 1.0.  
    See http://www.w3.org/DOM/ for details about DOM platform.  
   __________________________________________________________________________  
    
      Documentation for xmltree  
         doc xmltree  
    
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@xmltree/xmltree.m)
    """

    if _objdict is None:
      _objdict = _Runtime.call("xmltree", *args, **kwargs)
    super().__init__(_objdict)

  def add(self, *args, **kwargs):
    """  XMLTREE/ADD Method (add children to elements of an XML Tree)  
    FORMAT vararout = add(tree,uid,type,parameter)  
      
    tree      - XMLTree object  
    uid       - array of uid's  
    type      - 'element', 'chardata', 'cdata', 'pi' or 'comment'  
    parameter - property name (a character array unless type='pi' for  
                which parameter=struct('target','','value',''))  
     
    new_uid   - UID's of the newly created nodes  
     
           tree = add(tree,uid,type,parameter);  
           [tree, new_uid] = add(tree,uid,type,parameter);  
   __________________________________________________________________________  
     
    Add a node (element, chardata, cdata, pi or comment) in the XML Tree.  
    It adds a child to the element whose UID is iud.  
    Use attributes({'set','get','add','del','length'},...) function to   
    deal with the attributes of an element node (initialized empty).  
    The tree parameter must be in input AND in output.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@xmltree/add.m)
    """

    return _Runtime.call("add", self._as_matlab_object(), *args, **kwargs)


  def attributes(self, *args, **kwargs):
    """  XMLTREE/ATTRIBUTES Method (handle attributes of an element node)  
    FORMAT varargout = attributes(varargin)  
      
    tree    - XMLTree object  
    method  - 'set','get','add','del' or 'length'  
    uid     - the UID of an element node  
    n       - indice of the attribute  
    key     - string key="..."  
    val     - string ...="val"  
    attr    - cell array of struct(key,val) or just struct(key,val)  
    l       - number of attributes of the element node uid  
     
        tree = attributes(tree,'set',uid,n,key,val)  
        attr = attributes(tree,'get',uid[,n])  
        tree = attributes(tree,'add',uid,key,val)  
        tree = attributes(tree,'del',uid[,n])  
        l    = attributes(tree,'length',uid)  
   __________________________________________________________________________  
     
    Handle attributes of an element node.  
    The tree parameter must be in input AND in output for 'set', 'add' and  
    'del' methods.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@xmltree/attributes.m)
    """

    return _Runtime.call("attributes", self._as_matlab_object(), *args, **kwargs)


  def branch(self, *args, **kwargs):
    """  XMLTREE/BRANCH Branch Method  
    FORMAT uid = parent(tree,uid)  
      
    tree    - XMLTree object  
    uid     - UID of the root element of the subtree  
    subtree - XMLTree object (a subtree from tree)  
   __________________________________________________________________________  
     
    Return a subtree from a tree.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@xmltree/branch.m)
    """

    return _Runtime.call("branch", self._as_matlab_object(), *args, **kwargs)


  def char(self, *args, **kwargs):
    """  XMLTREE/CHAR Converter function from XMLTree to a description string  
    FORMAT s = char(tree)  
     
    tree - XMLTree object  
    s    - a description string of an XMLTree  
   __________________________________________________________________________  
     
    Return a string describing the XMLTree:  
                  'XMLTree object (x nodes) [filename]'  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@xmltree/char.m)
    """

    return _Runtime.call("char", self._as_matlab_object(), *args, **kwargs)


  def children(self, *args, **kwargs):
    """  XMLTREE/CHILDREN Return children's UIDs of node uid  
    FORMAT child = children(tree,uid)  
     
    tree   - a tree  
    uid    - uid of the element  
    child  - array of the UIDs of children of node uid  
   __________________________________________________________________________  
     
    Return UID's of children of node uid  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@xmltree/children.m)
    """

    return _Runtime.call("children", self._as_matlab_object(), *args, **kwargs)


  def convert(self, *args, **kwargs):
    """  XMLTREE/CONVERT Convert an XML tree into a structure  
      
    tree     - XMLTree object  
    uid      - uid of the root of the subtree, if provided.  
               Default is root  
    s        - converted structure  
   __________________________________________________________________________  
     
    Convert an XMLTree into a structure, when possible.  
    When several identical tags are present, a cell array is used.  
    The root tag is not saved in the structure.  
    If provided, only the structure corresponding to the subtree defined  
    by the uid UID is returned.  
     
    Example:  
    xml = '<a><b>field1</b><c>field2</c><b>field3</b></a>';  
    tree = convert(xmltree(xml));  
    <=> tree = struct('b',{{'field1', 'field3'}},'c','field2')  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@xmltree/convert.m)
    """

    return _Runtime.call("convert", self._as_matlab_object(), *args, **kwargs)


  def copy(self, *args, **kwargs):
    """  XMLTREE/COPY Copy Method (copy a subtree in another branch)  
    FORMAT tree = copy(tree,subuid,uid)  
      
    tree      - XMLTree object  
    subuid    - UID of the subtree to copy  
    uid       - UID of the element where the subtree must be duplicated  
   __________________________________________________________________________  
     
    Copy a subtree to another branch.  
    The tree parameter must be in input AND in output.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@xmltree/copy.m)
    """

    return _Runtime.call("copy", self._as_matlab_object(), *args, **kwargs)


  def delete(self, *args, **kwargs):
    """  XMLTREE/DELETE Delete (delete a subtree given its UID)  
      
    tree      - XMLTree object  
    uid       - array of UID's of subtrees to be deleted  
   __________________________________________________________________________  
     
    Delete a subtree given its UID  
    The tree parameter must be in input AND in output  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@xmltree/delete.m)
    """

    return _Runtime.call("delete", self._as_matlab_object(), *args, **kwargs)


  def display(self, *args, **kwargs):
    """  XMLTREE/DISPLAY Command window display of an XMLTree  
    FORMAT display(tree)  
      
    tree - XMLTree object  
   __________________________________________________________________________  
     
    This method is called when the semicolon is not used to terminate a  
    statement which returns an XMLTree.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@xmltree/display.m)
    """

    return _Runtime.call("display", self._as_matlab_object(), *args, **kwargs)


  def editor(self, *args, **kwargs):
    """ XMLTREE/EDITOR A Graphical User Interface for an XML tree  
     EDITOR(TREE) opens a new figure displaying the xmltree object TREE.  
     H = EDITOR(TREE) also returns the figure handle H.  
     
     This is a beta version of <xmltree/view> successor  
     
     See also XMLTREE  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@xmltree/editor.m)
    """

    return _Runtime.call("editor", self._as_matlab_object(), *args, **kwargs)


  def find(self, *args, **kwargs):
    """  XMLTREE/FIND Find elements in a tree with specified characteristics  
    FORMAT list = find(varargin)  
     
    tree  - XMLTree object  
    xpath - string path with specific grammar (XPath)  
    uid   - lists of root uid's  
    parameter/value - pair of pattern  
    list  - list of uid's of matched elements  
     
         list = find(tree,xpath)  
         list = find(tree,parameter,value[,parameter,value])  
         list = find(tree,uid,parameter,value[,parameter,value])  
     
    Grammar for addressing parts of an XML document:   
           XML Path Language XPath (http://www.w3.org/TR/xpath)  
    Example: /element1//element2[1]/element3[5]/element4  
   __________________________________________________________________________  
     
    Find elements in an XML tree with specified characteristics or given  
    a path (using a subset of XPath language).  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@xmltree/find.m)
    """

    return _Runtime.call("find", self._as_matlab_object(), *args, **kwargs)


  def flush(self, *args, **kwargs):
    """  XMLTREE/FLUSH Flush (Clear a subtree given its UID)  
      
    tree      - XMLTree object  
    uid       - array of UID's of subtrees to be cleared  
                Default is root  
   __________________________________________________________________________  
     
    Clear a subtree given its UID (remove all the leaves of the tree)  
    The tree parameter must be in input AND in output  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@xmltree/flush.m)
    """

    return _Runtime.call("flush", self._as_matlab_object(), *args, **kwargs)


  def get(self, *args, **kwargs):
    """  XMLTREE/GET Get Method (get object properties)  
    FORMAT value = get(tree,uid,parameter)  
      
    tree      - XMLTree object  
    uid       - array of uid's  
    parameter - property name  
    value     - property value  
   __________________________________________________________________________  
     
    Get object properties of a tree given their UIDs.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@xmltree/get.m)
    """

    return _Runtime.call("get", self._as_matlab_object(), *args, **kwargs)


  def getfilename(self, *args, **kwargs):
    """  XMLTREE/GETFILENAME Get filename method  
    FORMAT filename = getfilename(tree)  
      
    tree     - XMLTree object  
    filename - XML filename  
   __________________________________________________________________________  
     
    Return the filename of the XML tree if loaded from disk and an empty   
    string otherwise.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@xmltree/getfilename.m)
    """

    return _Runtime.call("getfilename", self._as_matlab_object(), *args, **kwargs)


  def isfield(self, *args, **kwargs):
    """  XMLTREE/ISFIELD Is parameter a field of tree{uid} ?  
    FORMAT F = isfield(tree,uid,parameter)  
     
    tree      - a tree  
    uid       - uid of the element  
    parameter - a field of the root tree  
    F         - 1 if present, 0 otherwise  
   __________________________________________________________________________  
     
    Is parameter a field of tree{uid} ?  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@xmltree/isfield.m)
    """

    return _Runtime.call("isfield", self._as_matlab_object(), *args, **kwargs)


  def length(self, *args, **kwargs):
    """  XMLTREE/LENGTH Length Method  
    FORMAT l = length(tree,r)  
      
    tree - XMLTree object  
    r    - 'real' if present, returns the real number of nodes in the  
            tree (deleted nodes aren't populated)  
    l    - length of the XML tree (number of nodes)  
   __________________________________________________________________________  
     
    Return the number of nodes of an XMLTree object.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@xmltree/length.m)
    """

    return _Runtime.call("length", self._as_matlab_object(), *args, **kwargs)


  def move(self, *args, **kwargs):
    """  XMLTREE/MOVE Move (move a subtree inside a tree from A to B)  
      
    tree   - XMLTree object  
    uida   - initial position of the subtree  
    uidb   - parent of the final position of the subtree  
   __________________________________________________________________________  
     
    Move a subtree inside a tree from A to B.  
    The tree parameter must be in input AND in output.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@xmltree/move.m)
    """

    return _Runtime.call("move", self._as_matlab_object(), *args, **kwargs)


  def parent(self, *args, **kwargs):
    """  XMLTREE/PARENT Parent Method  
    FORMAT uid = parent(tree,uid)  
      
    tree   - XMLTree object  
    uid    - UID of the lonely child  
    p      - UID of the parent ([] if root is the child)  
   __________________________________________________________________________  
     
    Return the uid of the parent of a node.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@xmltree/parent.m)
    """

    return _Runtime.call("parent", self._as_matlab_object(), *args, **kwargs)


  def root(self, *args, **kwargs):
    """  XMLTREE/ROOT Root Method  
    FORMAT uid = root(tree)  
      
    tree   - XMLTree object  
    uid    - UID of the root element of tree  
   __________________________________________________________________________  
     
    Return the uid of the root element of the tree.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@xmltree/root.m)
    """

    return _Runtime.call("root", self._as_matlab_object(), *args, **kwargs)


  def save(self, *args, **kwargs):
    """  XMLTREE/SAVE Save an XML tree in an XML file  
    FORMAT varargout = save(tree,filename)  
     
    tree      - XMLTree  
    filename  - XML output filename  
    varargout - XML string  
   __________________________________________________________________________  
     
    Convert an XML tree into a well-formed XML string and write it into  
    a file or return it as a string if no filename is provided.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@xmltree/save.m)
    """

    return _Runtime.call("save", self._as_matlab_object(), *args, **kwargs)


  def set(self, *args, **kwargs):
    """  XMLTREE/SET Method (set object properties)  
    FORMAT tree = set(tree,uid,parameter,value)  
      
    tree      - XMLTree object  
    uid       - array (or cell) of uid's  
    parameter - property name  
    value     - property value  
   __________________________________________________________________________  
     
    Set object properties given its uid and pairs parameter/value  
    The tree parameter must be in input AND in output  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@xmltree/set.m)
    """

    return _Runtime.call("set", self._as_matlab_object(), *args, **kwargs)


  def setfilename(self, *args, **kwargs):
    """  XMLTREE/SETFILENAME Set filename method  
    FORMAT tree = setfilename(tree,filename)  
      
    tree     - XMLTree object  
    filename - XML filename  
   __________________________________________________________________________  
     
    Set the filename linked to the XML tree as filename.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@xmltree/setfilename.m)
    """

    return _Runtime.call("setfilename", self._as_matlab_object(), *args, **kwargs)


  def view(self, *args, **kwargs):
    """  XMLTREE/VIEW View Method (deprecated)  
    FORMAT view(tree)  
      
    tree   - XMLTree object  
   __________________________________________________________________________  
     
    Display an XML tree in a graphical interface.  
     
    This function is DEPRECATED: use EDITOR instead.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/@xmltree/view.m)
    """

    return _Runtime.call("view", self._as_matlab_object(), *args, **kwargs)


